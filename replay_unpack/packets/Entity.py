#!/usr/bin/python
# coding=utf-8
import struct

from replay_unpack.base.packets.types.BinaryIStream import BinaryIStream
from replay_unpack.base.packets.types.Vector3 import Vector3
from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x5)
class Entity(PacketDataBase):
    def __init__(self, stream):
        self.entityID, = struct.unpack('i', stream.read(4))
        self.type, = struct.unpack('h', stream.read(2))
        self.spaceId, = struct.unpack('i', stream.read(4))
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        self.direction = Vector3(stream)

        # TODO: what is it?
        self.unknown1, = struct.unpack('i', stream.read(4))

        self.state = BinaryIStream(stream)
