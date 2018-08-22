#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from interfaces.EntityTrap import EntityTrap



class SectorBase(EntityTrap):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._isActive = None

        self._team = None

        self._baseID = 1.0

        self._sectorID = None

        self._maxPoints = '200.0'

        self._pointsPercentage = 0.0

        self._capturingStopped = 0.0

        self._onDamageCooldownTime = '5.0'

        self._radius = '50.0'

        self._isCaptured = None

        self._invadersCount = None

        self._expectedCaptureTime = '-1.0'


        # MRO fix

        EntityTrap.__init__(self)

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (8, 'isActive'),
            (8, 'team'),
            (8, 'baseID'),
            (8, 'sectorID'),
            (32, 'maxPoints'),
            (8, 'pointsPercentage'),
            (8, 'capturingStopped'),
            (32, 'onDamageCooldownTime'),
            (32, 'radius'),
            (8, 'isCaptured'),
            (8, 'invadersCount'),
            (32, 'expectedCaptureTime'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            
        ])
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



    ####################################
    #       PROPERTIES
    ####################################

# property size: 8
    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, value):
        self._isActive, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def baseID(self):
        return self._baseID

    @baseID.setter
    def baseID(self, value):
        self._baseID, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def sectorID(self):
        return self._sectorID

    @sectorID.setter
    def sectorID(self, value):
        self._sectorID, = unpack_variables(value, ['UINT8'])
# property size: 32
    @property
    def maxPoints(self):
        return self._maxPoints

    @maxPoints.setter
    def maxPoints(self, value):
        self._maxPoints, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def pointsPercentage(self):
        return self._pointsPercentage

    @pointsPercentage.setter
    def pointsPercentage(self, value):
        self._pointsPercentage, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def capturingStopped(self):
        return self._capturingStopped

    @capturingStopped.setter
    def capturingStopped(self, value):
        self._capturingStopped, = unpack_variables(value, ['BOOL'])
# property size: 32
    @property
    def onDamageCooldownTime(self):
        return self._onDamageCooldownTime

    @onDamageCooldownTime.setter
    def onDamageCooldownTime(self, value):
        self._onDamageCooldownTime, = unpack_variables(value, ['FLOAT32'])
# property size: 32
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def isCaptured(self):
        return self._isCaptured

    @isCaptured.setter
    def isCaptured(self, value):
        self._isCaptured, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def invadersCount(self):
        return self._invadersCount

    @invadersCount.setter
    def invadersCount(self, value):
        self._invadersCount, = unpack_variables(value, ['UINT8'])
# property size: 32
    @property
    def expectedCaptureTime(self):
        return self._expectedCaptureTime

    @expectedCaptureTime.setter
    def expectedCaptureTime(self, value):
        self._expectedCaptureTime, = unpack_variables(value, ['FLOAT32'])


    def get_summary(self):
        print '~' * 60
        print 'Entity name: ', self.__class__.__name__
        print 'Total entity client properties: {:>5}'.format(len(self._properties))
        print 'Total entity client methods: {:>5}'.format(len(self._methods))

        print
        print 'Listing entity properties:'
        print '{:>4} {:>40}'.format('idx', 'property name')
        for i, p in self.attributesMap.items():
            print '{:>4} {:>40}'.format(i, p)

        print
        print 'Listing entity methods:'
        print '{:>4} {:>40}'.format('idx', 'method name')
        for i, p in self.methodsMap.items():
            print '{:>4} {:>40}'.format(i, p)
        print '~' * 60
        print
        print


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)