#!/usr/bin/python
# coding=utf-8
import pickle

from replay_unpack.base.PlayersInfo import PlayersInfo
from Avatar import Avatar
from Vehicle import Vehicle

__author__ = "Aleksandr Shyshatsky"


class BattleController(object):
    def __init__(self, bigworld):
        self._achievements = {}
        self._ribbons = {}
        self._players = PlayersInfo()
        self._battle_result = None
        self._damage_map = {}
        self._shots_damage_map = {}
        self._death_map = []
        self._map = {}
        self._player_id = None

        self._dead_planes = []

        Avatar.g_onBattleEnd += self.onBattleEnd
        Avatar.g_onArenaStateReceived += self.onArenaStateReceived
        Avatar.g_onGameRoomStateChanged += self.onPlayerInfoUpdate
        Avatar.g_receiveVehicleDeath += self.receiveVehicleDeath
        Avatar.g_onRibbon += self.onRibbon
        Avatar.g_onAchievementEarned += self.onAchievementEarned
        Avatar.g_receiveDamageStat += self.receiveDamageStat
        Avatar.g_receive_planeDeath += self.receive_planeDeath

        Avatar.g_onBattleAchievementsRestored += self.receiveShotPack

        Vehicle.g_receiveDamagesOnShip += self.g_receiveDamagesOnShip

    def get_info(self):
        return dict(
            achievements=self._achievements,
            ribbons=self._ribbons,
            players=self._players.get_info(),
            battle_result=self._battle_result,
            damage_map=self._damage_map,
            shots_damage_map=self._shots_damage_map,
            death_map=self._death_map,
            map=self._map,
            player_id=self._player_id
        )

    def onBattleEnd(self, avatar, teamId, state):
        self._battle_result = dict(
            winner_team_id=teamId,
            victory_type=state
        )

    def onArenaStateReceived(self, avatar, arena_info):
        self._players.create_or_update_players(
            pickle.loads(arena_info['playersStates']))

    def onPlayerInfoUpdate(self, avatar, blob):
        self._players.create_or_update_players(
            pickle.loads(blob))

    def receiveDamageStat(self, avatar, blob):
        normalized = {}
        for (type_, bool_), value in pickle.loads(blob).items():
            normalized.setdefault(type_, {}).setdefault(bool_, 0)
            normalized[type_][bool_] = value
        self._damage_map.update(normalized)

    def onRibbon(self, avatar, ribbon_id):
        self._ribbons.setdefault(avatar.id, {}).setdefault(ribbon_id, 0)
        self._ribbons[avatar.id][ribbon_id] += 1

    def onAchievementEarned(self, avatar, avatar_id, achievement_id):
        self._achievements.setdefault(avatar_id, {}).setdefault(achievement_id, 0)
        self._achievements[avatar_id][achievement_id] += 1

    def receiveVehicleDeath(self, avatar, killedVehicleId, fraggerVehicleId, typeDeath):
        self._death_map.append((killedVehicleId, fraggerVehicleId, typeDeath))

    def g_receiveDamagesOnShip(self, vehicle, damages):
        for damage_info in damages:
            self._shots_damage_map.setdefault(vehicle.id, {}).setdefault(damage_info['vehicleID'], 0)
            self._shots_damage_map[vehicle.id][damage_info['vehicleID']] += damage_info['damage']

    def receive_planeDeath(self, avatar, planeID, reason, attackerId):
        self._dead_planes.append((planeID, reason, attackerId))

    def receiveShotPack(self, avatar, *args):
        print args

    @property
    def map(self):
        raise NotImplemented()

    @map.setter
    def map(self, value):
        self._map = value.lstrip('spaces/')

    @property
    def player_id(self):
        raise NotImplemented()

    @player_id.setter
    def player_id(self, value):
        self._player_id = value
