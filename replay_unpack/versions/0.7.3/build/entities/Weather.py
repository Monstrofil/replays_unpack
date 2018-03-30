#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Weather(object):
    
    g_startTransition = EventHook()
    
    g_prepareForTransition = EventHook()
    
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


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)