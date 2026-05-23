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
from .AccountInit import AccountInit
from .BattleStats import BattleStats
from .CameraInput import CameraInput
from .CameraState import CameraState
from .CellPlayerCreate import CellPlayerCreate
from .EntityCreate import EntityCreate
from .EntityTransform import EntityTransform
from .Heartbeat import Heartbeat
from .Map import Map
from .PlayerEntityId import PlayerEntityId
from .PlayerPosition import PlayerPosition
from .WeaponLockToggle import WeaponLockToggle

# 0.x ("generic") opcodes that are stable across all studied versions.
# The 0.11.x and 12.6+ tables diverge: WG inserted BattleStats at 0x22 in 12.6,
# shifting every opcode >= 0x22 by +1. See REPLAY_PACKET_FORMATS.md.
PACKETS_MAPPING_GENERIC = {
    0x0: BasePlayerCreate,
    0x1: CellPlayerCreate,
    0x2: EntityControl,
    0x3: EntityEnter,
    0x4: EntityLeave,
    0x5: EntityCreate,
    # 0x6 = onEntityRestore (variable; not observed in normal recordings)
    0x7: EntityProperty,
    0x8: EntityMethod,
    0x0a: Position,
    0x0e: Heartbeat,        # stable across versions (below the 0.x→12.6 +1 shift)
    0x16: Version,
    0x18: CameraState,
    0x1d: CameraInput,
    0x20: PlayerEntityId,
}
# NOTE: opcodes >= 0x22 are shifted by +1 in 12.6+, so AccountInit and
# WeaponLockToggle live in the version-specific maps below, NOT in GENERIC.

PACKETS_MAPPING = {
    **PACKETS_MAPPING_GENERIC,
    0x22: NestedProperty,
    0x25: AccountInit,        # pre-shift slot (12.6+ moves this to 0x26)
    0x27: Map,
    0x29: EntityTransform,    # pre-shift slot of the 12.6+ 0x2a/0x2c sibling
    0x2b: PlayerPosition,     # pre-shift slot for the size-32 player-position record
    0x2e: WeaponLockToggle,   # pre-shift slot (12.6+ moves this to 0x2f)
}

PACKETS_MAPPING_12_6 = {
    **PACKETS_MAPPING_GENERIC,
    0x22: BattleStats,
    0x23: NestedProperty,
    0x26: AccountInit,        # 12.6+ slot for the once-at-start account marker
    0x28: Map,
    0x2a: EntityTransform,    # AoI/transform delta (sibling of 0x2c)
    0x2c: PlayerPosition,     # 12.6+ slot for the size-32 player-position record
    0x2f: WeaponLockToggle,   # 12.6+ slot for the 1-byte weapon-lock toggle
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
    'EntityTransform',
    'CameraState',
    'CameraInput',
    'Heartbeat',
    'PlayerEntityId',
    'AccountInit',
    'WeaponLockToggle',
    'Version',
    'PACKETS_MAPPING',
    'PACKETS_MAPPING_12_6',
]
