#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

id_property_map = {0: 'accountDBID', 1: 'avatarId', 2: 'clanColor', 3: 'clanID', 4: 'clanTag', 5: 'crewParams', 6: 'dogTag', 7: 'fragsCount', 8: 'friendlyFireEnabled', 9: 'id', 10: 'invitationsEnabled', 11: 'isAbuser', 12: 'isAlive', 13: 'isBot', 14: 'isClientLoaded', 15: 'isConnected', 16: 'isHidden', 17: 'isLeaver', 18: 'isPreBattleOwner', 19: 'isSpectator', 20: 'killedBuildingsCount', 21: 'maxHealth', 22: 'name', 23: 'preBattleIdOnStart', 24: 'preBattleSign', 25: 'prebattleId', 26: 'rankInfoDump', 27: 'realm', 28: 'shipComponents', 29: 'shipId', 30: 'shipParamsId', 31: 'skinId', 32: 'teamId', 33: 'ttkStatus'}
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
