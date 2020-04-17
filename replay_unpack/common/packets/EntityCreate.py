# coding=utf-8
import struct

from replay_unpack.base.pretty_print_mixin import PrettyPrintObjectMixin
from replay_unpack.common.network.types import BinaryStream
from replay_unpack.common.network.types import Vector3


class EntityCreate(PrettyPrintObjectMixin):
    def __init__(self, stream):
        self.entityID, = struct.unpack('i', stream.read(4))
        self.type, = struct.unpack('h', stream.read(2))
        self.vehicleId, = struct.unpack('i', stream.read(4))
        self.spaceId, = struct.unpack('i', stream.read(4))
        self.position = Vector3(stream)
        self.direction = Vector3(stream)

        # TODO: what is it?
        self.unknown1, = struct.unpack('i', stream.read(4))

        self.state = BinaryStream(stream)
