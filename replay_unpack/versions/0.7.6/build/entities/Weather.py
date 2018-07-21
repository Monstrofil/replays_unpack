#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class Weather(object):
    
    g_startTransition = EventHook()
    
    g_prepareForTransition = EventHook()
    
    g_notification = EventHook()
    
    g_syncStartTransition = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._globalWeatherStateList = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (10000000000, 'globalWeatherStateList'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (1, 'startTransition'),
            (33, 'prepareForTransition'),
            (65, 'notification'),
            (33, 'syncStartTransition'),
            
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

# method size: 1
    @unpack_func_args([])
    def startTransition(self):
        self.g_startTransition.fire(self)
# method size: 33
    @unpack_func_args(['GAMEPARAMS_ID'])
    def prepareForTransition(self, arg1):
        self.g_prepareForTransition.fire(self, arg1)
# method size: 65
    @unpack_func_args(['FLOAT', 'GAMEPARAMS_ID'])
    def notification(self, arg1, arg2):
        self.g_notification.fire(self, arg1, arg2)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def syncStartTransition(self, arg1):
        self.g_syncStartTransition.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 10000000000
    @property
    def globalWeatherStateList(self):
        return self._globalWeatherStateList

    @globalWeatherStateList.setter
    def globalWeatherStateList(self, value):
        self._globalWeatherStateList, = unpack_variables(value, [['ARRAY', 'GLOBAL_WEATHER_STATE']])


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