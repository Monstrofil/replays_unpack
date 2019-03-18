#!/usr/bin/python
# coding=utf-8
import os
import struct

from io import BytesIO as StringIO

from replay_unpack.base.packets.types.Vector3 import Vector3
from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=10)
class Position(PacketDataBase):
    def __init__(self, stream):
        # type: (StringIO) -> ()
        self.entityId, = struct.unpack('i', stream.read(4))
        pos = stream.tell()
        stream.seek(0, os.SEEK_END)
        s_len = stream.tell()
        stream.seek(pos)
        if s_len > 45:
            self.spaceID, = struct.unpack('i', stream.read(4))
        else:
            self.spaceID = -1
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        self.positionError = Vector3(stream)
        self.yaw, = struct.unpack('f', stream.read(4))
        self.pitch, = struct.unpack('f', stream.read(4))
        self.roll, = struct.unpack('f', stream.read(4))
        self.is_error, = struct.unpack('b', stream.read(1))
