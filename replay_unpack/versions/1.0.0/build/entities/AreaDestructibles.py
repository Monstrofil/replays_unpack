#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.ArtilleryController import ArtilleryController
except:
    from ArtilleryController import ArtilleryController

try:
    from interfaces.BomberController import BomberController
except:
    from BomberController import BomberController

try:
    from interfaces.ProjectileController import ProjectileController
except:
    from ProjectileController import ProjectileController



class AreaDestructibles(ArtilleryController, BomberController, ProjectileController):
    
    g_reset = EventHook()
    
    g_damageDestructibleAndTakeOverProjectile = EventHook()
    
    g_damageDestructible = EventHook()
    
    g_receiveTaggedDestructibleKill = EventHook()
    
    g_createCellNearHere = EventHook()
    
    g_smartDestroy = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._chunkID = None

        self._destroyedModules = None

        self._destroyedFragiles = None

        self._fallenColumns = None

        self._fallenTrees = None

        self._destructibles = None

        self._waters = None

        self._resetCount = None

        self._arenaBase = None

        self._arenaGeometryID = None

        self._cp = None

        self._arena = None


        # MRO fix

        ArtilleryController.__init__(self)

        BomberController.__init__(self)

        ProjectileController.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def reset(self):
        self.g_reset.fire(self)

    @unpack_func_args(['UINT8', 'UINT8', 'FLOAT32', 'VECTOR3', 'VECTOR3', 'ATTACKER_INFO', 'SHOT_ID', 'INT32', 'UINT8', 'UINT8', ['ARRAY', 'MAILBOX'], ['ARRAY', 'FLOAT32', 2], 'FLOAT32', 'FLOAT64', 'VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT64'])
    def damageDestructibleAndTakeOverProjectile(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21):
        self.g_damageDestructibleAndTakeOverProjectile.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21)

    @unpack_func_args(['UINT8', 'UINT8', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'INT8', 'DESTRUCTIBLE_ATTACK_INFO'])
    def damageDestructible(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_damageDestructible.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['UINT8'])
    def receiveTaggedDestructibleKill(self, arg1):
        self.g_receiveTaggedDestructibleKill.fire(self, arg1)

    @unpack_func_args(['MAILBOX'])
    def createCellNearHere(self, arg1):
        self.g_createCellNearHere.fire(self, arg1)

    @unpack_func_args([])
    def smartDestroy(self):
        self.g_smartDestroy.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def chunkID(self):
        return self._chunkID

    @chunkID.setter
    def chunkID(self, value):
        self._chunkID, = unpack_variables(value, ['UINT16'])

    @property
    def destroyedModules(self):
        return self._destroyedModules

    @destroyedModules.setter
    def destroyedModules(self, value):
        self._destroyedModules, = unpack_variables(value, ['ARRAY', ['ARRAY', ['UINT8'], 3]])

    @property
    def destroyedFragiles(self):
        return self._destroyedFragiles

    @destroyedFragiles.setter
    def destroyedFragiles(self, value):
        self._destroyedFragiles, = unpack_variables(value, ['ARRAY', ['ARRAY', ['UINT8'], 3]])

    @property
    def fallenColumns(self):
        return self._fallenColumns

    @fallenColumns.setter
    def fallenColumns(self, value):
        self._fallenColumns, = unpack_variables(value, ['ARRAY', ['ARRAY', ['UINT8'], 3]])

    @property
    def fallenTrees(self):
        return self._fallenTrees

    @fallenTrees.setter
    def fallenTrees(self, value):
        self._fallenTrees, = unpack_variables(value, ['ARRAY', ['ARRAY', ['UINT8'], 5]])

    @property
    def destructibles(self):
        return self._destructibles

    @destructibles.setter
    def destructibles(self, value):
        self._destructibles, = unpack_variables(value, ['PYTHON'])

    @property
    def waters(self):
        return self._waters

    @waters.setter
    def waters(self, value):
        self._waters, = unpack_variables(value, ['ARRAY', ['ARRAY', ['FLOAT32'], 5]])

    @property
    def resetCount(self):
        return self._resetCount

    @resetCount.setter
    def resetCount(self, value):
        self._resetCount, = unpack_variables(value, ['UINT32'])

    @property
    def arenaBase(self):
        return self._arenaBase

    @arenaBase.setter
    def arenaBase(self, value):
        self._arenaBase, = unpack_variables(value, ['MAILBOX'])

    @property
    def arenaGeometryID(self):
        return self._arenaGeometryID

    @arenaGeometryID.setter
    def arenaGeometryID(self, value):
        self._arenaGeometryID, = unpack_variables(value, ['INT16'])

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp, = unpack_variables(value, ['PYTHON'])

    @property
    def arena(self):
        return self._arena

    @arena.setter
    def arena(self, value):
        self._arena, = unpack_variables(value, ['MAILBOX'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)