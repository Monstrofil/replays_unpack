#!/usr/bin/python
# coding=utf-8
from build.entities import BattleLogic

__author__ = "Aleksandr Shyshatsky"


class BattleLogic(BattleLogic):
    def __init__(self):
        self.methodsMap = {
            0: 'playEffectOnce',
        }

        self.attributesMap = {
            2: 'battleType',
            3: 'timeLeft',
            0: 'battleStage',
            1: 'scenarioPhase',
            4: 'state',
            5: 'debugText'
        }
        super(BattleLogic, self).__init__()
