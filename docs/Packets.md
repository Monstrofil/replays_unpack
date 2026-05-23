# Game packets

Packet IDs come from the BigWorld client/server protocol. The mapping
lives in `replay_unpack/clients/wows/network/packets/__init__.py`; WoWS
12.6 renumbered a few of them, so two tables are kept (`PACKETS_MAPPING`
and `PACKETS_MAPPING_12_6`) and the right one is picked per replay.

## Documented packets

* [Packet 0x0 (BasePlayerCreate)](packets/0x0.md)
* [Packet 0x1 (CellPlayerCreate)](packets/0x1.md)
* [Packet 0x2 (EntityControl)](packets/0x2.md)
* [Packet 0x3 (EntityEnter)](packets/0x3.md)
* [Packet 0x4 (EntityLeave)](packets/0x4.md)
* [Packet 0x5 (EntityCreate)](packets/0x5.md)
* [Packet 0x7 (EntityProperty)](packets/0x7.md)
* [Packet 0x8 (EntityMethod)](packets/0x8.md)
* [Packet 0x22 (NestedProperty / BattleStats since 12.6)](packets/0x22.md)
* [Packet 0x27 (Map, pre-12.6)](packets/0x27.md)

## Other packets handled in code

These are parsed but don't have a standalone doc yet — the struct lives
in the `packets/` package next to the others:

* `0x0a` — `Position` (entity position/orientation update)
* `0x16` — `Version` (client version string)
* `0x2b` — `PlayerPosition` (controlled-player + linked-entity position)
* `0x23` (12.6+) — `NestedProperty` (moved from `0x22`)
* `0x28` (12.6+) — `Map` (moved from `0x27`)
* `0x22` (12.6+) — `BattleStats` (post-battle results blob; triggers the
  battle-report builder in the WoWS client)
