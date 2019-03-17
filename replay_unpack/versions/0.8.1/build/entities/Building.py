#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from .interfaces.VisionOwner import VisionOwner
from .interfaces.AtbaOwner import AtbaOwner
from .interfaces.AirDefenceOwner import AirDefenceOwner
from .interfaces.DebugDrawEntity import DebugDrawEntity
from .interfaces.HitLocationManagerOwner import HitLocationManagerOwner
from .interfaces.AviationOwner import AviationOwner
from .interfaces.WeatherOwner import WeatherOwner
from .interfaces.ModelOwner import ModelOwner



class Building(VisionOwner, AtbaOwner, AirDefenceOwner, DebugDrawEntity, HitLocationManagerOwner, AviationOwner, WeatherOwner, ModelOwner):
    
    g_startOfflineBattle = EventHook()
    
    g_kill = EventHook()
    
    g_shootGuns = EventHook()
    
    g_syncArtilleryGun = EventHook()
    
    g_setArtilleryGunsDefaultYawsPitchsTo = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._paramsId = None

        self._teamId = None

        self._isAlive = 'True'

        self._isSuppressed = None

        self._targetPos = None

        self._isInOfflineMode = None

        self._debugText = None

        self._weatherParams = None


        # MRO fix

        VisionOwner.__init__(self)

        AtbaOwner.__init__(self)

        AirDefenceOwner.__init__(self)

        DebugDrawEntity.__init__(self)

        HitLocationManagerOwner.__init__(self)

        AviationOwner.__init__(self)

        WeatherOwner.__init__(self)

        ModelOwner.__init__(self)

        self._properties = getattr(self, '_properties', [])
        for item in [
            (32, 'paramsId'),
            (8, 'teamId'),
            (8, 'isAlive'),
            (8, 'isSuppressed'),
            (96, 'targetPos'),
            (8, 'isInOfflineMode'),
            (10000000000, 'debugText'),
            (608, 'weatherParams'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (1, 'startOfflineBattle'),
            (65, 'kill'),
            (17, 'shootGuns'),
            (105, 'syncArtilleryGun'),
            (9, 'setArtilleryGunsDefaultYawsPitchsTo'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._methods:
                continue
            self._methods.append(item)
        # sort methods by size
        self._methods.sort(key=itemgetter(0))
        return

    @property
    def attributesMap(self):
        d = {}
        for i, (_, name) in enumerate(self._properties):
            d[i] = name
        return d

    @property
    def methodsMap(self):
        d = {}
        for i, (_, name) in enumerate(self._methods):
            d[i] = name
        return d

    ####################################
    #      METHODS
    ####################################

# method size: 1
    @unpack_func_args([])
    def startOfflineBattle(self):
        self.g_startOfflineBattle.fire(self)
# method size: 65
    @unpack_func_args(['UINT32', 'UINT32'])
    def kill(self, arg1, arg2):
        self.g_kill.fire(self, arg1, arg2)
# method size: 17
    @unpack_func_args(['UINT16'])
    def shootGuns(self, arg1):
        self.g_shootGuns.fire(self, arg1)
# method size: 105
    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL'])
    def syncArtilleryGun(self, arg1, arg2, arg3, arg4):
        self.g_syncArtilleryGun.fire(self, arg1, arg2, arg3, arg4)
# method size: 9
    @unpack_func_args(['BOOL'])
    def setArtilleryGunsDefaultYawsPitchsTo(self, arg1):
        self.g_setArtilleryGunsDefaultYawsPitchsTo.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 32
    @property
    def paramsId(self):
        return self._paramsId

    @paramsId.setter
    def paramsId(self, value):
        self._paramsId, = unpack_variables(value, ['GAMEPARAMS_ID'])
# property size: 8
    @property
    def teamId(self):
        return self._teamId

    @teamId.setter
    def teamId(self, value):
        self._teamId, = unpack_variables(value, ['TEAM_ID'])
# property size: 8
    @property
    def isAlive(self):
        return self._isAlive

    @isAlive.setter
    def isAlive(self, value):
        self._isAlive, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def isSuppressed(self):
        return self._isSuppressed

    @isSuppressed.setter
    def isSuppressed(self, value):
        self._isSuppressed, = unpack_variables(value, ['BOOL'])
# property size: 96
    @property
    def targetPos(self):
        return self._targetPos

    @targetPos.setter
    def targetPos(self, value):
        self._targetPos, = unpack_variables(value, ['VECTOR3'])
# property size: 8
    @property
    def isInOfflineMode(self):
        return self._isInOfflineMode

    @isInOfflineMode.setter
    def isInOfflineMode(self, value):
        self._isInOfflineMode, = unpack_variables(value, ['BOOL'])
# property size: 10000000000
    @property
    def debugText(self):
        return self._debugText

    @debugText.setter
    def debugText(self, value):
        self._debugText, = unpack_variables(value, [['ARRAY', 'ENTITY_DEBUG_TEXT']])
# property size: 608
    @property
    def weatherParams(self):
        return self._weatherParams

    @weatherParams.setter
    def weatherParams(self, value):
        self._weatherParams, = unpack_variables(value, ['WEATHER_LOGIC_PARAMS'])


    def get_summary(self):
        print('~' * 60)
        print('Entity name: ', self.__class__.__name__)
        print('Total entity client properties: {:>5}'.format(len(self._properties)))
        print('Total entity client methods: {:>5}'.format(len(self._methods)))

        print()
        print('Listing entity properties:')
        print('{:>4} {:>40}'.format('idx', 'property name'))
        for i, p in self.attributesMap.items():
            print('{:>4} {:>40}'.format(i, p))

        print()
        print('Listing entity methods:')
        print('{:>4} {:>40}'.format('idx', 'method name'))
        for i, p in self.methodsMap.items():
            print('{:>4} {:>40}'.format(i, p))
        print('~' * 60)
        print()
        print()


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)