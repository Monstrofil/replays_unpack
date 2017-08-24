#!/usr/bin/python
# coding=utf-8
import os
import sys
from StringIO import StringIO

__author__ = "Aleksandr Shyshatsky"


class ReplayParser(object):
    BASE_PATH = os.path.dirname(__file__)

    def __init__(self, replay_path):
        self._replay_path = replay_path
        from replay_unpack.replay_decrypt import WoWSReplayDecrypt
        self._decrypter = WoWSReplayDecrypt(replay_path)

    def get_info(self):
        from replay_unpack.sentry import client
        json_data, replay_data = self._decrypter.get_replay_data()

        client_version = '.'.join(json_data['clientVersionFromXml'].split(', ')[:3])
        sys.path.append(os.path.join(self.BASE_PATH, 'replay_unpack', 'versions', client_version))

        try:
            hidden_data = self._get_hidden_data(replay_data)
        except Exception as e:
            client.captureException()
            hidden_data = None

        return dict(
            open=json_data,
            hidden=hidden_data
        )

    def _get_hidden_data(self, replay_data):
        from replay_unpack.replay_player import ReplayPlayer
        from replay_unpack.base.packets.BigWorldPacket import BigWorldPacket
        player = ReplayPlayer()
        io = StringIO(replay_data)
        while io.pos != io.len:
            packet = BigWorldPacket(io)
            player.on_packet(packet)
        return player.get_info()
