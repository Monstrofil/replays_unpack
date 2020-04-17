# coding=utf-8
import struct

from replay_unpack.base.pretty_print_mixin import PrettyPrintObjectMixin


class EntityControl(PrettyPrintObjectMixin):
    def __init__(self, stream):
        self.entityId, self.isControled = struct.unpack('ib', stream.read(5))
