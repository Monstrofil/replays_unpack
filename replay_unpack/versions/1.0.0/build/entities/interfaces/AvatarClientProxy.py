#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AvatarClientProxy(object):
    
    g_avatarClientProxy_updateOwnVehiclePosition = EventHook()
    
    g_avatarClientProxy_updateGunMarker = EventHook()
    
    g_avatarClientProxy_updateVehicleHealth = EventHook()
    
    g_avatarClientProxy_updateVehicleGunReloadTime = EventHook()
    
    g_avatarClientProxy_updateVehicleClipReloadTime = EventHook()
    
    g_avatarClientProxy_updateVehicleAmmo = EventHook()
    
    g_avatarClientProxy_updateVehicleOptionalDeviceStatus = EventHook()
    
    g_avatarClientProxy_updateVehicleMiscStatus = EventHook()
    
    g_avatarClientProxy_updateVehicleSetting = EventHook()
    
    g_avatarClientProxy_updateTargetingInfo = EventHook()
    
    g_avatarClientProxy_showOwnVehicleHitDirection = EventHook()
    
    g_avatarClientProxy_showShotResults = EventHook()
    
    g_avatarClientProxy_updatePlaneTrajectory = EventHook()
    
    g_avatarClientProxy_showHittingArea = EventHook()
    
    g_avatarClientProxy_showCarpetBombing = EventHook()
    
    g_avatarClientProxy_syncVehicleAttrs = EventHook()
    
    g_avatarClientProxy_showDevelopmentInfo = EventHook()
    
    g_avatarClientProxy_onBattleEvents = EventHook()
    
    g_avatarClientProxy_battleEventsSummary = EventHook()
    
    g_avatarClientProxy_welcomeToSector = EventHook()
    
    g_avatarClientProxy_onSectorShooting = EventHook()
    
    g_avatarClientProxy_onXPUpdated = EventHook()
    
    g_avatarClientProxy_onSmoke = EventHook()
    
    g_avatarClientProxy_onCombatEquipmentShotLaunched = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32'])
    def avatarClientProxy_updateOwnVehiclePosition(self, arg1, arg2, arg3, arg4):
        self.g_avatarClientProxy_updateOwnVehiclePosition.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'VECTOR3', 'FLOAT32'])
    def avatarClientProxy_updateGunMarker(self, arg1, arg2, arg3, arg4):
        self.g_avatarClientProxy_updateGunMarker.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'INT16', 'INT8', 'BOOL', 'BOOL'])
    def avatarClientProxy_updateVehicleHealth(self, arg1, arg2, arg3, arg4, arg5):
        self.g_avatarClientProxy_updateVehicleHealth.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['OBJECT_ID', 'FLOAT32', 'FLOAT32'])
    def avatarClientProxy_updateVehicleGunReloadTime(self, arg1, arg2, arg3):
        self.g_avatarClientProxy_updateVehicleGunReloadTime.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID', 'FLOAT32', 'FLOAT32', 'BOOL'])
    def avatarClientProxy_updateVehicleClipReloadTime(self, arg1, arg2, arg3, arg4):
        self.g_avatarClientProxy_updateVehicleClipReloadTime.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'INT32', 'UINT16', 'UINT16', 'INT16', 'INT16'])
    def avatarClientProxy_updateVehicleAmmo(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_avatarClientProxy_updateVehicleAmmo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'BOOL'])
    def avatarClientProxy_updateVehicleOptionalDeviceStatus(self, arg1, arg2, arg3):
        self.g_avatarClientProxy_updateVehicleOptionalDeviceStatus.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'INT32', ['ARRAY', 'FLOAT32']])
    def avatarClientProxy_updateVehicleMiscStatus(self, arg1, arg2, arg3, arg4):
        self.g_avatarClientProxy_updateVehicleMiscStatus.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'INT32'])
    def avatarClientProxy_updateVehicleSetting(self, arg1, arg2, arg3):
        self.g_avatarClientProxy_updateVehicleSetting.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32'])
    def avatarClientProxy_updateTargetingInfo(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_avatarClientProxy_updateTargetingInfo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['FLOAT32', 'OBJECT_ID', 'UINT16', 'UINT32', 'BOOL', 'BOOL', 'OBJECT_ID', 'UINT8'])
    def avatarClientProxy_showOwnVehicleHitDirection(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_avatarClientProxy_showOwnVehicleHitDirection.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args([['ARRAY', 'UINT64']])
    def avatarClientProxy_showShotResults(self, arg1):
        self.g_avatarClientProxy_showShotResults.fire(self, arg1)

    @unpack_func_args(['UINT16', 'UINT8', 'FLOAT64', 'VECTOR3', 'VECTOR2', 'FLOAT64', 'VECTOR3', 'VECTOR2', 'BOOL'])
    def avatarClientProxy_updatePlaneTrajectory(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_avatarClientProxy_updatePlaneTrajectory.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['UINT16', 'VECTOR3', 'VECTOR3', 'FLOAT64'])
    def avatarClientProxy_showHittingArea(self, arg1, arg2, arg3, arg4):
        self.g_avatarClientProxy_showHittingArea.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT16', 'VECTOR3', 'VECTOR3', 'FLOAT64'])
    def avatarClientProxy_showCarpetBombing(self, arg1, arg2, arg3, arg4):
        self.g_avatarClientProxy_showCarpetBombing.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['VEHICLE_SYNC_ATTRS'])
    def avatarClientProxy_syncVehicleAttrs(self, arg1):
        self.g_avatarClientProxy_syncVehicleAttrs.fire(self, arg1)

    @unpack_func_args(['UINT8', 'STRING'])
    def avatarClientProxy_showDevelopmentInfo(self, arg1, arg2):
        self.g_avatarClientProxy_showDevelopmentInfo.fire(self, arg1, arg2)

    @unpack_func_args([['ARRAY', 'BATTLE_EVENT']])
    def avatarClientProxy_onBattleEvents(self, arg1):
        self.g_avatarClientProxy_onBattleEvents.fire(self, arg1)

    @unpack_func_args(['BATTLE_EVENTS_SUMMARY'])
    def avatarClientProxy_battleEventsSummary(self, arg1):
        self.g_avatarClientProxy_battleEventsSummary.fire(self, arg1)

    @unpack_func_args(['UINT8', 'UINT8', 'UINT8', 'BOOL', 'FLOAT32', 'FLOAT32'])
    def avatarClientProxy_welcomeToSector(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_avatarClientProxy_welcomeToSector.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['UINT8'])
    def avatarClientProxy_onSectorShooting(self, arg1):
        self.g_avatarClientProxy_onSectorShooting.fire(self, arg1)

    @unpack_func_args(['INT16'])
    def avatarClientProxy_onXPUpdated(self, arg1):
        self.g_avatarClientProxy_onXPUpdated.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'SMOKE_INFO']])
    def avatarClientProxy_onSmoke(self, arg1):
        self.g_avatarClientProxy_onSmoke.fire(self, arg1)

    @unpack_func_args(['UINT16', 'VECTOR3'])
    def avatarClientProxy_onCombatEquipmentShotLaunched(self, arg1, arg2):
        self.g_avatarClientProxy_onCombatEquipmentShotLaunched.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)