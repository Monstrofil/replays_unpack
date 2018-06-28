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
            3: 'duration',
            4: 'timeLeft',
            0: 'battleStage',
            1: 'scenarioPhase',
            5: 'state',
            6: 'debugText',
            7: 'uiInfo',
            8: 'prerequisiteShips',
            9: 'prerequisiteEffects',
            10: 'prerequisiteWeathers'
        }

        super(BattleLogic, self).__init__()













