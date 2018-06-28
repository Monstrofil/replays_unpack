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


        self._globalWeatherStateList = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def startTransition(self):
        self.g_startTransition.fire(self)

    @unpack_func_args(['GAMEPARAMS_ID'])
    def prepareForTransition(self, arg1):
        self.g_prepareForTransition.fire(self, arg1)

    @unpack_func_args(['FLOAT', 'GAMEPARAMS_ID'])
    def notification(self, arg1, arg2):
        self.g_notification.fire(self, arg1, arg2)

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
    def globalWeatherStateList(self):
        return self._globalWeatherStateList

    @globalWeatherStateList.setter
    def globalWeatherStateList(self, value):
        self._globalWeatherStateList, = unpack_variables(value, [['ARRAY', 'GLOBAL_WEATHER_STATE']])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)