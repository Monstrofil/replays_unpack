#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


def bigworld_packet(type_):
    def real_wrapper(cls):
        g_Packets[type_] = cls
        return cls
    return real_wrapper


g_Packets = {}

