![Python package](https://github.com/Monstrofil/replays_unpack/actions/workflows/pythonpackage.yml/badge.svg)

# Replay Parser (WoWS, WoT, WoWP)

A pure-Python parser for BigWorld-engine replay files. It decodes the
replay container, decrypts and decompresses the replay stream, and "plays"
the packets back in memory using the same `.def` entity definitions the
real game client uses. On top of that raw playback you can hook in your
own client to collect whatever you need: live game state, damage / ribbon
events, post-battle results, animations, etc.

![sample animation rendered from replay data](docs/files/animation.gif)

## Supported games

| Game                 | Status     | Notes                                                       |
|----------------------|------------|-------------------------------------------------------------|
| World of Warships    | Primary    | All released versions from 0.8.0 through 15.4.0 are bundled |
| World of Tanks       | Reference  | A single bundled version (1.8.0) used as an example         |
| World of Warplanes   | Reference  | Wired up; not actively maintained                           |

New WoWS patches are added to `replay_unpack/clients/wows/versions/`
automatically by CI when WG ships a new client. See the `versions/`
directory for the full list.

## Install

```bash
pip install -r requirements.txt
python setup.py install
```

Python 3.10 is what CI runs against; anything 3.9+ should work. The only
non-stdlib runtime requirements are `pycryptodomex`, `lxml` and
`packaging`.

## Usage

### CLI

`replay_parser.py` is the entry point and works for all three games. It
auto-detects the game from the replay container and returns the parsed
state as JSON on stdout:

```bash
python replay_parser.py --replay path/to/replay.wowsreplay
```

Useful flags:

- `--strict_mode` — re-raise the first packet-parsing error instead of
  swallowing it. Use this when debugging an unsupported version.
- `--raw_data_output FILE` — also dump the decrypted+decompressed replay
  stream to `FILE` for offline inspection.
- `--log_level DEBUG` — verbose packet trace.

### As a library

```python
from replay_parser import ReplayParser

info = ReplayParser('path/to/replay.wowsreplay', strict=False).get_info()
# info['open']      -> the engine_data JSON header
# info['hidden']    -> whatever the game-specific client produced
# info['error']     -> error string if hidden-data parsing failed
```

The `hidden` payload comes from a game-specific `BattleController`. For
WoWS that includes the players list, damage map, achievements, ribbons,
death map, ship configurations and — when the replay contains the
post-battle `BattleStats` packet — a structured battle report (see
`replay_unpack/clients/wows/versions/<ver>/battle_report.py`).

### Writing a custom client

Subclass `ReplayPlayer` and override `_process_packet` to react to any
subset of the documented packets. `examples/wows_parser/` and
`examples/wows_parser_2/` are the minimal templates; `examples/wot_parser/`
shows the same idea for World of Tanks.

## How it works

- Replay container decoded into a header + encrypted/compressed payload
  (see [docs/Introduction.md](docs/Introduction.md)).
- Payload decrypted (Blowfish, hard-coded WG key) and zlib-decompressed.
- Bytes split into BigWorld packets; each packet type is parsed into a
  typed object (see [docs/Packets.md](docs/Packets.md)).
- Entity / method / property packets are dispatched against the `.def`
  files shipped under each `versions/<ver>/scripts/` directory, so adding
  support for a new game version is mostly about dropping in the new
  scripts — no hand-maintained packet IDs.
- A `BattleController` subscribes to the entity methods it cares about
  (`onArenaStateReceived`, `receiveDamageStat`, `onAchievementEarned`,
  `onBattleEnd`, …) and accumulates state.

For the algorithm used to compute method/property indexes from `.def`
files, see
[docs/Getting exposed index for properties and methods.md](docs/Getting%20exposed%20index%20for%20properties%20and%20methods.md).

## tools/

Helper scripts that produce the per-version data that lives under
`replay_unpack/clients/wows/versions/<ver>/`:

- `extract_constants.py` — runs inside [wows-sandbox] (Python 2.7) to
  dump player-property maps, ship-config schemas, damage-stat constants,
  etc. from the real game scripts.
- `generate_constants.py` + `constants.py.j2` — render the extracted
  JSON into the per-version `constants.py` module.
- `distill_gameparams.py` + `distill_schema.yaml` — distill the
  multi-hundred-MB `GameParams.data` pickle into a small lookup module
  (`game_params.py`) keyed by ID, used by the battle report builder to
  resolve ship / modifier / achievement IDs to canonical names.

[wows-sandbox]: https://github.com/Monstrofil/wows-sandbox

## Similar projects

- <https://github.com/evido/wotreplay-parser> (C++, WoT)
- <https://github.com/Aimdrol/WoT-Replay-Analyzer> (exe only, WoT)
- <https://github.com/Phalynx/WoT-Replay-To-JSON> (Python, WoT)
- <https://gist.github.com/benvanstaveren/2402016> (Perl, WoT)
- <https://github.com/thesilvervestgroup/wot-replay-parser> (PHP, WoT)

## Why this one

- Reimplements the BigWorld client/server protocol used in replays, not
  just a screen-scrape of a particular game's data.
- Entity methods and properties are resolved from the original `.def`
  files, so new game versions usually need data drops, not code changes.
- Extensible: bring your own `BattleController` / `ReplayPlayer`
  subclass to extract whatever data you need.
- Post-battle results (introduced in WoWS 12.6) are unpacked into a
  stable, machine-readable battle report.
