#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.Entity import Entity
from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class HitLocationManagerOwner(object):
    
    g_dev_hit = EventHook()
    
    g_causeDamage = EventHook()
    
    g_dev_hlSet = EventHook()
    
    g_dev_bot_spawnSplashAtShootPos = EventHook()
    
    g_dev_BurnFlood = EventHook()
    
    g_setBurnFlood = EventHook()
    
    g_drawSplash = EventHook()
    
    g_receiveSomeSplashInfo = EventHook()
    
    g_receiveHitLocationsInitialState = EventHook()
    
    g_receiveHitLocationStateChange = EventHook()
    
    g_dev_receiveHitLocationDamage = EventHook()
    
    g_setTimesToBurn = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._health = None

        self._regenerationHealth = '0.0'

        self._regeneratedHealth = '0.0'

        self._burningFlags = 0.0

        self._detonationEnabled = 1.0

        self._friendlyFireEnabled = 1.0


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['STRING', 'FLOAT32', 'BOOL', 'INT32', 'STRING'])
    def dev_hit(self, arg1, arg2, arg3, arg4, arg5):
        self.g_dev_hit.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['STRING', 'FLOAT32', 'BOOL', 'INT32', 'STRING'])
    def causeDamage(self, arg1, arg2, arg3, arg4, arg5):
        self.g_causeDamage.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['STRING', 'INT8'])
    def dev_hlSet(self, arg1, arg2):
        self.g_dev_hlSet.fire(self, arg1, arg2)

    @unpack_func_args([])
    def dev_bot_spawnSplashAtShootPos(self):
        self.g_dev_bot_spawnSplashAtShootPos.fire(self)

    @unpack_func_args(['UINT8', 'BOOL'])
    def dev_BurnFlood(self, arg1, arg2):
        self.g_dev_BurnFlood.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'BOOL'])
    def setBurnFlood(self, arg1, arg2):
        self.g_setBurnFlood.fire(self, arg1, arg2)

    @unpack_func_args(['VECTOR3', 'FLOAT32', 'UINT32', 'BOOL'])
    def drawSplash(self, arg1, arg2, arg3, arg4):
        self.g_drawSplash.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['BLOB', 'BOOL', 'BOOL'])
    def receiveSomeSplashInfo(self, arg1, arg2, arg3):
        self.g_receiveSomeSplashInfo.fire(self, arg1, arg2, arg3)

    @unpack_func_args([['ARRAY', 'UINT8'], ['ARRAY', 'UINT32']])
    def receiveHitLocationsInitialState(self, arg1, arg2):
        self.g_receiveHitLocationsInitialState.fire(self, arg1, arg2)

    @unpack_func_args(['UINT16', 'UINT32'])
    def receiveHitLocationStateChange(self, arg1, arg2):
        self.g_receiveHitLocationStateChange.fire(self, arg1, arg2)

    @unpack_func_args(['UINT32', 'STRING', 'UINT32'])
    def dev_receiveHitLocationDamage(self, arg1, arg2, arg3):
        self.g_dev_receiveHitLocationDamage.fire(self, arg1, arg2, arg3)

    @unpack_func_args([['ARRAY', 'FLOAT']])
    def setTimesToBurn(self, arg1):
        self.g_setTimesToBurn.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health, = unpack_variables(value, ['FLOAT32'])

    @property
    def regenerationHealth(self):
        return self._regenerationHealth

    @regenerationHealth.setter
    def regenerationHealth(self, value):
        self._regenerationHealth, = unpack_variables(value, ['FLOAT32'])

    @property
    def regeneratedHealth(self):
        return self._regeneratedHealth

    @regeneratedHealth.setter
    def regeneratedHealth(self, value):
        self._regeneratedHealth, = unpack_variables(value, ['FLOAT32'])

    @property
    def burningFlags(self):
        return self._burningFlags

    @burningFlags.setter
    def burningFlags(self, value):
        self._burningFlags, = unpack_variables(value, ['UINT8'])

    @property
    def detonationEnabled(self):
        return self._detonationEnabled

    @detonationEnabled.setter
    def detonationEnabled(self, value):
        self._detonationEnabled, = unpack_variables(value, ['BOOL'])

    @property
    def friendlyFireEnabled(self):
        return self._friendlyFireEnabled

    @friendlyFireEnabled.setter
    def friendlyFireEnabled(self, value):
        self._friendlyFireEnabled, = unpack_variables(value, ['BOOL'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)