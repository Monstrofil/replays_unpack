[![Build Status](https://travis-ci.org/Monstrofil/replays_unpack.svg?branch=master)](https://travis-ci.org/Monstrofil/replays_unpack)

# Replay Parser (WoT & WoWS)

The other one project that aims to decode replay files and provide ability to "play"
them without game client. Project provides public API that allows you to create your own
"client" which handles game events and does whatever you want (collect data and return json, 
create images and animations, etc).

Here is an example of what data can be retrived:
![cool anumation with tanks](docs/files/animation.gif)

## Similar Projects

- https://github.com/evido/wotreplay-parser (C++)
- https://github.com/Aimdrol/WoT-Replay-Analyzer (exe only)
- https://github.com/Phalynx/WoT-Replay-To-JSON (Python)
- https://gist.github.com/benvanstaveren/2402016 (Perl)
- https://github.com/thesilvervestgroup/wot-replay-parser (PHP)


## Why this one is better
- Fully reimplemented BigWorld client-server protocol used in replays;
- more than 9 completely parsed [packets](docs/Packets.md);
- great support of entities: methods [calls](docs/Packets/0x8.md), properties [change](docs/Packets/0x8.md) 
  (including [nested](docs/Packets/0x22.md) properties) without any hardcode: 
  we use .def files from game client to get subpacket ids;
- extendability and flexibility by providing public api (see examples).
