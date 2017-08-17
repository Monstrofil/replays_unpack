#!/usr/bin/python
# coding=utf-8
from build.entities import Vehicle

__author__ = "Aleksandr Shyshatsky"


class Vehicle(Vehicle):
    def __init__(self):
        self.methodsMap = {
            0: 'startOfflineBattle',
            6: 'onConsumableInterrupted',
            7: 'setAmmoArtilleryGun',
            34: 'setShotDecals',
            40: 'receiveDamagesOnShip',
            16: 'consumableUsed',
            8: 'setArtilleryGunsDefaultYawsPitchsTo',
            24: 'syncMyTorpedoTube',
            35: 'syncMyArtilleryGun',
            21: 'syncArtilleryGun',
            22: 'syncTorpedoTube',
            18: 'syncTorpedoState',
            29: 'kill',
            11: 'forceSink',
            12: 'bodySinkPartLurched',
            27: 'shootTorpedo',
            9: 'shootGuns',
            36: 'syncShipCracks',
            1: 'makeShipCracksActive',
            41: 'makeShipCracks',
            42: 'setReloadingStateTorpedoes',
            43: 'setReloadingStateArtillery',
            37: 'setConsumables',
            2: 'stopVarys',
            3: 'reflood',
            19: 'onShotDecal',
            13: 'receiveMirrorDamage',
            14: 'offlineSetAI',
            38: 'offlineRecieveMovementRoute',
            20: 'receiveVisibilityFactors',
            4: 'forceReloadTorpedoes',
            15: 'onSkillActivated',
            5: 'uniqueSkillActivated'
        }

        super(Vehicle, self).__init__()



