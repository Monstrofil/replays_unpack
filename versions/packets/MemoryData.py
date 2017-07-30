#!/usr/bin/python
# coding=utf-8
import struct

from base.decorators import bigworld_packet
from base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=-1)
class MemoryData(PacketDataBase):
    def __init__(self, stream):
        self.value = ':'.join(x.encode('hex') for x in stream.read())
