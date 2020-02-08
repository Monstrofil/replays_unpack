#!/usr/bin/python
# coding=utf-8

from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=-1)
class Unknown(PacketDataBase):
    def __init__(self, stream):
        self.value = stream.read()
