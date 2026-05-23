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
import math

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
            'count':    count,
            'local_id': ach_id,
            'index':    GAME_PARAMS_BY_ID[ach_id]['index'],
            'name':     GAME_PARAMS_BY_ID[ach_id]['name'],
            'ui_name':  GAME_PARAMS_BY_ID[ach_id].get('uiName'),
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


def _personal_summary_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    return {
        'kind': 'object',
        'data': {
            'damage':           p['damage'],
            'frags':            p['ships_killed'],
            'planes_killed':    p['planes_killed_by_ship'],
            'exp':              p['exp'],
            'base_exp':         p['raw_exp'],
            'scouting_damage':  p['scouting_damage'],
            'potential_damage': p['agro_art'] + p['agro_tpd'] + p['agro_air'] + p['agro_dbomb'],
            'capture_points':   p['capture_points'],
            'defense_points':   p['dropped_capture_points'],
        },
    }


def _personal_ribbons_section(info):
    p = info['post_battle']['public'][str(_local_account_db_id(info))]
    return {
        'kind': 'list',
        'data': [{'name': k, 'count': v}
                 for k, v in p.items()
                 if k.startswith('RIBBON_') and v],
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


_DIFFICULTY_SUFFIXES = ('_LOW_LVL', '_MEDIUM_LVL', '_HIGH_LVL', '_NIGHTMARE')


def _parse_scenario_difficulty(scenario_name):
    """Strip the runtime difficulty suffix from a scenario name.

    Operations expose difficulty via the scenario string the server picks at
    queue time (e.g. PCVO003_OP_01_03_s03_Labyrinth_HIGH_LVL). The base
    BattleScript record in GameParams has a static `difficulty` attribute,
    but the suffix is the actual difficulty played - it overrides the default.
    """
    for suffix in _DIFFICULTY_SUFFIXES:
        if scenario_name.endswith(suffix):
            return suffix.lstrip('_').lower()
    return None


_TASK_CATEGORY_MAIN      = 1
_TASK_CATEGORY_SECONDARY = 2
_TASK_CATEGORY_TRANSPORT = 3

_TASK_CATEGORY_NAMES = {
    _TASK_CATEGORY_MAIN:      'main',
    _TASK_CATEGORY_SECONDARY: 'secondary',
    _TASK_CATEGORY_TRANSPORT: 'transport',
}

# Task `status` semantics (inferred from observed data, only `3 == completed`
# is firmly attested across replays - other values lumped into "not completed").
_TASK_STATUS_COMPLETED = 3


def _task_record(t):
    return {
        'id':         t['id'],
        'category':   _TASK_CATEGORY_NAMES.get(t['category'], 'other'),
        'completed':  t['status'] == _TASK_STATUS_COMPLETED,
        'value':      t['currentValue'],
        'icon':       t['icon'] or None,
        'start_time': t['startTime'],
        'close_time': t['closeTime'],
    }


def _operation_outcome(info):
    winner = info['post_battle']['common']['winner_team_id']
    if winner == -1:
        return 'draw'
    return 'victory' if winner == _local_team_id(info) else 'defeat'


def _operation_tab(info):
    pb = info['post_battle']
    common = pb['common']
    tasks = common['battle_logic_info']['tasks']
    star_tasks = [t for t in tasks
                  if t['category'] in (_TASK_CATEGORY_MAIN, _TASK_CATEGORY_SECONDARY)]
    transport_tasks = [t for t in tasks if t['category'] == _TASK_CATEGORY_TRANSPORT]
    other_tasks = [t for t in tasks
                   if t['category'] not in (_TASK_CATEGORY_MAIN,
                                            _TASK_CATEGORY_SECONDARY,
                                            _TASK_CATEGORY_TRANSPORT)]
    stars_earned = sum(1 for t in star_tasks if t['status'] == _TASK_STATUS_COMPLETED)
    return {
        'sections': {
            'summary': {
                'kind': 'object',
                'data': {
                    'scenario':        common['scenario_name'],
                    'operation_id':    common['pve_operation_id'],
                    'difficulty':      _parse_scenario_difficulty(common['scenario_name']),
                    'outcome':         _operation_outcome(info),
                    'duration_sec':    common['duration_sec'],
                    'from_matchmaker': pb['private'].get('pve_details', {}).get('enter_matchmaker'),
                    'stars': {
                        # Some main tasks are multi-step prerequisites (e.g.
                        # OP_01_03_MAIN_TASK_PREQUEL -> OP_01_03_MAIN_TASK) which both
                        # appear as category=1; only the final step is awarded as a star.
                        # `earned` counts every cat-1/2 task with status==3, then we clamp
                        # to `max` to drop the extras. The post-battle UI universally caps
                        # operation stars at 5.
                        'earned': min(stars_earned, 5),
                        'max':    5,
                    },
                },
            },
            'tasks': {
                'kind': 'list',
                'data': [_task_record(t) for t in star_tasks],
            },
            'transports': {
                'kind': 'list',
                'data': [_task_record(t) for t in transport_tasks],
            },
            'drops': {
                'kind': 'object',
                'data': common['battle_logic_info'].get('drop', {}),
            },
            **({'other_tasks': {'kind': 'list',
                                'data': [_task_record(t) for t in other_tasks]}}
               if other_tasks else {}),
        },
    }


def _is_operation_battle(post_battle):
    return bool(post_battle['common'].get('pve_operation_id'))


# subtotal_economics entries are 4-tuples [source, factor, applied, ?].
# `source` is either a string tag (FIRST_WIN, CLAN_SUPPLY_BONUS, ...) or a
# numeric GameParams id (modernization / signal / camouflage / exterior).
# `applied` is the game's flag for whether the modifier actually contributed -
# entries with applied==False are listed in the UI but greyed out.
_MOD_LANES = ('sse', 'base', 'mod')


def _resolve_modifier_source(source):
    """Resolve a numeric GameParams id to {name, index, type, species}.

    String sources (FIRST_WIN, CLAN_SUPPLY_BONUS, ...) come straight from
    server-side enums and have no GameParams record - they are returned with
    `name` equal to the tag itself and no type info. Numeric sources are
    upgrade / exterior / crew / ability ids and resolve through the distilled
    GameParams; an unresolved int is returned with `name: None` so callers
    can still display the raw id without crashing.
    """
    if isinstance(source, str):
        return {'name': source}
    rec = GAME_PARAMS_BY_ID.get(source)
    if rec is None:
        return {'name': None}
    return {
        'name':    rec.get('name'),
        'index':   rec.get('index'),
        'type':    rec.get('typeinfo', {}).get('type'),
        'species': rec.get('typeinfo', {}).get('species'),
    }


def _modifier_record(entry, base_n, base_p):
    """Per-modifier record with both no-premium and with-premium contributions.

    The game UI mirrors each modifier across the two columns - same +X%, but
    a different absolute value - so each record carries `value` under both
    `without_premium` and `with_premium`. `ceil(base * factor)` matches the
    in-game per-modifier rounding (see `_modifier_contribution`).
    """
    source, factor, applied, _ = entry
    rec = {
        'source':   source,
        'resolved': _resolve_modifier_source(source),
        'factor':   factor,
        'applied':  applied,
    }
    if applied:
        rec['without_premium'] = {'value': math.ceil(base_n * factor)}
        rec['with_premium']    = {'value': math.ceil(base_p * factor)}
    return rec


def _applied_factor_sum(group):
    return sum(e[1] for lane in _MOD_LANES for e in group[lane] if e[2])


def _modifier_contribution(group, base):
    """Sum the per-modifier reward contribution against `base`.

    Empirically the in-game UI computes each applied modifier's reward
    contribution as `ceil(base * factor)` and then sums - rounding factors
    first and multiplying once gives values that drift by ±1, and standard
    half-to-even rounding lands a step below the displayed number. Matching
    the per-modifier ceil keeps the totals byte-identical to the screen.
    """
    return sum(math.ceil(base * e[1]) for lane in _MOD_LANES for e in group[lane] if e[2])


def _category_modifier_records(group, base_n, base_p):
    return {lane: [_modifier_record(e, base_n, base_p) for e in group[lane]]
            for lane in _MOD_LANES}


def _credits_spent(common):
    return {
        'service':    common['auto_repair_credits'],
        'ammunition': common['auto_load_credits'],
        'camouflage': common['auto_camo_credits'],
        'signals':    common['auto_signals_credits'],
        'boosters':   common['auto_boost_credits'],
    }


def _credits_economy_section(priv, common):
    init = priv['init_economics']
    sub = priv['subtotal_economics']
    base = init['credits']
    prem = common['wows_premium_credits_factor']
    spent_map = _credits_spent(common)
    total_spent = sum(spent_map.values())
    received_n = base
    received_p = math.ceil(base * prem)
    modifiers_n = _modifier_contribution(sub['credits'], base)
    modifiers_p = _modifier_contribution(sub['credits'], received_p)
    return {
        'kind': 'object',
        'data': {
            'modifiers': _category_modifier_records(sub['credits'], base, received_p),
            'spent':     spent_map,
            'penalty':       init['credits_penalty'],
            'compensation':  init['credits_compensation'],
            'without_premium': {
                'received':  received_n,
                'modifiers': modifiers_n,
                'spent':     total_spent,
                'total':     received_n + modifiers_n - total_spent,
            },
            'with_premium': {
                'premium_factor': prem,
                'received':  received_p,
                'modifiers': modifiers_p,
                'spent':     total_spent,
                'total':     received_p + modifiers_p - total_spent,
            },
        },
    }


def _exp_economy_section(priv, common, category):
    """Build the ship_exp / crew_exp section.

    Both categories share the same `received` value (init_economics.exp) and
    the same premium multiplier (wows_premium_exp_factor); they differ only
    in which subtotal_economics group supplies the modifier factors.
    """
    init = priv['init_economics']
    sub = priv['subtotal_economics'][category]
    base = init['exp']
    prem = common['wows_premium_exp_factor']
    received_n = base
    received_p = math.ceil(base * prem)
    modifiers_n = _modifier_contribution(sub, base)
    modifiers_p = _modifier_contribution(sub, received_p)
    return {
        'kind': 'object',
        'data': {
            'modifiers': _category_modifier_records(sub, base, received_p),
            'penalty':   init['exp_penalty'],
            'without_premium': {
                'received':  received_n,
                'modifiers': modifiers_n,
                'total':     received_n + modifiers_n,
            },
            'with_premium': {
                'premium_factor': prem,
                'received':  received_p,
                'modifiers': modifiers_p,
                'total':     received_p + modifiers_p,
            },
        },
    }


def _free_exp_economy_section(priv, common):
    """Free XP is awarded as a fraction (free_exp_factor) of ship XP and has
    its own modifier group. No premium factor is applied to free XP itself
    in the UI - it's reported as a single small total next to ship XP.
    """
    sub = priv['subtotal_economics']['free_exp']
    init = priv['init_economics']
    base_n = math.ceil(init['exp'] * common['free_exp_factor'])
    base_p = math.ceil(init['exp'] * common['wows_premium_exp_factor']
                                   * common['free_exp_factor'])
    return {
        'kind': 'object',
        'data': {
            'modifiers':       _category_modifier_records(sub, base_n, base_p),
            'free_exp_factor': common['free_exp_factor'],
        },
    }


def _elite_exp_economy_section(priv, common):
    sub = priv['subtotal_economics']['elite_exp']
    base_n = priv['init_economics']['exp']
    base_p = math.ceil(base_n * common['wows_premium_exp_factor'])
    return {
        'kind': 'object',
        'data': {'modifiers': _category_modifier_records(sub, base_n, base_p)},
    }


def _bonuses_economy_section(priv, common):
    """Account-wide multipliers (premium ship, global boosts, AoGAS) and the
    flags that say whether each consumable lane (camo/signals/boost/service)
    was actually applied. Useful for explaining why a modifier is or isn't
    in the modifier list.
    """
    return {
        'kind': 'object',
        'data': {
            'premium_credits_factor':       common['premium_credits_factor'],
            'premium_exp_factor':           common['premium_exp_factor'],
            'wows_premium_credits_factor':  common['wows_premium_credits_factor'],
            'wows_premium_exp_factor':      common['wows_premium_exp_factor'],
            'free_exp_factor':              common['free_exp_factor'],
            'aogas_factor':                 common['aogas_factor'],
            'globalboosts': priv.get('globalboosts_mods') or {},
            'applied': {
                'camo':    common['camo_applied'],
                'signals': common['signals_applied'],
                'boost':   common['boost_applied'],
                'service': common['serve_applied'],
            },
            'enabled': {
                'ship_service': common['ship_service_enabled'],
                'credits':      common['credits_enabled'],
                'exp':          common['exp_enabled'],
                'crew_exp':     common['crew_exp_enabled'],
                'free_exp':     common['free_exp_enabled'],
                'acc_points':   common['acc_points_enabled'],
            },
        },
    }


def _economy_tab(priv):
    common = priv['common_economics']
    return {
        'sections': {
            'credits':       _credits_economy_section(priv, common),
            'ship_exp':      _exp_economy_section(priv, common, 'ship_exp'),
            'commander_exp': _exp_economy_section(priv, common, 'crew_exp'),
            'free_exp':      _free_exp_economy_section(priv, common),
            'elite_exp':     _elite_exp_economy_section(priv, common),
            'bonuses':       _bonuses_economy_section(priv, common),
        },
    }


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
            'personal_score': {
                'sections': {
                    'summary':      _personal_summary_section(info),
                    'ribbons':      _personal_ribbons_section(info),
                    'achievements': _achievements_section(info),
                },
            },
            'economy': _economy_tab(post_battle['private']),
            **({'operation': _operation_tab(info)}
               if _is_operation_battle(post_battle) else {}),
        },
    }
