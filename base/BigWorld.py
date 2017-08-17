#!/usr/bin/python
# coding=utf-8
from base.PlayersInfo import PlayersInfo
from build.entities.plugins.BattleController import BattleController

__author__ = "Aleksandr Shyshatsky"


class BigWorld(object):
    def __init__(self):
        self.entities = {}
        self.battle_controller = BattleController()
