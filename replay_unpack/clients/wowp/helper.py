#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

import os

from replay_unpack.core.entity_def.definitions import Definitions

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_definitions(version):
    return Definitions(os.path.join(BASE_DIR, 'versions', version.replace('.', '_')))
