# coding=utf-8
import os
import struct

from replay_unpack.core.pretty_print_mixin import PrettyPrintObjectMixin


class BattleStats(PrettyPrintObjectMixin):
    def __init__(self, stream):
        self.payloadSize, = struct.unpack('i', stream.read(4))
        self.payload = stream.read(self.payloadSize)

        print(self.payload)
