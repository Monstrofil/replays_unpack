# coding=utf-8
import struct

from replay_unpack.base.pretty_print_mixin import PrettyPrintObjectMixin
from replay_unpack.common.network.types import BinaryStream
from replay_unpack.common.network.types import Vector3


class CellPlayerCreate(PrettyPrintObjectMixin):
    def __init__(self, stream):
        self.entityId, = struct.unpack('i', stream.read(4))
        self.spaceId, = struct.unpack('i', stream.read(4))
        self.unknown, = struct.unpack('h', stream.read(2))
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        self.direction = Vector3(stream)

        self.value = BinaryStream(stream)
