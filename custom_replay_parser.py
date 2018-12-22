#!/usr/bin/python
# coding=utf-8
import os
import sys
from StringIO import StringIO

from replay_unpack.base.DamageRecord import DamageRecord
from replay_unpack.base.packets.BigWorldPacket import BigWorldPacket
from replay_unpack.replay_decrypt import WoWSReplayDecrypt


class CustomReplayParser():
    def __init__(self, replay_path):
        self._replay_path = replay_path
        self._decrypter = WoWSReplayDecrypt(replay_path)
        self.json_data, self.replay_data = self._decrypter.get_replay_data()

        client_version = '.'.join(self.json_data['clientVersionFromXml'].split(', ')[:3])
        sys.path.append(os.path.join(os.path.dirname(__file__), 'replay_unpack', 'versions', client_version))

        from replay_unpack.replay_player import ReplayPlayer
        self.player = ReplayPlayer()

        self.packets = []
        self.damage_list = []

        self.customBinding()
        self._load_data()
        pass

    def _load_data(self):
        io = StringIO(self.replay_data)
        while io.pos != io.len:
            packet = BigWorldPacket(io)
            self.player.on_packet(packet)
            self.packets.append(packet)

    def customBinding(self):
        try:
            from build.entities import Vehicle
            Vehicle.g_receiveDamagesOnShip += self._customDamageRecord
        except Exception as e:
            pass

    def _customDamageRecord(self, vehicle, damages):
        for damage_info in damages:
            record = DamageRecord(self.packets[-1].time, vehicle, damage_info['vehicleID'], damage_info['damage'])
            o = (list(map(lambda x:{'owner':x.owner,'pos':x.position},self.get_all_ships())))
            self.damage_list.append(record)

    def get_all_ships(self):
        return list(filter(lambda x: 'vehicle' in str(type(x)).lower(), self._get_world().entities.values()))

    def get_ship_by_owner_id(self, ownerId):
        return self._get_world().entities[ownerId]
        vehicles = list(filter(lambda x: x.owner == ownerId, self.get_all_ships()))
        if len(vehicles) != 0:
            return vehicles[-1]
        else:
            return None

    def _get_world(self):
        return self.player._bigworld
