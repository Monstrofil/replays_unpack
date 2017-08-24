#!/usr/bin/python
# coding=utf-8
import json
import os
import sys
from StringIO import StringIO

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

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=str, required=True)

    namespace = parser.parse_args()
    print json.dumps(ReplayParser(namespace.replay).get_info(), indent=1)
    silence_stdout_until_process_exit()
