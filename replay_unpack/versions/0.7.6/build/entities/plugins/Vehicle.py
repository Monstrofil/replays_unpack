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
            36: 'setShotDecals',
            42: 'receiveDamagesOnShip',
            17: 'consumableUsed',
            8: 'setArtilleryGunsDefaultYawsPitchsTo',
            25: 'syncMyTorpedoTube',
            37: 'syncMyArtilleryGun',
            22: 'syncArtilleryGun',
            23: 'syncTorpedoTube',
            19: 'syncTorpedoState',
            12: 'forceSink',
            13: 'bodySinkPartLurched',
            29: 'shootTorpedo',
            9: 'shootGuns',
            38: 'syncShipCracks',
            1: 'makeShipCracksActive',
            43: 'makeShipCracks',
            44: 'setReloadingStateTorpedoes',
            45: 'setReloadingStateArtillery',
            39: 'setConsumables',
            2: 'stopVarys',
            3: 'reflood',
            20: 'onShotDecal',
            14: 'receiveMirrorDamage',
            15: 'offlineSetAI',
            40: 'offlineRecieveMovementRoute',
            21: 'receiveVisibilityFactors',
            4: 'forceReloadTorpedoes',
            16: 'onSkillActivated',
            5: 'uniqueSkillActivated',
            10: 'onConsumableEnabled',
        }

        self.attributesMap = {
            25: 'atbaTargets',
            26: 'airDefenseTargetId',
            15: 'airDefenseDispRadius',
            0: 'isAntiAirMode',
            27: 'antiAirAuras',
            16: 'health',
            17: 'regenerationHealth',
            18: 'regeneratedHealth',
            1: 'burningFlags',
            2: 'isOnForsage',
            19: 'regenCrewHpLimit',
            20: 'buoyancy',
            12: 'targetLocalPos',
            13: 'torpedoLocalPos',
            14: 'weaponLockFlags',
            21: 'owner',
            28: 'shipConfig',
            24: 'crewModifiersCompactParams',
            3: 'teamId',
            4: 'isAlive',
            22: 'selectedWeapon',
            5: 'serverSpeedRaw',
            6: 'speedSignDir',
            7: 'enginePower',
            8: 'isInOfflineMode',
            9: 'ignoreMapBorders',
            29: 'debugText',
            10: 'isBot',
            30: 'miscsPresetsStatus',
            23: 'draught',
            11: 'isFogHornOn'
        }

        super(Vehicle, self).__init__()

    def getLearnedSkills(self):
        """
        Skill has his own skill id.
        Packed format = sum(2 ** skill_id for skill_id in skills)
        So to turn it back, we must divide number by two;
        """
        learned_skills = self.crewModifiersCompactParams['learnedSkills']
        skill_id = 1
        while learned_skills != 0:
            if learned_skills % 2 == 1:
                yield skill_id
            learned_skills /= 2
            skill_id += 1
