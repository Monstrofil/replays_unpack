#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

id_property_map = {
    0: 'accountDBID',
    1: 'avatarId',
    2: 'clanTag',
    3: 'crewParams',
    4: 'fragsCount',
    5: 'id',
    6: 'invitationsEnabled',
    7: 'isAbuser',
    8: 'isAlive',
    9: 'isBot',
    10: 'isClientLoaded',
    11: 'isConnected',
    12: 'isHidden',
    13: 'isLeaver',
    14: 'isPreBattleOwner',
    15: 'killedBuildingsCount',
    16: 'maxHealth',
    17: 'name',
    18: 'preBattleIdOnStart',
    19: 'preBattleSign',
    20: 'prebattleId',
    21: 'rankInfoDump',
    22: 'shipComponents',
    23: 'shipId',
    24: 'shipParamsId',
    25: 'teamId',
    26: 'ttkStatus'
}

property_id_map = {value: key for key, value in id_property_map.items()}
