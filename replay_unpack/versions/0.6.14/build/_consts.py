#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

id_property_map = {0: 'accountDBID', 1: 'avatarId', 2: 'clanColor', 3: 'clanID', 4: 'clanTag', 5: 'crewParams', 6: 'fragsCount', 7: 'id', 8: 'invitationsEnabled', 9: 'isAbuser', 10: 'isAlive', 11: 'isBot', 12: 'isClientLoaded', 13: 'isConnected', 14: 'isHidden', 15: 'isLeaver', 16: 'isPreBattleOwner', 17: 'killedBuildingsCount', 18: 'maxHealth', 19: 'name', 20: 'preBattleIdOnStart', 21: 'preBattleSign', 22: 'prebattleId', 23: 'rankInfoDump', 24: 'shipComponents', 25: 'shipId', 26: 'shipParamsId', 27: 'teamId', 28: 'ttkStatus'}

property_id_map = {value: key for key, value in id_property_map.items()}
