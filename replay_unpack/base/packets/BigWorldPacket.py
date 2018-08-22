#!/usr/bin/python
# coding=utf-8
import struct
from StringIO import StringIO

from replay_unpack.base.decorators import bigworld_packet, g_Packets

__author__ = "Aleksandr Shyshatsky"


class BigWorldPacket(object):
    __slots__ = ['size', 'type', 'time', 'data']

    def __init__(self, stream):
        self.size, = struct.unpack('I', stream.read(4))
        self.type, = struct.unpack('I', stream.read(4))
        self.time, = struct.unpack('f', stream.read(4))

        class_ = g_Packets.get(self.type) or g_Packets[-1]
        self.data = class_(StringIO(stream.read(self.size)))

    def __repr__(self):
        return "TIME: {} TYPE: {} SIZE: {} DATA: {}".format(self.time, hex(self.type), self.size, self.data)
