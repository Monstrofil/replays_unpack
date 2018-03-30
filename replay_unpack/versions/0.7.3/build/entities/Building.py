#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.VisionOwner import VisionOwner
except:
    from VisionOwner import VisionOwner

try:
    from interfaces.AtbaOwner import AtbaOwner
except:
    from AtbaOwner import AtbaOwner

try:
    from interfaces.AirDefenceOwner import AirDefenceOwner
except:
    from AirDefenceOwner import AirDefenceOwner

try:
    from interfaces.DebugDrawEntity import DebugDrawEntity
except:
    from DebugDrawEntity import DebugDrawEntity

try:
    from interfaces.HitLocationManagerOwner import HitLocationManagerOwner
except:
    from HitLocationManagerOwner import HitLocationManagerOwner

try:
    from interfaces.AviationOwner import AviationOwner
except:
    from AviationOwner import AviationOwner

try:
    from interfaces.WeatherOwner import WeatherOwner
except:
    from WeatherOwner import WeatherOwner



class Building(VisionOwner, AtbaOwner, AirDefenceOwner, DebugDrawEntity, HitLocationManagerOwner, AviationOwner, WeatherOwner):
    
    g_startOfflineBattle = EventHook()
    
    g_kill = EventHook()
    
    g_shootGuns = EventHook()
    
    g_syncArtilleryGun = EventHook()
    
    g_setArtilleryGunsDefaultYawsPitchsTo = EventHook()
    
    g_onClientEnterWorld = EventHook()
    
    g_onClientLeaveWorld = EventHook()
    
    g_offlineOnHit = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._paramsId = None

        self._teamId = None

        self._isAlive = None

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

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def startOfflineBattle(self):
        self.g_startOfflineBattle.fire(self)

    @unpack_func_args(['UINT32', 'UINT32'])
    def kill(self, arg1, arg2):
        self.g_kill.fire(self, arg1, arg2)

    @unpack_func_args(['UINT16'])
    def shootGuns(self, arg1):
        self.g_shootGuns.fire(self, arg1)

    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL'])
    def syncArtilleryGun(self, arg1, arg2, arg3, arg4):
        self.g_syncArtilleryGun.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['BOOL'])
    def setArtilleryGunsDefaultYawsPitchsTo(self, arg1):
        self.g_setArtilleryGunsDefaultYawsPitchsTo.fire(self, arg1)

    @unpack_func_args([])
    def onClientEnterWorld(self):
        self.g_onClientEnterWorld.fire(self)

    @unpack_func_args([])
    def onClientLeaveWorld(self):
        self.g_onClientLeaveWorld.fire(self)

    @unpack_func_args(['ON_HIT_INFO'])
    def offlineOnHit(self, arg1):
        self.g_offlineOnHit.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def paramsId(self):
        return self._paramsId

    @paramsId.setter
    def paramsId(self, value):
        self._paramsId, = unpack_variables(value, ['GAMEPARAMS_ID'])

    @property
    def teamId(self):
        return self._teamId

    @teamId.setter
    def teamId(self, value):
        self._teamId, = unpack_variables(value, ['TEAM_ID'])

    @property
    def isAlive(self):
        return self._isAlive

    @isAlive.setter
    def isAlive(self, value):
        self._isAlive, = unpack_variables(value, ['BOOL'])

    @property
    def isSuppressed(self):
        return self._isSuppressed

    @isSuppressed.setter
    def isSuppressed(self, value):
        self._isSuppressed, = unpack_variables(value, ['BOOL'])

    @property
    def targetPos(self):
        return self._targetPos

    @targetPos.setter
    def targetPos(self, value):
        self._targetPos, = unpack_variables(value, ['VECTOR3'])

    @property
    def isInOfflineMode(self):
        return self._isInOfflineMode

    @isInOfflineMode.setter
    def isInOfflineMode(self, value):
        self._isInOfflineMode, = unpack_variables(value, ['BOOL'])

    @property
    def debugText(self):
        return self._debugText

    @debugText.setter
    def debugText(self, value):
        self._debugText, = unpack_variables(value, [['ARRAY', 'ENTITY_DEBUG_TEXT']])

    @property
    def weatherParams(self):
        return self._weatherParams

    @weatherParams.setter
    def weatherParams(self, value):
        self._weatherParams, = unpack_variables(value, ['WEATHER_LOGIC_PARAMS'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)