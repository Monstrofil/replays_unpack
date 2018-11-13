#!/usr/bin/python
# coding=utf-8
import struct

from StringIO import StringIO

from replay_unpack.base.packets.types.Vector3 import Vector3
from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=43)
class PlayerPosition(PacketDataBase):
    def __init__(self, stream):
        # type: (StringIO) -> ()

        self.entityId1 = struct.unpack('i', stream.read(4))
        self.entityId2 = struct.unpack('i', stream.read(4))

        self.position = Vector3(stream)
        self.rotation = Vector3(stream)



        pass

