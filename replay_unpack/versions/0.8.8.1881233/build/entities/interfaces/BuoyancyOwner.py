#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class BuoyancyOwner(object):
    
    g_setMiniGameCounter = EventHook()
    
    g_miniGameEnded = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._oxygen = None

        self._buoyancyCurrentState = None

        self._buoyancyCurrentWaterline = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        for item in [
            (32, 'oxygen'),
            (8, 'buoyancyCurrentState'),
            (32, 'buoyancyCurrentWaterline'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (9, 'setMiniGameCounter'),
            (1, 'miniGameEnded'),
            
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

# method size: 9
    @unpack_func_args(['UINT8'])
    def setMiniGameCounter(self, arg1):
        self.g_setMiniGameCounter.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def miniGameEnded(self):
        self.g_miniGameEnded.fire(self)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 32
    @property
    def oxygen(self):
        return self._oxygen

    @oxygen.setter
    def oxygen(self, value):
        self._oxygen, = unpack_variables(value, ['FLOAT'])
# property size: 8
    @property
    def buoyancyCurrentState(self):
        return self._buoyancyCurrentState

    @buoyancyCurrentState.setter
    def buoyancyCurrentState(self, value):
        self._buoyancyCurrentState, = unpack_variables(value, ['UINT8'])
# property size: 32
    @property
    def buoyancyCurrentWaterline(self):
        return self._buoyancyCurrentWaterline

    @buoyancyCurrentWaterline.setter
    def buoyancyCurrentWaterline(self, value):
        self._buoyancyCurrentWaterline, = unpack_variables(value, ['FLOAT'])


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