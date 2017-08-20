#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.Entity import Entity
from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Weather(object):
    
    g_startTransition = EventHook()
    
    g_prepareForTransition = EventHook()
    
    g_onChanged = EventHook()
    
    g_notification = EventHook()
    
    g_syncStartTransition = EventHook()
    
    g_onClientEnterWorld = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._configPath = None

        self._scheme = None

        self._weather = None

        self._transitionFactor = None

        self._visibilityFactor = None

        self._visibilityFactorByPlane = None

        self._GMIdealRadius = None

        self._airplanesSpeed = None

        self._burnDamage = None

        self._smokeLifeTime = None

        self._maxShipVisionDistance = None

        self._maxPlaneVisionDistance = None

        self._isBad = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def startTransition(self):
        self.g_startTransition.fire(self)

    @unpack_func_args([])
    def prepareForTransition(self):
        self.g_prepareForTransition.fire(self)

    @unpack_func_args([])
    def onChanged(self):
        self.g_onChanged.fire(self)

    @unpack_func_args(['FLOAT'])
    def notification(self, arg1):
        self.g_notification.fire(self, arg1)

    @unpack_func_args(['FLOAT'])
    def syncStartTransition(self, arg1):
        self.g_syncStartTransition.fire(self, arg1)

    @unpack_func_args([])
    def onClientEnterWorld(self):
        self.g_onClientEnterWorld.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def configPath(self):
        return self._configPath

    @configPath.setter
    def configPath(self, value):
        self._configPath, = unpack_variables(value, ['STRING'])

    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, value):
        self._scheme, = unpack_variables(value, ['UINT16'])

    @property
    def weather(self):
        return self._weather

    @weather.setter
    def weather(self, value):
        self._weather, = unpack_variables(value, ['UINT16'])

    @property
    def transitionFactor(self):
        return self._transitionFactor

    @transitionFactor.setter
    def transitionFactor(self, value):
        self._transitionFactor, = unpack_variables(value, ['FLOAT'])

    @property
    def visibilityFactor(self):
        return self._visibilityFactor

    @visibilityFactor.setter
    def visibilityFactor(self, value):
        self._visibilityFactor, = unpack_variables(value, ['FLOAT'])

    @property
    def visibilityFactorByPlane(self):
        return self._visibilityFactorByPlane

    @visibilityFactorByPlane.setter
    def visibilityFactorByPlane(self, value):
        self._visibilityFactorByPlane, = unpack_variables(value, ['FLOAT'])

    @property
    def GMIdealRadius(self):
        return self._GMIdealRadius

    @GMIdealRadius.setter
    def GMIdealRadius(self, value):
        self._GMIdealRadius, = unpack_variables(value, ['FLOAT'])

    @property
    def airplanesSpeed(self):
        return self._airplanesSpeed

    @airplanesSpeed.setter
    def airplanesSpeed(self, value):
        self._airplanesSpeed, = unpack_variables(value, ['FLOAT'])

    @property
    def burnDamage(self):
        return self._burnDamage

    @burnDamage.setter
    def burnDamage(self, value):
        self._burnDamage, = unpack_variables(value, ['FLOAT'])

    @property
    def smokeLifeTime(self):
        return self._smokeLifeTime

    @smokeLifeTime.setter
    def smokeLifeTime(self, value):
        self._smokeLifeTime, = unpack_variables(value, ['FLOAT'])

    @property
    def maxShipVisionDistance(self):
        return self._maxShipVisionDistance

    @maxShipVisionDistance.setter
    def maxShipVisionDistance(self, value):
        self._maxShipVisionDistance, = unpack_variables(value, ['FLOAT'])

    @property
    def maxPlaneVisionDistance(self):
        return self._maxPlaneVisionDistance

    @maxPlaneVisionDistance.setter
    def maxPlaneVisionDistance(self, value):
        self._maxPlaneVisionDistance, = unpack_variables(value, ['FLOAT'])

    @property
    def isBad(self):
        return self._isBad

    @isBad.setter
    def isBad(self, value):
        self._isBad, = unpack_variables(value, ['FLOAT'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)