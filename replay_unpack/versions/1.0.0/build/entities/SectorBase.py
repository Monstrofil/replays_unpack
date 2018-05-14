#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.EntityTrap import EntityTrap
except:
    from EntityTrap import EntityTrap



class SectorBase(EntityTrap):
    
    g_setMaxPointsFactor = EventHook()
    
    g_reset = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._pointsPerSecond = '1.0'

        self._maxPointsPerSecond = '3.0'

        self._ownerStopsCapturing = 0.0

        self._defaultPointsPerSecond = '1.0'

        self._defaultMaxPointsPerSecond = '3.0'

        self._isActive = None

        self._team = None

        self._baseID = 1.0

        self._sectorID = None

        self._maxPoints = '200.0'

        self._initMaxPoints = '200.0'

        self._pointsPercentage = 0.0

        self._capturingStopped = 0.0

        self._onDamageCooldownTime = '5.0'

        self._radius = '50.0'

        self._isCaptured = None

        self._invadersCount = None

        self._expectedCaptureTime = '-1.0'


        # MRO fix

        EntityTrap.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['FLOAT32'])
    def setMaxPointsFactor(self, arg1):
        self.g_setMaxPointsFactor.fire(self, arg1)

    @unpack_func_args([])
    def reset(self):
        self.g_reset.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def pointsPerSecond(self):
        return self._pointsPerSecond

    @pointsPerSecond.setter
    def pointsPerSecond(self, value):
        self._pointsPerSecond, = unpack_variables(value, ['FLOAT32'])

    @property
    def maxPointsPerSecond(self):
        return self._maxPointsPerSecond

    @maxPointsPerSecond.setter
    def maxPointsPerSecond(self, value):
        self._maxPointsPerSecond, = unpack_variables(value, ['FLOAT32'])

    @property
    def ownerStopsCapturing(self):
        return self._ownerStopsCapturing

    @ownerStopsCapturing.setter
    def ownerStopsCapturing(self, value):
        self._ownerStopsCapturing, = unpack_variables(value, ['BOOL'])

    @property
    def defaultPointsPerSecond(self):
        return self._defaultPointsPerSecond

    @defaultPointsPerSecond.setter
    def defaultPointsPerSecond(self, value):
        self._defaultPointsPerSecond, = unpack_variables(value, ['FLOAT32'])

    @property
    def defaultMaxPointsPerSecond(self):
        return self._defaultMaxPointsPerSecond

    @defaultMaxPointsPerSecond.setter
    def defaultMaxPointsPerSecond(self, value):
        self._defaultMaxPointsPerSecond, = unpack_variables(value, ['FLOAT32'])

    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, value):
        self._isActive, = unpack_variables(value, ['BOOL'])

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])

    @property
    def baseID(self):
        return self._baseID

    @baseID.setter
    def baseID(self, value):
        self._baseID, = unpack_variables(value, ['UINT8'])

    @property
    def sectorID(self):
        return self._sectorID

    @sectorID.setter
    def sectorID(self, value):
        self._sectorID, = unpack_variables(value, ['UINT8'])

    @property
    def maxPoints(self):
        return self._maxPoints

    @maxPoints.setter
    def maxPoints(self, value):
        self._maxPoints, = unpack_variables(value, ['FLOAT32'])

    @property
    def initMaxPoints(self):
        return self._initMaxPoints

    @initMaxPoints.setter
    def initMaxPoints(self, value):
        self._initMaxPoints, = unpack_variables(value, ['FLOAT32'])

    @property
    def pointsPercentage(self):
        return self._pointsPercentage

    @pointsPercentage.setter
    def pointsPercentage(self, value):
        self._pointsPercentage, = unpack_variables(value, ['UINT8'])

    @property
    def capturingStopped(self):
        return self._capturingStopped

    @capturingStopped.setter
    def capturingStopped(self, value):
        self._capturingStopped, = unpack_variables(value, ['BOOL'])

    @property
    def onDamageCooldownTime(self):
        return self._onDamageCooldownTime

    @onDamageCooldownTime.setter
    def onDamageCooldownTime(self, value):
        self._onDamageCooldownTime, = unpack_variables(value, ['FLOAT32'])

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT32'])

    @property
    def isCaptured(self):
        return self._isCaptured

    @isCaptured.setter
    def isCaptured(self, value):
        self._isCaptured, = unpack_variables(value, ['BOOL'])

    @property
    def invadersCount(self):
        return self._invadersCount

    @invadersCount.setter
    def invadersCount(self, value):
        self._invadersCount, = unpack_variables(value, ['UINT8'])

    @property
    def expectedCaptureTime(self):
        return self._expectedCaptureTime

    @expectedCaptureTime.setter
    def expectedCaptureTime(self, value):
        self._expectedCaptureTime, = unpack_variables(value, ['FLOAT32'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)