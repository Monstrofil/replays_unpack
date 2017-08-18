#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

property_id_map = {
    'accountDBID': 0,
    'avatarId': 1,
    'clanTag': 2,
    'crewParams': 3,
    'fragsCount': 4,
    'id': 5,
    'invitationsEnabled': 6,
    'isAbuser': 7,
    'isAlive': 8,
    'isBot': 9,
    'isClientLoaded': 10,
    'isConnected': 11,
    'isHidden': 12,
    'isLeaver': 13,
    'isPreBattleOwner': 14,
    'killedBuildingsCount': 15,
    'maxHealth': 16,
    'name': 17,
    'preBattleIdOnStart': 18,
    'preBattleSign': 19,
    'prebattleId': 20,
    'rankInfoDump': 21,
    'shipComponents': 22,
    'shipId': 23,
    'shipParamsId': 24,
    'teamId': 25,
    'ttkStatus': 26
}

id_property_map = {value: key for key, value in property_id_map.items()}
