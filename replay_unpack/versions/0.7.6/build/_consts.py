#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

property_id_map = {'crewParams': 5, 'isLeaver': 16, 'isConnected': 14, 'clanID': 3, 'dogTag': 6, 'isBot': 12, 'shipId': 26, 'avatarId': 1, 'id': 8, 'ttkStatus': 30, 'clanColor': 2, 'killedBuildingsCount': 18, 'maxHealth': 19, 'preBattleSign': 22, 'isAbuser': 10, 'clanTag': 4, 'isHidden': 15, 'isAlive': 11, 'preBattleIdOnStart': 21, 'prebattleId': 23, 'accountDBID': 0, 'isPreBattleOwner': 17, 'shipParamsId': 27, 'shipComponents': 25, 'name': 20, 'teamId': 29, 'invitationsEnabled': 9, 'fragsCount': 7, 'skinId': 28, 'isClientLoaded': 13, 'rankInfoDump': 24}
id_property_map = {value: key for key, value in property_id_map.items()}


class DamageStatsType:
    """See Avatar.DamageStatsType"""
    DAMAGE_STATS_ENEMY = 0
    DAMAGE_STATS_ALLY = 1
    DAMAGE_STATS_SPOT = 2
    DAMAGE_STATS_AGRO = 3
