#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class ClientSelectableCameraObject(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._cameraShift = None

        self._cameraPivot = None

        self._cameraYaw = None

        self._cameraPitch = None

        self._cameraUpcomingDuration = None

        self._cameraBackwardDuration = None

        self._cameraObjectAspect = None

        self._cameraMaxDistance = None

        self._enableYawLimits = None

        self._yawLimitMin = None

        self._yawLimitMax = None

        self._pitchLimitMin = None

        self._pitchLimitMax = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (96, 'cameraShift'),
            (96, 'cameraPivot'),
            (32, 'cameraYaw'),
            (32, 'cameraPitch'),
            (32, 'cameraUpcomingDuration'),
            (32, 'cameraBackwardDuration'),
            (32, 'cameraObjectAspect'),
            (32, 'cameraMaxDistance'),
            (8, 'enableYawLimits'),
            (32, 'yawLimitMin'),
            (32, 'yawLimitMax'),
            (32, 'pitchLimitMin'),
            (32, 'pitchLimitMax'),
            
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


    # property size: 96
    @property
    def cameraShift(self):
        return self._cameraShift

    @cameraShift.setter
    def cameraShift(self, value):
        self._cameraShift, = unpack_variables(value, ['VECTOR3'])

    # property size: 96
    @property
    def cameraPivot(self):
        return self._cameraPivot

    @cameraPivot.setter
    def cameraPivot(self, value):
        self._cameraPivot, = unpack_variables(value, ['VECTOR3'])

    # property size: 32
    @property
    def cameraYaw(self):
        return self._cameraYaw

    @cameraYaw.setter
    def cameraYaw(self, value):
        self._cameraYaw, = unpack_variables(value, ['FLOAT32'])

    # property size: 32
    @property
    def cameraPitch(self):
        return self._cameraPitch

    @cameraPitch.setter
    def cameraPitch(self, value):
        self._cameraPitch, = unpack_variables(value, ['FLOAT32'])

    # property size: 32
    @property
    def cameraUpcomingDuration(self):
        return self._cameraUpcomingDuration

    @cameraUpcomingDuration.setter
    def cameraUpcomingDuration(self, value):
        self._cameraUpcomingDuration, = unpack_variables(value, ['FLOAT32'])

    # property size: 32
    @property
    def cameraBackwardDuration(self):
        return self._cameraBackwardDuration

    @cameraBackwardDuration.setter
    def cameraBackwardDuration(self, value):
        self._cameraBackwardDuration, = unpack_variables(value, ['FLOAT32'])

    # property size: 32
    @property
    def cameraObjectAspect(self):
        return self._cameraObjectAspect

    @cameraObjectAspect.setter
    def cameraObjectAspect(self, value):
        self._cameraObjectAspect, = unpack_variables(value, ['FLOAT32'])

    # property size: 32
    @property
    def cameraMaxDistance(self):
        return self._cameraMaxDistance

    @cameraMaxDistance.setter
    def cameraMaxDistance(self, value):
        self._cameraMaxDistance, = unpack_variables(value, ['FLOAT32'])

    # property size: 8
    @property
    def enableYawLimits(self):
        return self._enableYawLimits

    @enableYawLimits.setter
    def enableYawLimits(self, value):
        self._enableYawLimits, = unpack_variables(value, ['BOOL'])

    # property size: 32
    @property
    def yawLimitMin(self):
        return self._yawLimitMin

    @yawLimitMin.setter
    def yawLimitMin(self, value):
        self._yawLimitMin, = unpack_variables(value, ['FLOAT32'])

    # property size: 32
    @property
    def yawLimitMax(self):
        return self._yawLimitMax

    @yawLimitMax.setter
    def yawLimitMax(self, value):
        self._yawLimitMax, = unpack_variables(value, ['FLOAT32'])

    # property size: 32
    @property
    def pitchLimitMin(self):
        return self._pitchLimitMin

    @pitchLimitMin.setter
    def pitchLimitMin(self, value):
        self._pitchLimitMin, = unpack_variables(value, ['FLOAT32'])

    # property size: 32
    @property
    def pitchLimitMax(self):
        return self._pitchLimitMax

    @pitchLimitMax.setter
    def pitchLimitMax(self, value):
        self._pitchLimitMax, = unpack_variables(value, ['FLOAT32'])


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)