#!/usr/bin/python
# coding=utf-8
import struct

from base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


class BinaryIStream(PacketDataBase):
    def __init__(self, stream):
        self._length, = struct.unpack('i', stream.read(4))
        self.value = stream.read(self._length)

