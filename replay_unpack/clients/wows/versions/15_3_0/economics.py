# coding=utf-8
"""Pure-Python port of SSE_Common.calculateTotalRewards from the WoWS client.

The numbers shown on the in-game "Credits and XP" screen (final credits, ship
XP, free XP, commander XP) are NOT stored verbatim in post_battle - they're
derived here from `init_economics` + `subtotal_economics` + `common_economics`.
The function and helpers mirror the original 1:1 (same names, same field
shapes, same per-step ceilMe rounding) so the output stays interpretable
against client source. Per-version because the formula and its constants can
shift across game updates.

Source: wows-sandbox decompiled `SSE_Common/__init__.py` (lines 25-233).
Caller pattern: `m92ea29c6/BattleResultsSystem.py` lines 159-162.
"""
import math


class PremiumTypes:
    NONE = 0
    COMMON = 1
    WOWS = 2


def ceilMe(x):
    return int(math.ceil(x))


def normalizeFactor(x):
    """Convert a multiplicative factor to additive form: 0.88 -> -0.12."""
    return round(x - 1.0, 2)


def getPremXPFactor(premium_type, common):
    if premium_type == PremiumTypes.WOWS:
        return common['wows_premium_exp_factor']
    if premium_type == PremiumTypes.COMMON:
        return common['premium_exp_factor']
    return 1.0


def getPremCRFactor(premium_type, common):
    if premium_type == PremiumTypes.WOWS:
        return common['wows_premium_credits_factor']
    if premium_type == PremiumTypes.COMMON:
        return common['premium_credits_factor']
    return 1.0


def applyAogasAndPenalty(value, aogas_factor, penalty):
    return max(0, ceilMe(value * aogas_factor + penalty))


def getModifierBonusItem(name, factor, applied, value):
    return {'name': name, 'factor': factor, 'applied': applied, 'value': value}


def _accumulate(out_bucket, items, premium_value, base_value,
                running_base, daily_first_win=False):
    """Walk a modifier stack [(id, fraction, applied, cap), ...].

    Each non-zero fraction contributes ceilMe(fraction * premium_value) to the
    bucket and ceilMe(fraction * base_value) to the running base total. Returns
    (new running_base, first_win_value or None).
    """
    first_win = None
    for item in items:
        if item[1] != 0:
            v = ceilMe(item[1] * premium_value)
            running_base += ceilMe(item[1] * base_value)
            if daily_first_win and item[0] == 'FIRST_WIN':
                first_win = v
            out_bucket['items'].append(getModifierBonusItem(item[0], item[1], item[2], v))
            out_bucket['sum'] += v
        running_base += item[3]
    return running_base, first_win


def calculateTotalRewards(premium_type, init, subtotals, common):
    out = {}
    xp_factor = getPremXPFactor(premium_type, common)
    cr_factor = getPremCRFactor(premium_type, common)
    aogas = common['aogas_factor']

    out['premium_type'] = premium_type
    out['aogas_factor'] = aogas
    out['aogas_online'] = common['aogas_online']

    for k in ('credits_modifiers', 'credits_basics', 'credits_sse',
              'exp_modifiers', 'exp_basics', 'exp_sse',
              'free_exp_modifiers', 'free_exp_basics', 'free_exp_sse',
              'crew_exp_modifiers', 'crew_exp_basics', 'crew_exp_sse',
              'acc_points_sse'):
        out[k] = {'items': [], 'sum': 0}
    out['exp_bonus_daily'] = 0

    # === Credits ===
    out['battle_credits'] = ceilMe(init['credits'] * cr_factor)
    out['credits_compensation'] = init['credits_compensation']
    out['credits_penalty'] = -init['credits_penalty']
    base_running = init['credits']

    if common['credits_enabled']:
        for stack_key, out_key in (('mod', 'credits_modifiers'),
                                   ('base', 'credits_basics'),
                                   ('sse', 'credits_sse')):
            base_running, _ = _accumulate(
                out[out_key], subtotals['credits'][stack_key],
                out['battle_credits'], init['credits'], base_running)

    # === Spendings ===
    serve_applied = common['serve_applied']
    camo_applied = common['camo_applied']
    signals_applied = common['signals_applied']
    boost_applied = common['boost_applied']

    out['spendings'] = {
        'credits_sum': 0,
        'gold_sum': 0,
        'details': {},
        'extends': {
            'auto_repair_modifiers': {'items': [], 'sum': 0},
            'auto_load_map': common['auto_load_list'],
            'auto_camo_list': common['auto_camo_list'],
            'auto_signals_list': common['auto_signals_list'],
            'auto_boost_list': common['auto_boost_list'],
        },
    }

    for item in common['auto_repair_list']:
        if item[1] != 0:
            v = ceilMe(item[1] * common['auto_repair_credits'])
            out['spendings']['extends']['auto_repair_modifiers']['items'].append(
                getModifierBonusItem(item[0], item[1], serve_applied, v))
            out['spendings']['extends']['auto_repair_modifiers']['sum'] += v

    for key, is_gold, applied, factor, amount in [
        ('auto_repair_credits',  False, serve_applied,
            normalizeFactor(common['auto_repair_factor']), common['auto_repair_credits']),
        ('auto_load_credits',    False, serve_applied,   0, common['auto_load_credits']),
        ('auto_camo_credits',    False, camo_applied,    0, common['auto_camo_credits']),
        ('auto_camo_gold',       True,  camo_applied,    0, common['auto_camo_gold']),
        ('auto_signals_credits', False, signals_applied, 0, common['auto_signals_credits']),
        ('auto_boost_credits',   False, boost_applied,   0, common['auto_boost_credits']),
        ('auto_boost_gold',      True,  boost_applied,   0, common['auto_boost_gold']),
    ]:
        item = getModifierBonusItem('', factor, applied, -amount)
        out['spendings']['details'][key] = item
        if item['applied']:
            if is_gold:
                out['spendings']['gold_sum'] += item['value']
            else:
                out['spendings']['credits_sum'] += item['value']

    out['credits_profit'] = (out['battle_credits']
                             + out['credits_compensation']
                             + out['credits_sse']['sum']
                             + out['credits_modifiers']['sum']
                             + out['credits_basics']['sum'])
    out['credits'] = applyAogasAndPenalty(out['credits_profit'], aogas, out['credits_penalty'])
    out['base_credits'] = applyAogasAndPenalty(
        base_running + out['credits_compensation'], aogas, out['credits_penalty'])
    out['total_credits'] = out['credits'] + out['spendings']['credits_sum']
    out['total_gold'] = out['spendings']['gold_sum']

    # === Ship XP ===
    out['battle_exp'] = ceilMe(init['exp'] * xp_factor)
    out['exp_penalty'] = -init['exp_penalty']
    base_running = init['exp']

    if common['exp_enabled']:
        for stack_key, out_key in (('mod', 'exp_modifiers'),
                                   ('base', 'exp_basics'),
                                   ('sse', 'exp_sse')):
            base_running, fw = _accumulate(
                out[out_key], subtotals['ship_exp'][stack_key],
                out['battle_exp'], init['exp'], base_running,
                daily_first_win=(stack_key == 'base'))
            if fw is not None:
                out['exp_bonus_daily'] = fw

    out['exp_profit'] = (out['battle_exp']
                         + out['exp_sse']['sum']
                         + out['exp_modifiers']['sum']
                         + out['exp_basics']['sum'])
    out['exp'] = applyAogasAndPenalty(out['exp_profit'], aogas, out['exp_penalty'])
    out['base_exp'] = applyAogasAndPenalty(base_running, aogas, out['exp_penalty'])

    # === Free XP ===
    if common['free_exp_enabled']:
        out['battle_free_exp'] = ceilMe(applyAogasAndPenalty(
            out['battle_exp'], aogas, out['exp_penalty']) * common['free_exp_factor'])
        base_free_init = ceilMe(applyAogasAndPenalty(
            init['exp'], aogas, out['exp_penalty']) * common['free_exp_factor'])
        base_running = base_free_init

        for stack_key, out_key in (('mod', 'free_exp_modifiers'),
                                   ('base', 'free_exp_basics'),
                                   ('sse', 'free_exp_sse')):
            base_running, _ = _accumulate(
                out[out_key], subtotals['free_exp'][stack_key],
                out['battle_free_exp'], base_free_init, base_running)

        out['free_exp_profit'] = (out['battle_free_exp']
                                  + out['free_exp_sse']['sum']
                                  + out['free_exp_modifiers']['sum']
                                  + out['free_exp_basics']['sum'])
        out['free_exp'] = applyAogasAndPenalty(out['free_exp_profit'], aogas, 0)
        out['base_free_exp'] = applyAogasAndPenalty(base_running, aogas, 0)

    # === Crew XP ===
    if common['crew_exp_enabled']:
        out['battle_crew_exp'] = out['battle_exp']
        out['crew_exp_penalty'] = out['exp_penalty']

        # crew_exp tracks no without-premium running total in the source
        for stack_key, out_key in (('mod', 'crew_exp_modifiers'),
                                   ('base', 'crew_exp_basics'),
                                   ('sse', 'crew_exp_sse')):
            for item in subtotals['crew_exp'][stack_key]:
                if item[1] != 0:
                    v = ceilMe(item[1] * out['battle_crew_exp'])
                    out[out_key]['items'].append(
                        getModifierBonusItem(item[0], item[1], item[2], v))
                    out[out_key]['sum'] += v

        out['crew_exp'] = applyAogasAndPenalty(
            out['battle_crew_exp']
            + out['crew_exp_sse']['sum']
            + out['crew_exp_modifiers']['sum']
            + out['crew_exp_basics']['sum'],
            aogas, out['crew_exp_penalty'])

    # === Account points ===
    acc_pts_enabled = int(common['acc_points_enabled'])
    for item in subtotals['acc_level']['sse']:
        if item[1] != 0:
            v = ceilMe(item[1] * acc_pts_enabled)
            out['acc_points_sse']['items'].append(
                getModifierBonusItem(item[0], item[1], item[2], v))
            out['acc_points_sse']['sum'] += v
    out['account_points'] = max(0, ceilMe(acc_pts_enabled + out['acc_points_sse']['sum']))

    return out
