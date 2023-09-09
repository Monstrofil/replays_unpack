# coding=utf-8

id_property_map = {0: 'accountDBID', 1: 'antiAbuseEnabled', 2: 'avatarId', 3: 'camouflageInfo',
                   4: 'clanColor', 5: 'clanID', 6: 'clanTag', 7: 'crewParams', 8: 'dogTag',
                   9: 'fragsCount', 10: 'friendlyFireEnabled', 11: 'id', 12: 'invitationsEnabled',
                   13: 'isAbuser', 14: 'isAlive', 15: 'isBot', 16: 'isClientLoaded', 17: 'isConnected',
                   18: 'isHidden', 19: 'isLeaver', 20: 'isPreBattleOwner', 21: 'isTShooter', 22: 'keyTargetMarkers',
                   23: 'killedBuildingsCount', 24: 'maxHealth', 25: 'name', 26: 'playerMode', 27: 'preBattleIdOnStart',
                   28: 'preBattleSign', 29: 'prebattleId', 30: 'realm', 31: 'shipComponents', 32: 'shipConfigDump',
                   33: 'shipId', 34: 'shipParamsId', 35: 'skinId', 36: 'teamId', 37: 'ttkStatus'}
property_id_map = {value: key for key, value in id_property_map.items()}

# ModsShell.API_v_1_0.battleGate.PlayersInfo.gSharedBotInfo._numMemberMap
id_property_map_bots = {0: 'accountDBID', 1: 'antiAbuseEnabled', 2: 'camouflageInfo', 3: 'clanColor',
                        4: 'clanID', 5: 'clanTag', 6: 'crewParams', 7: 'dogTag', 8: 'fragsCount',
                        9: 'friendlyFireEnabled', 10: 'id', 11: 'isAbuser', 12: 'isAlive',
                        13: 'isBot', 14: 'isHidden', 15: 'isTShooter', 16: 'keyTargetMarkers',
                        17: 'killedBuildingsCount', 18: 'maxHealth', 19: 'name', 20: 'realm',
                        21: 'shipComponents', 22: 'shipConfigDump', 23: 'shipId', 24: 'shipParamsId',
                        25: 'skinId', 26: 'teamId', 27: 'ttkStatus'}
property_id_map_bots = {value: key for key, value in id_property_map.items()}

# ModsShell.API_v_1_0.battleGate.PlayersInfo.gSharedObserverInfo._numMemberMap
id_property_map_observer = {0: 'accountDBID', 1: 'avatarId', 2: 'dogTag', 3: 'id', 4: 'invitationsEnabled',
                            5: 'isAlive',
                            6: 'isClientLoaded', 7: 'isConnected', 8: 'isLeaver', 9: 'isPreBattleOwner', 10: 'name',
                            11: 'playerMode', 12: 'preBattleIdOnStart', 13: 'preBattleSign', 14: 'prebattleId',
                            15: 'realm', 16: 'teamId'}
property_id_map_bots_observer = {value: key for key, value in id_property_map.items()}


class DamageStatsType:
    """See Avatar.DamageStatsType"""
    DAMAGE_STATS_ENEMY = 0
    DAMAGE_STATS_ALLY = 1
    DAMAGE_STATS_SPOT = 2
    DAMAGE_STATS_AGRO = 3


class Category(object):
    """Category of task to separate for UI"""

    CHALLENGE = 4
    PRIMARY = 1
    SECONDARY = 2
    TERTIARY = 3

    ids = {'Challenge': 4, 'Primary': 1, 'Secondary': 2, 'Tertiary': 3}
    names = {1: 'Primary', 2: 'Secondary', 3: 'Tertiary', 4: 'Challenge'}


class Status(object):
    CANCELED = 4
    FAILURE = 3
    IN_PROGRESS = 1
    NOT_STARTED = 0
    SUCCESS = 2
    UPDATED = 5

    ids = {'Updated': 5, 'Success': 2, 'Canceled': 4, 'NotStarted': 0, 'Failure': 3, 'InProgress': 1}
    names = {0: 'NotStarted', 1: 'InProgress', 2: 'Success', 3: 'Failure', 4: 'Canceled', 5: 'Updated'}


class TaskType(object):
    DIGIT = 1
    DIGIT_SINGLE = 5
    NO_TYPE = 0
    PROGRESS_BAR = 4
    REVERSED_TIMER = 3
    TIMER = 2

    names = {0: 'NoType', 1: 'Digit', 2: 'Timer', 3: 'ReversedTimer', 4: 'ProgressBar', 5: 'DigitSingle'}
    ids = {'ReversedTimer': 3, 'Digit': 1, 'DigitSingle': 5, 'Timer': 2, 'ProgressBar': 4, 'NoType': 0}


# {i: vars(j) for i,j in Vehicle.DeathReason._DeathReason__byId.items()}
DEATH_TYPES = {
    0: {'sound': 'Health', 'icon': 'frags', 'id': 0, 'name': 'NONE'},
    1: {'sound': 'Health', 'icon': 'frags', 'id': 1, 'name': 'ARTILLERY'},
    2: {'sound': 'ATBA', 'icon': 'icon_frag_atba', 'id': 2, 'name': 'ATBA'},
    3: {'sound': 'Torpedo', 'icon': 'icon_frag_torpedo', 'id': 3, 'name': 'TORPEDO'},
    4: {'sound': 'Bomb', 'icon': 'icon_frag_bomb', 'id': 4, 'name': 'BOMB'},
    5: {'sound': 'Torpedo', 'icon': 'icon_frag_torpedo', 'id': 5, 'name': 'TBOMB'},
    6: {'sound': 'Burning', 'icon': 'icon_frag_burning', 'id': 6, 'name': 'BURNING'},
    7: {'sound': 'RAM', 'icon': 'icon_frag_ram', 'id': 7, 'name': 'RAM'},
    8: {'sound': 'Health', 'icon': 'frags', 'id': 8, 'name': 'TERRAIN'},
    9: {'sound': 'Flood', 'icon': 'icon_frag_flood', 'id': 9, 'name': 'FLOOD'},
    10: {'sound': 'Health', 'icon': 'frags', 'id': 10, 'name': 'MIRROR'},
    11: {'sound': 'Torpedo', 'icon': 'icon_frag_naval_mine', 'id': 11, 'name': 'SEA_MINE'},
    12: {'sound': 'Health', 'icon': 'frags', 'id': 12, 'name': 'SPECIAL'},
    13: {'sound': 'DepthCharge', 'icon': 'icon_frag_depthbomb', 'id': 13, 'name': 'DBOMB'},
    14: {'sound': 'Rocket', 'icon': 'icon_frag_rocket', 'id': 14, 'name': 'ROCKET'},
    15: {'sound': 'Detonate', 'icon': 'icon_frag_detonate', 'id': 15, 'name': 'DETONATE'},
    16: {'sound': 'Health', 'icon': 'frags', 'id': 16, 'name': 'HEALTH'},
    17: {'sound': 'Shell_AP', 'icon': 'icon_frag_main_caliber', 'id': 17, 'name': 'AP_SHELL'},
    18: {'sound': 'Shell_HE', 'icon': 'icon_frag_main_caliber', 'id': 18, 'name': 'HE_SHELL'},
    19: {'sound': 'Shell_CS', 'icon': 'icon_frag_main_caliber', 'id': 19, 'name': 'CS_SHELL'},
    20: {'sound': 'Fel', 'icon': 'icon_frag_fel', 'id': 20, 'name': 'FEL'},
    21: {'sound': 'Portal', 'icon': 'icon_frag_portal', 'id': 21, 'name': 'PORTAL'},
    22: {'sound': 'SkipBomb', 'icon': 'icon_frag_skip', 'id': 22, 'name': 'SKIP_BOMB'},
    23: {'sound': 'SECTOR_WAVE', 'icon': 'icon_frag_wave', 'id': 23, 'name': 'SECTOR_WAVE'},
    24: {'sound': 'Health', 'icon': 'icon_frag_acid', 'id': 24, 'name': 'ACID'},
    25: {'sound': 'LASER', 'icon': 'icon_frag_laser', 'id': 25, 'name': 'LASER'},
    26: {'sound': 'Match', 'icon': 'icon_frag_octagon', 'id': 26, 'name': 'MATCH'},
    27: {'sound': 'Timer', 'icon': 'icon_timer', 'id': 27, 'name': 'TIMER'},
    28: {'sound': 'DepthCharge', 'icon': 'icon_frag_depthbomb', 'id': 28, 'name': 'ADBOMB'}
}

# >>> CrewModifiers.SkillTypeEnum.ID_TO_NAME
SKILL_TYPE_ID_TO_NAME = {
    0: 'NoneSkill', 1: 'GmReloadAaDamageConstant', 2: 'DefenceCritFireFlooding', 3: 'GmTurn', 4: 'TorpedoReload',
    5: 'ConsumablesCrashcrewRegencrewReload', 6: 'ConsumablesDuration', 7: 'DetectionTorpedoRange',
    8: 'HeFireProbability',
    9: 'GmRangeAaDamageBubbles', 10: 'PlanesDefenseDamageConstant', 11: 'PlanesForsageDuration',
    12: 'DetectionVisibilityRange', 13: 'ConsumablesReload', 14: 'DefenceFireProbability', 15: 'PlanesAimingBoost',
    16: 'PlanesSpeed', 17: 'ConsumablesAdditional', 18: 'DefenseCritProbability', 19: 'DetectionAlert',
    20: 'Maneuverability', 21: 'GmShellReload', 22: 'PlanesConsumablesCallfightersUpgrade',
    23: 'ArmamentReloadAaDamage',
    24: 'TorpedoSpeed', 25: 'DefenseHp', 26: 'AtbaAccuracy', 27: 'AaPrioritysectorDamageConstant',
    28: 'DetectionAiming',
    29: 'PlanesReload', 30: 'TorpedoDamage', 31: 'ConsumablesFighterAdditional',
    32: 'PlanesConsumablesSpeedboosterReload',
    33: 'HePenetration', 34: 'DetectionDirection', 35: 'AaDamageConstantBubbles', 36: 'AaDamageConstantBubblesCv',
    37: 'ApDamageBb', 38: 'ApDamageCa', 39: 'ApDamageDd', 40: 'AtbaRange', 41: 'AtbaUpgrade',
    42: 'ConsumablesCrashcrewRegencrewUpgrade', 43: 'ConsumablesSpotterUpgrade', 44: 'DefenceUw',
    45: 'DetectionVisibilityCrashcrew', 46: 'HeFireProbabilityCv', 47: 'HeSapDamage', 48: 'PlanesApDamage',
    49: 'PlanesConsumablesCallfightersAdditional', 50: 'PlanesConsumablesCallfightersPreparationtime',
    51: 'PlanesConsumablesCallfightersRange', 52: 'PlanesConsumablesRegeneratehealthUpgrade',
    53: 'PlanesDefenseDamageBubbles', 54: 'PlanesDivebomberSpeed', 55: 'PlanesForsageRenewal', 56: 'PlanesHp',
    57: 'PlanesTorpedoArmingrange', 58: 'PlanesTorpedoSpeed', 59: 'PlanesTorpedoUwReduced',
    60: 'TorpedoFloodingProbability', 61: 'TriggerSpeedBb', 62: 'TriggerGmAtbaReloadBb', 63: 'TriggerGmAtbaReloadCa',
    64: 'TriggerGmReload', 65: 'TriggerSpeed', 66: 'TriggerSpeedAccuracy', 67: 'TriggerSpreading',
    68: 'TriggerPingerReloadBuff', 69: 'TriggerPingerSpeedBuff', 70: 'SubmarineHoldSectors',
    71: 'TriggerConsSonarTimeCoeff', 72: 'TriggerSeenTorpedoReload', 73: 'SubmarineTorpedoPingDamage',
    74: 'TriggerConsRudderTimeCoeff', 75: 'SubmarineBatteryCapacity', 76: 'SubmarineDangerAlert',
    77: 'SubmarineBatteryBurnDown', 78: 'SubmarineSpeed', 79: 'SubmarineConsumablesReload',
    80: 'SubmarineConsumablesDuration', 81: 'TriggerBurnGmReload', 82: 'ArmamentReloadSubmarine'
}

# CrewModifiers.ShipTypes.TYPE_BY_ID
SHIP_TYPE_BY_ID = {
    0: 'AirCarrier',
    1: 'Battleship',
    2: 'Cruiser',
    3: 'Destroyer',
    4: 'Auxiliary',
    5: 'Submarine'
}

# BattleResultsSystem.unpackClientPublicRes.func_globals['CLIENT_PUBLIC_RESULTS']
CLIENT_PUBLIC_RESULTS = (
    'account_db_id', 'name', 'clan_id', 'clan_tag', 'clan_color', 'clan_league', 'team_id', 'vehicle_type_id',
    'prebattle_id', 'home_realm', 'achievements', 'rank_battles_season_id', 'rank_info_dump', 'prebattle_sign',
    'initial_prebattle_id', 'max_health', 'is_hidden', 'playerMode', 'isMercenary', 'brawl_rating_data', 'remained_hp',
    'is_alive', 'life_time_sec', 'distance', 'capture_points', 'dropped_capture_points', 'first_ships_spotted_by_ship',
    'first_ships_spotted_by_plane', 'first_planes_spotted_by_ship', 'first_planes_spotted_by_plane',
    'first_plane_items_spotted_by_ship', 'first_plane_items_spotted_by_plane', 'ships_killed', 'team_ships_killed',
    'killer_building_id', 'shots_main_ap', 'shots_main_cs', 'shots_main_he', 'shots_atba_ap', 'shots_atba_cs',
    'shots_atba_he', 'shots_tpd', 'shots_bomb', 'shots_bomb_avia', 'shots_bomb_alt', 'shots_bomb_airsupport',
    'shots_dbomb_airsupport', 'shots_tbomb', 'shots_tbomb_avia', 'shots_tbomb_alt', 'shots_tbomb_airsupport',
    'shots_rocket', 'shots_rocket_avia', 'shots_rocket_alt', 'shots_rocket_airsupport', 'shots_skip', 'shots_skip_avia',
    'shots_skip_alt', 'shots_skip_airsupport', 'shots_adbomb', 'shots_dbomb', 'shots_sea_mine', 'hits_main_ap',
    'hits_main_cs', 'hits_main_he', 'hits_atba_ap', 'hits_atba_cs', 'hits_atba_he', 'hits_tpd', 'hits_bomb',
    'hits_bomb_avia', 'hits_bomb_alt', 'hits_bomb_airsupport', 'hits_tbomb', 'hits_tbomb_avia', 'hits_tbomb_alt',
    'hits_tbomb_airsupport', 'hits_ram', 'hits_fire', 'hits_flood', 'hits_dbomb', 'hits_rocket', 'hits_rocket_avia',
    'hits_rocket_alt', 'hits_rocket_airsupport', 'hits_skip', 'hits_skip_avia', 'hits_skip_alt', 'hits_skip_airsupport',
    'hits_dbomb_airsupport', 'hits_adbomb', 'hits_sea_mine', 'received_hits_main_ap', 'received_hits_main_cs',
    'received_hits_main_he', 'received_hits_atba_ap', 'received_hits_atba_cs', 'received_hits_atba_he',
    'received_hits_tpd',
    'received_hits_bomb', 'received_hits_bomb_avia', 'received_hits_bomb_alt', 'received_hits_bomb_airsupport',
    'received_hits_tbomb', 'received_hits_tbomb_avia', 'received_hits_tbomb_alt', 'received_hits_tbomb_airsupport',
    'received_hits_ram', 'received_hits_fire', 'received_hits_flood', 'received_hits_sea_mine', 'received_hits_dbomb',
    'received_hits_rocket', 'received_hits_rocket_avia', 'received_hits_rocket_alt', 'received_hits_rocket_airsupport',
    'received_hits_skip', 'received_hits_skip_avia', 'received_hits_skip_alt', 'received_hits_skip_airsupport',
    'received_hits_dbomb_airsupport', 'received_hits_from_buildings_main_ap', 'received_hits_from_buildings_main_cs',
    'received_hits_from_buildings_main_he', 'received_hits_from_buildings_atba_ap',
    'received_hits_from_buildings_atba_cs',
    'received_hits_from_buildings_atba_he', 'received_hits_from_buildings_fire', 'received_hits_from_buildings_flood',
    'received_hits_from_buildings_bomb_avia', 'received_hits_from_buildings_tbomb_avia',
    'received_hits_from_buildings_rocket_avia', 'received_hits_from_buildings_skip_avia',
    'received_hits_from_buildings_bomb_alt', 'received_hits_from_buildings_tbomb_alt',
    'received_hits_from_buildings_rocket_alt', 'received_hits_from_buildings_skip_alt',
    'received_hits_from_buildings_bomb_airsupport', 'received_hits_from_buildings_dbomb_airsupport',
    'received_hits_from_buildings_tbomb_airsupport', 'received_hits_from_buildings_rocket_airsupport',
    'received_hits_from_buildings_skip_airsupport', 'damage_main_ap', 'damage_main_cs', 'damage_main_he',
    'damage_atba_ap',
    'damage_atba_cs', 'damage_atba_he', 'damage_tpd_normal', 'damage_tpd_deep', 'damage_tpd_alter', 'damage_bomb',
    'damage_bomb_avia', 'damage_bomb_alt', 'damage_bomb_airsupport', 'damage_tbomb', 'damage_tbomb_avia',
    'damage_tbomb_alt', 'damage_tbomb_airsupport', 'damage_ram', 'damage_fire', 'damage_flood', 'damage_dbomb_direct',
    'damage_dbomb_splash', 'damage_sea_mine', 'damage_rocket', 'damage_rocket_avia', 'damage_rocket_alt',
    'damage_rocket_airsupport', 'damage_skip', 'damage_skip_avia', 'damage_skip_alt', 'damage_skip_airsupport',
    'damage_wave', 'damage_charge_laser', 'damage_pulse_laser', 'damage_axis_laser', 'damage_dbomb_airsupport',
    'damage_adbomb', 'received_damage_main_ap', 'received_damage_main_cs', 'received_damage_main_he',
    'received_damage_tpd_normal', 'received_damage_tpd_deep', 'received_damage_tpd_alter', 'received_damage_bomb',
    'received_damage_bomb_avia', 'received_damage_bomb_alt', 'received_damage_bomb_airsupport', 'received_damage_tbomb',
    'received_damage_tbomb_avia', 'received_damage_tbomb_alt', 'received_damage_tbomb_airsupport',
    'received_damage_ram',
    'received_damage_atba_ap', 'received_damage_atba_cs', 'received_damage_atba_he', 'received_damage_fire',
    'received_damage_flood', 'received_damage_mirror', 'received_damage_sea_mine', 'received_damage_special',
    'received_damage_dbomb', 'received_damage_rocket', 'received_damage_rocket_avia', 'received_damage_rocket_alt',
    'received_damage_rocket_airsupport', 'received_damage_skip', 'received_damage_skip_avia',
    'received_damage_skip_alt',
    'received_damage_skip_airsupport', 'received_damage_dbomb_airsupport', 'received_damage_adbomb',
    'received_damage_from_buildings_main_ap', 'received_damage_from_buildings_main_cs',
    'received_damage_from_buildings_main_he', 'received_damage_from_buildings_atba_ap',
    'received_damage_from_buildings_atba_cs', 'received_damage_from_buildings_atba_he',
    'received_damage_from_buildings_fire', 'received_damage_from_buildings_flood',
    'received_damage_from_buildings_bomb_avia', 'received_damage_from_buildings_tbomb_avia',
    'received_damage_from_buildings_rocket_avia', 'received_damage_from_buildings_skip_avia',
    'received_damage_from_buildings_bomb_alt', 'received_damage_from_buildings_tbomb_alt',
    'received_damage_from_buildings_rocket_alt', 'received_damage_from_buildings_skip_alt',
    'received_damage_from_buildings_bomb_airsupport', 'received_damage_from_buildings_dbomb_airsupport',
    'received_damage_from_buildings_tbomb_airsupport', 'received_damage_from_buildings_rocket_airsupport',
    'received_damage_from_buildings_skip_airsupport', 'module_kills', 'module_crits', 'module_major_crits',
    'module_fires',
    'module_floods', 'received_module_crits_artillery', 'received_module_crits_torpedo_tube',
    'received_module_crits_atba',
    'received_module_crits_air_defense', 'received_module_crits_engine', 'received_module_crits_steering_gear',
    'received_module_crits_pinger', 'received_module_kills_artillery', 'received_module_kills_torpedo_tube',
    'received_module_kills_atba', 'received_module_kills_air_defense', 'received_module_kills_depth_charge_gun',
    'battle_drops_picked', 'battle_picked_drop_points', 'team_captured_drop_count', 'planes_killed_by_ship',
    'planes_killed_by_plane', 'team_planes_killed', 'planes_lost_scouts', 'planes_lost_sfighters',
    'planes_lost_fighters',
    'planes_lost_fighters_avia', 'planes_lost_fighters_airsupport', 'planes_lost_bombers', 'planes_lost_bombers_avia',
    'planes_lost_bombers_airsupport', 'planes_lost_tbombers', 'planes_lost_tbombers_avia',
    'planes_lost_tbombers_airsupport', 'planes_lost_skipbombers', 'planes_lost_skipbombers_avia',
    'planes_lost_skipbombers_airsupport', 'planes_lost_fighters_alt', 'planes_lost_bombers_alt',
    'planes_lost_tbombers_alt',
    'planes_lost_skipbombers_alt', 'scouts_total_killed', 'sfighters_total_killed', 'fighters_total_killed',
    'fighters_total_killed_avia', 'fighters_total_killed_alt', 'fighters_total_killed_airsupport',
    'bombers_total_killed',
    'bombers_total_killed_avia', 'bombers_total_killed_alt', 'bombers_total_killed_airsupport', 'tbombers_total_killed',
    'tbombers_total_killed_avia', 'tbombers_total_killed_alt', 'tbombers_total_killed_airsupport',
    'skipbombers_total_killed', 'skipbombers_total_killed_avia', 'skipbombers_total_killed_alt',
    'skipbombers_total_killed_airsupport', 'planes_killed_by_scouts', 'planes_killed_by_fighters',
    'planes_killed_by_bombers', 'planes_killed_by_tbombers', 'planes_killed_by_sfighters',
    'planes_killed_by_skipbombers',
    'sfighters_killed_by_ship', 'sfighters_killed_by_fighters', 'sfighters_killed_by_bombers',
    'sfighters_killed_by_tbombers', 'sfighters_killed_by_sfighters', 'sfighters_killed_by_scouts',
    'sfighters_killed_by_skipbombers', 'scouts_killed_by_ship', 'scouts_killed_by_fighters', 'scouts_killed_by_bombers',
    'scouts_killed_by_tbombers', 'scouts_killed_by_sfighters', 'scouts_killed_by_scouts',
    'scouts_killed_by_skipbombers',
    'fighters_killed_by_ship', 'fighters_killed_by_ship_avia', 'fighters_killed_by_ship_alt',
    'fighters_killed_by_ship_airsupport', 'fighters_killed_by_fighters', 'fighters_killed_by_fighters_avia',
    'fighters_killed_by_fighters_alt', 'fighters_killed_by_fighters_airsupport', 'fighters_killed_by_bombers',
    'fighters_killed_by_tbombers', 'fighters_killed_by_sfighters', 'fighters_killed_by_sfighters_avia',
    'fighters_killed_by_sfighters_alt', 'fighters_killed_by_sfighters_airsupport', 'fighters_killed_by_scouts',
    'fighters_killed_by_skipbombers', 'bombers_killed_by_ship', 'bombers_killed_by_ship_avia',
    'bombers_killed_by_ship_alt',
    'bombers_killed_by_ship_airsupport', 'bombers_killed_by_fighters', 'bombers_killed_by_fighters_avia',
    'bombers_killed_by_fighters_alt', 'bombers_killed_by_fighters_airsupport', 'bombers_killed_by_bombers',
    'bombers_killed_by_tbombers', 'bombers_killed_by_sfighters', 'bombers_killed_by_sfighters_avia',
    'bombers_killed_by_sfighters_alt', 'bombers_killed_by_sfighters_airsupport', 'bombers_killed_by_scouts',
    'bombers_killed_by_skipbombers', 'tbombers_killed_by_ship', 'tbombers_killed_by_ship_avia',
    'tbombers_killed_by_ship_alt', 'tbombers_killed_by_ship_airsupport', 'tbombers_killed_by_fighters',
    'tbombers_killed_by_fighters_avia', 'tbombers_killed_by_fighters_alt', 'tbombers_killed_by_fighters_airsupport',
    'tbombers_killed_by_bombers', 'tbombers_killed_by_tbombers', 'tbombers_killed_by_sfighters',
    'tbombers_killed_by_sfighters_avia', 'tbombers_killed_by_sfighters_alt', 'tbombers_killed_by_sfighters_airsupport',
    'tbombers_killed_by_scouts', 'tbombers_killed_by_skipbombers', 'skipbombers_killed_by_ship',
    'skipbombers_killed_by_ship_avia', 'skipbombers_killed_by_ship_alt', 'skipbombers_killed_by_ship_airsupport',
    'skipbombers_killed_by_fighters', 'skipbombers_killed_by_fighters_alt', 'skipbombers_killed_by_fighters_avia',
    'skipbombers_killed_by_fighters_airsupport', 'skipbombers_killed_by_bombers', 'skipbombers_killed_by_tbombers',
    'skipbombers_killed_by_sfighters', 'skipbombers_killed_by_sfighters_avia', 'skipbombers_killed_by_sfighters_alt',
    'skipbombers_killed_by_sfighters_airsupport', 'skipbombers_killed_by_scouts', 'skipbombers_killed_by_skipbombers',
    'raw_exp', 'exp', 'interactions', 'buildingInteractions', 'is_abuser', 'killer_db_id', 'killer_veh_id',
    'killer_weapon',
    'was_detonated', 'tpds_spotted', 'scouting_damage', 'scouting_fires', 'cp_capture_points', 'cp_dropped_points',
    'agro_art', 'agro_tpd', 'agro_air', 'agro_dbomb', 'team_captured_points', 'team_dropped_points',
    'damage_airdefense',
    'damage_planes_by_plane', 'vehicle_damage_by_airdefense', 'vehicle_damage_planes_by_plane', 'damage', 'resources',
    'enemy_energy_burned', 'teamLadder', 'key_target_markers', 'planes_killed_scouts', 'planes_killed_sfighters',
    'planes_killed_fighters', 'planes_killed_bombers', 'planes_killed_tbombers', 'planes_killed_skipbombers',
    'he_hits_bomb', 'he_hits_bomb_avia', 'he_hits_bomb_airsupport', 'pierced_hits_main', 'team_damage', 'planes_lost',
    'pt_reward_boost', 'pt_reward_slow', 'RIBBON_MAIN_CALIBER', 'RIBBON_TORPEDO', 'RIBBON_BOMB', 'RIBBON_PLANE',
    'RIBBON_CRIT', 'RIBBON_FRAG', 'RIBBON_BURN', 'RIBBON_FLOOD', 'RIBBON_CITADEL', 'RIBBON_BASE_DEFENSE',
    'RIBBON_BASE_CAPTURE', 'RIBBON_BASE_CAPTURE_ASSIST', 'RIBBON_SUPPRESSED', 'RIBBON_SECONDARY_CALIBER',
    'RIBBON_MAIN_CALIBER_OVER_PENETRATION', 'RIBBON_MAIN_CALIBER_PENETRATION', 'RIBBON_MAIN_CALIBER_NO_PENETRATION',
    'RIBBON_MAIN_CALIBER_RICOCHET', 'RIBBON_BUILDING_KILL', 'RIBBON_DETECTED', 'RIBBON_BOMB_OVER_PENETRATION',
    'RIBBON_BOMB_PENETRATION', 'RIBBON_BOMB_NO_PENETRATION', 'RIBBON_BOMB_RICOCHET', 'RIBBON_ROCKET',
    'RIBBON_ROCKET_PENETRATION', 'RIBBON_ROCKET_NO_PENETRATION', 'RIBBON_SPLANE', 'RIBBON_BULGE', 'RIBBON_BOMB_BULGE',
    'RIBBON_ROCKET_BULGE', 'RIBBON_DBOMB', 'RIBBON_ACOUSTIC_HIT', 'RIBBON_DROP', 'RIBBON_ROCKET_RICOCHET',
    'RIBBON_ROCKET_OVER_PENETRATION', 'RIBBON_WAVE_KILL_TORPEDO', 'RIBBON_WAVE_CUT_WAVE', 'RIBBON_WAVE_HIT_VEHICLE',
    'RIBBON_ACOUSTIC_HIT_VEHICLE_NEW', 'RIBBON_ACOUSTIC_HIT_VEHICLE_CURR', 'RIBBON_ACOUSTIC_HIT_VEHICLE_BLOCK',
    'RIBBON_ACID', 'RIBBON_DBOMB_FULL_DAMAGE', 'RIBBON_DBOMB_PARTIAL_DAMAGE', 'RIBBON_MINE', 'RIBBON_DEMINING_MINE',
    'RIBBON_DEMINING_MINEFIELD')

# >>> BattleResultsSystem.unpackCommonRes.func_globals['COMMON_RESULTS']
COMMON_RESULTS = (
    'arena_id', 'cluster_id', 'start_dt', 'winner_team_id', 'win_type_id', 'team_build_type_id', 'clan_season_type',
    'clan_season_id', 'duration_sec', 'map_type_id', 'scenario_name', 'survey_id', 'game_mode', 'sse_info',
    'battle_logic_info', 'weather_preset_id', 'pve_operation_id', 'event_operation_id')

# BattleResultsSystem.unpackCommonRes.func_globals['PLAYER_PRIVATE_RESULTS']
PLAYER_PRIVATE_RESULTS = (
    'team_id', 'killer_db_id', 'killer_building_id', 'killer_building_params', 'premium_type', 'account_prev_tier',
    'account_points_prev', 'init_economics', 'common_economics', 'subtotal_economics', 'globalboosts_mods', 'tasks',
    'epics', 'chains', 'campaign_tasks', 'bonus_tags', 'ship_aces', 'survey_info', 'rank_battles_season_id',
    'rank_stars_old', 'rank_stars_gained', 'rank_stars_new', 'rank_old', 'rank_new', 'rank_league',
    'rank_victories_old',
    'rank_victories_new', 'rank_victory_rewards', 'first_rank_rewards', 'rank_qualification_rewards',
    'fast_rank_qualification_rewards', 'rank_victory_rewards_progress', 'battles_to_clean_abuse', 'abuser_status',
    'abuser_cleaned', 'is_afk', 'is_leaver', 'is_tshooter', 'is_complained', 'is_griefer', 'is_ineffective',
    'crew_dump',
    'pve_details', 'arc_details', 'bonus_currency', 'isMercenary', 'teamLadder')

# >>> BattleResultsSystem.unpackCommonRes.func_globals['INIT_ECONOMICS']
INIT_ECONOMICS = ('credits', 'credits_penalty', 'exp_penalty', 'exp', 'credits_compensation')

# >>> BattleResultsSystem.unpackCommonRes.func_globals['COMMON_ECONOMICS']
COMMON_ECONOMICS = (
    'auto_repair_list', 'auto_repair_credits', 'auto_repair_factor', 'auto_load_list', 'auto_load_credits',
    'auto_camo_credits', 'auto_camo_gold', 'auto_camo_list', 'auto_boost_list', 'auto_boost_credits', 'auto_boost_gold',
    'deficit_list', 'ship_service_enabled', 'credits_enabled', 'exp_enabled', 'crew_exp_enabled', 'free_exp_enabled',
    'acc_points_enabled', 'clan_supply_bonuses_enabled', 'free_exp_factor', 'premium_credits_factor',
    'premium_exp_factor',
    'wows_premium_credits_factor', 'wows_premium_exp_factor', 'camo_applied', 'boost_applied', 'serve_applied',
    'aogas_factor', 'aogas_online')

# >>> BattleResultsSystem.unpackCommonRes.func_globals['SUBTOTAL_ECONOMICS']
SUBTOTAL_ECONOMICS = ('elite_exp', 'free_exp', 'ship_exp', 'credits', 'crew_exp', 'acc_level')

# >>> BattleResultsSystem.CLIENT_VEH_INTERACTION_DETAILS
CLIENT_VEH_INTERACTION_DETAILS = (
    'is_primary_spotted_by_ship', 'is_primary_spotted_by_plane', 'is_killed', 'hits_main_ap', 'hits_main_cs',
    'hits_main_he', 'hits_atba_ap', 'hits_atba_cs', 'hits_atba_he', 'hits_tpd', 'hits_bomb', 'hits_bomb_avia',
    'hits_bomb_alt', 'hits_bomb_airsupport', 'hits_tbomb', 'hits_tbomb_avia', 'hits_tbomb_alt', 'hits_tbomb_airsupport',
    'hits_fire', 'hits_ram', 'hits_flood', 'hits_dbomb', 'hits_rocket', 'hits_rocket_avia', 'hits_rocket_alt',
    'hits_rocket_airsupport', 'hits_skip', 'hits_skip_avia', 'hits_skip_alt', 'hits_skip_airsupport',
    'hits_dbomb_airsupport', 'hits_adbomb', 'hits_sea_mine', 'he_hits_main_ap', 'he_hits_main_cs', 'he_hits_main_he',
    'he_hits_atba_ap', 'he_hits_atba_cs', 'he_hits_atba_he', 'he_hits_bomb', 'damage_main_ap', 'damage_main_cs',
    'damage_main_he', 'damage_atba_ap', 'damage_atba_cs', 'damage_atba_he', 'damage_tpd_normal', 'damage_tpd_deep',
    'damage_tpd_alter', 'damage_bomb', 'damage_bomb_avia', 'damage_bomb_alt', 'damage_bomb_airsupport',
    'damage_dbomb_airsupport', 'damage_tbomb', 'damage_tbomb_avia', 'damage_tbomb_alt', 'damage_tbomb_airsupport',
    'damage_fire', 'damage_ram', 'damage_flood', 'damage_dbomb_direct', 'damage_dbomb_splash', 'damage_sea_mine',
    'damage_rocket', 'damage_rocket_avia', 'damage_rocket_alt', 'damage_rocket_airsupport', 'damage_skip',
    'damage_skip_avia', 'damage_skip_alt', 'damage_skip_airsupport', 'damage_wave', 'damage_charge_laser',
    'damage_pulse_laser', 'damage_axis_laser', 'damage_adbomb', 'fires', 'floods', 'crits', 'citadels',
    'module_crits_artillery', 'module_crits_torpedo_tube', 'module_crits_atba', 'module_crits_air_defense',
    'module_crits_engine', 'module_crits_steering_gear', 'module_crits_pinger', 'module_kills_artillery',
    'module_kills_torpedo_tube', 'module_kills_atba', 'module_kills_air_defense', 'module_kills_depth_charge',
    'scouts_total_killed', 'sfighters_total_killed', 'fighters_total_killed', 'fighters_total_killed_avia',
    'fighters_total_killed_alt', 'fighters_total_killed_airsupport', 'bombers_total_killed',
    'bombers_total_killed_avia',
    'bombers_total_killed_alt', 'bombers_total_killed_airsupport', 'tbombers_total_killed',
    'tbombers_total_killed_avia',
    'tbombers_total_killed_alt', 'tbombers_total_killed_airsupport', 'skipbombers_total_killed',
    'skipbombers_total_killed_avia', 'skipbombers_total_killed_alt', 'skipbombers_total_killed_airsupport',
    'planes_killed_by_ship', 'planes_killed_by_scouts', 'planes_killed_by_fighters', 'planes_killed_by_bombers',
    'planes_killed_by_tbombers', 'planes_killed_by_sfighters', 'planes_killed_by_skipbombers',
    'sfighters_killed_by_ship',
    'sfighters_killed_by_fighters', 'sfighters_killed_by_bombers', 'sfighters_killed_by_tbombers',
    'sfighters_killed_by_sfighters', 'sfighters_killed_by_scouts', 'sfighters_killed_by_skipbombers',
    'scouts_killed_by_ship', 'scouts_killed_by_fighters', 'scouts_killed_by_bombers', 'scouts_killed_by_tbombers',
    'scouts_killed_by_sfighters', 'scouts_killed_by_scouts', 'scouts_killed_by_skipbombers', 'fighters_killed_by_ship',
    'fighters_killed_by_ship_avia', 'fighters_killed_by_ship_alt', 'fighters_killed_by_ship_airsupport',
    'fighters_killed_by_fighters', 'fighters_killed_by_fighters_avia', 'fighters_killed_by_fighters_alt',
    'fighters_killed_by_fighters_airsupport', 'fighters_killed_by_bombers', 'fighters_killed_by_tbombers',
    'fighters_killed_by_sfighters', 'fighters_killed_by_sfighters_avia', 'fighters_killed_by_sfighters_alt',
    'fighters_killed_by_sfighters_airsupport', 'fighters_killed_by_scouts', 'fighters_killed_by_skipbombers',
    'bombers_killed_by_ship', 'bombers_killed_by_ship_avia', 'bombers_killed_by_ship_alt',
    'bombers_killed_by_ship_airsupport', 'bombers_killed_by_fighters', 'bombers_killed_by_fighters_avia',
    'bombers_killed_by_fighters_alt', 'bombers_killed_by_fighters_airsupport', 'bombers_killed_by_bombers',
    'bombers_killed_by_tbombers', 'bombers_killed_by_sfighters', 'bombers_killed_by_sfighters_avia',
    'bombers_killed_by_sfighters_alt', 'bombers_killed_by_sfighters_airsupport', 'bombers_killed_by_scouts',
    'bombers_killed_by_skipbombers', 'tbombers_killed_by_ship', 'tbombers_killed_by_ship_avia',
    'tbombers_killed_by_ship_alt', 'tbombers_killed_by_ship_airsupport', 'tbombers_killed_by_fighters',
    'tbombers_killed_by_fighters_avia', 'tbombers_killed_by_fighters_alt', 'tbombers_killed_by_fighters_airsupport',
    'tbombers_killed_by_bombers', 'tbombers_killed_by_tbombers', 'tbombers_killed_by_sfighters',
    'tbombers_killed_by_sfighters_avia', 'tbombers_killed_by_sfighters_alt', 'tbombers_killed_by_sfighters_airsupport',
    'tbombers_killed_by_scouts', 'tbombers_killed_by_skipbombers', 'skipbombers_killed_by_ship',
    'skipbombers_killed_by_ship_avia', 'skipbombers_killed_by_ship_alt', 'skipbombers_killed_by_ship_airsupport',
    'skipbombers_killed_by_fighters', 'skipbombers_killed_by_fighters_avia', 'skipbombers_killed_by_fighters_alt',
    'skipbombers_killed_by_fighters_airsupport', 'skipbombers_killed_by_bombers', 'skipbombers_killed_by_tbombers',
    'skipbombers_killed_by_sfighters', 'skipbombers_killed_by_sfighters_avia', 'skipbombers_killed_by_sfighters_alt',
    'skipbombers_killed_by_sfighters_airsupport', 'skipbombers_killed_by_scouts', 'skipbombers_killed_by_skipbombers',
    'planes_killed', 'damage_fighters_const', 'damage_bombers_const', 'damage_tbombers_const',
    'damage_skipbombers_const',
    'damage_abilityplanes_const', 'damage_fighters_bubble', 'damage_bombers_bubble', 'damage_tbombers_bubble',
    'damage_skipbombers_bubble', 'damage_abilityplanes_bubble', 'damage_fighters_alt_const', 'damage_bombers_alt_const',
    'damage_tbombers_alt_const', 'damage_skipbombers_alt_const', 'damage_fighters_alt_bubble',
    'damage_bombers_alt_bubble',
    'damage_tbombers_alt_bubble', 'damage_skipbombers_alt_bubble', 'damage_airdefense', 'damage_planes_by_plane',
    'scouting_damage')

# >>> BattleResultsSystem.CLIENT_BUILDING_INTERACTION_DETAILS
CLIENT_BUILDING_INTERACTION_DETAILS = (
    'building_params_id', 'is_vehicle_killed', 'sfighters_killed', 'scouts_killed', 'fighters_killed', 'bombers_killed',
    'tbombers_killed', 'skipbombers_killed', 'suppression_count', 'building_fires', 'building_floods',
    'building_hits_main_he', 'building_hits_main_ap', 'building_hits_main_cs', 'building_damage_main_he',
    'building_damage_main_ap', 'building_damage_main_cs', 'building_damage_flood', 'building_damage_fire',
    'building_damage_bomb_ap', 'building_damage_bomb_he', 'building_damage_tbomb', 'building_crits_artillery',
    'building_crits_atba', 'building_crits_air_defense', 'building_kills_artillery', 'building_kills_atba',
    'building_kills_air_defense', 'vehicle_fires', 'vehicle_hits_main_he', 'vehicle_hits_main_ap',
    'vehicle_hits_main_cs',
    'vehicle_hits_atba_he', 'vehicle_hits_atba_ap', 'vehicle_hits_atba_cs', 'vehicle_hits_tpd', 'vehicle_hits_bomb',
    'vehicle_hits_bomb_avia', 'vehicle_hits_bomb_alt', 'vehicle_hits_bomb_airsupport', 'vehicle_hits_tbomb',
    'vehicle_hits_tbomb_avia', 'vehicle_hits_tbomb_alt', 'vehicle_hits_tbomb_airsupport', 'vehicle_hits_rocket',
    'vehicle_hits_rocket_avia', 'vehicle_hits_rocket_alt', 'vehicle_hits_rocket_airsupport', 'vehicle_hits_skip',
    'vehicle_hits_skip_avia', 'vehicle_hits_skip_alt', 'vehicle_hits_skip_airsupport', 'vehicle_damage_main_he',
    'vehicle_damage_main_ap', 'vehicle_damage_main_cs', 'vehicle_damage_atba_he', 'vehicle_damage_atba_ap',
    'vehicle_damage_atba_cs', 'vehicle_damage_tpd', 'vehicle_damage_fire', 'vehicle_damage_flood',
    'vehicle_damage_bomb',
    'vehicle_damage_bomb_avia', 'vehicle_damage_bomb_alt', 'vehicle_damage_bomb_airsupport', 'vehicle_damage_tbomb',
    'vehicle_damage_tbomb_avia', 'vehicle_damage_tbomb_alt', 'vehicle_damage_tbomb_airsupport', 'vehicle_damage_rocket',
    'vehicle_damage_rocket_avia', 'vehicle_damage_rocket_alt', 'vehicle_damage_rocket_airsupport',
    'vehicle_damage_skip',
    'vehicle_damage_skip_avia', 'vehicle_damage_skip_alt', 'vehicle_damage_skip_airsupport', 'vehicle_crits_artillery',
    'vehicle_crits_atba', 'vehicle_crits_air_defense', 'vehicle_kills_artillery', 'vehicle_kills_atba',
    'vehicle_kills_air_defense', 'building_killed', 'airfield_planes_killed', 'airfield_planes_killed_by_plane',
    'airfield_scouts_total_killed', 'airfield_sfighters_total_killed', 'airfield_fighters_total_killed',
    'airfield_bombers_total_killed', 'airfield_tbombers_total_killed', 'airfield_planes_killed_by_scouts',
    'airfield_planes_killed_by_ship', 'airfield_planes_killed_by_fighters', 'airfield_planes_killed_by_bombers',
    'airfield_planes_killed_by_tbombers', 'airfield_planes_killed_by_sfighters', 'airfield_sfighters_killed_by_ship',
    'airfield_sfighters_killed_by_fighters', 'airfield_sfighters_killed_by_bombers',
    'airfield_sfighters_killed_by_tbombers', 'airfield_sfighters_killed_by_sfighters',
    'airfield_sfighters_killed_by_scouts', 'airfield_scouts_killed_by_ship', 'airfield_scouts_killed_by_fighters',
    'airfield_scouts_killed_by_bombers', 'airfield_scouts_killed_by_tbombers', 'airfield_scouts_killed_by_sfighters',
    'airfield_scouts_killed_by_scouts', 'airfield_fighters_killed_by_ship', 'airfield_fighters_killed_by_fighters',
    'airfield_fighters_killed_by_bombers', 'airfield_fighters_killed_by_tbombers',
    'airfield_fighters_killed_by_sfighters',
    'airfield_fighters_killed_by_scouts', 'airfield_bombers_killed_by_ship', 'airfield_bombers_killed_by_fighters',
    'airfield_bombers_killed_by_bombers', 'airfield_bombers_killed_by_tbombers', 'airfield_bombers_killed_by_sfighters',
    'airfield_bombers_killed_by_scouts', 'airfield_tbombers_killed_by_ship', 'airfield_tbombers_killed_by_fighters',
    'airfield_tbombers_killed_by_bombers', 'airfield_tbombers_killed_by_tbombers',
    'airfield_tbombers_killed_by_sfighters',
    'airfield_tbombers_killed_by_scouts', 'airfield_skipbombers_killed_by_ship',
    'airfield_skipbombers_killed_by_fighters',
    'airfield_skipbombers_killed_by_bombers', 'airfield_skipbombers_killed_by_tbombers',
    'airfield_skipbombers_killed_by_sfighters', 'airfield_skipbombers_killed_by_scouts')

# BattleResultsSystem.BUILDINGS_FULL_RESULTS
BUILDINGS_FULL_RESULTS = ('id', 'uniqueId', 'teamId', 'paramsId')

# >>> BattleResultsSystem.DAMAGE_FIELDS_BUILDING
DAMAGE_FIELDS_BUILDING = ['planes_killed_by_ship', 'vehicle_hits_all', 'vehicle_kills_artillery',
                          'vehicle_crits_air_defense', 'vehicle_hits_bomb', 'vehicle_module_total',
                          'vehicle_hits_main_ap', 'vehicle_hits_atba_ap', 'vehicle_damage_atba_he',
                          'vehicle_damage_main_ap', 'vehicle_damage_main_he', 'vehicle_hits_atba_he',
                          'vehicle_damage_etc', 'vehicle_crits_atba', 'vehicle_damage_all', 'vehicle_hits_atba',
                          'vehicle_hits_main', 'vehicle_damage_main', 'vehicle_damage_fire', 'vehicle_module_crits',
                          'vehicle_module_kills', 'vehicle_kills_atba', 'vehicle_crits_artillery',
                          'vehicle_hits_main_he', 'vehicle_damage_atba', 'vehicle_fires', 'vehicle_damage_flood',
                          'vehicle_damage_atba_ap', 'vehicle_kills_air_defense', 'vehicle_damage_bomb',
                          'vehicle_hits_rocket', 'vehicle_damage_rocket', 'vehicle_hits_tbomb', 'vehicle_damage_tbomb',
                          'vehicle_hits_tpd', 'vehicle_damage_tpd', 'vehicle_hits_main_cs', 'vehicle_hits_atba_cs',
                          'vehicle_damage_main_cs', 'vehicle_damage_atba_cs', 'vehicle_hits_skip',
                          'vehicle_damage_skip']

# >>> BattleResultsSystem.ClientCrew.DUMP_FIELDS_INDICES
CREW_DUMP_FILEDS_INDICIES = {'vanities': 11, 'name': 2, 'level': 4, 'skills': 5, 'experience': 3, 'paramsId': 1,
                             'adaptationExperiencePenalty': 8, 'retrainingType': 10, 'adaptationExperienceEarned': 9,
                             'id': 0, 'guiAppearance': 7, 'specialization': 6}
