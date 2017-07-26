#!/usr/bin/python
# coding=utf-8
from StringIO import StringIO

from base.packets.BigWorldPacket import BigWorldPacket
from replay_decrypt import WoWSReplayDecrypt
from versions.packets import *
__author__ = "Aleksandr Shyshatsky"


class ReplayParser(object):
    def __init__(self, replay_path):
        self._replay_path = replay_path
        self._decrypter = WoWSReplayDecrypt(replay_path)

    def get_info(self):
        json_data, replay_data = self._decrypter.get_replay_data()
        io = StringIO(replay_data)

        entities = dict(
            types=dict(
                allies=set(),
                enemy=set(),
            ),
            positions=dict(),
            map=''
        )

        while io.pos != io.len:
            packet = BigWorldPacket(io)

            if isinstance(packet.data, Map):
                entities['map'] = packet.data.name

            if isinstance(packet.data, Position):
                position_data = {
                    'position': packet.data.position,
                    'rotation': packet.data.rotation
                }
                entities['positions'].setdefault(packet.time, {})[packet.data.avatarId] = position_data

            if isinstance(packet.data, Entity):
                # .setdefault(packet.data.type, set())
                if packet.time == 0:
                    entities['types']['allies'].add(packet.data.entityID)
                else:
                    entities['types']['enemy'].add(packet.data.entityID)
        return entities

# ReplayParser('play.wowsreplay').get_info()