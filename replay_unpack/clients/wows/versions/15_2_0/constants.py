# coding=utf-8

id_property_map = {0: 'accountDBID', 1: 'antiAbuseEnabled', 2: 'avatarId', 3: 'camouflageInfo',
                   4: 'clanColor', 5: 'clanID', 6: 'clanTag', 7: 'crewParams', 8: 'dogTag',
                   9: 'fragsCount', 10: 'friendlyFireEnabled', 11: 'id', 12: 'invitationsEnabled',
                   13: 'isAbuser', 14: 'isAlive', 15: 'isBot', 16: 'isClientLoaded', 17: 'isConnected',
                   18: 'isHidden', 19: 'isLeaver', 20: 'isPreBattleOwner', 21: 'isTShooter', 22: 'keyTargetMarkers',
                   23: 'killedBuildingsCount', 24: 'maxHealth', 25: 'name', 26: 'playerMode', 27: 'preBattleIdOnStart',
                   28: 'preBattleSign', 29: 'prebattleId', 30: 'realm', 31: 'shipComponents', 32: 'shipConfigDump',
                   33: 'shipId', 34: 'shipParamsId', 35: 'skinId', 36: 'teamId', 37: 'ttkStatus'}
property_id_map = {value: key for key, value in id_property_map.items()}

# ModsShell.API_v_1_0.battleGate.PlayersInfo.gSharedBotInfo._numMemberMap
id_property_map_bots = {0: 'accountDBID', 1: 'antiAbuseEnabled', 2: 'camouflageInfo', 3: 'clanColor',
                        4: 'clanID', 5: 'clanTag', 6: 'crewParams', 7: 'dogTag', 8: 'fragsCount',
                        9: 'friendlyFireEnabled', 10: 'id', 11: 'isAbuser', 12: 'isAlive',
                        13: 'isBot', 14: 'isHidden', 15: 'isTShooter', 16: 'keyTargetMarkers',
                        17: 'killedBuildingsCount', 18: 'maxHealth', 19: 'name', 20: 'realm',
                        21: 'shipComponents', 22: 'shipConfigDump', 23: 'shipId', 24: 'shipParamsId',
                        25: 'skinId', 26: 'teamId', 27: 'ttkStatus'}
property_id_map_bots = {value: key for key, value in id_property_map.items()}


# ModsShell.API_v_1_0.battleGate.PlayersInfo.gSharedObserverInfo._numMemberMap
id_property_map_observer = {0: 'accountDBID', 1: 'avatarId', 2: 'dogTag', 3: 'id', 4: 'invitationsEnabled', 5: 'isAlive',
                            6: 'isClientLoaded', 7: 'isConnected', 8: 'isLeaver', 9: 'isPreBattleOwner', 10: 'name',
                            11: 'playerMode', 12: 'preBattleIdOnStart', 13: 'preBattleSign', 14: 'prebattleId',
                            15: 'realm', 16: 'teamId'}
property_id_map_bots_observer = {value: key for key, value in id_property_map.items()}



class DamageStatsType:
    """See Avatar.DamageStatsType"""
    DAMAGE_STATS_ENEMY = 0
    DAMAGE_STATS_ALLY = 1
    DAMAGE_STATS_SPOT = 2
    DAMAGE_STATS_AGRO = 3


class Category(object):
    """Category of task to separate for UI"""

    CHALLENGE = 4
    PRIMARY = 1
    SECONDARY = 2
    TERTIARY = 3

    ids = {'Challenge': 4, 'Primary': 1, 'Secondary': 2, 'Tertiary': 3}
    names = {1: 'Primary', 2: 'Secondary', 3: 'Tertiary', 4: 'Challenge'}


class Status(object):
    CANCELED = 4
    FAILURE = 3
    IN_PROGRESS = 1
    NOT_STARTED = 0
    SUCCESS = 2
    UPDATED = 5

    ids = {'Updated': 5, 'Success': 2, 'Canceled': 4, 'NotStarted': 0, 'Failure': 3, 'InProgress': 1}
    names = {0: 'NotStarted', 1: 'InProgress', 2: 'Success', 3: 'Failure', 4: 'Canceled', 5: 'Updated'}


class TaskType(object):
    DIGIT = 1
    DIGIT_SINGLE = 5
    NO_TYPE = 0
    PROGRESS_BAR = 4
    REVERSED_TIMER = 3
    TIMER = 2

    names = {0: 'NoType', 1: 'Digit', 2: 'Timer', 3: 'ReversedTimer', 4: 'ProgressBar', 5: 'DigitSingle'}
    ids = {'ReversedTimer': 3, 'Digit': 1, 'DigitSingle': 5, 'Timer': 2, 'ProgressBar': 4, 'NoType': 0}


# {i: vars(j) for i,j in Vehicle.DeathReason._DeathReason__byId.items()}
DEATH_TYPES = {
    0: {'sound': 'Health', 'icon': 'frags', 'id': 0, 'name': 'NONE'},
    1: {'sound': 'Health', 'icon': 'frags', 'id': 1, 'name': 'ARTILLERY'},
    2: {'sound': 'ATBA', 'icon': 'icon_frag_atba', 'id': 2, 'name': 'ATBA'},
    3: {'sound': 'Torpedo', 'icon': 'icon_frag_torpedo', 'id': 3, 'name': 'TORPEDO'},
    4: {'sound': 'Bomb', 'icon': 'icon_frag_bomb', 'id': 4, 'name': 'BOMB'},
    5: {'sound': 'Torpedo', 'icon': 'icon_frag_torpedo', 'id': 5, 'name': 'TBOMB'},
    6: {'sound': 'Burning', 'icon': 'icon_frag_burning', 'id': 6, 'name': 'BURNING'},
    7: {'sound': 'RAM', 'icon': 'icon_frag_ram', 'id': 7, 'name': 'RAM'},
    8: {'sound': 'Health', 'icon': 'frags', 'id': 8, 'name': 'TERRAIN'},
    9: {'sound': 'Flood', 'icon': 'icon_frag_flood', 'id': 9, 'name': 'FLOOD'},
    10: {'sound': 'Health', 'icon': 'frags', 'id': 10, 'name': 'MIRROR'},
    11: {'sound': 'Torpedo', 'icon': 'icon_frag_naval_mine', 'id': 11, 'name': 'SEA_MINE'},
    12: {'sound': 'Health', 'icon': 'frags', 'id': 12, 'name': 'SPECIAL'},
    13: {'sound': 'DepthCharge', 'icon': 'icon_frag_depthbomb', 'id': 13, 'name': 'DBOMB'},
    14: {'sound': 'Rocket', 'icon': 'icon_frag_rocket', 'id': 14, 'name': 'ROCKET'},
    15: {'sound': 'Detonate', 'icon': 'icon_frag_detonate', 'id': 15, 'name': 'DETONATE'},
    16: {'sound': 'Health', 'icon': 'frags', 'id': 16, 'name': 'HEALTH'},
    17: {'sound': 'Shell_AP', 'icon': 'icon_frag_main_caliber', 'id': 17, 'name': 'AP_SHELL'},
    18: {'sound': 'Shell_HE', 'icon': 'icon_frag_main_caliber', 'id': 18, 'name': 'HE_SHELL'},
    19: {'sound': 'Shell_CS', 'icon': 'icon_frag_main_caliber', 'id': 19, 'name': 'CS_SHELL'},
    20: {'sound': 'Fel', 'icon': 'icon_frag_fel', 'id': 20, 'name': 'FEL'},
    21: {'sound': 'Portal', 'icon': 'icon_frag_portal', 'id': 21, 'name': 'PORTAL'},
    22: {'sound': 'SkipBomb', 'icon': 'icon_frag_skip', 'id': 22, 'name': 'SKIP_BOMB'},
    23: {'sound': 'SECTOR_WAVE', 'icon': 'icon_frag_wave', 'id': 23, 'name': 'SECTOR_WAVE'},
    24: {'sound': 'Health', 'icon': 'icon_frag_acid', 'id': 24, 'name': 'ACID'},
    25: {'sound': 'LASER', 'icon': 'icon_frag_laser', 'id': 25, 'name': 'LASER'},
    26: {'sound': 'Match', 'icon': 'icon_frag_octagon', 'id': 26, 'name': 'MATCH'},
    27: {'sound': 'Timer', 'icon': 'icon_timer', 'id': 27, 'name': 'TIMER'},
    28: {'sound': 'DepthCharge', 'icon': 'icon_frag_depthbomb', 'id': 28, 'name': 'ADBOMB'}
}

# >>> CrewModifiers.SkillTypeEnum.ID_TO_NAME
SKILL_TYPE_ID_TO_NAME = {
    0: 'NoneSkill', 1: 'GmReloadAaDamageConstant', 2: 'DefenceCritFireFlooding', 3: 'GmTurn', 4: 'TorpedoReload',
    5: 'ConsumablesCrashcrewRegencrewReload', 6: 'ConsumablesDuration', 7: 'DetectionTorpedoRange',
    8: 'HeFireProbability',
    9: 'GmRangeAaDamageBubbles', 10: 'PlanesDefenseDamageConstant', 11: 'PlanesForsageDuration',
    12: 'DetectionVisibilityRange', 13: 'ConsumablesReload', 14: 'DefenceFireProbability', 15: 'PlanesAimingBoost',
    16: 'PlanesSpeed', 17: 'ConsumablesAdditional', 18: 'DefenseCritProbability', 19: 'DetectionAlert',
    20: 'Maneuverability', 21: 'GmShellReload', 22: 'PlanesConsumablesCallfightersUpgrade',
    23: 'ArmamentReloadAaDamage',
    24: 'TorpedoSpeed', 25: 'DefenseHp', 26: 'AtbaAccuracy', 27: 'AaPrioritysectorDamageConstant',
    28: 'DetectionAiming',
    29: 'PlanesReload', 30: 'TorpedoDamage', 31: 'ConsumablesFighterAdditional',
    32: 'PlanesConsumablesSpeedboosterReload',
    33: 'HePenetration', 34: 'DetectionDirection', 35: 'AaDamageConstantBubbles', 36: 'AaDamageConstantBubblesCv',
    37: 'ApDamageBb', 38: 'ApDamageCa', 39: 'ApDamageDd', 40: 'AtbaRange', 41: 'AtbaUpgrade',
    42: 'ConsumablesCrashcrewRegencrewUpgrade', 43: 'ConsumablesSpotterUpgrade', 44: 'DefenceUw',
    45: 'DetectionVisibilityCrashcrew', 46: 'HeFireProbabilityCv', 47: 'HeSapDamage', 48: 'PlanesApDamage',
    49: 'PlanesConsumablesCallfightersAdditional', 50: 'PlanesConsumablesCallfightersPreparationtime',
    51: 'PlanesConsumablesCallfightersRange', 52: 'PlanesConsumablesRegeneratehealthUpgrade',
    53: 'PlanesDefenseDamageBubbles', 54: 'PlanesDivebomberSpeed', 55: 'PlanesForsageRenewal', 56: 'PlanesHp',
    57: 'PlanesTorpedoArmingrange', 58: 'PlanesTorpedoSpeed', 59: 'PlanesTorpedoUwReduced',
    60: 'TorpedoFloodingProbability', 61: 'TriggerSpeedBb', 62: 'TriggerGmAtbaReloadBb', 63: 'TriggerGmAtbaReloadCa',
    64: 'TriggerGmReload', 65: 'TriggerSpeed', 66: 'TriggerSpeedAccuracy', 67: 'TriggerSpreading',
    68: 'TriggerPingerReloadBuff', 69: 'TriggerPingerSpeedBuff', 70: 'SubmarineHoldSectors',
    71: 'TriggerConsSonarTimeCoeff', 72: 'TriggerSeenTorpedoReload', 73: 'SubmarineTorpedoPingDamage',
    74: 'TriggerConsRudderTimeCoeff', 75: 'SubmarineBatteryCapacity', 76: 'SubmarineDangerAlert',
    77: 'SubmarineBatteryBurnDown', 78: 'SubmarineSpeed', 79: 'SubmarineConsumablesReload',
    80: 'SubmarineConsumablesDuration', 81: 'TriggerBurnGmReload', 82: 'ArmamentReloadSubmarine'
}


# CrewModifiers.ShipTypes.TYPE_BY_ID
SHIP_TYPE_BY_ID = {
    0: 'AirCarrier',
    1: 'Battleship',
    2: 'Cruiser',
    3: 'Destroyer',
    4: 'Auxiliary',
    5: 'Submarine'
}
