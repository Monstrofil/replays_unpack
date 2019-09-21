#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class SubmarineSearchPoint(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._radius = None

        self._lifeTime = None

        self._counter = None

        self._inSafeTime = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        for item in [
            (32, 'radius'),
            (32, 'lifeTime'),
            (8, 'counter'),
            (8, 'inSafeTime'),
            
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
    def lifeTime(self):
        return self._lifeTime

    @lifeTime.setter
    def lifeTime(self, value):
        self._lifeTime, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter, = unpack_variables(value, ['INT8'])
# property size: 8
    @property
    def inSafeTime(self):
        return self._inSafeTime

    @inSafeTime.setter
    def inSafeTime(self, value):
        self._inSafeTime, = unpack_variables(value, ['BOOL'])


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