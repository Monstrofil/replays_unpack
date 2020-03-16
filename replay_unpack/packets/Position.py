#!/usr/bin/python
# coding=utf-8
import struct
from io import BytesIO as StringIO

from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase
from replay_unpack.base.packets.types.Vector3 import Vector3

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=10)
class Position(PacketDataBase):

    __slots__ = (
        'entityId',
        'vehicleId',
        'position',
        'positionError',
        'yaw',
        'pitch',
        'roll',
        'is_error'
    )

    def __init__(self, stream):
        # type: (StringIO) -> ()
        self.entityId, = struct.unpack('i', stream.read(4))
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        self.positionError = Vector3(stream)
        self.yaw, = struct.unpack('f', stream.read(4))
        self.pitch, = struct.unpack('f', stream.read(4))
        self.roll, = struct.unpack('f', stream.read(4))
        self.is_error, = struct.unpack('b', stream.read(1))
