#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.Chat import Chat
except:
    from Chat import Chat

try:
    from interfaces.PlayerMessenger_chat2 import PlayerMessenger_chat2
except:
    from PlayerMessenger_chat2 import PlayerMessenger_chat2

try:
    from interfaces.ClientCommandsPort import ClientCommandsPort
except:
    from ClientCommandsPort import ClientCommandsPort

try:
    from interfaces.InvitationsClient import InvitationsClient
except:
    from InvitationsClient import InvitationsClient

try:
    from interfaces.AccountAuthTokenProviderClient import AccountAuthTokenProviderClient
except:
    from AccountAuthTokenProviderClient import AccountAuthTokenProviderClient

try:
    from interfaces.AvatarClientProxy import AvatarClientProxy
except:
    from AvatarClientProxy import AvatarClientProxy

try:
    from interfaces.AvatarObserver import AvatarObserver
except:
    from AvatarObserver import AvatarObserver

try:
    from interfaces.TeamHealthBar_Avatar import TeamHealthBar_Avatar
except:
    from TeamHealthBar_Avatar import TeamHealthBar_Avatar

try:
    from interfaces.ProtectionZoneController_Avatar import ProtectionZoneController_Avatar
except:
    from ProtectionZoneController_Avatar import ProtectionZoneController_Avatar

try:
    from interfaces.RecoveryMechanic_Avatar import RecoveryMechanic_Avatar
except:
    from RecoveryMechanic_Avatar import RecoveryMechanic_Avatar

try:
    from interfaces.DestructibleEntity_Avatar import DestructibleEntity_Avatar
except:
    from DestructibleEntity_Avatar import DestructibleEntity_Avatar

try:
    from interfaces.RespawnController_Avatar import RespawnController_Avatar
except:
    from RespawnController_Avatar import RespawnController_Avatar

try:
    from interfaces.AvatarEpic import AvatarEpic
except:
    from AvatarEpic import AvatarEpic



class Avatar(Chat, PlayerMessenger_chat2, ClientCommandsPort, InvitationsClient, AccountAuthTokenProviderClient, AvatarClientProxy, AvatarObserver, TeamHealthBar_Avatar, ProtectionZoneController_Avatar, RecoveryMechanic_Avatar, DestructibleEntity_Avatar, RespawnController_Avatar, AvatarEpic):
    
    g_update = EventHook()
    
    g_onKickedFromServer = EventHook()
    
    g_onIGRTypeChanged = EventHook()
    
    g_onAutoAimVehicleLost = EventHook()
    
    g_receiveAccountStats = EventHook()
    
    g_updateVehicleHealth = EventHook()
    
    g_updateVehicleGunReloadTime = EventHook()
    
    g_updateVehicleClipReloadTime = EventHook()
    
    g_updateVehicleAmmo = EventHook()
    
    g_onSwitchViewpoint = EventHook()
    
    g_onBootcampEvent = EventHook()
    
    g_updateVehicleOptionalDeviceStatus = EventHook()
    
    g_updateVehicleMiscStatus = EventHook()
    
    g_updateVehicleSetting = EventHook()
    
    g_updateTargetingInfo = EventHook()
    
    g_updateGunMarker = EventHook()
    
    g_updateOwnVehiclePosition = EventHook()
    
    g_showOwnVehicleHitDirection = EventHook()
    
    g_showVehicleDamageInfo = EventHook()
    
    g_showOtherVehicleDamagedDevices = EventHook()
    
    g_showShotResults = EventHook()
    
    g_updatePlaneTrajectory = EventHook()
    
    g_showHittingArea = EventHook()
    
    g_showCarpetBombing = EventHook()
    
    g_showDevelopmentInfo = EventHook()
    
    g_showTracer = EventHook()
    
    g_stopTracer = EventHook()
    
    g_explodeProjectile = EventHook()
    
    g_onRoundFinished = EventHook()
    
    g_onKickedFromArena = EventHook()
    
    g_onBattleEvents = EventHook()
    
    g_battleEventsSummary = EventHook()
    
    g_updateArena = EventHook()
    
    g_updatePositions = EventHook()
    
    g_receivePhysicsDebugInfo = EventHook()
    
    g_updateCarriedFlagPositions = EventHook()
    
    g_receiveNotification = EventHook()
    
    g_onRepairPointAction = EventHook()
    
    g_updateAvatarPrivateStats = EventHook()
    
    g_updateResourceAmount = EventHook()
    
    g_updateGasAttackState = EventHook()
    
    g_syncVehicleAttrs = EventHook()
    
    g_onFrictionWithVehicle = EventHook()
    
    g_onCollisionWithVehicle = EventHook()
    
    g_onSmoke = EventHook()
    
    g_onCombatEquipmentShotLaunched = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._name = None

        self._arenaUniqueID = None

        self._arenaTypeID = None

        self._arenaBonusType = None

        self._arenaGuiType = None

        self._arenaExtraData = None

        self._weatherPresetID = None

        self._denunciationsLeft = None

        self._clientCtx = None

        self._tkillIsSuspected = None

        self._team = None

        self._playerVehicleID = None

        self._isObserverBothTeams = None

        self._isGunLocked = None

        self._ownVehicleGear = None

        self._ownVehicleAuxPhysicsData = None

        self._isHistoricallyAccurate = None


        # MRO fix

        Chat.__init__(self)

        PlayerMessenger_chat2.__init__(self)

        ClientCommandsPort.__init__(self)

        InvitationsClient.__init__(self)

        AccountAuthTokenProviderClient.__init__(self)

        AvatarClientProxy.__init__(self)

        AvatarObserver.__init__(self)

        TeamHealthBar_Avatar.__init__(self)

        ProtectionZoneController_Avatar.__init__(self)

        RecoveryMechanic_Avatar.__init__(self)

        DestructibleEntity_Avatar.__init__(self)

        RespawnController_Avatar.__init__(self)

        AvatarEpic.__init__(self)

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (10000000000, 'name'),
            (64, 'arenaUniqueID'),
            (32, 'arenaTypeID'),
            (8, 'arenaBonusType'),
            (8, 'arenaGuiType'),
            (10000000000, 'arenaExtraData'),
            (8, 'weatherPresetID'),
            (16, 'denunciationsLeft'),
            (10000000000, 'clientCtx'),
            (8, 'tkillIsSuspected'),
            (8, 'team'),
            (32, 'playerVehicleID'),
            (8, 'isObserverBothTeams'),
            (8, 'isGunLocked'),
            (8, 'ownVehicleGear'),
            (64, 'ownVehicleAuxPhysicsData'),
            (8, 'isHistoricallyAccurate'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (10000000000, 'update'),
            (10000000000, 'onKickedFromServer'),
            (10000000000, 'onIGRTypeChanged'),
            (8, 'onAutoAimVehicleLost'),
            (10000000000, 'receiveAccountStats'),
            (72, 'updateVehicleHealth'),
            (96, 'updateVehicleGunReloadTime'),
            (104, 'updateVehicleClipReloadTime'),
            (120, 'updateVehicleAmmo'),
            (128, 'onSwitchViewpoint'),
            (10000000000, 'onBootcampEvent'),
            (48, 'updateVehicleOptionalDeviceStatus'),
            (10000000000, 'updateVehicleMiscStatus'),
            (72, 'updateVehicleSetting'),
            (288, 'updateTargetingInfo'),
            (256, 'updateGunMarker'),
            (256, 'updateOwnVehiclePosition'),
            (168, 'showOwnVehicleHitDirection'),
            (88, 'showVehicleDamageInfo'),
            (10000000000, 'showOtherVehicleDamagedDevices'),
            (10000000000, 'showShotResults'),
            (480, 'updatePlaneTrajectory'),
            (272, 'showHittingArea'),
            (272, 'showCarpetBombing'),
            (10000000000, 'showDevelopmentInfo'),
            (336, 'showTracer'),
            (128, 'stopTracer'),
            (10000000000, 'explodeProjectile'),
            (16, 'onRoundFinished'),
            (8, 'onKickedFromArena'),
            (10000000000, 'onBattleEvents'),
            (264, 'battleEventsSummary'),
            (10000000000, 'updateArena'),
            (10000000000, 'updatePositions'),
            (10000000000, 'receivePhysicsDebugInfo'),
            (10000000000, 'updateCarriedFlagPositions'),
            (10000000000, 'receiveNotification'),
            (48, 'onRepairPointAction'),
            (10000000000, 'updateAvatarPrivateStats'),
            (40, 'updateResourceAmount'),
            (72, 'updateGasAttackState'),
            (16, 'syncVehicleAttrs'),
            (136, 'onFrictionWithVehicle'),
            (128, 'onCollisionWithVehicle'),
            (10000000000, 'onSmoke'),
            (112, 'onCombatEquipmentShotLaunched'),
            
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


    # method size: 10000000000
    @unpack_func_args(['STRING'])
    def update(self, arg1):
        self.g_update.fire(self, arg1)

    # method size: 10000000000
    @unpack_func_args(['STRING', 'BOOL', 'UINT32'])
    def onKickedFromServer(self, arg1, arg2, arg3):
        self.g_onKickedFromServer.fire(self, arg1, arg2, arg3)

    # method size: 10000000000
    @unpack_func_args(['STRING'])
    def onIGRTypeChanged(self, arg1):
        self.g_onIGRTypeChanged.fire(self, arg1)

    # method size: 8
    @unpack_func_args(['UINT8'])
    def onAutoAimVehicleLost(self, arg1):
        self.g_onAutoAimVehicleLost.fire(self, arg1)

    # method size: 10000000000
    @unpack_func_args(['UINT32', 'STRING'])
    def receiveAccountStats(self, arg1, arg2):
        self.g_receiveAccountStats.fire(self, arg1, arg2)

    # method size: 72
    @unpack_func_args(['OBJECT_ID', 'INT16', 'INT8', 'BOOL', 'BOOL'])
    def updateVehicleHealth(self, arg1, arg2, arg3, arg4, arg5):
        self.g_updateVehicleHealth.fire(self, arg1, arg2, arg3, arg4, arg5)

    # method size: 96
    @unpack_func_args(['OBJECT_ID', 'FLOAT32', 'FLOAT32'])
    def updateVehicleGunReloadTime(self, arg1, arg2, arg3):
        self.g_updateVehicleGunReloadTime.fire(self, arg1, arg2, arg3)

    # method size: 104
    @unpack_func_args(['OBJECT_ID', 'FLOAT32', 'FLOAT32', 'BOOL'])
    def updateVehicleClipReloadTime(self, arg1, arg2, arg3, arg4):
        self.g_updateVehicleClipReloadTime.fire(self, arg1, arg2, arg3, arg4)

    # method size: 120
    @unpack_func_args(['OBJECT_ID', 'INT32', 'UINT16', 'UINT8', 'INT16', 'INT16'])
    def updateVehicleAmmo(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_updateVehicleAmmo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    # method size: 128
    @unpack_func_args(['OBJECT_ID', 'VECTOR3'])
    def onSwitchViewpoint(self, arg1, arg2):
        self.g_onSwitchViewpoint.fire(self, arg1, arg2)

    # method size: 10000000000
    @unpack_func_args([['ARRAY', 'UINT64']])
    def onBootcampEvent(self, arg1):
        self.g_onBootcampEvent.fire(self, arg1)

    # method size: 48
    @unpack_func_args(['OBJECT_ID', 'UINT8', 'BOOL'])
    def updateVehicleOptionalDeviceStatus(self, arg1, arg2, arg3):
        self.g_updateVehicleOptionalDeviceStatus.fire(self, arg1, arg2, arg3)

    # method size: 10000000000
    @unpack_func_args(['OBJECT_ID', 'UINT8', 'INT32', ['ARRAY', 'FLOAT32']])
    def updateVehicleMiscStatus(self, arg1, arg2, arg3, arg4):
        self.g_updateVehicleMiscStatus.fire(self, arg1, arg2, arg3, arg4)

    # method size: 72
    @unpack_func_args(['OBJECT_ID', 'UINT8', 'INT32'])
    def updateVehicleSetting(self, arg1, arg2, arg3):
        self.g_updateVehicleSetting.fire(self, arg1, arg2, arg3)

    # method size: 288
    @unpack_func_args(['FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32'])
    def updateTargetingInfo(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_updateTargetingInfo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    # method size: 256
    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'VECTOR3', 'FLOAT32'])
    def updateGunMarker(self, arg1, arg2, arg3, arg4):
        self.g_updateGunMarker.fire(self, arg1, arg2, arg3, arg4)

    # method size: 256
    @unpack_func_args(['VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32'])
    def updateOwnVehiclePosition(self, arg1, arg2, arg3, arg4):
        self.g_updateOwnVehiclePosition.fire(self, arg1, arg2, arg3, arg4)

    # method size: 168
    @unpack_func_args(['FLOAT32', 'OBJECT_ID', 'UINT16', 'UINT32', 'BOOL', 'BOOL', 'OBJECT_ID', 'UINT8'])
    def showOwnVehicleHitDirection(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_showOwnVehicleHitDirection.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    # method size: 88
    @unpack_func_args(['OBJECT_ID', 'UINT8', 'EXTRA_ID', 'OBJECT_ID', 'UINT8'])
    def showVehicleDamageInfo(self, arg1, arg2, arg3, arg4, arg5):
        self.g_showVehicleDamageInfo.fire(self, arg1, arg2, arg3, arg4, arg5)

    # method size: 10000000000
    @unpack_func_args(['OBJECT_ID', ['ARRAY', 'EXTRA_ID'], ['ARRAY', 'EXTRA_ID']])
    def showOtherVehicleDamagedDevices(self, arg1, arg2, arg3):
        self.g_showOtherVehicleDamagedDevices.fire(self, arg1, arg2, arg3)

    # method size: 10000000000
    @unpack_func_args([['ARRAY', 'UINT64']])
    def showShotResults(self, arg1):
        self.g_showShotResults.fire(self, arg1)

    # method size: 480
    @unpack_func_args(['UINT16', 'UINT8', 'FLOAT64', 'VECTOR3', 'VECTOR2', 'FLOAT64', 'VECTOR3', 'VECTOR2', 'BOOL'])
    def updatePlaneTrajectory(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_updatePlaneTrajectory.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    # method size: 272
    @unpack_func_args(['UINT16', 'VECTOR3', 'VECTOR3', 'FLOAT64'])
    def showHittingArea(self, arg1, arg2, arg3, arg4):
        self.g_showHittingArea.fire(self, arg1, arg2, arg3, arg4)

    # method size: 272
    @unpack_func_args(['UINT16', 'VECTOR3', 'VECTOR3', 'FLOAT64'])
    def showCarpetBombing(self, arg1, arg2, arg3, arg4):
        self.g_showCarpetBombing.fire(self, arg1, arg2, arg3, arg4)

    # method size: 10000000000
    @unpack_func_args(['UINT8', 'STRING'])
    def showDevelopmentInfo(self, arg1, arg2):
        self.g_showDevelopmentInfo.fire(self, arg1, arg2)

    # method size: 336
    @unpack_func_args(['OBJECT_ID', 'SHOT_ID', 'BOOL', 'UINT8', 'VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32'])
    def showTracer(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_showTracer.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    # method size: 128
    @unpack_func_args(['SHOT_ID', 'VECTOR3'])
    def stopTracer(self, arg1, arg2):
        self.g_stopTracer.fire(self, arg1, arg2)

    # method size: 10000000000
    @unpack_func_args(['SHOT_ID', 'UINT8', 'UINT8', 'VECTOR3', 'VECTOR3', ['ARRAY', 'UINT32']])
    def explodeProjectile(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_explodeProjectile.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    # method size: 16
    @unpack_func_args(['INT8', 'UINT8'])
    def onRoundFinished(self, arg1, arg2):
        self.g_onRoundFinished.fire(self, arg1, arg2)

    # method size: 8
    @unpack_func_args(['UINT8'])
    def onKickedFromArena(self, arg1):
        self.g_onKickedFromArena.fire(self, arg1)

    # method size: 10000000000
    @unpack_func_args([['ARRAY', 'BATTLE_EVENT']])
    def onBattleEvents(self, arg1):
        self.g_onBattleEvents.fire(self, arg1)

    # method size: 264
    @unpack_func_args(['BATTLE_EVENTS_SUMMARY'])
    def battleEventsSummary(self, arg1):
        self.g_battleEventsSummary.fire(self, arg1)

    # method size: 10000000000
    @unpack_func_args(['UINT8', 'STRING'])
    def updateArena(self, arg1, arg2):
        self.g_updateArena.fire(self, arg1, arg2)

    # method size: 10000000000
    @unpack_func_args([['ARRAY', 'UINT8'], ['ARRAY', 'INT16']])
    def updatePositions(self, arg1, arg2):
        self.g_updatePositions.fire(self, arg1, arg2)

    # method size: 10000000000
    @unpack_func_args(['STRING'])
    def receivePhysicsDebugInfo(self, arg1):
        self.g_receivePhysicsDebugInfo.fire(self, arg1)

    # method size: 10000000000
    @unpack_func_args([['ARRAY', 'UINT8'], ['ARRAY', 'INT16']])
    def updateCarriedFlagPositions(self, arg1, arg2):
        self.g_updateCarriedFlagPositions.fire(self, arg1, arg2)

    # method size: 10000000000
    @unpack_func_args(['STRING'])
    def receiveNotification(self, arg1):
        self.g_receiveNotification.fire(self, arg1)

    # method size: 48
    @unpack_func_args(['UINT8', 'UINT8', 'FLOAT32'])
    def onRepairPointAction(self, arg1, arg2, arg3):
        self.g_onRepairPointAction.fire(self, arg1, arg2, arg3)

    # method size: 10000000000
    @unpack_func_args(['STRING'])
    def updateAvatarPrivateStats(self, arg1):
        self.g_updateAvatarPrivateStats.fire(self, arg1)

    # method size: 40
    @unpack_func_args(['UINT8', 'UINT32'])
    def updateResourceAmount(self, arg1, arg2):
        self.g_updateResourceAmount.fire(self, arg1, arg2)

    # method size: 72
    @unpack_func_args(['UINT8', 'FLOAT32', 'FLOAT32'])
    def updateGasAttackState(self, arg1, arg2, arg3):
        self.g_updateGasAttackState.fire(self, arg1, arg2, arg3)

    # method size: 16
    @unpack_func_args(['VEHICLE_SYNC_ATTRS'])
    def syncVehicleAttrs(self, arg1):
        self.g_syncVehicleAttrs.fire(self, arg1)

    # method size: 136
    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'UINT8'])
    def onFrictionWithVehicle(self, arg1, arg2, arg3):
        self.g_onFrictionWithVehicle.fire(self, arg1, arg2, arg3)

    # method size: 128
    @unpack_func_args(['VECTOR3', 'FLOAT32'])
    def onCollisionWithVehicle(self, arg1, arg2):
        self.g_onCollisionWithVehicle.fire(self, arg1, arg2)

    # method size: 10000000000
    @unpack_func_args([['ARRAY', 'SMOKE_INFO']])
    def onSmoke(self, arg1):
        self.g_onSmoke.fire(self, arg1)

    # method size: 112
    @unpack_func_args(['UINT16', 'VECTOR3'])
    def onCombatEquipmentShotLaunched(self, arg1, arg2):
        self.g_onCombatEquipmentShotLaunched.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################


    # property size: 10000000000
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name, = unpack_variables(value, ['STRING'])

    # property size: 64
    @property
    def arenaUniqueID(self):
        return self._arenaUniqueID

    @arenaUniqueID.setter
    def arenaUniqueID(self, value):
        self._arenaUniqueID, = unpack_variables(value, ['UINT64'])

    # property size: 32
    @property
    def arenaTypeID(self):
        return self._arenaTypeID

    @arenaTypeID.setter
    def arenaTypeID(self, value):
        self._arenaTypeID, = unpack_variables(value, ['INT32'])

    # property size: 8
    @property
    def arenaBonusType(self):
        return self._arenaBonusType

    @arenaBonusType.setter
    def arenaBonusType(self, value):
        self._arenaBonusType, = unpack_variables(value, ['UINT8'])

    # property size: 8
    @property
    def arenaGuiType(self):
        return self._arenaGuiType

    @arenaGuiType.setter
    def arenaGuiType(self, value):
        self._arenaGuiType, = unpack_variables(value, ['UINT8'])

    # property size: 10000000000
    @property
    def arenaExtraData(self):
        return self._arenaExtraData

    @arenaExtraData.setter
    def arenaExtraData(self, value):
        self._arenaExtraData, = unpack_variables(value, ['PYTHON'])

    # property size: 8
    @property
    def weatherPresetID(self):
        return self._weatherPresetID

    @weatherPresetID.setter
    def weatherPresetID(self, value):
        self._weatherPresetID, = unpack_variables(value, ['UINT8'])

    # property size: 16
    @property
    def denunciationsLeft(self):
        return self._denunciationsLeft

    @denunciationsLeft.setter
    def denunciationsLeft(self, value):
        self._denunciationsLeft, = unpack_variables(value, ['INT16'])

    # property size: 10000000000
    @property
    def clientCtx(self):
        return self._clientCtx

    @clientCtx.setter
    def clientCtx(self, value):
        self._clientCtx, = unpack_variables(value, ['STRING'])

    # property size: 8
    @property
    def tkillIsSuspected(self):
        return self._tkillIsSuspected

    @tkillIsSuspected.setter
    def tkillIsSuspected(self, value):
        self._tkillIsSuspected, = unpack_variables(value, ['BOOL'])

    # property size: 8
    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])

    # property size: 32
    @property
    def playerVehicleID(self):
        return self._playerVehicleID

    @playerVehicleID.setter
    def playerVehicleID(self, value):
        self._playerVehicleID, = unpack_variables(value, ['OBJECT_ID'])

    # property size: 8
    @property
    def isObserverBothTeams(self):
        return self._isObserverBothTeams

    @isObserverBothTeams.setter
    def isObserverBothTeams(self, value):
        self._isObserverBothTeams, = unpack_variables(value, ['BOOL'])

    # property size: 8
    @property
    def isGunLocked(self):
        return self._isGunLocked

    @isGunLocked.setter
    def isGunLocked(self, value):
        self._isGunLocked, = unpack_variables(value, ['BOOL'])

    # property size: 8
    @property
    def ownVehicleGear(self):
        return self._ownVehicleGear

    @ownVehicleGear.setter
    def ownVehicleGear(self, value):
        self._ownVehicleGear, = unpack_variables(value, ['UINT8'])

    # property size: 64
    @property
    def ownVehicleAuxPhysicsData(self):
        return self._ownVehicleAuxPhysicsData

    @ownVehicleAuxPhysicsData.setter
    def ownVehicleAuxPhysicsData(self, value):
        self._ownVehicleAuxPhysicsData, = unpack_variables(value, ['UINT64'])

    # property size: 8
    @property
    def isHistoricallyAccurate(self):
        return self._isHistoricallyAccurate

    @isHistoricallyAccurate.setter
    def isHistoricallyAccurate(self, value):
        self._isHistoricallyAccurate, = unpack_variables(value, ['BOOL'])


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)