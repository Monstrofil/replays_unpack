#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class HitLocationManagerOwner(object):
    
    g_drawSplash = EventHook()
    
    g_receiveSomeSplashInfo = EventHook()
    
    g_receiveHitLocationsInitialState = EventHook()
    
    g_receiveHitLocationStateChange = EventHook()
    
    g_dev_receiveHitLocationDamage = EventHook()
    
    g_setTimesToBurn = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._health = None

        self._regenerationHealth = '0.0'

        self._regeneratedHealth = '0.0'

        self._burningFlags = 0.0


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        for item in [
            (32, 'health'),
            (32, 'regenerationHealth'),
            (32, 'regeneratedHealth'),
            (8, 'burningFlags'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (169, 'drawSplash'),
            (10000000001, 'receiveSomeSplashInfo'),
            (10000000002, 'receiveHitLocationsInitialState'),
            (49, 'receiveHitLocationStateChange'),
            (10000000001, 'dev_receiveHitLocationDamage'),
            (10000000001, 'setTimesToBurn'),
            
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

# method size: 169
    @unpack_func_args(['VECTOR3', 'FLOAT32', 'UINT32', 'BOOL'])
    def drawSplash(self, arg1, arg2, arg3, arg4):
        self.g_drawSplash.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000001
    @unpack_func_args(['BLOB', 'BOOL', 'BOOL'])
    def receiveSomeSplashInfo(self, arg1, arg2, arg3):
        self.g_receiveSomeSplashInfo.fire(self, arg1, arg2, arg3)
# method size: 10000000002
    @unpack_func_args([['ARRAY', 'UINT8'], ['ARRAY', 'UINT32']])
    def receiveHitLocationsInitialState(self, arg1, arg2):
        self.g_receiveHitLocationsInitialState.fire(self, arg1, arg2)
# method size: 49
    @unpack_func_args(['UINT16', 'UINT32'])
    def receiveHitLocationStateChange(self, arg1, arg2):
        self.g_receiveHitLocationStateChange.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['UINT32', 'STRING', 'UINT32'])
    def dev_receiveHitLocationDamage(self, arg1, arg2, arg3):
        self.g_dev_receiveHitLocationDamage.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args([['ARRAY', 'FLOAT']])
    def setTimesToBurn(self, arg1):
        self.g_setTimesToBurn.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 32
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health, = unpack_variables(value, ['FLOAT32'])
# property size: 32
    @property
    def regenerationHealth(self):
        return self._regenerationHealth

    @regenerationHealth.setter
    def regenerationHealth(self, value):
        self._regenerationHealth, = unpack_variables(value, ['FLOAT32'])
# property size: 32
    @property
    def regeneratedHealth(self):
        return self._regeneratedHealth

    @regeneratedHealth.setter
    def regeneratedHealth(self, value):
        self._regeneratedHealth, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def burningFlags(self):
        return self._burningFlags

    @burningFlags.setter
    def burningFlags(self, value):
        self._burningFlags, = unpack_variables(value, ['UINT8'])


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