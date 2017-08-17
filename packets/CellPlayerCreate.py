#!/usr/bin/python
# coding=utf-8
import struct
from base.decorators import bigworld_packet
from base.packets.PacketData import PacketDataBase
from base.packets.types.BinaryIStream import BinaryIStream
from base.packets.types.Vector3 import Vector3

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x1)
class CellPlayerCreate(PacketDataBase):
    def __init__(self, stream):
        self.entityId, = struct.unpack('i', stream.read(4))
        self.spaceId, = struct.unpack('i', stream.read(4))
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        self.direction = Vector3(stream)

        self.value = BinaryIStream(stream)
