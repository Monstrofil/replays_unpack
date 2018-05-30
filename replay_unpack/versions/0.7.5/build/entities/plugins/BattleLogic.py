#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

from build.entities import BattleLogic


class BattleLogic(BattleLogic):
    def __init__(self):
        self.methodsMap = {
            0: 'playEffectOnce'
        }

        self.attributesMap = {
            2: 'battleType',
            3: 'timeLeft',
            0: 'battleStage',
            1: 'scenarioPhase',
            4: 'state',
            5: 'debugText',
            6: 'uiInfo',
            7: 'prerequisiteShips',
            8: 'prerequisiteEffects',
            9: 'prerequisiteWeathers'
        }

        super(BattleLogic, self).__init__()
