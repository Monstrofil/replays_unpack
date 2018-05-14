#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

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
    
    g_autoAim = EventHook()
    
    g_moveTo = EventHook()
    
    g_bindToVehicle = EventHook()
    
    g_monitorVehicleDamagedDevices = EventHook()
    
    g_onOwnVehicleStatusChanged = EventHook()
    
    g_allowUnbindingFromVehicle = EventHook()
    
    g_forbidUnbindingFromVehicle = EventHook()
    
    g_fullyDiscloseVehicles = EventHook()
    
    g_receiveVisibilityUpdate = EventHook()
    
    g_receiveVisibilityLists = EventHook()
    
    g_receivePositionsFromArena = EventHook()
    
    g_receiveVehiclePositionFromArena = EventHook()
    
    g_receiveVehicleDamagedDevices = EventHook()
    
    g_lockGunOnClient = EventHook()
    
    g_showShotResults = EventHook()
    
    g_showTracer = EventHook()
    
    g_stopTracer = EventHook()
    
    g_explodeProjectile = EventHook()
    
    g_refreshVehicle = EventHook()
    
    g_activateEquipment = EventHook()
    
    g_setEquipmentApplicationPoint = EventHook()
    
    g_sendFinalStats = EventHook()
    
    g_switchViewPointOrBindToVehicle = EventHook()
    
    g_grantRagePoints = EventHook()
    
    g_harm_receiveAttackResults = EventHook()
    
    g_activateGasAttack = EventHook()
    
    g_pauseMechanics = EventHook()
    
    g_updateOwnVehicleAuxPhysicsDataAndGear = EventHook()
    
    g_sendAmmoStatusToClient = EventHook()
    
    g_kickSelf = EventHook()
    
    g_setClientReady = EventHook()
    
    g_leaveArena = EventHook()
    
    g_unlockUnusedVehicles = EventHook()
    
    g_confirmBattleResultsReceiving = EventHook()
    
    g_makeDenunciation = EventHook()
    
    g_banUnbanUser = EventHook()
    
    g_requestToken = EventHook()
    
    g_banForTKill = EventHook()
    
    g_sendAccountStats = EventHook()
    
    g_setClientCtx = EventHook()
    
    g_updateArena = EventHook()
    
    g_updatePositions = EventHook()
    
    g_showVehicleDamageInfo = EventHook()
    
    g_vehicle_moveWith = EventHook()
    
    g_vehicle_shoot = EventHook()
    
    g_vehicle_trackWorldPointWithGun = EventHook()
    
    g_vehicle_trackRelativePointWithGun = EventHook()
    
    g_vehicle_stopTrackingWithGun = EventHook()
    
    g_vehicle_changeSetting = EventHook()
    
    g_vehicle_teleport = EventHook()
    
    g_vehicle_replenishAmmo = EventHook()
    
    g_createCellNearHere = EventHook()
    
    g_onRemovedFromArena = EventHook()
    
    g_onKickedFromArena = EventHook()
    
    g_onRoundStarted = EventHook()
    
    g_onRoundFinished = EventHook()
    
    g_leaveDisconnected = EventHook()
    
    g_setVehicleDevelopmentFeature = EventHook()
    
    g_setDevelopmentFeature = EventHook()
    
    g_addBotToArena = EventHook()
    
    g_receiveFakeShot = EventHook()
    
    g_logStreamCorruption = EventHook()
    
    g_sendFinalStats = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._state = None

        self._name = None

        self._account = None

        self._playerVehicle = None

        self._arena = None

        self._arenaUniqueID = None

        self._arenaTypeID = None

        self._arenaBonusType = None

        self._arenaGuiType = None

        self._arenaExtraData = None

        self._weatherPresetID = None

        self._denunciationsLeft = None

        self._clientCtx = None

        self._tkillIsSuspected = None

        self._arenaBase = None

        self._team = None

        self._playerVehicleBase = None

        self._playerVehicleID = None

        self._playerVehicleTypeCompDescr = None

        self._isObserverBothTeams = None

        self._isGunLocked = None

        self._ownVehicleGear = None

        self._ownVehicleAuxPhysicsData = None

        self._ammo = None

        self._ammoViews = None

        self._cp = None

        self._historyLoggingFlags = None

        self._heatmapLoggingFlags = None

        self._accountDBIDOnCell = None

        self._arenaUniqueIDOnCell = None

        self._arenaTypeIDOnCell = None

        self._arenaBonusTypeOnCell = None

        self._orderingRoster = None

        self._viewpoints = None

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

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['STRING'])
    def update(self, arg1):
        self.g_update.fire(self, arg1)

    @unpack_func_args(['STRING', 'BOOL', 'UINT32'])
    def onKickedFromServer(self, arg1, arg2, arg3):
        self.g_onKickedFromServer.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING'])
    def onIGRTypeChanged(self, arg1):
        self.g_onIGRTypeChanged.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def onAutoAimVehicleLost(self, arg1):
        self.g_onAutoAimVehicleLost.fire(self, arg1)

    @unpack_func_args(['UINT32', 'STRING'])
    def receiveAccountStats(self, arg1, arg2):
        self.g_receiveAccountStats.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'INT16', 'INT8', 'BOOL', 'BOOL'])
    def updateVehicleHealth(self, arg1, arg2, arg3, arg4, arg5):
        self.g_updateVehicleHealth.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['OBJECT_ID', 'FLOAT32', 'FLOAT32'])
    def updateVehicleGunReloadTime(self, arg1, arg2, arg3):
        self.g_updateVehicleGunReloadTime.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID', 'FLOAT32', 'FLOAT32', 'BOOL'])
    def updateVehicleClipReloadTime(self, arg1, arg2, arg3, arg4):
        self.g_updateVehicleClipReloadTime.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'INT32', 'UINT16', 'UINT8', 'INT16', 'INT16'])
    def updateVehicleAmmo(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_updateVehicleAmmo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['OBJECT_ID', 'VECTOR3'])
    def onSwitchViewpoint(self, arg1, arg2):
        self.g_onSwitchViewpoint.fire(self, arg1, arg2)

    @unpack_func_args([['ARRAY', 'UINT64']])
    def onBootcampEvent(self, arg1):
        self.g_onBootcampEvent.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'BOOL'])
    def updateVehicleOptionalDeviceStatus(self, arg1, arg2, arg3):
        self.g_updateVehicleOptionalDeviceStatus.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'INT32', ['ARRAY', 'FLOAT32']])
    def updateVehicleMiscStatus(self, arg1, arg2, arg3, arg4):
        self.g_updateVehicleMiscStatus.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'INT32'])
    def updateVehicleSetting(self, arg1, arg2, arg3):
        self.g_updateVehicleSetting.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32'])
    def updateTargetingInfo(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_updateTargetingInfo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'VECTOR3', 'FLOAT32'])
    def updateGunMarker(self, arg1, arg2, arg3, arg4):
        self.g_updateGunMarker.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32'])
    def updateOwnVehiclePosition(self, arg1, arg2, arg3, arg4):
        self.g_updateOwnVehiclePosition.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['FLOAT32', 'OBJECT_ID', 'UINT16', 'UINT32', 'BOOL', 'BOOL', 'OBJECT_ID', 'UINT8'])
    def showOwnVehicleHitDirection(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_showOwnVehicleHitDirection.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'EXTRA_ID', 'OBJECT_ID', 'UINT8'])
    def showVehicleDamageInfo(self, arg1, arg2, arg3, arg4, arg5):
        self.g_showVehicleDamageInfo.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['OBJECT_ID', ['ARRAY', 'EXTRA_ID'], ['ARRAY', 'EXTRA_ID']])
    def showOtherVehicleDamagedDevices(self, arg1, arg2, arg3):
        self.g_showOtherVehicleDamagedDevices.fire(self, arg1, arg2, arg3)

    @unpack_func_args([['ARRAY', 'UINT64']])
    def showShotResults(self, arg1):
        self.g_showShotResults.fire(self, arg1)

    @unpack_func_args(['UINT16', 'UINT8', 'FLOAT64', 'VECTOR3', 'VECTOR2', 'FLOAT64', 'VECTOR3', 'VECTOR2', 'BOOL'])
    def updatePlaneTrajectory(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_updatePlaneTrajectory.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['UINT16', 'VECTOR3', 'VECTOR3', 'FLOAT64'])
    def showHittingArea(self, arg1, arg2, arg3, arg4):
        self.g_showHittingArea.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT16', 'VECTOR3', 'VECTOR3', 'FLOAT64'])
    def showCarpetBombing(self, arg1, arg2, arg3, arg4):
        self.g_showCarpetBombing.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'STRING'])
    def showDevelopmentInfo(self, arg1, arg2):
        self.g_showDevelopmentInfo.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'SHOT_ID', 'BOOL', 'UINT8', 'VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32'])
    def showTracer(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_showTracer.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['SHOT_ID', 'VECTOR3'])
    def stopTracer(self, arg1, arg2):
        self.g_stopTracer.fire(self, arg1, arg2)

    @unpack_func_args(['SHOT_ID', 'UINT8', 'UINT8', 'VECTOR3', 'VECTOR3', ['ARRAY', 'UINT32']])
    def explodeProjectile(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_explodeProjectile.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['INT8', 'UINT8'])
    def onRoundFinished(self, arg1, arg2):
        self.g_onRoundFinished.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8'])
    def onKickedFromArena(self, arg1):
        self.g_onKickedFromArena.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'BATTLE_EVENT']])
    def onBattleEvents(self, arg1):
        self.g_onBattleEvents.fire(self, arg1)

    @unpack_func_args(['BATTLE_EVENTS_SUMMARY'])
    def battleEventsSummary(self, arg1):
        self.g_battleEventsSummary.fire(self, arg1)

    @unpack_func_args(['UINT8', 'STRING'])
    def updateArena(self, arg1, arg2):
        self.g_updateArena.fire(self, arg1, arg2)

    @unpack_func_args([['ARRAY', 'UINT8'], ['ARRAY', 'INT16']])
    def updatePositions(self, arg1, arg2):
        self.g_updatePositions.fire(self, arg1, arg2)

    @unpack_func_args(['STRING'])
    def receivePhysicsDebugInfo(self, arg1):
        self.g_receivePhysicsDebugInfo.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'UINT8'], ['ARRAY', 'INT16']])
    def updateCarriedFlagPositions(self, arg1, arg2):
        self.g_updateCarriedFlagPositions.fire(self, arg1, arg2)

    @unpack_func_args(['STRING'])
    def receiveNotification(self, arg1):
        self.g_receiveNotification.fire(self, arg1)

    @unpack_func_args(['UINT8', 'UINT8', 'FLOAT32'])
    def onRepairPointAction(self, arg1, arg2, arg3):
        self.g_onRepairPointAction.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING'])
    def updateAvatarPrivateStats(self, arg1):
        self.g_updateAvatarPrivateStats.fire(self, arg1)

    @unpack_func_args(['UINT8', 'UINT32'])
    def updateResourceAmount(self, arg1, arg2):
        self.g_updateResourceAmount.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'FLOAT32', 'FLOAT32'])
    def updateGasAttackState(self, arg1, arg2, arg3):
        self.g_updateGasAttackState.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['VEHICLE_SYNC_ATTRS'])
    def syncVehicleAttrs(self, arg1):
        self.g_syncVehicleAttrs.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'UINT8'])
    def onFrictionWithVehicle(self, arg1, arg2, arg3):
        self.g_onFrictionWithVehicle.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['VECTOR3', 'FLOAT32'])
    def onCollisionWithVehicle(self, arg1, arg2):
        self.g_onCollisionWithVehicle.fire(self, arg1, arg2)

    @unpack_func_args([['ARRAY', 'SMOKE_INFO']])
    def onSmoke(self, arg1):
        self.g_onSmoke.fire(self, arg1)

    @unpack_func_args(['UINT16', 'VECTOR3'])
    def onCombatEquipmentShotLaunched(self, arg1, arg2):
        self.g_onCombatEquipmentShotLaunched.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID'])
    def autoAim(self, arg1):
        self.g_autoAim.fire(self, arg1)

    @unpack_func_args(['VECTOR3'])
    def moveTo(self, arg1):
        self.g_moveTo.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID'])
    def bindToVehicle(self, arg1):
        self.g_bindToVehicle.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID'])
    def monitorVehicleDamagedDevices(self, arg1):
        self.g_monitorVehicleDamagedDevices.fire(self, arg1)

    @unpack_func_args(['INT8', 'INT8', 'BOOL', 'BOOL'])
    def onOwnVehicleStatusChanged(self, arg1, arg2, arg3, arg4):
        self.g_onOwnVehicleStatusChanged.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args([])
    def allowUnbindingFromVehicle(self):
        self.g_allowUnbindingFromVehicle.fire(self)

    @unpack_func_args(['INT8'])
    def forbidUnbindingFromVehicle(self, arg1):
        self.g_forbidUnbindingFromVehicle.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'OBJECT_ID']])
    def fullyDiscloseVehicles(self, arg1):
        self.g_fullyDiscloseVehicles.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'BOOL', 'BOOL', 'BOOL'])
    def receiveVisibilityUpdate(self, arg1, arg2, arg3, arg4):
        self.g_receiveVisibilityUpdate.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'PYTHON', 'PYTHON'])
    def receiveVisibilityLists(self, arg1, arg2, arg3):
        self.g_receiveVisibilityLists.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['BOOL', ['ARRAY', 'OBJECT_ID'], ['ARRAY', 'UINT8'], ['ARRAY', 'FLOAT32'], ['ARRAY', 'OBJECT_ID'], ['ARRAY', 'BOOL']])
    def receivePositionsFromArena(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_receivePositionsFromArena.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'UINT8'])
    def receiveVehiclePositionFromArena(self, arg1, arg2, arg3):
        self.g_receiveVehiclePositionFromArena.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID', ['ARRAY', 'EXTRA_ID'], ['ARRAY', 'EXTRA_ID']])
    def receiveVehicleDamagedDevices(self, arg1, arg2, arg3):
        self.g_receiveVehicleDamagedDevices.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['BOOL'])
    def lockGunOnClient(self, arg1):
        self.g_lockGunOnClient.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'UINT64']])
    def showShotResults(self, arg1):
        self.g_showShotResults.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'SHOT_ID', 'BOOL', 'BOOL', 'UINT8', 'VECTOR3', 'VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32'])
    def showTracer(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_showTracer.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['SHOT_ID', 'VECTOR3'])
    def stopTracer(self, arg1, arg2):
        self.g_stopTracer.fire(self, arg1, arg2)

    @unpack_func_args(['SHOT_ID', 'UINT8', 'UINT8', 'VECTOR3', 'VECTOR3', ['ARRAY', 'UINT32']])
    def explodeProjectile(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_explodeProjectile.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['UINT16'])
    def refreshVehicle(self, arg1):
        self.g_refreshVehicle.fire(self, arg1)

    @unpack_func_args(['UINT16'])
    def activateEquipment(self, arg1):
        self.g_activateEquipment.fire(self, arg1)

    @unpack_func_args(['UINT16', 'VECTOR3', 'VECTOR2'])
    def setEquipmentApplicationPoint(self, arg1, arg2, arg3):
        self.g_setEquipmentApplicationPoint.fire(self, arg1, arg2, arg3)

    @unpack_func_args([])
    def sendFinalStats(self):
        self.g_sendFinalStats.fire(self)

    @unpack_func_args(['BOOL', 'OBJECT_ID'])
    def switchViewPointOrBindToVehicle(self, arg1, arg2):
        self.g_switchViewPointOrBindToVehicle.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'FLOAT32'])
    def grantRagePoints(self, arg1, arg2):
        self.g_grantRagePoints.fire(self, arg1, arg2)

    @unpack_func_args(['ATTACK_RESULTS'])
    def harm_receiveAttackResults(self, arg1):
        self.g_harm_receiveAttackResults.fire(self, arg1)

    @unpack_func_args(['FLOAT32'])
    def activateGasAttack(self, arg1):
        self.g_activateGasAttack.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def pauseMechanics(self, arg1):
        self.g_pauseMechanics.fire(self, arg1)

    @unpack_func_args(['UINT64', 'UINT8'])
    def updateOwnVehicleAuxPhysicsDataAndGear(self, arg1, arg2):
        self.g_updateOwnVehicleAuxPhysicsDataAndGear.fire(self, arg1, arg2)

    @unpack_func_args([])
    def sendAmmoStatusToClient(self):
        self.g_sendAmmoStatusToClient.fire(self)

    @unpack_func_args(['STRING', 'BOOL', 'FLOAT32'])
    def kickSelf(self, arg1, arg2, arg3):
        self.g_kickSelf.fire(self, arg1, arg2, arg3)

    @unpack_func_args([])
    def setClientReady(self):
        self.g_setClientReady.fire(self)

    @unpack_func_args(['CLIENT_STATISTICS'])
    def leaveArena(self, arg1):
        self.g_leaveArena.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'INT32']])
    def unlockUnusedVehicles(self, arg1):
        self.g_unlockUnusedVehicles.fire(self, arg1)

    @unpack_func_args([])
    def confirmBattleResultsReceiving(self):
        self.g_confirmBattleResultsReceiving.fire(self)

    @unpack_func_args(['DB_ID', 'INT32', 'INT8'])
    def makeDenunciation(self, arg1, arg2, arg3):
        self.g_makeDenunciation.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['DB_ID', 'UINT8', 'UINT32', 'STRING', 'INT8'])
    def banUnbanUser(self, arg1, arg2, arg3, arg4, arg5):
        self.g_banUnbanUser.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT16', 'UINT8'])
    def requestToken(self, arg1, arg2):
        self.g_requestToken.fire(self, arg1, arg2)

    @unpack_func_args([])
    def banForTKill(self):
        self.g_banForTKill.fire(self)

    @unpack_func_args(['UINT32', ['ARRAY', 'STRING']])
    def sendAccountStats(self, arg1, arg2):
        self.g_sendAccountStats.fire(self, arg1, arg2)

    @unpack_func_args(['STRING'])
    def setClientCtx(self, arg1):
        self.g_setClientCtx.fire(self, arg1)

    @unpack_func_args(['UINT8', 'STRING', ['ARRAY', 'DISCLOSE_EVENT']])
    def updateArena(self, arg1, arg2, arg3):
        self.g_updateArena.fire(self, arg1, arg2, arg3)

    @unpack_func_args([['ARRAY', 'OBJECT_ID'], ['ARRAY', 'FLOAT32']])
    def updatePositions(self, arg1, arg2):
        self.g_updatePositions.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'EXTRA_ID', 'OBJECT_ID', 'UINT8'])
    def showVehicleDamageInfo(self, arg1, arg2, arg3, arg4, arg5):
        self.g_showVehicleDamageInfo.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT8'])
    def vehicle_moveWith(self, arg1):
        self.g_vehicle_moveWith.fire(self, arg1)

    @unpack_func_args([])
    def vehicle_shoot(self):
        self.g_vehicle_shoot.fire(self)

    @unpack_func_args(['VECTOR3'])
    def vehicle_trackWorldPointWithGun(self, arg1):
        self.g_vehicle_trackWorldPointWithGun.fire(self, arg1)

    @unpack_func_args(['VECTOR3'])
    def vehicle_trackRelativePointWithGun(self, arg1):
        self.g_vehicle_trackRelativePointWithGun.fire(self, arg1)

    @unpack_func_args(['FLOAT32', 'FLOAT32'])
    def vehicle_stopTrackingWithGun(self, arg1, arg2):
        self.g_vehicle_stopTrackingWithGun.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'INT32'])
    def vehicle_changeSetting(self, arg1, arg2):
        self.g_vehicle_changeSetting.fire(self, arg1, arg2)

    @unpack_func_args(['VECTOR3', 'FLOAT32'])
    def vehicle_teleport(self, arg1, arg2):
        self.g_vehicle_teleport.fire(self, arg1, arg2)

    @unpack_func_args([])
    def vehicle_replenishAmmo(self):
        self.g_vehicle_replenishAmmo.fire(self)

    @unpack_func_args(['MAILBOX'])
    def createCellNearHere(self, arg1):
        self.g_createCellNearHere.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def onRemovedFromArena(self, arg1):
        self.g_onRemovedFromArena.fire(self, arg1)

    @unpack_func_args(['UINT64', 'UINT16'])
    def onKickedFromArena(self, arg1, arg2):
        self.g_onKickedFromArena.fire(self, arg1, arg2)

    @unpack_func_args([])
    def onRoundStarted(self):
        self.g_onRoundStarted.fire(self)

    @unpack_func_args(['INT8', 'UINT8'])
    def onRoundFinished(self, arg1, arg2):
        self.g_onRoundFinished.fire(self, arg1, arg2)

    @unpack_func_args([])
    def leaveDisconnected(self):
        self.g_leaveDisconnected.fire(self)

    @unpack_func_args(['OBJECT_ID', 'STRING', 'INT32', 'STRING'])
    def setVehicleDevelopmentFeature(self, arg1, arg2, arg3, arg4):
        self.g_setVehicleDevelopmentFeature.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['STRING', 'INT32', 'STRING'])
    def setDevelopmentFeature(self, arg1, arg2, arg3):
        self.g_setDevelopmentFeature.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING', 'UINT8', 'STRING'])
    def addBotToArena(self, arg1, arg2, arg3):
        self.g_addBotToArena.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'FLOAT32', 'VECTOR3', 'VECTOR3', 'UINT8'])
    def receiveFakeShot(self, arg1, arg2, arg3, arg4, arg5):
        self.g_receiveFakeShot.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['INT16', 'INT32', 'INT32', 'INT32', 'INT32'])
    def logStreamCorruption(self, arg1, arg2, arg3, arg4, arg5):
        self.g_logStreamCorruption.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args([])
    def sendFinalStats(self):
        self.g_sendFinalStats.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state, = unpack_variables(value, ['UINT16'])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name, = unpack_variables(value, ['STRING'])

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account, = unpack_variables(value, ['MAILBOX'])

    @property
    def playerVehicle(self):
        return self._playerVehicle

    @playerVehicle.setter
    def playerVehicle(self, value):
        self._playerVehicle, = unpack_variables(value, ['MAILBOX'])

    @property
    def arena(self):
        return self._arena

    @arena.setter
    def arena(self, value):
        self._arena, = unpack_variables(value, ['MAILBOX'])

    @property
    def arenaUniqueID(self):
        return self._arenaUniqueID

    @arenaUniqueID.setter
    def arenaUniqueID(self, value):
        self._arenaUniqueID, = unpack_variables(value, ['UINT64'])

    @property
    def arenaTypeID(self):
        return self._arenaTypeID

    @arenaTypeID.setter
    def arenaTypeID(self, value):
        self._arenaTypeID, = unpack_variables(value, ['INT32'])

    @property
    def arenaBonusType(self):
        return self._arenaBonusType

    @arenaBonusType.setter
    def arenaBonusType(self, value):
        self._arenaBonusType, = unpack_variables(value, ['UINT8'])

    @property
    def arenaGuiType(self):
        return self._arenaGuiType

    @arenaGuiType.setter
    def arenaGuiType(self, value):
        self._arenaGuiType, = unpack_variables(value, ['UINT8'])

    @property
    def arenaExtraData(self):
        return self._arenaExtraData

    @arenaExtraData.setter
    def arenaExtraData(self, value):
        self._arenaExtraData, = unpack_variables(value, ['PYTHON'])

    @property
    def weatherPresetID(self):
        return self._weatherPresetID

    @weatherPresetID.setter
    def weatherPresetID(self, value):
        self._weatherPresetID, = unpack_variables(value, ['UINT8'])

    @property
    def denunciationsLeft(self):
        return self._denunciationsLeft

    @denunciationsLeft.setter
    def denunciationsLeft(self, value):
        self._denunciationsLeft, = unpack_variables(value, ['INT16'])

    @property
    def clientCtx(self):
        return self._clientCtx

    @clientCtx.setter
    def clientCtx(self, value):
        self._clientCtx, = unpack_variables(value, ['STRING'])

    @property
    def tkillIsSuspected(self):
        return self._tkillIsSuspected

    @tkillIsSuspected.setter
    def tkillIsSuspected(self, value):
        self._tkillIsSuspected, = unpack_variables(value, ['BOOL'])

    @property
    def arenaBase(self):
        return self._arenaBase

    @arenaBase.setter
    def arenaBase(self, value):
        self._arenaBase, = unpack_variables(value, ['MAILBOX'])

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])

    @property
    def playerVehicleBase(self):
        return self._playerVehicleBase

    @playerVehicleBase.setter
    def playerVehicleBase(self, value):
        self._playerVehicleBase, = unpack_variables(value, ['MAILBOX'])

    @property
    def playerVehicleID(self):
        return self._playerVehicleID

    @playerVehicleID.setter
    def playerVehicleID(self, value):
        self._playerVehicleID, = unpack_variables(value, ['OBJECT_ID'])

    @property
    def playerVehicleTypeCompDescr(self):
        return self._playerVehicleTypeCompDescr

    @playerVehicleTypeCompDescr.setter
    def playerVehicleTypeCompDescr(self, value):
        self._playerVehicleTypeCompDescr, = unpack_variables(value, ['UINT16'])

    @property
    def isObserverBothTeams(self):
        return self._isObserverBothTeams

    @isObserverBothTeams.setter
    def isObserverBothTeams(self, value):
        self._isObserverBothTeams, = unpack_variables(value, ['BOOL'])

    @property
    def isGunLocked(self):
        return self._isGunLocked

    @isGunLocked.setter
    def isGunLocked(self, value):
        self._isGunLocked, = unpack_variables(value, ['BOOL'])

    @property
    def ownVehicleGear(self):
        return self._ownVehicleGear

    @ownVehicleGear.setter
    def ownVehicleGear(self, value):
        self._ownVehicleGear, = unpack_variables(value, ['UINT8'])

    @property
    def ownVehicleAuxPhysicsData(self):
        return self._ownVehicleAuxPhysicsData

    @ownVehicleAuxPhysicsData.setter
    def ownVehicleAuxPhysicsData(self, value):
        self._ownVehicleAuxPhysicsData, = unpack_variables(value, ['UINT64'])

    @property
    def ammo(self):
        return self._ammo

    @ammo.setter
    def ammo(self, value):
        self._ammo, = unpack_variables(value, ['ARRAY', ['INT32']])

    @property
    def ammoViews(self):
        return self._ammoViews

    @ammoViews.setter
    def ammoViews(self, value):
        self._ammoViews, = unpack_variables(value, ['AVATAR_AMMO_VIEWS'])

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp, = unpack_variables(value, ['PYTHON'])

    @property
    def historyLoggingFlags(self):
        return self._historyLoggingFlags

    @historyLoggingFlags.setter
    def historyLoggingFlags(self, value):
        self._historyLoggingFlags, = unpack_variables(value, ['UINT32'])

    @property
    def heatmapLoggingFlags(self):
        return self._heatmapLoggingFlags

    @heatmapLoggingFlags.setter
    def heatmapLoggingFlags(self, value):
        self._heatmapLoggingFlags, = unpack_variables(value, ['UINT32'])

    @property
    def accountDBIDOnCell(self):
        return self._accountDBIDOnCell

    @accountDBIDOnCell.setter
    def accountDBIDOnCell(self, value):
        self._accountDBIDOnCell, = unpack_variables(value, ['DB_ID'])

    @property
    def arenaUniqueIDOnCell(self):
        return self._arenaUniqueIDOnCell

    @arenaUniqueIDOnCell.setter
    def arenaUniqueIDOnCell(self, value):
        self._arenaUniqueIDOnCell, = unpack_variables(value, ['UINT64'])

    @property
    def arenaTypeIDOnCell(self):
        return self._arenaTypeIDOnCell

    @arenaTypeIDOnCell.setter
    def arenaTypeIDOnCell(self, value):
        self._arenaTypeIDOnCell, = unpack_variables(value, ['INT32'])

    @property
    def arenaBonusTypeOnCell(self):
        return self._arenaBonusTypeOnCell

    @arenaBonusTypeOnCell.setter
    def arenaBonusTypeOnCell(self, value):
        self._arenaBonusTypeOnCell, = unpack_variables(value, ['UINT8'])

    @property
    def orderingRoster(self):
        return self._orderingRoster

    @orderingRoster.setter
    def orderingRoster(self, value):
        self._orderingRoster, = unpack_variables(value, ['ARRAY', ['AVATAR_VEHICLE_ROSTER']])

    @property
    def viewpoints(self):
        return self._viewpoints

    @viewpoints.setter
    def viewpoints(self, value):
        self._viewpoints, = unpack_variables(value, ['ARRAY', ['VECTOR3']])

    @property
    def isHistoricallyAccurate(self):
        return self._isHistoricallyAccurate

    @isHistoricallyAccurate.setter
    def isHistoricallyAccurate(self, value):
        self._isHistoricallyAccurate, = unpack_variables(value, ['BOOL'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)