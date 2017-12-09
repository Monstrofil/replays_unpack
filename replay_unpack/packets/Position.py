#!/usr/bin/python
# coding=utf-8
import struct

from StringIO import StringIO

from replay_unpack.base.packets.types.Vector3 import Vector3
from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=10)
class Position(PacketDataBase):
    def __init__(self, stream):
        # type: (StringIO) -> ()
        self.entityId, = struct.unpack('i', stream.read(4))
        if stream.len > 45:
            self.spaceID, = struct.unpack('i', stream.read(4))
        else:
            self.spaceID = -1
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        self.positionError = Vector3(stream)
        self.rotation = Vector3(stream)
        self.is_error, = struct.unpack('b', stream.read(1))
