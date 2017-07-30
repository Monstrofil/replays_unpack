#!/usr/bin/python
# coding=utf-8
import struct
from StringIO import StringIO

from base.decorators import bigworld_packet, g_Packets

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=1)
class BigWorldPacket(object):
    __slots__ = ['size', 'type', 'time', 'data']

    def __init__(self, stream):
        self.size, = struct.unpack('I', stream.read(4))
        self.type, = struct.unpack('I', stream.read(4))
        self.time, = struct.unpack('f', stream.read(4))

        class_ = g_Packets.get(self.type) or g_Packets[-1]
        try:
            self.data = class_(StringIO(stream.read(self.size)))
        except Exception, e:
            self.data = None

    def __repr__(self):
        return "TIME: {} TYPE: {} SIZE: {} DATA: {}".format(self.time, hex(self.type), self.size, self.data)
