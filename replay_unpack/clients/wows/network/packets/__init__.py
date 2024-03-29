# coding=utf-8
from replay_unpack.core.packets import (
    EntityControl,
    EntityEnter,
    EntityLeave,
    EntityProperty,
    EntityMethod,
    NestedProperty,
    BasePlayerCreate,
    Position,
    Version
)
from .BattleStats import BattleStats
from .CellPlayerCreate import CellPlayerCreate
from .EntityCreate import EntityCreate
from .Map import Map
from .PlayerPosition import PlayerPosition

PACKETS_MAPPING_GENERIC = {
    0x0: BasePlayerCreate,
    0x1: CellPlayerCreate,
    0x2: EntityControl,
    0x3: EntityEnter,
    0x4: EntityLeave,
    0x5: EntityCreate,
    # 0x6
    0x7: EntityProperty,
    0x8: EntityMethod,
    0x0a: Position,
    0x16: Version,
    0x2b: PlayerPosition
}

PACKETS_MAPPING = {
    **PACKETS_MAPPING_GENERIC,
    0x27: Map,
    0x22: NestedProperty,
}

PACKETS_MAPPING_12_6 = {
    **PACKETS_MAPPING_GENERIC,
    0x22: BattleStats,
    0x23: NestedProperty,
    0x28: Map,
}

__all__ = [
    'EntityMethod',
    'Map',
    'Position',
    'EntityCreate',
    'EntityEnter',
    'EntityLeave',
    'EntityControl',
    'BasePlayerCreate',
    'EntityProperty',
    'CellPlayerCreate',
    'NestedProperty',
    'PlayerPosition',
    'Version',
    'PACKETS_MAPPING',
    'PACKETS_MAPPING_12_6'
]
