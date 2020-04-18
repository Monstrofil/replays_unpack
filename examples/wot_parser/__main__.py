#!/usr/bin/python
# coding=utf-8

from replay_unpack.replay_reader import ReplayReader
from wot_parser.player import ReplayPlayer

if __name__ == "__main__":
    reader = ReplayReader(r"C:\Users\shish\Desktop\15866367817879_ussr_R171_IS_3_II_canada_a.wotreplay")
    replay = reader.get_replay_data()

    version = '.'.join(replay.engine_data.get('clientVersionFromXml')
                       .replace('World of Tanks v.', '')
                       .replace(' ', '.')
                       .replace('#', '')
                       .split('.')[:3])

    player = ReplayPlayer(version)
    player.play(replay.decrypted_data, strict_mode=True)
