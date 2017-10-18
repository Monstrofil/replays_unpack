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

f = open('Teinor.csv', 'wb')
print Player._fields
w = csv.DictWriter(f, Player._fields, delimiter=';')
w.writeheader()

for i, file in enumerate(listdir(BASE_DIR)):
    print file
    players = {}

    replayInfo = ReplayParser(path.join(BASE_DIR, file)).get_info()['hidden']

    if replayInfo is None:
        print 'UNKNOWN result'
        continue
    winnerTeamId = replayInfo['battle_result']['winner_team_id']

    for player in replayInfo['players'].itervalues():
        vehicleId = player['shipId']
        players[vehicleId] = Player(
            DATABASE_ID=player['accountDBID'],
            NAME=player['name'],
            GOLD=300 if player['teamId'] == winnerTeamId else 0,
            REPLAY=file
        )

    vehicleId = next(player['shipId'] for player in replayInfo['players'].itervalues() if player['avatarId'] == replayInfo['player_id'])
    killerVehicleId = next((killer for victim, killer, _ in replayInfo['death_map'] if victim == vehicleId), -1)

    if killerVehicleId != -1:
        players[killerVehicleId] = Player(
                DATABASE_ID=players[killerVehicleId].DATABASE_ID,
                NAME=players[killerVehicleId].NAME,
                GOLD=players[killerVehicleId].GOLD + 500,
                REPLAY=players[killerVehicleId].REPLAY
        )

    w.writerows(dict(zip(Player._fields, p)) for p in players.values())

f.close()
