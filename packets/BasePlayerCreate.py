#!/usr/bin/python
# coding=utf-8
import struct
from base.decorators import bigworld_packet
from base.packets.PacketData import PacketDataBase
from base.packets.types.BinaryIStream import BinaryIStream

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x0)
class BasePlayerCreate(PacketDataBase):
    def __init__(self, stream):
        self.entityId, = struct.unpack('i', stream.read(4))
        self.entityType, = struct.unpack('h', stream.read(2))

        self.value = BinaryIStream(stream)
