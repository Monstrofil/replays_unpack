#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class DetachedTurret(object):
    
    g_onStaticCollision = EventHook()
    
    g_showDamageFromShot = EventHook()
    
    g_receiveShot = EventHook()
    
    g_receiveExplosion = EventHook()
    
    g_applyForceToCOM = EventHook()
    
    g_onDamageVehicle = EventHook()
    
    g_smartDestroy = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._cp = None

        self._arenaTypeID = None

        self._velocity = None

        self._angularVelocity = None

        self._vehicleCompDescr = None

        self._isUnderWater = None

        self._isCollidingWithWorld = None

        self._vehicleID = None

        self._attackerInfo = None

        self._vehicleInfo = None

        self._isAtackerProxy = None

        self._arena = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['FLOAT32', 'VECTOR3', 'VECTOR3'])
    def onStaticCollision(self, arg1, arg2, arg3):
        self.g_onStaticCollision.fire(self, arg1, arg2, arg3)

    @unpack_func_args([['ARRAY', 'UINT64'], 'UINT8'])
    def showDamageFromShot(self, arg1, arg2):
        self.g_showDamageFromShot.fire(self, arg1, arg2)

    @unpack_func_args(['ATTACKER_INFO', 'SHOT_ID', 'INT32', 'VECTOR3', 'VECTOR3', 'VECTOR3'])
    def receiveShot(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_receiveShot.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['VECTOR3', 'FLOAT32', 'FLOAT32', 'UINT8'])
    def receiveExplosion(self, arg1, arg2, arg3, arg4):
        self.g_receiveExplosion.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['VECTOR3'])
    def applyForceToCOM(self, arg1):
        self.g_applyForceToCOM.fire(self, arg1)

    @unpack_func_args([])
    def onDamageVehicle(self):
        self.g_onDamageVehicle.fire(self)

    @unpack_func_args([])
    def smartDestroy(self):
        self.g_smartDestroy.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp, = unpack_variables(value, ['PYTHON'])

    @property
    def arenaTypeID(self):
        return self._arenaTypeID

    @arenaTypeID.setter
    def arenaTypeID(self, value):
        self._arenaTypeID, = unpack_variables(value, ['INT32'])

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity, = unpack_variables(value, ['VECTOR3'])

    @property
    def angularVelocity(self):
        return self._angularVelocity

    @angularVelocity.setter
    def angularVelocity(self, value):
        self._angularVelocity, = unpack_variables(value, ['VECTOR3'])

    @property
    def vehicleCompDescr(self):
        return self._vehicleCompDescr

    @vehicleCompDescr.setter
    def vehicleCompDescr(self, value):
        self._vehicleCompDescr, = unpack_variables(value, ['STRING'])

    @property
    def isUnderWater(self):
        return self._isUnderWater

    @isUnderWater.setter
    def isUnderWater(self, value):
        self._isUnderWater, = unpack_variables(value, ['BOOL'])

    @property
    def isCollidingWithWorld(self):
        return self._isCollidingWithWorld

    @isCollidingWithWorld.setter
    def isCollidingWithWorld(self, value):
        self._isCollidingWithWorld, = unpack_variables(value, ['BOOL'])

    @property
    def vehicleID(self):
        return self._vehicleID

    @vehicleID.setter
    def vehicleID(self, value):
        self._vehicleID, = unpack_variables(value, ['INT32'])

    @property
    def attackerInfo(self):
        return self._attackerInfo

    @attackerInfo.setter
    def attackerInfo(self, value):
        self._attackerInfo, = unpack_variables(value, ['ATTACKER_INFO'])

    @property
    def vehicleInfo(self):
        return self._vehicleInfo

    @vehicleInfo.setter
    def vehicleInfo(self, value):
        self._vehicleInfo, = unpack_variables(value, ['ATTACKER_INFO'])

    @property
    def isAtackerProxy(self):
        return self._isAtackerProxy

    @isAtackerProxy.setter
    def isAtackerProxy(self, value):
        self._isAtackerProxy, = unpack_variables(value, ['BOOL'])

    @property
    def arena(self):
        return self._arena

    @arena.setter
    def arena(self, value):
        self._arena, = unpack_variables(value, ['MAILBOX'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)