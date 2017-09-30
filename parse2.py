#!/usr/bin/python
# coding=utf-8
import csv
from collections import namedtuple

__author__ = "Aleksandr Shyshatsky"

# Ваша команда победила вы живы Ваша команда получает по 300
# Ваша команда победила вас убили Ваша команда получает по 300, убивший - 500
# Ваша комнада проиграла вы живы Вражеская команда получает по 300
# Ваша комнада проиграла вас убили Вражеская команда получает по 300, убивший - 800

from replay_parser import ReplayParser

from os import listdir, path

BASE_DIR = r"C:\Users\shish\Desktop\replays"

Player = namedtuple('Player', [
    'DATABASE_ID',
    'NAME',
    'GOLD',
    'REPLAY'
])

f = open('report.csv', 'wb')
print Player._fields
w = csv.DictWriter(f, Player._fields, delimiter=';')
w.writeheader()

for i, file in enumerate(listdir(BASE_DIR)):
    print file
    players = {}
    info = ReplayParser(path.join(BASE_DIR, file)).get_info()

    replayInfo = info['hidden']
    if replayInfo is None:
        print 'OOOPS', info
        continue
    player_id = replayInfo['player_id']

    for player in replayInfo['players'].itervalues():
        if player['avatarId'] == player_id:
            if player_id in replayInfo['achievements']:
                print player
                p = Player(
                    DATABASE_ID=player['accountDBID'],
                    NAME=player['name'],
                    GOLD=1,
                    REPLAY=file
                )
                w.writerow(dict(zip(Player._fields, p)))

f.close()
