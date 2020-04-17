# coding=utf-8

property_id_map = {'crewParams': 6, 'isLeaver': 18, 'camouflageInfo': 2, 'clanID': 4, 'dogTag': 7, 'isBot': 14,
                   'shipId': 29, 'avatarId': 1, 'id': 10, 'ttkStatus': 33, 'realm': 27, 'clanColor': 3,
                   'killedBuildingsCount': 20, 'playerMode': 23, 'maxHealth': 21, 'preBattleSign': 25, 'isAbuser': 12,
                   'clanTag': 5, 'isHidden': 17, 'isAlive': 13, 'preBattleIdOnStart': 24, 'prebattleId': 26,
                   'accountDBID': 0, 'isConnected': 16, 'isPreBattleOwner': 19, 'shipParamsId': 30,
                   'shipComponents': 28, 'name': 22, 'teamId': 32, 'invitationsEnabled': 11, 'fragsCount': 8,
                   'skinId': 31, 'friendlyFireEnabled': 9, 'isClientLoaded': 15}
id_property_map = {value: key for key, value in property_id_map.items()}


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
