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

# TODO: fix the mapping
PACKETS_MAPPING = {
    0x0: BasePlayerCreate,
    0x2: EntityControl,
    0x3: EntityEnter,
    0x4: EntityLeave,
    0x7: EntityProperty,
    0x8: EntityMethod,
    0x22: NestedProperty,
    0x0a: Position,
    0x16: Version,
}

__all__ = [
    'EntityMethod',
    'Position',
    'EntityEnter',
    'EntityLeave',
    'EntityControl',
    'BasePlayerCreate',
    'EntityProperty',
    'NestedProperty',
    'Version',
    'PACKETS_MAPPING'
]
