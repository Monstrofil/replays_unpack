#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class FlockExotic(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._animSpeedMax = '1.0'

        self._animSpeedMin = '1.0'

        self._modelCount = 5.0

        self._modelName = None

        self._modelName2 = None

        self._speed = '0.2'

        self._initSpeedRandom = '0.3 0.4'

        self._speedRandom = '0.8 1.0'

        self._accelerationTime = 5.0

        self._triggerRadius = 20.0

        self._explosionRadius = '10 20'

        self._spawnRadius = 5.0

        self._spawnHeight = 5.0

        self._flightRadius = 50.0

        self._flightHeight = 15.0

        self._flightAngleMin = 0.0

        self._flightAngleMax = 360.0

        self._flightOffsetFromOrigin = 0.0

        self._lifeTime = 7.0

        self._respawnTime = 5.0

        self._flightSound = 'ambient_nature_trigger_soaring_birds'


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################



    ####################################
    #       PROPERTIES
    ####################################


    @property
    def animSpeedMax(self):
        return self._animSpeedMax

    @animSpeedMax.setter
    def animSpeedMax(self, value):
        self._animSpeedMax, = unpack_variables(value, ['FLOAT'])

    @property
    def animSpeedMin(self):
        return self._animSpeedMin

    @animSpeedMin.setter
    def animSpeedMin(self, value):
        self._animSpeedMin, = unpack_variables(value, ['FLOAT'])

    @property
    def modelCount(self):
        return self._modelCount

    @modelCount.setter
    def modelCount(self, value):
        self._modelCount, = unpack_variables(value, ['UINT8'])

    @property
    def modelName(self):
        return self._modelName

    @modelName.setter
    def modelName(self, value):
        self._modelName, = unpack_variables(value, ['STRING'])

    @property
    def modelName2(self):
        return self._modelName2

    @modelName2.setter
    def modelName2(self, value):
        self._modelName2, = unpack_variables(value, ['STRING'])

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed, = unpack_variables(value, ['FLOAT'])

    @property
    def initSpeedRandom(self):
        return self._initSpeedRandom

    @initSpeedRandom.setter
    def initSpeedRandom(self, value):
        self._initSpeedRandom, = unpack_variables(value, ['VECTOR2'])

    @property
    def speedRandom(self):
        return self._speedRandom

    @speedRandom.setter
    def speedRandom(self, value):
        self._speedRandom, = unpack_variables(value, ['VECTOR2'])

    @property
    def accelerationTime(self):
        return self._accelerationTime

    @accelerationTime.setter
    def accelerationTime(self, value):
        self._accelerationTime, = unpack_variables(value, ['FLOAT'])

    @property
    def triggerRadius(self):
        return self._triggerRadius

    @triggerRadius.setter
    def triggerRadius(self, value):
        self._triggerRadius, = unpack_variables(value, ['FLOAT'])

    @property
    def explosionRadius(self):
        return self._explosionRadius

    @explosionRadius.setter
    def explosionRadius(self, value):
        self._explosionRadius, = unpack_variables(value, ['VECTOR2'])

    @property
    def spawnRadius(self):
        return self._spawnRadius

    @spawnRadius.setter
    def spawnRadius(self, value):
        self._spawnRadius, = unpack_variables(value, ['FLOAT'])

    @property
    def spawnHeight(self):
        return self._spawnHeight

    @spawnHeight.setter
    def spawnHeight(self, value):
        self._spawnHeight, = unpack_variables(value, ['FLOAT'])

    @property
    def flightRadius(self):
        return self._flightRadius

    @flightRadius.setter
    def flightRadius(self, value):
        self._flightRadius, = unpack_variables(value, ['FLOAT'])

    @property
    def flightHeight(self):
        return self._flightHeight

    @flightHeight.setter
    def flightHeight(self, value):
        self._flightHeight, = unpack_variables(value, ['FLOAT'])

    @property
    def flightAngleMin(self):
        return self._flightAngleMin

    @flightAngleMin.setter
    def flightAngleMin(self, value):
        self._flightAngleMin, = unpack_variables(value, ['FLOAT'])

    @property
    def flightAngleMax(self):
        return self._flightAngleMax

    @flightAngleMax.setter
    def flightAngleMax(self, value):
        self._flightAngleMax, = unpack_variables(value, ['FLOAT'])

    @property
    def flightOffsetFromOrigin(self):
        return self._flightOffsetFromOrigin

    @flightOffsetFromOrigin.setter
    def flightOffsetFromOrigin(self, value):
        self._flightOffsetFromOrigin, = unpack_variables(value, ['FLOAT'])

    @property
    def lifeTime(self):
        return self._lifeTime

    @lifeTime.setter
    def lifeTime(self, value):
        self._lifeTime, = unpack_variables(value, ['FLOAT'])

    @property
    def respawnTime(self):
        return self._respawnTime

    @respawnTime.setter
    def respawnTime(self, value):
        self._respawnTime, = unpack_variables(value, ['FLOAT'])

    @property
    def flightSound(self):
        return self._flightSound

    @flightSound.setter
    def flightSound(self, value):
        self._flightSound, = unpack_variables(value, ['STRING'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)