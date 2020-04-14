#!/usr/bin/python
# coding=utf-8
import struct

from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x3)
class EntityEnter(PacketDataBase):
    def __init__(self, stream):
        self.entityId, self.spaceId, self.vehicleID = struct.unpack('iii', stream.read(12))
        assert stream.read() == b''
