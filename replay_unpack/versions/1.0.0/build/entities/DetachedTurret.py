#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class DetachedTurret(object):
    
    g_onStaticCollision = EventHook()
    
    g_showDamageFromShot = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._vehicleCompDescr = None

        self._isUnderWater = None

        self._isCollidingWithWorld = None

        self._vehicleID = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (10000000000, 'vehicleCompDescr'),
            (8, 'isUnderWater'),
            (8, 'isCollidingWithWorld'),
            (32, 'vehicleID'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (224, 'onStaticCollision'),
            (10000000000, 'showDamageFromShot'),
            
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


    # method size: 224
    @unpack_func_args(['FLOAT32', 'VECTOR3', 'VECTOR3'])
    def onStaticCollision(self, arg1, arg2, arg3):
        self.g_onStaticCollision.fire(self, arg1, arg2, arg3)

    # method size: 10000000000
    @unpack_func_args([['ARRAY', 'UINT64'], 'UINT8'])
    def showDamageFromShot(self, arg1, arg2):
        self.g_showDamageFromShot.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################


    # property size: 10000000000
    @property
    def vehicleCompDescr(self):
        return self._vehicleCompDescr

    @vehicleCompDescr.setter
    def vehicleCompDescr(self, value):
        self._vehicleCompDescr, = unpack_variables(value, ['STRING'])

    # property size: 8
    @property
    def isUnderWater(self):
        return self._isUnderWater

    @isUnderWater.setter
    def isUnderWater(self, value):
        self._isUnderWater, = unpack_variables(value, ['BOOL'])

    # property size: 8
    @property
    def isCollidingWithWorld(self):
        return self._isCollidingWithWorld

    @isCollidingWithWorld.setter
    def isCollidingWithWorld(self, value):
        self._isCollidingWithWorld, = unpack_variables(value, ['BOOL'])

    # property size: 32
    @property
    def vehicleID(self):
        return self._vehicleID

    @vehicleID.setter
    def vehicleID(self, value):
        self._vehicleID, = unpack_variables(value, ['INT32'])


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)