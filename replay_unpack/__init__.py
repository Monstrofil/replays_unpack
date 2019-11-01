#!/usr/bin/python
# coding=utf-8
import os
import sys
from replay_unpack.base.packets.BigWorldPacket import BigWorldPacket
from replay_unpack.replay_decrypt import WoWSReplayDecrypt

from .packets import *

# because wg uses protocol in a really strange way
# and passes pickes in it
FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')
sys.path.append(FIXTURES_PATH)

__author__ = "Aleksandr Shyshatsky"
__all__ = ['BigWorldPacket', 'WoWSReplayDecrypt']
