#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class AirDefenceOwner(object):
    
    g_receiveBubbles = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._airDefenseTargetIds = None

        self._airDefenseDispRadius = '0.0'

        self._isAntiAirMode = 0.0

        self._antiAirAuras = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        for item in [
            (10000000000, 'airDefenseTargetIds'),
            (32, 'airDefenseDispRadius'),
            (8, 'isAntiAirMode'),
            (10000000000, 'antiAirAuras'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (10000000001, 'receiveBubbles'),
            
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

# method size: 10000000001
    @unpack_func_args(['BUBBLE_PACK', 'UINT8'])
    def receiveBubbles(self, arg1, arg2):
        self.g_receiveBubbles.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 10000000000
    @property
    def airDefenseTargetIds(self):
        return self._airDefenseTargetIds

    @airDefenseTargetIds.setter
    def airDefenseTargetIds(self, value):
        self._airDefenseTargetIds, = unpack_variables(value, [['ARRAY', ['ARRAY', 'PLANE_ID']]])
# property size: 32
    @property
    def airDefenseDispRadius(self):
        return self._airDefenseDispRadius

    @airDefenseDispRadius.setter
    def airDefenseDispRadius(self, value):
        self._airDefenseDispRadius, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def isAntiAirMode(self):
        return self._isAntiAirMode

    @isAntiAirMode.setter
    def isAntiAirMode(self, value):
        self._isAntiAirMode, = unpack_variables(value, ['BOOL'])
# property size: 10000000000
    @property
    def antiAirAuras(self):
        return self._antiAirAuras

    @antiAirAuras.setter
    def antiAirAuras(self, value):
        self._antiAirAuras, = unpack_variables(value, [['ARRAY', 'AIR_DEFENCE_AURA']])


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