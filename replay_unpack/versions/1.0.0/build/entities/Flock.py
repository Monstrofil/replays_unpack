#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class Flock(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._modelName = None

        self._modelName2 = None

        self._modelCount = 5.0

        self._yawSpeed = '1.0'

        self._pitchSpeed = '0.002'

        self._rollSpeed = '0.05'

        self._animSpeedMin = '1.0'

        self._animSpeedMax = '1.0'

        self._height = '50.0'

        self._radius = '100.0'

        self._deadZoneRadius = '0.0'

        self._speedAtBottom = '0.5'

        self._speedAtTop = '0.2'

        self._decisionTime = '7.0'

        self._flyAroundCenter = 0.0


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (10000000000, 'modelName'),
            (10000000000, 'modelName2'),
            (8, 'modelCount'),
            (32, 'yawSpeed'),
            (32, 'pitchSpeed'),
            (32, 'rollSpeed'),
            (32, 'animSpeedMin'),
            (32, 'animSpeedMax'),
            (32, 'height'),
            (32, 'radius'),
            (32, 'deadZoneRadius'),
            (32, 'speedAtBottom'),
            (32, 'speedAtTop'),
            (32, 'decisionTime'),
            (8, 'flyAroundCenter'),
            
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


    # property size: 10000000000
    @property
    def modelName(self):
        return self._modelName

    @modelName.setter
    def modelName(self, value):
        self._modelName, = unpack_variables(value, ['STRING'])

    # property size: 10000000000
    @property
    def modelName2(self):
        return self._modelName2

    @modelName2.setter
    def modelName2(self, value):
        self._modelName2, = unpack_variables(value, ['STRING'])

    # property size: 8
    @property
    def modelCount(self):
        return self._modelCount

    @modelCount.setter
    def modelCount(self, value):
        self._modelCount, = unpack_variables(value, ['UINT8'])

    # property size: 32
    @property
    def yawSpeed(self):
        return self._yawSpeed

    @yawSpeed.setter
    def yawSpeed(self, value):
        self._yawSpeed, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def pitchSpeed(self):
        return self._pitchSpeed

    @pitchSpeed.setter
    def pitchSpeed(self, value):
        self._pitchSpeed, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def rollSpeed(self):
        return self._rollSpeed

    @rollSpeed.setter
    def rollSpeed(self, value):
        self._rollSpeed, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def animSpeedMin(self):
        return self._animSpeedMin

    @animSpeedMin.setter
    def animSpeedMin(self, value):
        self._animSpeedMin, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def animSpeedMax(self):
        return self._animSpeedMax

    @animSpeedMax.setter
    def animSpeedMax(self, value):
        self._animSpeedMax, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def deadZoneRadius(self):
        return self._deadZoneRadius

    @deadZoneRadius.setter
    def deadZoneRadius(self, value):
        self._deadZoneRadius, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def speedAtBottom(self):
        return self._speedAtBottom

    @speedAtBottom.setter
    def speedAtBottom(self, value):
        self._speedAtBottom, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def speedAtTop(self):
        return self._speedAtTop

    @speedAtTop.setter
    def speedAtTop(self, value):
        self._speedAtTop, = unpack_variables(value, ['FLOAT'])

    # property size: 32
    @property
    def decisionTime(self):
        return self._decisionTime

    @decisionTime.setter
    def decisionTime(self, value):
        self._decisionTime, = unpack_variables(value, ['FLOAT'])

    # property size: 8
    @property
    def flyAroundCenter(self):
        return self._flyAroundCenter

    @flyAroundCenter.setter
    def flyAroundCenter(self, value):
        self._flyAroundCenter, = unpack_variables(value, ['BOOL'])


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)