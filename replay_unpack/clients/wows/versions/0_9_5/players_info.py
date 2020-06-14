# coding=utf-8
from .constants import id_property_map


class PlayersInfo(object):
    def __init__(self):
        self._players = {}

    def _convert_to_dict(self, player_info):
        # type: (list[tuple]) -> dict
        player_dict = dict()
        for key, value in player_info:
            player_dict[id_property_map[key]] = value
        return player_dict

    def create_or_update_players(self, players_info):
        for player_info in players_info:
            player_dict = self._convert_to_dict(player_info)

            self._players.setdefault(player_dict['id'], {}).update(player_dict)

    def get_info(self):
        return self._players

    def __repr__(self):
        return str(self._players)
