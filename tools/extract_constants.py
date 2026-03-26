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


# Output
output = {'data': data}
if errors:
    output['errors'] = errors

print(json.dumps(output, sort_keys=True))
