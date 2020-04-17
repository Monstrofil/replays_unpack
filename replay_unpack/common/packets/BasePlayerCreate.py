# coding=utf-8
import struct

from replay_unpack.base.pretty_print_mixin import PrettyPrintObjectMixin
from replay_unpack.common.network.types import BinaryStream


class BasePlayerCreate(PrettyPrintObjectMixin):
    """
    This method is called to create a new player as far as required to
    talk to the base entity. Only data shared between the base and the
    client is provided in this method - the cell data will be provided by
    onCellPlayerCreate later if the player is put on the cell also.
    """

    def __init__(self, stream):
        self.entityId, = struct.unpack('i', stream.read(4))
        self.entityType, = struct.unpack('h', stream.read(2))

        self.value = BinaryStream(stream)
