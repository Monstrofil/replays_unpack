#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.Destructible import Destructible
except:
    from Destructible import Destructible



class DestructibleEntity(Destructible):
    
    g_onHealthChanged = EventHook()
    
    g_showDamageFromShot = EventHook()
    
    g_showDamageFromExplosion = EventHook()
    
    g_start = EventHook()
    
    g_stop = EventHook()
    
    g_reset = EventHook()
    
    g_smartDestroy = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._arena = None

        self._arenaBase = None

        self._isActive = None

        self._team = None

        self._destructibleEntityID = None

        self._health = None

        self._isDestructibleDestroyed = 'false'

        self._typeID = 1.0

        self._initActive = 0.0

        self._linkedMapActivities = None

        self._damageStickers = None

        self._explosionDamageFactor = '0.5'

        self._cp = None


        # MRO fix

        Destructible.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT16', 'OBJECT_ID', 'UINT8', 'INT32'])
    def onHealthChanged(self, arg1, arg2, arg3, arg4):
        self.g_onHealthChanged.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args([['ARRAY', 'UINT64'], 'UINT8'])
    def showDamageFromShot(self, arg1, arg2):
        self.g_showDamageFromShot.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'UINT8', 'UINT8'])
    def showDamageFromExplosion(self, arg1, arg2, arg3, arg4):
        self.g_showDamageFromExplosion.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args([])
    def start(self):
        self.g_start.fire(self)

    @unpack_func_args([])
    def stop(self):
        self.g_stop.fire(self)

    @unpack_func_args([])
    def reset(self):
        self.g_reset.fire(self)

    @unpack_func_args([])
    def smartDestroy(self):
        self.g_smartDestroy.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def arena(self):
        return self._arena

    @arena.setter
    def arena(self, value):
        self._arena, = unpack_variables(value, ['MAILBOX'])

    @property
    def arenaBase(self):
        return self._arenaBase

    @arenaBase.setter
    def arenaBase(self, value):
        self._arenaBase, = unpack_variables(value, ['MAILBOX'])

    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, value):
        self._isActive, = unpack_variables(value, ['BOOL'])

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])

    @property
    def destructibleEntityID(self):
        return self._destructibleEntityID

    @destructibleEntityID.setter
    def destructibleEntityID(self, value):
        self._destructibleEntityID, = unpack_variables(value, ['UINT8'])

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health, = unpack_variables(value, ['FLOAT32'])

    @property
    def isDestructibleDestroyed(self):
        return self._isDestructibleDestroyed

    @isDestructibleDestroyed.setter
    def isDestructibleDestroyed(self, value):
        self._isDestructibleDestroyed, = unpack_variables(value, ['BOOL'])

    @property
    def typeID(self):
        return self._typeID

    @typeID.setter
    def typeID(self, value):
        self._typeID, = unpack_variables(value, ['UINT8'])

    @property
    def initActive(self):
        return self._initActive

    @initActive.setter
    def initActive(self, value):
        self._initActive, = unpack_variables(value, ['BOOL'])

    @property
    def linkedMapActivities(self):
        return self._linkedMapActivities

    @linkedMapActivities.setter
    def linkedMapActivities(self, value):
        self._linkedMapActivities, = unpack_variables(value, ['STRING'])

    @property
    def damageStickers(self):
        return self._damageStickers

    @damageStickers.setter
    def damageStickers(self, value):
        self._damageStickers, = unpack_variables(value, ['ARRAY', ['UINT64']])

    @property
    def explosionDamageFactor(self):
        return self._explosionDamageFactor

    @explosionDamageFactor.setter
    def explosionDamageFactor(self, value):
        self._explosionDamageFactor, = unpack_variables(value, ['FLOAT32'])

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp, = unpack_variables(value, ['PYTHON'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)