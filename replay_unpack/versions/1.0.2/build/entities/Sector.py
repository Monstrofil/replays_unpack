#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class Sector(object):
    
    g_showBomb = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._groupID = None

        self._sectorID = 1.0

        self._playerGroup = None

        self._IDInPlayerGroup = None

        self._lengthX = '0.0'

        self._lengthZ = '0.0'

        self._team = None

        self._state = None

        self._transitionTime = '1.0'

        self._endOfTransitionPeriod = '-1.0'


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (8, 'groupID'),
            (8, 'sectorID'),
            (8, 'playerGroup'),
            (8, 'IDInPlayerGroup'),
            (32, 'lengthX'),
            (32, 'lengthZ'),
            (8, 'team'),
            (8, 'state'),
            (32, 'transitionTime'),
            (32, 'endOfTransitionPeriod'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (97, 'showBomb'),
            
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

# method size: 97
    @unpack_func_args(['VECTOR3'])
    def showBomb(self, arg1):
        self.g_showBomb.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 8
    @property
    def groupID(self):
        return self._groupID

    @groupID.setter
    def groupID(self, value):
        self._groupID, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def sectorID(self):
        return self._sectorID

    @sectorID.setter
    def sectorID(self, value):
        self._sectorID, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def playerGroup(self):
        return self._playerGroup

    @playerGroup.setter
    def playerGroup(self, value):
        self._playerGroup, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def IDInPlayerGroup(self):
        return self._IDInPlayerGroup

    @IDInPlayerGroup.setter
    def IDInPlayerGroup(self, value):
        self._IDInPlayerGroup, = unpack_variables(value, ['UINT8'])
# property size: 32
    @property
    def lengthX(self):
        return self._lengthX

    @lengthX.setter
    def lengthX(self, value):
        self._lengthX, = unpack_variables(value, ['FLOAT32'])
# property size: 32
    @property
    def lengthZ(self):
        return self._lengthZ

    @lengthZ.setter
    def lengthZ(self, value):
        self._lengthZ, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state, = unpack_variables(value, ['UINT8'])
# property size: 32
    @property
    def transitionTime(self):
        return self._transitionTime

    @transitionTime.setter
    def transitionTime(self, value):
        self._transitionTime, = unpack_variables(value, ['FLOAT32'])
# property size: 32
    @property
    def endOfTransitionPeriod(self):
        return self._endOfTransitionPeriod

    @endOfTransitionPeriod.setter
    def endOfTransitionPeriod(self, value):
        self._endOfTransitionPeriod, = unpack_variables(value, ['FLOAT32'])


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