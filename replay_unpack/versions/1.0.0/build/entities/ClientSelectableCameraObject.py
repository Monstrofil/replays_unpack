#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

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

        return

    ####################################
    #      METHODS
    ####################################



    ####################################
    #       PROPERTIES
    ####################################


    @property
    def cameraShift(self):
        return self._cameraShift

    @cameraShift.setter
    def cameraShift(self, value):
        self._cameraShift, = unpack_variables(value, ['VECTOR3'])

    @property
    def cameraPivot(self):
        return self._cameraPivot

    @cameraPivot.setter
    def cameraPivot(self, value):
        self._cameraPivot, = unpack_variables(value, ['VECTOR3'])

    @property
    def cameraYaw(self):
        return self._cameraYaw

    @cameraYaw.setter
    def cameraYaw(self, value):
        self._cameraYaw, = unpack_variables(value, ['FLOAT32'])

    @property
    def cameraPitch(self):
        return self._cameraPitch

    @cameraPitch.setter
    def cameraPitch(self, value):
        self._cameraPitch, = unpack_variables(value, ['FLOAT32'])

    @property
    def cameraUpcomingDuration(self):
        return self._cameraUpcomingDuration

    @cameraUpcomingDuration.setter
    def cameraUpcomingDuration(self, value):
        self._cameraUpcomingDuration, = unpack_variables(value, ['FLOAT32'])

    @property
    def cameraBackwardDuration(self):
        return self._cameraBackwardDuration

    @cameraBackwardDuration.setter
    def cameraBackwardDuration(self, value):
        self._cameraBackwardDuration, = unpack_variables(value, ['FLOAT32'])

    @property
    def cameraObjectAspect(self):
        return self._cameraObjectAspect

    @cameraObjectAspect.setter
    def cameraObjectAspect(self, value):
        self._cameraObjectAspect, = unpack_variables(value, ['FLOAT32'])

    @property
    def cameraMaxDistance(self):
        return self._cameraMaxDistance

    @cameraMaxDistance.setter
    def cameraMaxDistance(self, value):
        self._cameraMaxDistance, = unpack_variables(value, ['FLOAT32'])

    @property
    def enableYawLimits(self):
        return self._enableYawLimits

    @enableYawLimits.setter
    def enableYawLimits(self, value):
        self._enableYawLimits, = unpack_variables(value, ['BOOL'])

    @property
    def yawLimitMin(self):
        return self._yawLimitMin

    @yawLimitMin.setter
    def yawLimitMin(self, value):
        self._yawLimitMin, = unpack_variables(value, ['FLOAT32'])

    @property
    def yawLimitMax(self):
        return self._yawLimitMax

    @yawLimitMax.setter
    def yawLimitMax(self, value):
        self._yawLimitMax, = unpack_variables(value, ['FLOAT32'])

    @property
    def pitchLimitMin(self):
        return self._pitchLimitMin

    @pitchLimitMin.setter
    def pitchLimitMin(self, value):
        self._pitchLimitMin, = unpack_variables(value, ['FLOAT32'])

    @property
    def pitchLimitMax(self):
        return self._pitchLimitMax

    @pitchLimitMax.setter
    def pitchLimitMax(self, value):
        self._pitchLimitMax, = unpack_variables(value, ['FLOAT32'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)