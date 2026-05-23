# coding=utf-8
"""
Opcode 0x18 — periodic camera-state snapshot from WGReplayController.

Produced by the per-tick writer `FUN_14055a7c0`; the playback restore path is
`FUN_14055ae20 case 0x18` which calls `FUN_140569dc0` (40 bytes) + two trailing
reads (u32, u64) for the 52-byte variant. Field offsets in the controller's
struct (DAT_148eccc00) are noted in comments.

WARNING — observed behaviour across all sampled replays (0.11.11, 13.2.0,
15.4.0, etc.) is that this record is emitted as a HEARTBEAT every ~0.1s but
the producer never populates the fields: every record's payload is exactly
40 bytes of zero followed by three f32 = -1.0. Those values match the
constructor's initial state (FUN_140557c50 sets ctrl+0x154 = -1.0f,
ctrl+0x158 = -1.0f, ctrl+0x15c = -1.0f and leaves Vec3 fields zeroed).

Interpretation: the live-game camera path that should update these fields
isn't taken by the recording client used to capture these replays. The packet
is real and consumes its bytes correctly, but is informationally empty.
"""
import struct
import math

from replay_unpack.core import PrettyPrintObjectMixin
from replay_unpack.core.network.types import Vector3


class CameraState(PrettyPrintObjectMixin):
    __slots__ = (
        'aim_point',        # Vec3 at ctrl+0x124..+0x12f (NaN-guarded; default 0,0,0)
        'view_state',       # u32  at ctrl+0x138         (default 0)
        'forward_dir',      # Vec3 at ctrl+0x13c..+0x147 (default 0,0,0)
        'up_dir',           # Vec3 at ctrl+0x148..+0x153 (default 0,0,0)
        'flag_u32',         # u32  at ctrl+0x154         (default 0xBF800000 = -1.0f)
        'flag_u64',         # u64  at ctrl+0x158         (default 0xBF800000_BF800000)
        'is_populated',     # True iff any field deviates from its constructor default
    )

    _DEFAULT_FLAG_U32 = 0xBF800000          # -1.0f as bits
    _DEFAULT_FLAG_U64 = 0xBF800000BF800000  # two -1.0f packed

    def __init__(self, stream):
        self.aim_point = Vector3(stream)
        self.view_state, = struct.unpack('I', stream.read(4))
        self.forward_dir = Vector3(stream)
        self.up_dir = Vector3(stream)
        self.flag_u32, = struct.unpack('I', stream.read(4))
        self.flag_u64, = struct.unpack('Q', stream.read(8))

        # Convenience: is this record actually carrying data, or is it the
        # default sentinel? Use bit-level comparison to avoid NaN/-0 weirdness.
        self.is_populated = (
            self.aim_point.x != 0.0 or self.aim_point.y != 0.0 or self.aim_point.z != 0.0
            or self.view_state != 0
            or self.forward_dir.x != 0.0 or self.forward_dir.y != 0.0 or self.forward_dir.z != 0.0
            or self.up_dir.x != 0.0 or self.up_dir.y != 0.0 or self.up_dir.z != 0.0
            or self.flag_u32 != self._DEFAULT_FLAG_U32
            or self.flag_u64 != self._DEFAULT_FLAG_U64
        )
