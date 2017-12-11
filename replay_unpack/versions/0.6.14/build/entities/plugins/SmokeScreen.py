#!/usr/bin/python
# coding=utf-8
from build.entities import SmokeScreen

__author__ = "Aleksandr Shyshatsky"


class SmokeScreen(SmokeScreen):
    def __init__(self):
        self.attributesMap = {
            1: 'bcRadius',
            4: 'points',
            2: 'radius',
            3: 'height',
            0: 'activePointIndex',
        }

        super(SmokeScreen, self).__init__()


