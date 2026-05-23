# coding=utf-8
"""
Opcode 0x1d — packed camera/weapon-input snapshot.

Companion of 0x18 (CameraState): same writer (FUN_14055a7c0) emits 0x1d on the
same tick whenever the LIVE input state field at ctrl+0x1b4 is not -1.

Encoding (from writer FUN_14055a7c0):
    cVar2 = *(ctrl + 0x1c4)            # u8 boolean sign flag
    iVar3 = *(ctrl + 0x1b8)            # i32 source, clamped to [0, 999]
    uVar6 = *(ctrl + 0x1b4)            # u32 source, clamped to [0, 255]
    packed_u32 = (sign_bit_mask & 0xff000000) | (iVar3 << 8) | uVar6

Playback (from FUN_14056a310 = opcode 0x1d handler):
    uVar2 = read_u32(file)
    ctrl[0x1bc] = uVar2 & 0xff           # u8 low_byte
    ctrl[0x1c0] = (uVar2 >> 8) & 0xffff  # u16 mid_word
    ctrl[0x1c4] = (uVar2 & 0xff000000) != 0    # bool sign

So the same field at ctrl+0x1c4 is the sign on BOTH sides; the controller
keeps separate "live" (0x1b4/0x1b8) and "playback" (0x1bc/0x1c0) shadows of
the input state. Both fields are initialised to -1 in the constructor.

Real-world value pattern in observed 15.4 replays:
    sign always 0; low_byte clusters around 102-109; mid_word in [19, 121].
    Plausible meaning: weapon/zoom slot tracker (low_byte) plus a small
    counter (mid_word) — both within the documented clamp ranges.
"""
import struct

from replay_unpack.core import PrettyPrintObjectMixin


class CameraInput(PrettyPrintObjectMixin):
    __slots__ = ('packed', 'low_byte', 'mid_word', 'sign')

    def __init__(self, stream):
        self.packed, = struct.unpack('I', stream.read(4))
        self.low_byte = self.packed & 0xff
        self.mid_word = (self.packed >> 8) & 0xffff
        self.sign = (self.packed >> 24) & 0xff
