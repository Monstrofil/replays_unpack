#!/usr/bin/python
# coding=utf-8
import struct

from base.decorators import bigworld_packet
from base.packets.PacketData import PacketDataBase
from base.packets.types.BinaryIStream import BinaryIStream

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x8)
class EntityMethod(PacketDataBase):
    def __init__(self, stream):
        self.vehicleId, = struct.unpack('I', stream.read(4))
        self.subtype, = struct.unpack('I', stream.read(4))

        self.data = BinaryIStream(stream)
