#!/usr/bin/python
# coding=utf-8
import struct

from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase
from replay_unpack.base.packets.types.BinaryIStream import BinaryIStream

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x8)
class EntityMethod(PacketDataBase):
    def __init__(self, stream):
        self.entityId, = struct.unpack('I', stream.read(4))
        self.messageId, = struct.unpack('I', stream.read(4))

        self.data = BinaryIStream(stream)
