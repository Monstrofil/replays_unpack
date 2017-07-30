#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


class PacketDataBase(object):
    def __repr__(self):
        return "<{}>: {}".format(self.__class__.__name__, self.__dict__)
