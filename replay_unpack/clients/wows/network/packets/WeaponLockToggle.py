# coding=utf-8
"""
Opcode 0x2f — weapon lock / pin-target boolean toggle.

Producer: FUN_14055ce70 (1-byte char written). Playback handler:
FUN_14056a980 reads 1 byte, forwards to FUN_14055ce70 with a Python callback
that sets `weaponLock` (true/false) on the player.

Empirically appears in alternating 1/0 pairs (press / release events).
"""
import struct

from replay_unpack.core import PrettyPrintObjectMixin


class WeaponLockToggle(PrettyPrintObjectMixin):
    __slots__ = ('locked',)

    def __init__(self, stream):
        v, = struct.unpack('B', stream.read(1))
        self.locked = bool(v)
