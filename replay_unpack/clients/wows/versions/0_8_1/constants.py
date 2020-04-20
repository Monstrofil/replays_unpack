# coding=utf-8

property_id_map = {'crewParams': 5, 'isLeaver': 16, 'isConnected': 14, 'clanID': 3, 'dogTag': 6, 'isBot': 12,
                   'shipId': 27, 'avatarId': 1, 'id': 8, 'ttkStatus': 31, 'realm': 25, 'clanColor': 2,
                   'killedBuildingsCount': 18, 'maxHealth': 19, 'preBattleSign': 22, 'isAbuser': 10, 'clanTag': 4,
                   'isHidden': 15, 'isAlive': 11, 'preBattleIdOnStart': 21, 'prebattleId': 23, 'accountDBID': 0,
                   'isPreBattleOwner': 17, 'shipParamsId': 28, 'shipComponents': 26, 'name': 20, 'teamId': 30,
                   'invitationsEnabled': 9, 'fragsCount': 7, 'skinId': 29, 'isClientLoaded': 13, 'rankInfoDump': 24}
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
