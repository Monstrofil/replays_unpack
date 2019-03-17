#!/usr/bin/python
# coding=utf-8
import struct
from io import BytesIO as StringIO

from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


class BinaryIStream(PacketDataBase):
    def __init__(self, stream):
        self._length, = struct.unpack('I', stream.read(4))
        self.value = stream.read(self._length)

    def io(self):
        return StringIO(self.value)

