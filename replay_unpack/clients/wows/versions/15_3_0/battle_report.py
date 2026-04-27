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
from .game_params import BY_ID as GAME_PARAMS_BY_ID


def _combat_missions_section(post_battle):
    raw = post_battle['private']['tasks']
    return {
        'kind': 'object',
        'data': {
            task_id: {k: v for k, v in task.items() if k != 'rewards'}
            for task_id, task in raw.items()
        },
    }


_RANK_FIELDS = (
    'rank_battles_season_id',
    'rank_league',
    'rank_old',
    'rank_new',
    'rank_stars_old',
    'rank_stars_gained',
    'rank_stars_new',
    'rank_victories_old',
    'rank_victories_new',
    'rank_victory_rewards_progress',
)


def _ranked_section(post_battle):
    private = post_battle['private']
    return {
        'kind': 'object',
        'data': {f: private[f] for f in _RANK_FIELDS},
    }


def _local_account_db_id(info):
    player_id = info['player_id']
    return next(p['accountDBID']
                for p in info['players'].values()
                if p['avatarId'] == player_id)


def _resolve_achievements(raw):
    return [
        {
            'count': count,
            'index': GAME_PARAMS_BY_ID[ach_id]['index'],
            'name':  GAME_PARAMS_BY_ID[ach_id]['name'],
        }
        for ach_id, count in raw
    ]


def _achievements_section(info):
    account_id = _local_account_db_id(info)
    return {
        'kind': 'list',
        'data': _resolve_achievements(
            info['post_battle']['public'][str(account_id)]['achievements']),
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


def _torpedo_stats(p):
    if p['shots_tpd'] is None:
        return {'shots': None, 'hits': None, 'damage': None}
    return {
        'shots':  p['shots_tpd'],
        'hits':   p['hits_tpd'],
        'damage': (p['damage_tpd_normal']
                 + p['damage_tpd_deep']
                 + p['damage_tpd_alter']),
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
            'torpedoes': _torpedo_stats(p),
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


def _decode_rank_info_dump(dump):
    """Unpack RankBattlesCommon.accountRankInfoPackerUnpacker (bitCounts [3, 16, 7, 4]).

    Layout, low to high: league(4) | rank(7) | season_id(16) | stage(3).
    Returns None for the no-rank case (league == 0), matching getRankInfo.
    """
    league = dump & 0xF
    if league == 0:
        return None
    return {'league': league, 'position': (dump >> 4) & 0x7F}


def _team_score_record(player, public, local_account_db_id, local_stars):
    p = public[str(player['accountDBID'])]
    ship = GAME_PARAMS_BY_ID[p['vehicle_type_id']]
    is_own = player['accountDBID'] == local_account_db_id
    record = {
        'squad_id':      player.get('preBattleIdOnStart', 0),
        'team_id':       player['teamId'],
        'clan_tag':      player['clanTag'],
        'username':      player['name'],
        'is_own':        is_own,
        'is_alive':      player['isAlive'],
        'ship_type':     ship['typeinfo']['species'],
        'ship_name':     ship['index'],
        'ship_level':    ship['level'],
        'frags':         p['ships_killed'],
        'planes_killed': p['planes_killed_by_ship'],
        'exp':           p['exp'],
        'achievements':  _resolve_achievements(p['achievements']),
    }
    rank = _decode_rank_info_dump(p.get('rank_info_dump', 0))
    if rank is not None:
        if is_own and local_stars is not None:
            rank['stars'] = local_stars
        record['rank'] = rank
    return record


def _local_team_id(info):
    player_id = info['player_id']
    return next(p['teamId']
                for p in info['players'].values()
                if p['avatarId'] == player_id)


def _team_score_sections(info):
    public = info['post_battle']['public']
    ally_team_id = _local_team_id(info)
    local_account_db_id = _local_account_db_id(info)
    local_stars = info['post_battle']['private'].get('rank_stars_old')
    allies, enemies = [], []
    for player in info['players'].values():
        if str(player['accountDBID']) not in public:
            continue
        record = _team_score_record(player, public, local_account_db_id, local_stars)
        (allies if player['teamId'] == ally_team_id else enemies).append(record)
    return (
        {'kind': 'list', 'data': allies},
        {'kind': 'list', 'data': enemies},
    )


def build_battle_report(info):
    """Build the report from the controller's get_info() dict."""
    post_battle = info['post_battle']
    if post_battle is None:
        return {'tabs': {}}

    results_sections = {
        'combat_missions': _combat_missions_section(post_battle),
        'achievements':    _achievements_section(info),
    }
    if 'rank_battles_season_id' in post_battle['private']:
        results_sections['ranked'] = _ranked_section(post_battle)

    return {
        'tabs': {
            'results': {
                'sections': results_sections,
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
            'team_score': {
                'sections': dict(zip(('allies', 'enemies'),
                                     _team_score_sections(info))),
            },
        },
    }
