# coding=utf-8

id_property_map = {0: 'accountDBID', 1: 'avatarId', 2: 'camouflageInfo', 3: 'clanColor', 4: 'clanID', 5: 'clanTag',
                   6: 'crewParams', 7: 'dogTag', 8: 'fragsCount', 9: 'friendlyFireEnabled', 10: 'id',
                   11: 'invitationsEnabled', 12: 'isAbuser', 13: 'isAlive', 14: 'isBot', 15: 'isClientLoaded',
                   16: 'isConnected', 17: 'isHidden', 18: 'isLeaver', 19: 'isPreBattleOwner', 20: 'isTShooter',
                   21: 'killedBuildingsCount', 22: 'maxHealth', 23: 'name', 24: 'playerMode', 25: 'preBattleIdOnStart',
                   26: 'preBattleSign', 27: 'prebattleId', 28: 'realm', 29: 'shipComponents', 30: 'shipId',
                   31: 'shipParamsId', 32: 'skinId', 33: 'teamId', 34: 'ttkStatus'}
property_id_map = {value: key for key, value in id_property_map.items()}


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
    21: {'sound': 'Portal', 'icon': 'icon_frag_portal', 'id': 21, 'name': 'PORTAL'}
}
