# coding=utf-8
"""
Opcode 0x26 — AccountInit, written once at session start.

Producer: FUN_14056e1a0. It is called from inside the 0x00 (BasePlayerCreate)
writer just BEFORE BasePlayerCreate emits its own record. The function looks
up the "Account" entity type in a global name->slot map, then writes:

    u32 entity_id         (the player avatar's entity_id, same as 0x00)
    u16 account_type_idx  (the index of the "Account" entity type in the
                           definitions table — varies per build)
    u32 reserved          (always written as literal 0)

Total: 10 bytes.

Confirmed empirically in 15.4 replay: `(542843, 3, 0)` — entity_id matches the
0x00/BasePlayerCreate's entity_id from the same replay.
"""
import struct

from replay_unpack.core import PrettyPrintObjectMixin


class AccountInit(PrettyPrintObjectMixin):
    __slots__ = ('entityId', 'accountTypeIdx', 'reserved')

    def __init__(self, stream):
        self.entityId, = struct.unpack('i', stream.read(4))
        self.accountTypeIdx, = struct.unpack('H', stream.read(2))
        self.reserved, = struct.unpack('I', stream.read(4))
