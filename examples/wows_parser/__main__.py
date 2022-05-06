#!/usr/bin/python
# coding=utf-8

from replay_unpack.replay_reader import ReplayReader
from player import ReplayPlayer

if __name__ == "__main__":
    reader = ReplayReader(r"E:\Games\World_of_Warships_RU\replays\20210530_180427_PBSD510-Druid_38_Canada.wowsreplay")
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
