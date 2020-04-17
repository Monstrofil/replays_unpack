# coding=utf-8
import struct

from replay_unpack.base.pretty_print_mixin import PrettyPrintObjectMixin


class EntityEnter(PrettyPrintObjectMixin):
    """
    Fires when entity enters AOI and starts
    receiving updates from server
    """

    def __init__(self, stream):
        self.entityId, self.spaceId, self.vehicleID = \
            struct.unpack('iii', stream.read(12))
