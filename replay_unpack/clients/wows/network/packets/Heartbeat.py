# coding=utf-8
"""
Opcode 0x0e — periodic heartbeat.

Producer: FUN_14056d310. Writes 4 bytes (an undefined4 from the wrapped
handler's input) on every tick the wrapper fires.

Empirical observation: across the entire 15.4 replay (count=7812 records),
the payload is byte-identical `00 00 00 a0 24 49 c2 3f`, which is exactly
8 bytes (not 4) — the writer's playback handler FUN_140569560 reads
`fread(&local_res8, 8, ...)` and forwards via `wrapped[+0xf8](u64)`.

Interpretation: heartbeat carrying a fixed constant. Decoded as f64 the value
is 0.14286 = 1/7, which might be a default tick interval baseline; but since
it never varies in any sampled replay, treating it as an opaque 8-byte token
is the safest interpretation.
"""
import struct

from replay_unpack.core import PrettyPrintObjectMixin


class Heartbeat(PrettyPrintObjectMixin):
    """8-byte heartbeat / keepalive marker."""

    __slots__ = ('raw', 'as_double')

    _DEFAULT = 0x3FC24924A0000000  # observed constant value across all sampled replays

    def __init__(self, stream):
        self.raw, = struct.unpack('Q', stream.read(8))
        self.as_double, = struct.unpack('d', struct.pack('Q', self.raw))
