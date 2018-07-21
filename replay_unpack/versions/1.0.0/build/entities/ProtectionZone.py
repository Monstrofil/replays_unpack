#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class ProtectionZone(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._zoneID = 1.0

        self._lengthX = '300.0'

        self._lengthZ = '500.0'

        self._team = 0.0

        self._isActive = 'False'


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (8, 'zoneID'),
            (32, 'lengthX'),
            (32, 'lengthZ'),
            (8, 'team'),
            (8, 'isActive'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            
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



    ####################################
    #       PROPERTIES
    ####################################


    # property size: 8
    @property
    def zoneID(self):
        return self._zoneID

    @zoneID.setter
    def zoneID(self, value):
        self._zoneID, = unpack_variables(value, ['UINT8'])

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
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, value):
        self._isActive, = unpack_variables(value, ['BOOL'])


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)