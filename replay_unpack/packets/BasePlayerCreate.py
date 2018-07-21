#!/usr/bin/python
# coding=utf-8
import struct
from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase
from replay_unpack.base.packets.types.BinaryIStream import BinaryIStream

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x0)
class BasePlayerCreate(PacketDataBase):
    """
    This method is called to create a new player as far as required to
    talk to the base entity. Only data shared between the base and the
    client is provided in this method - the cell data will be provided by
    onCellPlayerCreate later if the player is put on the cell also.
    """

    def __init__(self, stream):
        self.entityId, = struct.unpack('i', stream.read(4))
        self.entityType, = struct.unpack('h', stream.read(2))

        self.value = BinaryIStream(stream)
