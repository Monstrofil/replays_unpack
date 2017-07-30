#!/usr/bin/python
# coding=utf-8
import struct
from StringIO import StringIO

from base.decorators import bigworld_packet, g_Packets, g_SubPackets
from base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=8)
class GameLogic(PacketDataBase):
    def __init__(self, stream):
        self.vehicleId, = struct.unpack('I', stream.read(4))
        self.subtype, = struct.unpack('I', stream.read(4))
        self.size, = struct.unpack('I', stream.read(4))

        class_ = g_SubPackets.get(self.subtype) or g_Packets[-1]
        self.data = class_(StringIO(stream.read(self.size)))
