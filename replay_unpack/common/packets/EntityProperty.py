# coding=utf-8
import struct

from replay_unpack.base.pretty_print_mixin import PrettyPrintObjectMixin
from replay_unpack.common.network.types import BinaryStream


class EntityProperty(PrettyPrintObjectMixin):
    """
    Fires when servers requests client to change
    entity's property with some arguments
    """
    __slots__ = (
        'objectID',
        'messageId',
        'data',
    )

    def __init__(self, stream):
        self.objectID, = struct.unpack('I', stream.read(4))
        self.messageId, = struct.unpack('I', stream.read(4))
        self.data = BinaryStream(stream)
