#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

id_property_map = {0: 'accountDBID', 1: 'avatarId', 2: 'clanColor', 3: 'clanID', 4: 'clanTag', 5: 'crewParams', 6: 'dogTag', 7: 'fragsCount', 8: 'id', 9: 'invitationsEnabled', 10: 'isAbuser', 11: 'isAlive', 12: 'isBot', 13: 'isClientLoaded', 14: 'isConnected', 15: 'isHidden', 16: 'isLeaver', 17: 'isPreBattleOwner', 18: 'killedBuildingsCount', 19: 'maxHealth', 20: 'name', 21: 'preBattleIdOnStart', 22: 'preBattleSign', 23: 'prebattleId', 24: 'rankInfoDump', 25: 'shipComponents', 26: 'shipId', 27: 'shipParamsId', 28: 'teamId', 29: 'ttkStatus'}

property_id_map = {value: key for key, value in id_property_map.items()}
