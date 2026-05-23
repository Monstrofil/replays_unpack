# coding=utf-8
"""
Strict byte-consumption + value-sanity test for newly-added packet types.

For each opcode we added a parser for, verify two things across real replays:
  1. The parser consumes EXACTLY the packet's `size` field — no under-read
     (leftover bytes) and no over-read (would raise on short stream).
  2. Decoded field values match documented semantics — Vec3s within map
     bounds, yaw within +/-pi, entity_ids that match known created entities,
     etc.  This catches misaligned layouts that happen to consume the right
     number of bytes but interpret fields wrong.
"""
import math
import os
import struct
from collections import defaultdict
from io import BytesIO
from unittest import TestCase, main

from replay_unpack.replay_reader import ReplayReader
from replay_unpack.clients.wows.network.packets import (
    AccountInit, BasePlayerCreate, CameraInput, CameraState, CellPlayerCreate,
    EntityControl, EntityCreate, EntityLeave, EntityTransform, Heartbeat,
    PlayerEntityId, PlayerPosition, Position, WeaponLockToggle,
)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def walk_records(decrypted):
    off, n = 0, len(decrypted)
    while off + 12 <= n:
        size, ptype, t = struct.unpack_from("<IIf", decrypted, off)
        if size > 5_000_000 or off + 12 + size > n:
            return
        yield ptype, t, size, decrypted[off + 12: off + 12 + size]
        off += 12 + size


STRICT_OPCODES = {
    0x0e: (Heartbeat, 8),
    0x18: (CameraState, 52),
    0x1d: (CameraInput, 4),
    0x20: (PlayerEntityId, 4),
    0x26: (AccountInit, 10),
    0x2a: (EntityTransform, 32),
    0x2c: (EntityTransform, 32),
    0x2f: (WeaponLockToggle, 1),
}

STRICT_OLD = {
    0x02: (EntityControl, 5),
    0x04: (EntityLeave, 4),
    0x0a: (Position, 45),
}


REPLAYS_MODERN = [
    ("12.11.1", "data/random_replays/12_11_1_cn/20231214_203306_PFSC210-Marseille_46_Estuary.wowsreplay"),
    ("13.2.0", "data/random_replays/13_2_0/2214_1710519704_20240315_171005_PSSC106-Baleares_08_NE_passage.wowsreplay"),
    ("15.4.0", "data/random_replays/15_4_0/232273.wowsreplay"),
]


class TestPacketFormatStrict(TestCase):
    def _decrypted(self, rel_path):
        full = os.path.join(BASE_DIR, rel_path)
        if not os.path.isfile(full):
            self.skipTest("missing replay: %s" % rel_path)
        return ReplayReader(full).get_replay_data().decrypted_data

    def _check_strict_consumption(self, rel_path):
        decrypted = self._decrypted(rel_path)
        seen = defaultdict(int)
        size_mismatches = []
        parse_failures = []
        leftover_failures = []
        for ptype, t, size, payload in walk_records(decrypted):
            seen[ptype] += 1
            entry = STRICT_OPCODES.get(ptype) or STRICT_OLD.get(ptype)
            if entry is None:
                continue
            cls, expected = entry
            if expected is not None and size != expected:
                size_mismatches.append((ptype, size, expected))
                continue
            stream = BytesIO(payload)
            try:
                cls(stream)
            except Exception as e:
                parse_failures.append((ptype, size, repr(e)))
                continue
            leftover = stream.read()
            if leftover:
                leftover_failures.append((ptype, size, len(leftover)))
        self.assertEqual([], size_mismatches, "size mismatches in %s" % rel_path)
        self.assertEqual([], parse_failures, "parse failures in %s" % rel_path)
        self.assertEqual([], leftover_failures, "incomplete consumption in %s" % rel_path)
        return seen

    # === Strict consumption coverage ===

    def test_consumption_12_11_1(self):
        seen = self._check_strict_consumption(REPLAYS_MODERN[0][1])
        for op in (0x18, 0x1d, 0x2a, 0x2c):
            self.assertGreater(seen[op], 0, "opcode 0x%x never appeared" % op)

    def test_consumption_13_2_0(self):
        seen = self._check_strict_consumption(REPLAYS_MODERN[1][1])
        for op in (0x18, 0x1d):
            self.assertGreater(seen[op], 0, "opcode 0x%x never appeared" % op)

    def test_consumption_15_4_0(self):
        seen = self._check_strict_consumption(REPLAYS_MODERN[2][1])
        for op in (0x18, 0x1d, 0x2a, 0x2c):
            self.assertGreater(seen[op], 0, "opcode 0x%x never appeared" % op)

    # === Field-value sanity ===

    def _entity_ids_from(self, decrypted):
        ids = set()
        for ptype, t, size, payload in walk_records(decrypted):
            stream = BytesIO(payload)
            try:
                if ptype == 0x00:
                    ids.add(BasePlayerCreate(stream).entityId)
                elif ptype == 0x01:
                    ids.add(CellPlayerCreate(stream).entityId)
                elif ptype == 0x05:
                    ids.add(EntityCreate(stream).entityID)
            except Exception:
                pass
        return ids

    def test_0x18_is_default_sentinel_in_15_4(self):
        """0x18 records in every sampled replay are constructor defaults (no data)."""
        decrypted = self._decrypted(REPLAYS_MODERN[2][1])
        populated = 0
        total = 0
        for ptype, t, size, payload in walk_records(decrypted):
            if ptype != 0x18:
                continue
            total += 1
            rec = CameraState(BytesIO(payload))
            if rec.is_populated:
                populated += 1
        self.assertGreater(total, 0)
        # If this ever flips (a recording with REAL camera data appears),
        # the assertion will fire and we should investigate the layout.
        self.assertEqual(0, populated,
                         "Unexpected: %d/%d CameraState records carry "
                         "non-default data — re-examine layout." %
                         (populated, total))

    def test_0x1d_clamps_respected(self):
        decrypted = self._decrypted(REPLAYS_MODERN[2][1])
        for ptype, t, size, payload in walk_records(decrypted):
            if ptype != 0x1d:
                continue
            rec = CameraInput(BytesIO(payload))
            self.assertLessEqual(rec.low_byte, 255)
            self.assertLessEqual(rec.mid_word, 999, "v1 must be clamped to 0..999")
            # Sign byte must be 0 or 0xff (boolean flag's encoded form)
            self.assertIn(rec.sign, (0, 0xff))

    def test_0x2a_position_within_map_and_tail_zero(self):
        decrypted = self._decrypted(REPLAYS_MODERN[2][1])
        known_entities = self._entity_ids_from(decrypted)
        n = 0
        unknown_entities = 0
        nonzero_tail = 0
        for ptype, t, size, payload in walk_records(decrypted):
            if ptype != 0x2a:
                continue
            n += 1
            rec = EntityTransform(BytesIO(payload))
            # Position within typical map (-1500..1500m on each axis, water y=0)
            self.assertLess(abs(rec.position.x), 1500)
            self.assertLess(abs(rec.position.z), 1500)
            self.assertEqual(0.0, rec.position.y, "ships are at water level")
            # Empirical: trailing 3 u32 are always exactly 0 on 0x2a
            if any(v != 0 for v in rec.tail_u32s):
                nonzero_tail += 1
            if rec.entityId not in known_entities:
                unknown_entities += 1
        self.assertGreater(n, 0)
        self.assertEqual(0, unknown_entities,
                         "0x2a should reference only known entities")
        self.assertEqual(0, nonzero_tail,
                         "0x2a's trailing 12 bytes should always be zero")

    def test_0x0e_heartbeat_is_constant(self):
        """Every 0x0e record in every sampled replay carries the same fixed
        8-byte token (1/7 as f64). If this ever varies, our 'opaque token'
        interpretation is wrong and we should re-investigate."""
        decrypted = self._decrypted(REPLAYS_MODERN[2][1])
        values = set()
        for ptype, t, size, payload in walk_records(decrypted):
            if ptype != 0x0e:
                continue
            rec = Heartbeat(BytesIO(payload))
            values.add(rec.raw)
        self.assertEqual(1, len(values),
                         "Heartbeat payload varied — saw %d distinct values: %s" %
                         (len(values), sorted(values)))
        only = values.pop()
        # Confirm the documented constant. LE bytes 00 00 00 a0 24 49 c2 3f
        # → u64 0x3FC24924A0000000 → f64 ≈ 0.14286 ≈ 1/7.
        self.assertEqual(0x3FC24924A0000000, only)

    def test_0x20_player_entity_matches_2c_vehicle(self):
        """0x20 emits the player's vehicle entity_id, which must match the
        vehicleId field that 0x2c PlayerPosition records use to link the
        avatar to its vehicle."""
        decrypted = self._decrypted(REPLAYS_MODERN[2][1])
        player_ids = []
        linked_vehicles = set()
        for ptype, t, size, payload in walk_records(decrypted):
            if ptype == 0x20:
                player_ids.append(PlayerEntityId(BytesIO(payload)).vehicleId)
            elif ptype == 0x2c:
                rec = EntityTransform(BytesIO(payload))
                if rec.vehicleId != 0:
                    linked_vehicles.add(rec.vehicleId)
        self.assertEqual(1, len(player_ids),
                         "expected exactly one 0x20 record")
        self.assertIn(player_ids[0], linked_vehicles,
                      "0x20's vehicleId should appear as 0x2c's vehicleId link")

    def test_0x26_accountinit_matches_baseplayer(self):
        """0x26 fires once at session start with the player's avatar
        entity_id — must match the entity_id from 0x00 BasePlayerCreate."""
        decrypted = self._decrypted(REPLAYS_MODERN[2][1])
        bp_ids = []
        ai_ids = []
        for ptype, t, size, payload in walk_records(decrypted):
            if ptype == 0x00:
                bp_ids.append(BasePlayerCreate(BytesIO(payload)).entityId)
            elif ptype == 0x26:
                ai_ids.append(AccountInit(BytesIO(payload)).entityId)
        self.assertEqual(1, len(bp_ids))
        self.assertEqual(1, len(ai_ids))
        self.assertEqual(bp_ids[0], ai_ids[0])

    def test_0x2f_weapon_lock_paired(self):
        """WeaponLock toggles must come in alternating ON/OFF pairs (a press
        is always followed by a release within the same recording)."""
        decrypted = self._decrypted(REPLAYS_MODERN[2][1])
        seq = []
        for ptype, t, size, payload in walk_records(decrypted):
            if ptype != 0x2f:
                continue
            seq.append(WeaponLockToggle(BytesIO(payload)).locked)
        self.assertTrue(seq, "expected some 0x2f records")
        # Every record value alternates with its predecessor (T,F,T,F,...)
        for i in range(1, len(seq)):
            self.assertNotEqual(seq[i - 1], seq[i],
                                "0x2f at index %d did not alternate: %s" % (i, seq))
        # Count is even (every press has a release)
        self.assertEqual(0, len(seq) % 2,
                         "Unpaired weapon-lock event — sequence: %s" % seq)

    def test_0x2c_playerposition_semantics(self):
        decrypted = self._decrypted(REPLAYS_MODERN[2][1])
        known_entities = self._entity_ids_from(decrypted)
        n_linked = 0
        n_standalone = 0
        bad_yaw = 0
        for ptype, t, size, payload in walk_records(decrypted):
            if ptype != 0x2c:
                continue
            rec = EntityTransform(BytesIO(payload))
            self.assertIn(rec.entityId, known_entities)
            if rec.vehicleId != 0:
                # Linked record: position=(0,0,0), all-zero trailing
                self.assertEqual(0.0, rec.position.x)
                self.assertEqual(0.0, rec.position.y)
                self.assertEqual(0.0, rec.position.z)
                self.assertIn(rec.vehicleId, known_entities)
                n_linked += 1
            else:
                # Standalone: position is the vehicle's real location,
                # yaw is the heading (must be within +/-pi).
                n_standalone += 1
                if not (-math.pi - 0.01 <= rec.yaw <= math.pi + 0.01):
                    bad_yaw += 1
        self.assertGreater(n_linked, 0, "expected some avatar->vehicle linked records")
        self.assertGreater(n_standalone, 0, "expected some standalone records")
        self.assertEqual(0, bad_yaw, "all yaws must be in +/-pi")


if __name__ == "__main__":
    main()
