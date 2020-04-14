#!/usr/bin/python
# coding=utf-8
import struct

from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


# @bigworld_packet(type_=0x2)
class EntityControl(PacketDataBase):
    def __init__(self, stream):
        self.entityId, self.isControled = struct.unpack('ib', stream.read(5))
