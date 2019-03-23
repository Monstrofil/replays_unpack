#!/usr/bin/python
# coding=utf-8
import json
import os
import sys
import logging
from io import BytesIO as StringIO

from replay_unpack.base.packets.BigWorldPacket import BigWorldPacket
from replay_unpack.replay_decrypt import WoWSReplayDecrypt

__author__ = "Aleksandr Shyshatsky"


class ReplayParser(object):
    BASE_PATH = os.path.dirname(__file__)

    def __init__(self, replay_path):
        self._replay_path = replay_path
        self._decrypter = WoWSReplayDecrypt(replay_path)

    def get_info(self):
        json_data, replay_data = self._decrypter.get_replay_data()

        client_version = '.'.join(json_data['clientVersionFromXml'].split(', ')[:3])
        error = None
        try:
            hidden_data = self._get_hidden_data(replay_data, client_version)
        except RuntimeError as e:
            error = str(e)
            hidden_data = None
        except Exception as e:
            logging.exception(e)
            hidden_data = None

        return dict(
            open=json_data,
            hidden=hidden_data,
            error=error
        )

    def _get_hidden_data(self, replay_data: bytes, client_version: str):
        from replay_unpack.replay_player import ReplayPlayer
        player = ReplayPlayer(client_version)
        io = StringIO(replay_data)
        while io.tell() != len(replay_data):
            packet = BigWorldPacket(io)
            # noinspection PyBroadException
            try:
                player.on_packet(packet)
            except Exception:
                logging.error("Problem with packet %s:%s:%s", packet.time, packet.type, type(packet.data))
                raise
        return player.get_info()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=str, required=True)
    parser.add_argument(
        '--log_level',
        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
        required=False,
        default='ERROR'
    )

    namespace = parser.parse_args()
    logging.basicConfig(
        level=getattr(logging, namespace.log_level))
    replay_info = ReplayParser(namespace.replay).get_info()
    print(json.dumps(replay_info, indent=1))
