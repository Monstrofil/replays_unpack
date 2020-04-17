# coding=utf-8

id_property_map = {0: 'accountDBID', 1: 'avatarId', 2: 'camouflageInfo', 3: 'clanColor', 4: 'clanID', 5: 'clanTag',
                   6: 'crewParams', 7: 'dogTag', 8: 'fragsCount', 9: 'friendlyFireEnabled', 10: 'id',
                   11: 'invitationsEnabled', 12: 'isAbuser', 13: 'isAlive', 14: 'isBot', 15: 'isClientLoaded',
                   16: 'isConnected', 17: 'isHidden', 18: 'isLeaver', 19: 'isPreBattleOwner', 20: 'isSpectator',
                   21: 'killedBuildingsCount', 22: 'maxHealth', 23: 'name', 24: 'preBattleIdOnStart',
                   25: 'preBattleSign', 26: 'prebattleId', 27: 'realm', 28: 'shipComponents', 29: 'shipId',
                   30: 'shipParamsId', 31: 'skinId', 32: 'teamId', 33: 'ttkStatus'}
property_id_map = {value: key for key, value in id_property_map.items()}


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
