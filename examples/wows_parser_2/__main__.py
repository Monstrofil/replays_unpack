#!/usr/bin/python
# coding=utf-8
import argparse
import glob

from replay_unpack.replay_reader import ReplayReader
from player import ReplayPlayer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pattern', required=True)

    args = parser.parse_args()
    for path in glob.glob(args.pattern):
        print("Checking", path)

        reader = ReplayReader(path)
        replay = reader.get_replay_data()

        try:
            player = ReplayPlayer(replay.engine_data
                                  .get('clientVersionFromXml')
                                  .replace(' ', '')
                                  .split(','))
        except RuntimeError as e:
            print('skip', e)
        else:
            player.play(replay.decrypted_data, strict_mode=True)
