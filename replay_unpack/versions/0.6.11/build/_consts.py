#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

id_property_map = {0: 'accountDBID', 1: 'avatarId', 2: 'clanID', 3: 'clanTag', 4: 'crewParams', 5: 'fragsCount',
                   6: 'id', 7: 'invitationsEnabled', 8: 'isAbuser', 9: 'isAlive', 10: 'isBot', 11: 'isClientLoaded',
                   12: 'isConnected', 13: 'isHidden', 14: 'isLeaver', 15: 'isPreBattleOwner',
                   16: 'killedBuildingsCount', 17: 'maxHealth', 18: 'name', 19: 'preBattleIdOnStart',
                   20: 'preBattleSign', 21: 'prebattleId', 22: 'rankInfoDump', 23: 'shipComponents', 24: 'shipId',
                   25: 'shipParamsId', 26: 'teamId', 27: 'ttkStatus'}

property_id_map = {value: key for key, value in id_property_map.items()}
