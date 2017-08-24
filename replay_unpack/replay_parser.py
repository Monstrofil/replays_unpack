#!/usr/bin/python
# coding=utf-8
import os
import sys
from StringIO import StringIO

from replay_unpack import WoWSReplayDecrypt, client, BigWorldPacket

__author__ = "Aleksandr Shyshatsky"


class ReplayParser(object):
    BASE_PATH = os.path.dirname(__file__)

    def __init__(self, replay_path):
        self._replay_path = replay_path
        self._decrypter = WoWSReplayDecrypt(replay_path)

    def get_info(self):
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
        player = ReplayPlayer()
        io = StringIO(replay_data)
        while io.pos != io.len:
            packet = BigWorldPacket(io)
            player.on_packet(packet)
        return player.get_info()