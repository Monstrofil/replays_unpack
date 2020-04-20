# coding=utf-8

from replay_unpack.core import PrettyPrintObjectMixin


class Test(PrettyPrintObjectMixin):
    def __init__(self, stream):
        self.r = stream.read()
