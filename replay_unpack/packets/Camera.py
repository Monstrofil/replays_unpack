#!/usr/bin/python
# coding=utf-8
import struct

from replay_unpack.base.packets.types.Vector3 import Vector3
from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=36)
class Camera(PacketDataBase):
    def __init__(self, stream):
        try:
            self.unknown1, = struct.unpack('f', stream.read(4))
            self.unknown2, = struct.unpack('f', stream.read(4))
            self.unknown3, = struct.unpack('f', stream.read(4))

            self.unknown4, = struct.unpack('f', stream.read(4))

            self.unknown5, = struct.unpack('f', stream.read(4))
            self.unknown6, = struct.unpack('f', stream.read(4))
            self.unknown7, = struct.unpack('f', stream.read(4))

            self.fov, = struct.unpack('f', stream.read(4))
            self.position = Vector3(stream)
            self.direction = Vector3(stream)
        except:
            pass
