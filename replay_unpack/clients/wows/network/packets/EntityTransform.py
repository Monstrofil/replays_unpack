# coding=utf-8
"""
Opcodes 0x2a and 0x2c — entity transform / AoI delta updates.

Both opcodes share an identical 32-byte body emitted by writers FUN_14056d8b0
(0x2a, vtable slot 14 of WGReplayMessageHandler) and FUN_14056dbd0 (0x2c,
vtable slot 18). Their playback handlers at 0x14056aa60 / 0x14056ae00 are jump
thunks into the same shared restore logic.

Observed values (15.4 sample replay, 32B payload):
    0x2a — 681 records, entity ids matching known entities, position varies
           realistically across the map (water-level y=0), trailing 12 bytes
           ALWAYS ZERO across every record.
    0x2c — 16684 records, two-entity link pattern:
           * entityId == avatar, vehicleId == vehicle, position = (0,0,0)
             with all-zero trailing 12 bytes;
           * entityId == vehicle, vehicleId == 0, real Vec3 position,
             yaw in [-pi, +pi], small pitch/roll values.
           This is exactly the PlayerPosition semantics ('avatar follows
           vehicle' linkage; physical orientation when vehicle is direct).

The wire format is the same 32-byte (u32, u32, Vec3, u32, u32, u32) layout for
both opcodes; semantic interpretation of the trailing 12 bytes differs by
opcode (zero placeholders in 0x2a, yaw/pitch/roll floats in 0x2c).
"""
import struct

from replay_unpack.core import PrettyPrintObjectMixin
from replay_unpack.core.network.types import Vector3


class EntityTransform(PrettyPrintObjectMixin):
    """Common 32-byte layout for 0x2a / 0x2c.

    The last three 4-byte fields are exposed as both `yaw_pitch_roll` (floats)
    and `tail_u32s` (raw integers) so the caller can interpret based on the
    opcode it received. For 0x2c they are yaw/pitch/roll in radians; for 0x2a
    they are always zero placeholders.
    """

    __slots__ = (
        'entityId',
        'vehicleId',
        'position',
        'yaw',
        'pitch',
        'roll',
        'tail_u32s',
    )

    def __init__(self, stream):
        self.entityId, = struct.unpack('i', stream.read(4))
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        tail = stream.read(12)
        self.yaw, self.pitch, self.roll = struct.unpack('<fff', tail)
        self.tail_u32s = struct.unpack('<III', tail)
