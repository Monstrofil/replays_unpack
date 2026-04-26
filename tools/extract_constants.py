# coding=utf-8
"""
Extraction script that runs inside wows-sandbox (Python 2.7).
Reads game data from scripts.zip and outputs JSON to stdout.

Usage:
    cd wows-sandbox
    PYTHONHOME=3rdparty/cpython ./wows_shell /path/to/extract_constants.py
"""
import json
import sys
import traceback

data = {}
errors = []


def safe_extract(name, func):
    try:
        func()
    except Exception as e:
        errors.append('%s: %s' % (name, traceback.format_exc()))


def _find_players_info_module():
    """Find the obfuscated module that contains gSharedPlayerInfo."""
    for name, mod in sys.modules.items():
        if mod is not None and hasattr(mod, 'gSharedPlayerInfo'):
            return mod
    raise ImportError('Could not find module with gSharedPlayerInfo')


# Player property maps
def extract_property_maps():
    mod = _find_players_info_module()
    data['id_property_map'] = dict(mod.gSharedPlayerInfo._numMemberMap)
    data['id_property_map_bots'] = dict(mod.gSharedBotInfo._numMemberMap)
    data['id_property_map_observer'] = dict(mod.gSharedObserverInfo._numMemberMap)

safe_extract('property_maps', extract_property_maps)


# Death types: {i: vars(j) for i,j in Vehicle.DeathReason._DeathReason__byId.items()}
def extract_death_types():
    from Vehicle import DeathReason
    death_types = {}
    for i, j in DeathReason._DeathReason__byId.items():
        entry = vars(j)
        # Filter to only JSON-serializable fields
        death_types[i] = {
            k: v for k, v in entry.items()
            if isinstance(v, (int, float, str, type(u''), bool, type(None)))
        }
    data['death_types'] = death_types

safe_extract('death_types', extract_death_types)


# CrewModifiers.SkillTypeEnum.ID_TO_NAME
def extract_skill_types():
    from CrewModifiers import SkillTypeEnum
    data['skill_type_id_to_name'] = dict(SkillTypeEnum.ID_TO_NAME)

safe_extract('skill_type_id_to_name', extract_skill_types)


# CrewModifiers.ShipTypes.TYPE_BY_ID (tuple, not dict)
def extract_ship_types():
    from CrewModifiers import ShipTypes
    type_by_id = ShipTypes.TYPE_BY_ID
    data['ship_type_by_id'] = {i: v for i, v in enumerate(type_by_id)}

safe_extract('ship_type_by_id', extract_ship_types)


# Avatar.DamageStatsType
def extract_damage_stats():
    from Avatar import DamageStatsType
    result = {}
    for attr in dir(DamageStatsType):
        if attr.startswith('DAMAGE_STATS_'):
            result[attr] = getattr(DamageStatsType, attr)
    data['damage_stats'] = result

safe_extract('damage_stats', extract_damage_stats)


# BattleResultsUtils.Category (stable re-export of CommonBattleLogicClasses enum)
def extract_category():
    from BattleResultsUtils import Category
    result = {}
    for attr in dir(Category):
        val = getattr(Category, attr)
        if isinstance(val, int):
            result[attr] = val
    result['ids'] = dict(Category.ids)
    result['names'] = dict(Category.names)
    data['category'] = result

safe_extract('category', extract_category)


# Status and TaskType live in the same obfuscated submodule,
# but Category's __module__ tells us where to find them.
def extract_status_and_tasktype():
    from BattleResultsUtils import Category
    mod_name = Category.__module__
    mod = sys.modules[mod_name]

    # Status
    Status = mod.Status
    st = {}
    for attr in dir(Status):
        val = getattr(Status, attr)
        if isinstance(val, int):
            st[attr] = val
    st['ids'] = dict(Status.ids)
    st['names'] = dict(Status.names)
    data['status'] = st

    # TaskType
    TaskType = mod.TaskType
    tt = {}
    for attr in dir(TaskType):
        val = getattr(TaskType, attr)
        if isinstance(val, int):
            tt[attr] = val
    tt['ids'] = dict(TaskType.ids)
    tt['names'] = dict(TaskType.names)
    data['task_type'] = tt

safe_extract('status_and_tasktype', extract_status_and_tasktype)


# BattleResultsSystem constants (field name tuples for post-battle results)
def extract_battle_results():
    # Find the BattleResultsSystem module (obfuscated name like m92ea29c6.BattleResultsSystem)
    brs_mod = None
    for name, mod in sys.modules.items():
        if mod is not None and name.endswith('.BattleResultsSystem'):
            brs_mod = mod
            break

    if brs_mod is None:
        raise ImportError('Could not find BattleResultsSystem module')

    # Get constants from func_globals of an unpack function
    fg = brs_mod.unpackCommonRes.func_globals

    result = {}
    for const_name in (
        'CLIENT_PUBLIC_RESULTS', 'COMMON_RESULTS', 'PLAYER_PRIVATE_RESULTS',
        'INIT_ECONOMICS', 'COMMON_ECONOMICS', 'SUBTOTAL_ECONOMICS',
        'CLIENT_VEH_INTERACTION_DETAILS', 'CLIENT_BUILDING_INTERACTION_DETAILS',
    ):
        val = fg.get(const_name)
        if val is not None:
            result[const_name] = list(val)

    # Module-level attributes
    for const_name in ('BUILDINGS_FULL_RESULTS',):
        val = getattr(brs_mod, const_name, None)
        if val is not None:
            result[const_name] = list(val)

    data['battle_results'] = result

safe_extract('battle_results', extract_battle_results)


# CURRENCY_ID_TO_WALLET_ASSET_NAME: maps the integer 'type' in post-battle reward
# bundles ([[op, {type: int, count: int}], ...]) to a stable wallet-asset name
# (e.g. 0 -> 'credits', 46 -> 'dockyardum_2'). Module name is obfuscated, so we
# search by attribute and signature instead of importing.
def extract_currency_id_to_name():
    target = None
    for name, mod in sys.modules.items():
        if mod is None:
            continue
        val = getattr(mod, 'CURRENCY_ID_TO_WALLET_ASSET_NAME', None)
        if isinstance(val, dict) and val.get(0) == 'credits':
            target = val
            break
    if target is None:
        raise ImportError('CURRENCY_ID_TO_WALLET_ASSET_NAME not found')
    data['currency_id_to_name'] = {int(k): v for k, v in target.items()}

safe_extract('currency_id_to_name', extract_currency_id_to_name)


# ShipConfig constants for decoding shipConfigDump
def extract_ship_config():
    # Find ShipConfig module
    sc_mod = sys.modules.get('ShipConfig')
    if sc_mod is None:
        raise ImportError('Could not find ShipConfig module')

    fg = sc_mod.makeCompactDescription.func_globals
    result = {}
    result['UNIT_TYPE_NAMES'] = list(fg['UNIT_TYPE_NAMES'])

    # Slot system metadata: order and which have autobuy
    # allSlotSystems = (modernizationSlots, exteriorSlots, abilitySlots,
    #                   ensignSlots, ecoboostSlots, battleCardSlots)
    slot_fg = sc_mod.ShipSlots.__init__.func_globals
    slot_systems = []
    for cls_name in ('ModernizationSlots', 'ExteriorSlots', 'AbilitySlots',
                     'EnsignSlots', 'EcoboostSlots', 'BattleCardSlots'):
        cls = slot_fg[cls_name]
        has_autobuy = bool(getattr(cls, 'AUTO_BUY_CATEGORIES', []))
        has_color_schemes = 'colorSchemes' in cls.initFromCompactDescr.func_code.co_names
        slot_systems.append({
            'name': cls_name,
            'has_autobuy': has_autobuy,
            'has_color_schemes': has_color_schemes,
        })
    result['SLOT_SYSTEMS'] = slot_systems

    data['ship_config'] = result

safe_extract('ship_config', extract_ship_config)


# Output
output = {'data': data}
if errors:
    output['errors'] = errors

print(json.dumps(output, sort_keys=True))
