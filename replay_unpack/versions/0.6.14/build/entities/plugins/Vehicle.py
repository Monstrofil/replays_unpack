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
            35: 'setShotDecals',
            41: 'receiveDamagesOnShip',
            16: 'consumableUsed',
            8: 'setArtilleryGunsDefaultYawsPitchsTo',
            24: 'syncMyTorpedoTube',
            36: 'syncMyArtilleryGun',
            21: 'syncArtilleryGun',
            22: 'syncTorpedoTube',
            18: 'syncTorpedoState',
            30: 'kill',
            11: 'forceSink',
            12: 'bodySinkPartLurched',
            28: 'shootTorpedo',
            9: 'shootGuns',
            37: 'syncShipCracks',
            1: 'makeShipCracksActive',
            42: 'makeShipCracks',
            43: 'setReloadingStateTorpedoes',
            44: 'setReloadingStateArtillery',
            38: 'setConsumables',
            2: 'stopVarys',
            3: 'reflood',
            19: 'onShotDecal',
            13: 'receiveMirrorDamage',
            14: 'offlineSetAI',
            39: 'offlineRecieveMovementRoute',
            20: 'receiveVisibilityFactors',
            4: 'forceReloadTorpedoes',
            15: 'onSkillActivated',
            5: 'uniqueSkillActivated',
        }

        self.attributesMap = {
            24: 'atbaTargets',
            25: 'airDefenseTargetId',
            14: 'airDefenseDispRadius',
            0: 'isAntiAirMode',
            15: 'health',
            16: 'regenerationHealth',
            17: 'regeneratedHealth',
            1: 'burningFlags',
            2: 'isOnForsage',
            18: 'regenCrewHpLimit',
            19: 'buoyancy',
            11: 'targetLocalPos',
            12: 'torpedoLocalPos',
            13: 'weaponLockFlags',
            20: 'owner',
            26: 'shipConfig',
            23: 'crewModifiersCompactParams',
            3: 'teamId',
            4: 'isAlive',
            21: 'selectedWeapon',
            5: 'serverSpeedRaw',
            6: 'speedSignDir',
            7: 'enginePower',
            8: 'isInOfflineMode',
            9: 'ignoreMapBorders',
            27: 'debugText',
            10: 'isBot',
            28: 'miscsPresetsStatus',
            22: 'draught',
        }

        super(Vehicle, self).__init__()
