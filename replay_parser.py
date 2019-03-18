#!/usr/bin/python
# coding=utf-8
import json
import os
import sys
import logging
from io import BytesIO as StringIO

from replay_unpack.base.packets.BigWorldPacket import BigWorldPacket
from replay_unpack.replay_decrypt import WoWSReplayDecrypt
from replay_unpack.sentry import client

__author__ = "Aleksandr Shyshatsky"


def silence_stdout_until_process_exit():
    """
    Upon process exit, Sentry sometimes prints:

        Sentry is attempting to send 1 pending error messages
        Waiting up to 10 seconds
        Press Ctrl-C to quit

    This causes us to get emails from cron which are useless noise, since the
    exceptions end up in sentry anyway. "Real" exceptions print to stderr, not
    stdout, so this shouldn't silence anything important.

    See also this issue: https://github.com/getsentry/raven-python/issues/904
    """
    sys.stdout = StringIO()


class ReplayParser(object):
    BASE_PATH = os.path.dirname(__file__)

    def __init__(self, replay_path):
        self._replay_path = replay_path
        self._decrypter = WoWSReplayDecrypt(replay_path)

    def get_info(self):
        json_data, replay_data = self._decrypter.get_replay_data()

        client_version = '.'.join(json_data['clientVersionFromXml'].split(', ')[:3])
        sys.path.append(os.path.join(self.BASE_PATH, 'replay_unpack', 'versions', client_version))
        client.tags["clientVersionFromXml"] = client_version

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
                logging.error("Problem with packet %s:%s", packet.time, packet.type)
                raise
        return player.get_info()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=str, required=True)
    parser.add_argument('--debug', action='store_true', required=False)

    namespace = parser.parse_args()
    logging.basicConfig(
        level=logging.DEBUG if namespace.debug else logging.CRITICAL)
    replay_info = ReplayParser(namespace.replay).get_info()
    print(json.dumps(replay_info, indent=1))
    silence_stdout_until_process_exit()
