[![Build Status](https://travis-ci.org/Monstrofil/replays_unpack.svg?branch=master)](https://travis-ci.org/Monstrofil/replays_unpack)

# WoWS replays parser

This tool re-implements part of wows (BigWorld) client-server protocol allowing to "play" replays without game client and get all needed information.

## Example

Command
```
replay_parser.py --replay="C:\Users\shish\Desktop\replays\2326_1582297987_Indomitable_37_Ridge.wowsreplay" --strict
```

Output
```
{
 "open": {
  "clientVersionFromXml": "0,9,1,2280585",
  "gameMode": 7,
  "clientVersionFromExe": "0,9,1,2280585",
  "scenarioUiCategoryId": 2,
  "mapDisplayName": "37_Ridge",
  "mapId": 21,
  "weatherParams": {
   "0": [
    "PCOW005_Evening"
   ],
   "1": [
    "PCOW010_Rain_Logic",
    "PCOW005_Evening"
   ]
  },
  "mapBorder": null,
  "duration": 1200,
  "gameLogic": "Domination",
  "name": "9x9",
  "scenario": "Skirmish_Domination",
  "playerID": 0,
  "vehicles": [
   {
    "shipId": 4180620752,
    "relation": 1,
    "id": 135003008,
    "name": "Brushlesss"
   }
   ...
  ],
  "playersPerTeam": 9,
  "dateTime": "21.02.2020 16:38:50",
  "mapName": "spaces/37_Ridge",
  "playerName": "artemon749",
  "scenarioConfigId": 147,
  "teamsCount": 2,
  "logic": "Domination",
  "playerVehicle": "PBSA508-Indomitable",
  "battleDuration": 1200
 },
 "hidden": {
  "achievements": {},
  "ribbons": {
   "1154556": {
    "19": 3,
    "26": 49,
    "25": 87,
    "4": 7,
    "6": 15,
    "9": 17,
    "5": 2,
    "21": 25,
    "22": 55,
    "3": 7,
    "10": 1,
    "11": 1,
    "27": 2
   }
  },
  "players": {
   "135003008": {
    "accountDBID": 108274646,
    "avatarId": 1154552,
    "camouflageInfo": [
     4293849008,
     0
    ],
    "clanColor": 13408614,
    "clanID": 423955,
    "clanTag": "CRUIS",
    "crewParams": [
     4291995088,
     [
      0,
      0,
      0,
      0
     ]
    ],
    "dogTag": [
     4253010864,
     4136586160
    ],
    "fragsCount": 0,
    "friendlyFireEnabled": true,
    "id": 135003008,
    "invitationsEnabled": 0,
    "isAbuser": false,
    "isAlive": false,
    "isBot": false,
    "isClientLoaded": false,
    "isConnected": false,
    "isHidden": false,
    "isLeaver": true,
    "isPreBattleOwner": false,
    "killedBuildingsCount": 0,
    "maxHealth": 80900,
    "name": "Brushlesss",
    "playerMode": {
     "fixedDict": {
      "playerModeType": 0,
      "observedTeamId": 0
     }
    },
    "preBattleIdOnStart": 0,
    "preBattleSign": 0,
    "prebattleId": 0,
    "realm": "RU",
    "shipComponents": {
     "engine": "AB1_Engine",
     "airDefense": "A_AirDefense",
     "radars": "A_Radars",
     "artillery": "AB1_Artillery",
     "torpedoes": "TorpedoesDefault",
     "atba": "A_ATBA",
     "scout": "ScoutTypeDefault",
     "aiParams": "AIParams",
     "fighter": "FighterTypeDefault",
     "finders": "A_Finders",
     "hydrophone": "HydrophoneDefault",
     "flightControl": "FlightControlDefault",
     "fireControl": "AB1_FireControl",
     "airArmament": "AB_AirArmament",
     "cameras": "Cameras",
     "underwaterCamera": "UnderwaterCamera",
     "torpedoBomber": "TorpedoBomberTypeDefault",
     "directors": "A_Directors",
     "hull": "A_Hull",
     "diveBomber": "DiveBomberTypeDefault",
     "auxiliaryPlane": "AuxiliaryPlaneTypeDefault",
     "depthCharges": "DepthChargeGunsDefault"
    },
    "shipId": 1154553,
    "shipParamsId": 4180620752,
    "skinId": 4180620752,
    "teamId": 0,
    "ttkStatus": false
   },
   "521958": {
    "accountDBID": 5389565,
    "avatarId": 1154554,
    "camouflageInfo": [
     4182273968,
     0
    ],
    "clanColor": 14931616,
    "clanID": 430467,
    "clanTag": "VOY",
    "crewParams": [
     4293044208,
     [
      0,
      0,
      0,
      0
     ]
    ],
    "dogTag": [
     4253010864,
     4154411952
    ],
    "fragsCount": 2,
    "friendlyFireEnabled": true,
    "id": 521958,
    "invitationsEnabled": 0,
    "isAbuser": false,
    "isAlive": true,
    "isBot": false,
    "isClientLoaded": true,
    "isConnected": true,
    "isHidden": false,
    "isLeaver": false,
    "isPreBattleOwner": false,
    "killedBuildingsCount": 0,
    "maxHealth": 27500,
    "name": "Pavor_nocturnus",
    "playerMode": {
     "fixedDict": {
      "playerModeType": 0,
      "observedTeamId": 0
     }
    },
    "preBattleIdOnStart": 0,
    "preBattleSign": 0,
    "prebattleId": 0,
    "realm": "RU",
    "shipComponents": {
     "engine": "EngineDefault",
     "airDefense": "AirDefenseDefault",
     "radars": "RadarsDefault",
     "artillery": "ArtilleryDefault",
     "torpedoes": "TorpedoesDefault",
     "atba": "ATBADefault",
     "scout": "ScoutTypeDefault",
     "aiParams": "AIParams",
     "fighter": "FighterTypeDefault",
     "finders": "FindersDefault",
     "hydrophone": "HydrophoneDefault",
     "flightControl": "FlightControlDefault",
     "fireControl": "FireControlDefault",
     "airArmament": "AirArmamentDefault",
     "cameras": "Cameras",
     "underwaterCamera": "UnderwaterCamera",
     "torpedoBomber": "TorpedoBomberTypeDefault",
     "directors": "DirectorsDefault",
     "hull": "HullDefault",
     "diveBomber": "DiveBomberTypeDefault",
     "auxiliaryPlane": "AuxiliaryPlaneTypeDefault",
     "depthCharges": "DepthChargeGunsDefault"
    },
    "shipId": 1154555,
    "shipParamsId": 4288591856,
    "skinId": 4288591856,
    "teamId": 0,
    "ttkStatus": false
   }
   ...
  },
  "battle_result": {
   "winner_team_id": 0,
   "victory_type": 9
  },
  "death_map": [
   [
    1154571,
    1154587,
    4
   ],
   [
    1154585,
    1154581,
    2
   ]
  ],
  "map": "37_Ridge",
  "player_id": 1154556,
  "control_points": [
   {
    "position": [
     -279.99969482421875,
     0.0
    ],
    "radius": 135.0,
    "innerRadius": 0.0,
    "buoy_modelID": 4290944628,
    "nextControlPoint": -1,
    "controlPointType": 1,
    "timerName": "",
    "teamId": 0,
    "progress": [
     0.0,
     60.0
    ],
    "neutralProgress": 0.0,
    "invaderTeam": -1,
    "bothInside": 0,
    "hasInvaders": 0,
    "isEnabled": 1,
    "isVisible": 1
   },
   {
    "position": [
     150.0,
     -0.000396728515625
    ],
    "radius": 135.0,
    "innerRadius": 0.0,
    "buoy_modelID": 4290944628,
    "nextControlPoint": -1,
    "controlPointType": 1,
    "timerName": "",
    "teamId": 0,
    "progress": [
     0.0,
     60.0
    ],
    "neutralProgress": 0.0,
    "invaderTeam": -1,
    "bothInside": 0,
    "hasInvaders": 1,
    "isEnabled": 1,
    "isVisible": 1
   },
   {
    "position": [
     536.9974975585938,
     -0.0001983642578125
    ],
    "radius": 135.0,
    "innerRadius": 0.0,
    "buoy_modelID": 4290944628,
    "nextControlPoint": -1,
    "controlPointType": 1,
    "timerName": "",
    "teamId": 0,
    "progress": [
     0.0,
     60.0
    ],
    "neutralProgress": 0.0,
    "invaderTeam": -1,
    "bothInside": 0,
    "hasInvaders": 1,
    "isEnabled": 1,
    "isVisible": 1
   }
  ],
  "tasks": [],
  "skills": {
   "1154587": [
    2,    3,
    12,
    21,
    30
   ]   
  }
 },
 "error": null
}

Process finished with exit code 0

```


Detailed docs coming.
