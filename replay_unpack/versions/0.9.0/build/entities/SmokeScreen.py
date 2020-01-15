#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from interfaces.WeatherOwner import WeatherOwner



class SmokeScreen(WeatherOwner):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._bcRadius = None

        self._points = None

        self._radius = None

        self._height = None

        self._activePointIndex = None

        self._spawnPointEffect = None

        self._livePointEffect = None


        # MRO fix

        WeatherOwner.__init__(self)

        self._properties = getattr(self, '_properties', [])
        for item in [
            (32, 'bcRadius'),
            (10000000000, 'points'),
            (32, 'radius'),
            (32, 'height'),
            (8, 'activePointIndex'),
            (10000000000, 'spawnPointEffect'),
            (10000000000, 'livePointEffect'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            
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



    ####################################
    #       PROPERTIES
    ####################################

# property size: 32
    @property
    def bcRadius(self):
        return self._bcRadius

    @bcRadius.setter
    def bcRadius(self, value):
        self._bcRadius, = unpack_variables(value, ['FLOAT32'])
# property size: 10000000000
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points, = unpack_variables(value, [['ARRAY', 'VECTOR2']])
# property size: 32
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT32'])
# property size: 32
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def activePointIndex(self):
        return self._activePointIndex

    @activePointIndex.setter
    def activePointIndex(self, value):
        self._activePointIndex, = unpack_variables(value, ['INT8'])
# property size: 10000000000
    @property
    def spawnPointEffect(self):
        return self._spawnPointEffect

    @spawnPointEffect.setter
    def spawnPointEffect(self, value):
        self._spawnPointEffect, = unpack_variables(value, ['STRING'])
# property size: 10000000000
    @property
    def livePointEffect(self):
        return self._livePointEffect

    @livePointEffect.setter
    def livePointEffect(self, value):
        self._livePointEffect, = unpack_variables(value, ['STRING'])


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