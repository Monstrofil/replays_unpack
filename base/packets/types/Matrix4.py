#!/usr/bin/python
# coding=utf-8
import struct

from base.packets.PacketData import PacketDataBase

__author__ = "Aleksandr Shyshatsky"


class Matrix4(PacketDataBase):
    def __init__(self, stream):
        self.m11, = struct.unpack('f', stream.read(4))
        self.m12, = struct.unpack('f', stream.read(4))
        self.m13, = struct.unpack('f', stream.read(4))
        self.m14, = struct.unpack('f', stream.read(4))
        self.m21, = struct.unpack('f', stream.read(4))
        self.m22, = struct.unpack('f', stream.read(4))
        self.m23, = struct.unpack('f', stream.read(4))
        self.m24, = struct.unpack('f', stream.read(4))
        self.m31, = struct.unpack('f', stream.read(4))
        self.m32, = struct.unpack('f', stream.read(4))
        self.m33, = struct.unpack('f', stream.read(4))
        self.m34, = struct.unpack('f', stream.read(4))
        self.m41, = struct.unpack('f', stream.read(4))
        self.m42, = struct.unpack('f', stream.read(4))
        self.m43, = struct.unpack('f', stream.read(4))
        self.m44, = struct.unpack('f', stream.read(4))
