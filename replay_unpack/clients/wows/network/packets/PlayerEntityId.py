# coding=utf-8
"""
Opcode 0x20 — one-shot "this is the player's vehicle" tag.

Producer: FUN_14055d390. Writes a single i32 holding the entity_id of the
vehicle the recording is anchored to. Confirmed empirically: in the 15.4
replay, value = 542844, which matches the vehicleId field of 0x2c
PlayerPosition records.
"""
import struct

from replay_unpack.core import PrettyPrintObjectMixin


class PlayerEntityId(PrettyPrintObjectMixin):
    __slots__ = ('vehicleId',)

    def __init__(self, stream):
        self.vehicleId, = struct.unpack('i', stream.read(4))
