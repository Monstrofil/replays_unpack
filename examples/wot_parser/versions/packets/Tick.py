# coding=utf-8
import struct

from replay_unpack.core import PrettyPrintObjectMixin


class Tick(PrettyPrintObjectMixin):
    def __init__(self, stream):
        self.t, = struct.unpack('B', stream.read(1))
        self.t1, = struct.unpack('B', stream.read(1))
        self.t2, = struct.unpack('h', stream.read(2))
