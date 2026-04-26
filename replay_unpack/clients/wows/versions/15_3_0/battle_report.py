# coding=utf-8
"""Build a machine-consumable, extensible battle-report structure from raw post_battle.

Output shape:
    {
      "tabs": {
        "<tab_id>": {
          "sections": {
            "<section_id>": {"kind": "list"|"object", "data": ...},
          },
        },
      },
    }

This is a per-version module: section field names and selection rules may
shift between game versions, so each version's `battle_controller.get_info()`
imports its own `battle_report` from the same dir.

Each section mirrors the raw post_battle payload as closely as possible -
same keys, same nesting, same casing. When a value is an opaque integer ID
for which we have a stable lookup (CURRENCY_ID_TO_NAME, distilled
GameParams), we resolve it to the canonical record so the section stays
meaningful in a database even if the game's numeric enum gets renumbered
later.

Trust boundary: `build_battle_report` checks for the no-data case (no
BattleStats packet during replay -> post_battle is None). Past that point
the post_battle schema is trusted; section builders index directly into
nested fields and rely on the version's lookup tables being exhaustive.
Bumping a version with a new currency or achievement means re-running the
constants extraction / GameParams distillation.

The original post_battle dict is never mutated. Sections build new outer
containers and share unchanged nested values by reference.
"""
from .constants import CURRENCY_ID_TO_NAME
from .game_params import BY_ID as GAME_PARAMS_BY_ID


def _resolve_rewards(rewards):
    return [
        [[op, {**payload, 'type': CURRENCY_ID_TO_NAME[payload['type']]}]
         for op, payload in bundle]
        for bundle in rewards
    ]


def _combat_missions_section(post_battle):
    raw = post_battle['private']['tasks']
    data = {
        task_id: {**task, 'rewards': _resolve_rewards(task['rewards'])}
        for task_id, task in raw.items()
    }
    return {
        'kind': 'object',
        'data': data,
    }


def _local_account_db_id(info):
    player_id = info['player_id']
    return next(p['accountDBID']
                for p in info['players'].values()
                if p['avatarId'] == player_id)


def _achievements_section(info):
    account_id = _local_account_db_id(info)
    raw = info['post_battle']['public'][str(account_id)]['achievements']
    return {
        'kind': 'list',
        'data': [
            {
                'count': count,
                'index': GAME_PARAMS_BY_ID[ach_id]['index'],
                'name':  GAME_PARAMS_BY_ID[ach_id]['name'],
            }
            for ach_id, count in raw
        ],
    }


def _shell_stats(p, suffix):
    return {
        'shots':  p['shots_'  + suffix],
        'hits':   p['hits_'   + suffix],
        'damage': p['damage_' + suffix],
    }


def _received_stats(p, suffix):
    return {
        'hits':   p['received_hits_'   + suffix],
        'damage': p['received_damage_' + suffix],
    }


def _interaction_damage(inter):
    return sum(v for k, v in inter.items() if k.startswith('damage_'))


def _interaction_record(target_id, inter, public):
    target = public[target_id]
    ship = GAME_PARAMS_BY_ID[target['vehicle_type_id']]
    damage = _interaction_damage(inter)
    return {
        'ship_type':    ship['typeinfo']['species'],
        'ship_name':    ship['index'],
        'ship_level':   ship['level'],
        'username':     target['name'],
        'is_destroyed': bool(inter['ship_killed']),
        'is_damaged':   damage > 0,
        'damage_count': damage,
    }


def _ship_damage_section(info):
    account_id = _local_account_db_id(info)
    p = info['post_battle']['public'][str(account_id)]
    return {
        'kind': 'object',
        'data': {
            'total': p['damage'],
            'main_battery': {
                'ap': _shell_stats(p, 'main_ap'),
                'he': _shell_stats(p, 'main_he'),
            },
            'secondary': {
                'ap': _shell_stats(p, 'atba_ap'),
                'he': _shell_stats(p, 'atba_he'),
            },
            'airstrike': {
                'bombs':         _shell_stats(p, 'bomb_airsupport'),
                'depth_charges': _shell_stats(p, 'dbomb_airsupport'),
            },
            'other': {
                'ram':   p['damage_ram'],
                'fire':  p['damage_fire'],
                'flood': p['damage_flood'],
            },
        },
    }


def _aircraft_damage_section(info):
    account_id = _local_account_db_id(info)
    p = info['post_battle']['public'][str(account_id)]
    return {
        'kind': 'object',
        'data': {
            'damage':        p['damage_airdefense'],
            'planes_killed': p['planes_killed_by_ship'],
        },
    }


def _damage_received_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    return {
        'kind': 'object',
        'data': {
            'total': sum(v for k, v in p.items() if k.startswith('received_damage_')),
            'main_battery': {
                'ap': _received_stats(p, 'main_ap'),
                'he': _received_stats(p, 'main_he'),
            },
            'secondary': {
                'ap': _received_stats(p, 'atba_ap'),
                'he': _received_stats(p, 'atba_he'),
            },
            'torpedoes': {
                'hits':   p['received_hits_tpd'],
                'damage': (p['received_damage_tpd_normal']
                         + p['received_damage_tpd_deep']
                         + p['received_damage_tpd_alter']),
            },
            'airstrike': {
                'bombs':         _received_stats(p, 'bomb_airsupport'),
                'depth_charges': _received_stats(p, 'dbomb_airsupport'),
            },
            'other': {
                'ram':   p['received_damage_ram'],
                'fire':  p['received_damage_fire'],
                'flood': p['received_damage_flood'],
            },
        },
    }


def _warships_destroyed_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    return {
        'kind': 'object',
        'data': {
            'count': sum(1 for inter in p['interactions'].values()
                         if inter['ship_killed']),
        },
    }


def _warships_damaged_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    return {
        'kind': 'object',
        'data': {
            'count': sum(1 for inter in p['interactions'].values()
                         if not inter['ship_killed']
                         and _interaction_damage(inter) > 0),
        },
    }


def _planes_destroyed_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    return {
        'kind': 'object',
        'data': {
            'count': p['planes_killed_by_ship'],
        },
    }


def _interactions_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    public = info['post_battle']['public']
    return {
        'kind': 'list',
        'data': [_interaction_record(tid, inter, public)
                 for tid, inter in p['interactions'].items()],
    }


def _team_play_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    return {
        'kind': 'object',
        'data': {
            'spotting_damage': p['scouting_damage'],
            'potential_damage': {
                'artillery':    p['agro_art'],
                'torpedo':      p['agro_tpd'],
                'air':          p['agro_air'],
                'depth_charge': p['agro_dbomb'],
            },
            'spotted': {
                'ships':     p['first_ships_spotted_by_ship']  + p['first_ships_spotted_by_plane'],
                'planes':    p['first_planes_spotted_by_ship'] + p['first_planes_spotted_by_plane'],
                'torpedoes': p['tpds_spotted'],
            },
            'capture_points': p['capture_points'],
            'defense_points': p['dropped_capture_points'],
        },
    }


def _objective_points_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    return {
        'kind': 'object',
        'data': {
            'victory': {
                'general':       p['victory_points_victory_general'],
                'by_kill':       p['victory_points_victory_by_kill'],
                'by_capture':    p['victory_points_victory_by_capture'],
                'by_score_zero': p['victory_points_victory_by_score_zero'],
            },
            'ship_destruction': {
                'destroyer':  p['victory_points_kill_destroyer'],
                'cruiser':    p['victory_points_kill_cruiser'],
                'battleship': p['victory_points_kill_battleship'],
                'carrier':    p['victory_points_kill_carrier'],
                'submarine':  p['victory_points_kill_submarine'],
                'own':        p['victory_points_own_ship_kill'],
            },
            'key_area_defense': {
                'base_capture':       p['victory_points_cp_base_capture'],
                'neutral_capture':    p['victory_points_cp_neutral_capture'],
                'team_capture':       p['victory_points_cp_team_capture'],
                'hold':               p['victory_points_cp_hold'],
                'base_block':         p['victory_points_cp_base_block'],
                'neutral_block':      p['victory_points_cp_neutral_block'],
                'team_block':         p['victory_points_cp_team_block'],
                'earning_block':      p['victory_points_cp_earning_block'],
                'base_drop':          p['victory_points_cp_base_drop'],
                'neutral_drop':       p['victory_points_cp_neutral_drop'],
                'team_drop':          p['victory_points_cp_team_drop'],
                'battle_end_base':    p['victory_points_cp_battle_end_base'],
                'battle_end_neutral': p['victory_points_cp_battle_end_neutral'],
                'battle_end_team':    p['victory_points_cp_battle_end_team'],
            },
        },
    }


def build_battle_report(info):
    """Build the report from the controller's get_info() dict."""
    post_battle = info['post_battle']
    if post_battle is None:
        return {'tabs': {}}

    return {
        'tabs': {
            'results': {
                'sections': {
                    'combat_missions': _combat_missions_section(post_battle),
                    'achievements':    _achievements_section(info),
                },
            },
            'details': {
                'sections': {
                    'damage_to_ships':    _ship_damage_section(info),
                    'damage_received':    _damage_received_section(info),
                    'warships_destroyed': _warships_destroyed_section(info),
                    'warships_damaged':   _warships_damaged_section(info),
                    'interactions':       _interactions_section(info),
                    'damage_to_aircraft': _aircraft_damage_section(info),
                    'planes_destroyed':   _planes_destroyed_section(info),
                    'team_play':          _team_play_section(info),
                    'objective_points':   _objective_points_section(info),
                },
            },
        },
    }
