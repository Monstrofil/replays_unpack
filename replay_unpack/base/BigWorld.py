#!/usr/bin/python
# coding=utf-8
from replay_unpack.base.PlayersInfo import PlayersInfo
from build.entities.plugins.BattleController import BattleController

__author__ = "Aleksandr Shyshatsky"


class BigWorld(object):
    def __init__(self):
        self.entities = {}
        self.battle_controller = BattleController(self)

    @property
    def battleLogic(self):
        return next(e for e in self.entities.values() if e.__class__.__name__ == 'BattleLogic')
