#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

property_id_map = {'crewParams': 5, 'isLeaver': 17, 'isConnected': 15, 'clanID': 3, 'dogTag': 6, 'isBot': 13, 'shipId': 28, 'avatarId': 1, 'id': 9, 'ttkStatus': 32, 'realm': 26, 'clanColor': 2, 'killedBuildingsCount': 19, 'maxHealth': 20, 'preBattleSign': 23, 'isAbuser': 11, 'clanTag': 4, 'isHidden': 16, 'isAlive': 12, 'preBattleIdOnStart': 22, 'prebattleId': 24, 'accountDBID': 0, 'isPreBattleOwner': 18, 'shipParamsId': 29, 'shipComponents': 27, 'name': 21, 'teamId': 31, 'invitationsEnabled': 10, 'fragsCount': 7, 'skinId': 30, 'friendlyFireEnabled': 8, 'isClientLoaded': 14, 'rankInfoDump': 25}
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
