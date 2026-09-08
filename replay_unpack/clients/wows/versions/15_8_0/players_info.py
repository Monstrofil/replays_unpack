# coding=utf-8
import logging
import struct

from replay_unpack.core.unicoding import unicodize
from .constants import (
    id_property_map,
    id_property_map_bots,
    id_property_map_observer
)

try:
    from .constants import UNIT_TYPE_NAMES, SLOT_SYSTEMS
except ImportError:
    UNIT_TYPE_NAMES = SLOT_SYSTEMS = None

logger = logging.getLogger(__name__)


def decode_ship_config_dump(data):
    """Decode binary shipConfigDump into a structured dict."""
    if UNIT_TYPE_NAMES is None or SLOT_SYSTEMS is None:
        return None
    if not data or len(data) < 16:
        return None

    try:
        values = struct.unpack(f'<{len(data) // 4}I', data)
    except struct.error:
        return None

    it = iter(values)
    result = {}
    result['version'] = next(it)
    result['shipConfigId'] = next(it)
    next(it)  # total count

    n_units = next(it)
    components = {}
    for i in range(n_units):
        v = next(it)
        if v and i < len(UNIT_TYPE_NAMES):
            components[UNIT_TYPE_NAMES[i]] = v
    result['components'] = components

    result['externalConfigId'] = next(it)

    for slot in SLOT_SYSTEMS:
        n = next(it)
        items = [next(it) for _ in range(n)]
        result[slot['name']] = [x for x in items if x]
        if slot['has_autobuy']:
            result[slot['name'] + '_autobuy'] = next(it)
        if slot['has_color_schemes']:
            n_schemes = next(it)
            result['color_schemes'] = {next(it): next(it) for _ in range(n_schemes)}

    result['naval_flag_id'] = next(it)
    return result


class PlayerType:
    PLAYER = 1
    BOT = 2
    OBSERVER = 3


class PlayersInfo(object):
    def __init__(self):
        self._players = {}

    def _convert_to_dict(self, player_info, player_type):
        # type: (list[tuple], int) -> dict
        if player_type == PlayerType.PLAYER:
            property_map = id_property_map
        elif player_type == PlayerType.BOT:
            property_map = id_property_map_bots
        elif player_type == PlayerType.OBSERVER:
            property_map = id_property_map_observer
        else:
            raise RuntimeError('Unknown player')

        player_dict = dict()
        for key, value in player_info:
            # wargaming still uses python 2 which has poor unicode support
            # as we are unpickling the data, we have to guess what is unicode
            # and what was originally intended to be bytes
            value = unicodize(value)
            player_dict[property_map[key]] = value

        if 'shipConfigDump' in player_dict:
            decoded = decode_ship_config_dump(player_dict['shipConfigDump'])
            if decoded is not None:
                player_dict['shipConfigDump'] = decoded

        return player_dict

    def create_or_update_players(self, players_info, players_type=PlayerType.PLAYER):
        for player_info in players_info:
            player_dict = self._convert_to_dict(player_info, players_type)

            self._players.setdefault(player_dict['id'], {}).update(player_dict)

    def get_info(self):
        return self._players

    def __repr__(self):
        return str(self._players)
