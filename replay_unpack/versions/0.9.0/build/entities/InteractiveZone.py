#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class InteractiveZone(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._radius = '5.0'

        self._ownerId = 0.0

        self._name = '""'

        self._teamId = 0.0

        self._state = None

        self._type = None

        self._useRing = 'True'


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        for item in [
            (32, 'radius'),
            (32, 'ownerId'),
            (10000000000, 'name'),
            (8, 'teamId'),
            (24, 'state'),
            (8, 'type'),
            (8, 'useRing'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            
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



    ####################################
    #       PROPERTIES
    ####################################

# property size: 32
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT32'])
# property size: 32
    @property
    def ownerId(self):
        return self._ownerId

    @ownerId.setter
    def ownerId(self, value):
        self._ownerId, = unpack_variables(value, ['ENTITY_ID'])
# property size: 10000000000
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name, = unpack_variables(value, ['STRING'])
# property size: 8
    @property
    def teamId(self):
        return self._teamId

    @teamId.setter
    def teamId(self, value):
        self._teamId, = unpack_variables(value, ['TEAM_ID'])
# property size: 24
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state, = unpack_variables(value, ['INTERACTIVE_ZONE_ENTITY_STATE'])
# property size: 8
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def useRing(self):
        return self._useRing

    @useRing.setter
    def useRing(self, value):
        self._useRing, = unpack_variables(value, ['BOOL'])


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