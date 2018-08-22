#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from interfaces.Destructible import Destructible



class DestructibleEntity(Destructible):
    
    g_onHealthChanged = EventHook()
    
    g_showDamageFromShot = EventHook()
    
    g_showDamageFromExplosion = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._isActive = None

        self._team = None

        self._destructibleEntityID = None

        self._health = None

        self._isDestructibleDestroyed = 'false'

        self._typeID = 1.0

        self._linkedMapActivities = None

        self._damageStickers = None


        # MRO fix

        Destructible.__init__(self)

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (8, 'isActive'),
            (8, 'team'),
            (8, 'destructibleEntityID'),
            (32, 'health'),
            (8, 'isDestructibleDestroyed'),
            (8, 'typeID'),
            (10000000000, 'linkedMapActivities'),
            (10000000000, 'damageStickers'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (89, 'onHealthChanged'),
            (10000000001, 'showDamageFromShot'),
            (145, 'showDamageFromExplosion'),
            
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

# method size: 89
    @unpack_func_args(['INT16', 'OBJECT_ID', 'UINT8', 'INT32'])
    def onHealthChanged(self, arg1, arg2, arg3, arg4):
        self.g_onHealthChanged.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000001
    @unpack_func_args([['ARRAY', 'UINT64'], 'UINT8'])
    def showDamageFromShot(self, arg1, arg2):
        self.g_showDamageFromShot.fire(self, arg1, arg2)
# method size: 145
    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'UINT8', 'UINT8'])
    def showDamageFromExplosion(self, arg1, arg2, arg3, arg4):
        self.g_showDamageFromExplosion.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 8
    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, value):
        self._isActive, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def destructibleEntityID(self):
        return self._destructibleEntityID

    @destructibleEntityID.setter
    def destructibleEntityID(self, value):
        self._destructibleEntityID, = unpack_variables(value, ['UINT8'])
# property size: 32
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def isDestructibleDestroyed(self):
        return self._isDestructibleDestroyed

    @isDestructibleDestroyed.setter
    def isDestructibleDestroyed(self, value):
        self._isDestructibleDestroyed, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def typeID(self):
        return self._typeID

    @typeID.setter
    def typeID(self, value):
        self._typeID, = unpack_variables(value, ['UINT8'])
# property size: 10000000000
    @property
    def linkedMapActivities(self):
        return self._linkedMapActivities

    @linkedMapActivities.setter
    def linkedMapActivities(self, value):
        self._linkedMapActivities, = unpack_variables(value, ['STRING'])
# property size: 10000000000
    @property
    def damageStickers(self):
        return self._damageStickers

    @damageStickers.setter
    def damageStickers(self, value):
        self._damageStickers, = unpack_variables(value, [['ARRAY', 'UINT64']])


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