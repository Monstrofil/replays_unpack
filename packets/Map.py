#!/usr/bin/python
# coding=utf-8
import struct

from base.decorators import bigworld_packet
from base.packets.PacketData import PacketDataBase
from base.packets.types.Matrix4 import Matrix4

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x27)
class Map(PacketDataBase):
    def __init__(self, stream):
        self.spaceId, = struct.unpack('i', stream.read(4))
        self.arenaId, = struct.unpack('q', stream.read(8))
        _name_size, = struct.unpack('i', stream.read(4))
        self.name = stream.read(_name_size)
        self.matrix = Matrix4(stream)
