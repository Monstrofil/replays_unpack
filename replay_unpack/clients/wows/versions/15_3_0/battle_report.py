# coding=utf-8
"""Build a machine-consumable, extensible battle-report structure from raw post_battle.

Output shape:
    {
      "tabs": [
        {
          "id": str,
          "sections": [
            {"id": str, "kind": "list"|"object", "data": ...},
          ],
        },
      ]
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
from .economics import calculateTotalRewards
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
        'id': 'combat_missions',
        'kind': 'object',
        'data': data,
    }


def _local_account_db_id(info):
    player_id = info['player_id']
    return next(p['accountDBID']
                for p in info['players'].values()
                if p['avatarId'] == player_id)


def _economics_section(info):
    private = info['post_battle']['private']
    return {
        'id': 'economics',
        'kind': 'object',
        'data': calculateTotalRewards(
            private['premium_type'],
            private['init_economics'],
            private['subtotal_economics'],
            private['common_economics']),
    }


def _achievements_section(info):
    account_id = _local_account_db_id(info)
    raw = info['post_battle']['public'][str(account_id)]['achievements']
    return {
        'id': 'achievements',
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


def build_battle_report(info):
    """Build the report from the controller's get_info() dict."""
    post_battle = info['post_battle']
    if post_battle is None:
        return {'tabs': []}

    return {
        'tabs': [
            {
                'id': 'results',
                'sections': [
                    _combat_missions_section(post_battle),
                    _achievements_section(info),
                    _economics_section(info),
                ],
            },
        ],
    }
