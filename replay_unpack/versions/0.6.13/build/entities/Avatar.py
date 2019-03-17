#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from .interfaces.VoiceChatClient import VoiceChatClient
except:
    from VoiceChatClient import VoiceChatClient

try:
    from .interfaces.StatsPublisher import StatsPublisher
except:
    from StatsPublisher import StatsPublisher



class Avatar(VoiceChatClient, StatsPublisher):
    
    g_onVisibilityChanged = EventHook()
    
    g_receiveVehicleDeath = EventHook()
    
    g_onConnected = EventHook()
    
    g_receiveShellInfo = EventHook()
    
    g_onGameRoomStateChanged = EventHook()
    
    g_onNewPlayerSpawnedInBattle = EventHook()
    
    g_onBattleEnd = EventHook()
    
    g_onBattleInterrupted = EventHook()
    
    g_receiveShotPack = EventHook()
    
    g_receiveProjectileTrace = EventHook()
    
    g_receiveDamageReport = EventHook()
    
    g_targetLoss = EventHook()
    
    g_receive_addSquadron = EventHook()
    
    g_receive_addMinimapSquadron = EventHook()
    
    g_receive_removeMinimapSquadron = EventHook()
    
    g_receive_updateMinimapSquadronPosition = EventHook()
    
    g_receive_setSquadronActive = EventHook()
    
    g_receive_removeSquadron = EventHook()
    
    g_receive_updateSquadron = EventHook()
    
    g_receive_bombDropped = EventHook()
    
    g_receive_planeDeath = EventHook()
    
    g_receive_squadrounOutOfFuel = EventHook()
    
    g_receive_squadronNotify = EventHook()
    
    g_receive_squadronDropBombs = EventHook()
    
    g_receive_assignOrderStatus = EventHook()
    
    g_receive_squadronChangeState = EventHook()
    
    g_receive_squadronPopOrder = EventHook()
    
    g_receive_lastOrdersCanceled = EventHook()
    
    g_receive_cancelOrder = EventHook()
    
    g_receive_squadronAddOrders = EventHook()
    
    g_receive_squadronChangeOrderGoal = EventHook()
    
    g_receive_squadronClearOrders = EventHook()
    
    g_receive_squadronAttackPlaneState = EventHook()
    
    g_receive_squadronUpdatePassiveAura = EventHook()
    
    g_receive_refresh = EventHook()
    
    g_receive_squadronFormation = EventHook()
    
    g_receive_landSquadron = EventHook()
    
    g_receive_targetID = EventHook()
    
    g_receive_prepareBombing = EventHook()
    
    g_receive_startBombing = EventHook()
    
    g_receive_startTorpedo = EventHook()
    
    g_receive_inDefenceChanged = EventHook()
    
    g_battleLogicAction = EventHook()
    
    g_receive_CommonCMD = EventHook()
    
    g_onChatMessage = EventHook()
    
    g_notifyStartAttackPlane = EventHook()
    
    g_notifyStopAttackPlane = EventHook()
    
    g_onShipCollision = EventHook()
    
    g_onEndShipCollision = EventHook()
    
    g_onDisconnectedFromServer = EventHook()
    
    g_onArenaStateReceived = EventHook()
    
    g_receiveChatHistory = EventHook()
    
    g_onCheckGamePing = EventHook()
    
    g_onCheckCellPing = EventHook()
    
    g_updateMinimapVisionInfo = EventHook()
    
    g_onRibbon = EventHook()
    
    g_onWorldStateReceived = EventHook()
    
    g_onAchievementEarned = EventHook()
    
    g_onBattleAchievementsRestored = EventHook()
    
    g_receiveAvatarInfo = EventHook()
    
    g_onEvaluationAccepted = EventHook()
    
    g_artilleryAlert = EventHook()
    
    g_capturedAsAGoal = EventHook()
    
    g_onEnterPreBattle = EventHook()
    
    g_onLeavePreBattle = EventHook()
    
    g_createPreBattle = EventHook()
    
    g_leavePreBattle = EventHook()
    
    g_onOwnerChanged = EventHook()
    
    g_receivePlayerData = EventHook()
    
    g_updatePreBattlesInfo = EventHook()
    
    g_preBattleJoined = EventHook()
    
    g_changePreBattleGrants = EventHook()
    
    g_onActionFailed = EventHook()
    
    g_onShutdownTime = EventHook()
    
    g_onBuildingsDataChanged = EventHook()
    
    g_receiveDamageStat = EventHook()
    
    g_inviteToPreBattle = EventHook()
    
    g_onInviteSent = EventHook()
    
    g_onInviteRevoked = EventHook()
    
    g_onInviteRejected = EventHook()
    
    g_onInviteAccepted = EventHook()
    
    g_rejectInvite = EventHook()
    
    g_updateCoolDown = EventHook()
    
    g_revokeInvite = EventHook()
    
    g_startAppearing = EventHook()
    
    g_startDissapearing = EventHook()
    
    g_setIntuitionAngle = EventHook()
    
    g_hideIntuitionIndicator = EventHook()
    
    g_ownSmokeCreated = EventHook()
    
    g_clientInsideSmoke = EventHook()
    
    g_vehicleLeaveSmoke = EventHook()
    
    g_notifyAboutSmokePenalty = EventHook()
    
    g_ownSmokeStartsFade = EventHook()
    
    g_ownSmokeTimeLifeChanges = EventHook()
    
    g_useConsumable = EventHook()
    
    g_updateFov = EventHook()
    
    g_switchTorpedoState = EventHook()
    
    g_setSelectedWeapon = EventHook()
    
    g_setArtilleryAmmo = EventHook()
    
    g_shootTorpedoes = EventHook()
    
    g_shootGuns = EventHook()
    
    g_shootGunsSalvo = EventHook()
    
    g_dontShootGuns = EventHook()
    
    g_forceTorpedoesReload = EventHook()
    
    g_moveTo = EventHook()
    
    g_updateMovFlags = EventHook()
    
    g_setWeaponLock = EventHook()
    
    g_updateWeaponTargetPos = EventHook()
    
    g_setCruiseControl = EventHook()
    
    g_setRudderAngle = EventHook()
    
    g_switchATBA = EventHook()
    
    g_assignOrder = EventHook()
    
    g_changeOrderGoal = EventHook()
    
    g_squadronRemoveOrder = EventHook()
    
    g_cancelAllOrders = EventHook()
    
    g_onClientReady = EventHook()
    
    g_dev_switchIdealGunHack = EventHook()
    
    g_dev_switchIdealATBASelectedGunId = EventHook()
    
    g_dev_setFloatCellAppData = EventHook()
    
    g_dev_setFloatShipParam = EventHook()
    
    g_dev_recreatePhysics = EventHook()
    
    g_dev_bot_spawnSplashAtShootPos = EventHook()
    
    g_checkGamePing = EventHook()
    
    g_dev_setDeathParams = EventHook()
    
    g_dev_killEntity = EventHook()
    
    g_dev_setPhysicParams = EventHook()
    
    g_leaveBattle = EventHook()
    
    g_makeEvaluation = EventHook()
    
    g_cmdBindToVehicle = EventHook()
    
    g_cmdSetVision = EventHook()
    
    g_send_CommonCMD = EventHook()
    
    g_onClientLoaded = EventHook()
    
    g_chatMessage = EventHook()
    
    g_checkGamePing = EventHook()
    
    g_addBan = EventHook()
    
    g_removeBan = EventHook()
    
    g_dev_earnAchievementInBattle = EventHook()
    
    g_dev_spawnBot = EventHook()
    
    g_createPreBattle = EventHook()
    
    g_joinPreBattle = EventHook()
    
    g_onLeavePreBattle = EventHook()
    
    g_leavePreBattle = EventHook()
    
    g_touchAccount = EventHook()
    
    g_lock = EventHook()
    
    g_unlock = EventHook()
    
    g_dismiss = EventHook()
    
    g_changeOwner = EventHook()
    
    g_kick = EventHook()
    
    g_quitPreBattle = EventHook()
    
    g_onBecomePlayer = EventHook()
    
    g_cmdI2 = EventHook()
    
    g_cmdI1 = EventHook()
    
    g_requestRejectInvite = EventHook()
    
    g_sendInvite = EventHook()
    
    g_setInvitationsEnabled = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._ownShipId = 0.0

        self._useATBAandAirDefense = 0.0

        self._vehiclePosition = None

        self._teamId = None

        self._isBattleStopped = 1.0

        self._selectedWeapon = 0.0

        self._isFlyMode = None

        self._intuitionActive = None

        self._attrs = 0.0

        self._isInOfflineMode = None

        self._minefields = None


        # MRO fix

        VoiceChatClient.__init__(self)

        StatsPublisher.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8'])
    def onVisibilityChanged(self, arg1):
        self.g_onVisibilityChanged.fire(self, arg1)

    @unpack_func_args(['ENTITY_ID', 'ENTITY_ID', 'UINT32'])
    def receiveVehicleDeath(self, arg1, arg2, arg3):
        self.g_receiveVehicleDeath.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING'])
    def onConnected(self, arg1):
        self.g_onConnected.fire(self, arg1)

    @unpack_func_args(['GAMEPARAMS_ID', 'UINT32', 'UINT32', 'ENTITY_ID', 'UINT32', 'UINT32', 'UINT32', 'UINT8', 'UINT8', 'INT16', ['ARRAY', 'UINT32']])
    def receiveShellInfo(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_receiveShellInfo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['BLOB'])
    def onGameRoomStateChanged(self, arg1):
        self.g_onGameRoomStateChanged.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def onNewPlayerSpawnedInBattle(self, arg1):
        self.g_onNewPlayerSpawnedInBattle.fire(self, arg1)

    @unpack_func_args(['TEAM_ID', 'UINT8'])
    def onBattleEnd(self, arg1, arg2):
        self.g_onBattleEnd.fire(self, arg1, arg2)

    @unpack_func_args([])
    def onBattleInterrupted(self):
        self.g_onBattleInterrupted.fire(self)

    @unpack_func_args([['ARRAY', 'SHOT'], ['ARRAY', 'TORPEDOSHOT'], ['ARRAY', 'SHOTKILL'], ['ARRAY', 'EXPLOSION']])
    def receiveShotPack(self, arg1, arg2, arg3, arg4):
        self.g_receiveShotPack.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'BLOB', 'ENTITY_ID', 'BOOL'])
    def receiveProjectileTrace(self, arg1, arg2, arg3, arg4):
        self.g_receiveProjectileTrace.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['BLOB', 'INT16', 'BOOL'])
    def receiveDamageReport(self, arg1, arg2, arg3):
        self.g_receiveDamageReport.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT16'])
    def targetLoss(self, arg1, arg2):
        self.g_targetLoss.fire(self, arg1, arg2)

    @unpack_func_args(['GAMEPARAMS_ID', 'UINT8', 'SQUADRON_STATE'])
    def receive_addSquadron(self, arg1, arg2, arg3):
        self.g_receive_addSquadron.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['PLANE_ID', 'TEAM_ID', 'GAMEPARAMS_ID', 'VECTOR3'])
    def receive_addMinimapSquadron(self, arg1, arg2, arg3, arg4):
        self.g_receive_addMinimapSquadron.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['PLANE_ID'])
    def receive_removeMinimapSquadron(self, arg1):
        self.g_receive_removeMinimapSquadron.fire(self, arg1)

    @unpack_func_args(['PLANE_ID', 'VECTOR3'])
    def receive_updateMinimapSquadronPosition(self, arg1, arg2):
        self.g_receive_updateMinimapSquadronPosition.fire(self, arg1, arg2)

    @unpack_func_args(['SQUADRON_STATE'])
    def receive_setSquadronActive(self, arg1):
        self.g_receive_setSquadronActive.fire(self, arg1)

    @unpack_func_args(['PLANE_ID'])
    def receive_removeSquadron(self, arg1):
        self.g_receive_removeSquadron.fire(self, arg1)

    @unpack_func_args(['PLANE_ID', 'FLOAT', 'PLANE_PATH'])
    def receive_updateSquadron(self, arg1, arg2, arg3):
        self.g_receive_updateSquadron.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['PLANE_ID'])
    def receive_bombDropped(self, arg1):
        self.g_receive_bombDropped.fire(self, arg1)

    @unpack_func_args(['PLANE_ID', 'UINT8', 'INT64'])
    def receive_planeDeath(self, arg1, arg2, arg3):
        self.g_receive_planeDeath.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['PLANE_ID'])
    def receive_squadrounOutOfFuel(self, arg1):
        self.g_receive_squadrounOutOfFuel.fire(self, arg1)

    @unpack_func_args(['INT8', 'INT8'])
    def receive_squadronNotify(self, arg1, arg2):
        self.g_receive_squadronNotify.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'VECTOR3', 'VECTOR3'])
    def receive_squadronDropBombs(self, arg1, arg2, arg3):
        self.g_receive_squadronDropBombs.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT8', 'INT8', 'BOOL'])
    def receive_assignOrderStatus(self, arg1, arg2, arg3):
        self.g_receive_assignOrderStatus.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT8', 'INT8'])
    def receive_squadronChangeState(self, arg1, arg2):
        self.g_receive_squadronChangeState.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'INT8'])
    def receive_squadronPopOrder(self, arg1, arg2):
        self.g_receive_squadronPopOrder.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'UINT8'])
    def receive_lastOrdersCanceled(self, arg1, arg2):
        self.g_receive_lastOrdersCanceled.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'UINT8'])
    def receive_cancelOrder(self, arg1, arg2):
        self.g_receive_cancelOrder.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', ['ARRAY', 'ORDER_DEF']])
    def receive_squadronAddOrders(self, arg1, arg2):
        self.g_receive_squadronAddOrders.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'UINT8', 'GOAL_DEF'])
    def receive_squadronChangeOrderGoal(self, arg1, arg2, arg3):
        self.g_receive_squadronChangeOrderGoal.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT8', 'INT8'])
    def receive_squadronClearOrders(self, arg1, arg2):
        self.g_receive_squadronClearOrders.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'FLOAT', 'FLOAT'])
    def receive_squadronAttackPlaneState(self, arg1, arg2, arg3):
        self.g_receive_squadronAttackPlaneState.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['PLANE_ID', 'BOOL'])
    def receive_squadronUpdatePassiveAura(self, arg1, arg2):
        self.g_receive_squadronUpdatePassiveAura.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB'])
    def receive_refresh(self, arg1):
        self.g_receive_refresh.fire(self, arg1)

    @unpack_func_args(['PLANE_ID', 'INT32'])
    def receive_squadronFormation(self, arg1, arg2):
        self.g_receive_squadronFormation.fire(self, arg1, arg2)

    @unpack_func_args(['PLANE_ID'])
    def receive_landSquadron(self, arg1):
        self.g_receive_landSquadron.fire(self, arg1)

    @unpack_func_args(['PLANE_ID', 'PLANE_ID', 'BOOL'])
    def receive_targetID(self, arg1, arg2, arg3):
        self.g_receive_targetID.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['PLANE_ID', 'BOOL', 'BOOL', ['ARRAY', 'VECTOR3']])
    def receive_prepareBombing(self, arg1, arg2, arg3, arg4):
        self.g_receive_prepareBombing.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['PLANE_ID', 'VECTOR3'])
    def receive_startBombing(self, arg1, arg2):
        self.g_receive_startBombing.fire(self, arg1, arg2)

    @unpack_func_args(['PLANE_ID', 'BOOL', 'BOOL', ['ARRAY', 'VECTOR3']])
    def receive_startTorpedo(self, arg1, arg2, arg3, arg4):
        self.g_receive_startTorpedo.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'UINT8'])
    def receive_inDefenceChanged(self, arg1, arg2):
        self.g_receive_inDefenceChanged.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB'])
    def battleLogicAction(self, arg1):
        self.g_battleLogicAction.fire(self, arg1)

    @unpack_func_args(['BOOL', 'PLAYER_ID', 'UINT8', 'UINT32', 'UINT64'])
    def receive_CommonCMD(self, arg1, arg2, arg3, arg4, arg5):
        self.g_receive_CommonCMD.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['ENTITY_ID', 'STRING', 'STRING', 'STRING'])
    def onChatMessage(self, arg1, arg2, arg3, arg4):
        self.g_onChatMessage.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT8', 'TARGET_ID', 'INT8'])
    def notifyStartAttackPlane(self, arg1, arg2, arg3):
        self.g_notifyStartAttackPlane.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT8', 'TARGET_ID', 'INT8'])
    def notifyStopAttackPlane(self, arg1, arg2, arg3):
        self.g_notifyStopAttackPlane.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['ENTITY_ID', 'VECTOR3', 'FLOAT'])
    def onShipCollision(self, arg1, arg2, arg3):
        self.g_onShipCollision.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['ENTITY_ID'])
    def onEndShipCollision(self, arg1):
        self.g_onEndShipCollision.fire(self, arg1)

    @unpack_func_args(['UINT32', 'UINT8'])
    def onDisconnectedFromServer(self, arg1, arg2):
        self.g_onDisconnectedFromServer.fire(self, arg1, arg2)

    @unpack_func_args(['ARENA_STATE'])
    def onArenaStateReceived(self, arg1):
        self.g_onArenaStateReceived.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def receiveChatHistory(self, arg1):
        self.g_receiveChatHistory.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def onCheckCellPing(self, arg1):
        self.g_onCheckCellPing.fire(self, arg1)

    @unpack_func_args(['MINIMAPINFO', 'MINIMAPINFO'])
    def updateMinimapVisionInfo(self, arg1, arg2):
        self.g_updateMinimapVisionInfo.fire(self, arg1, arg2)

    @unpack_func_args(['INT8'])
    def onRibbon(self, arg1):
        self.g_onRibbon.fire(self, arg1)

    @unpack_func_args([])
    def onWorldStateReceived(self):
        self.g_onWorldStateReceived.fire(self)

    @unpack_func_args(['ENTITY_ID', 'UINT32'])
    def onAchievementEarned(self, arg1, arg2):
        self.g_onAchievementEarned.fire(self, arg1, arg2)

    @unpack_func_args([['ARRAY', 'UINT32']])
    def onBattleAchievementsRestored(self, arg1):
        self.g_onBattleAchievementsRestored.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def receiveAvatarInfo(self, arg1):
        self.g_receiveAvatarInfo.fire(self, arg1)

    @unpack_func_args(['UINT8', 'INT8'])
    def onEvaluationAccepted(self, arg1, arg2):
        self.g_onEvaluationAccepted.fire(self, arg1, arg2)

    @unpack_func_args(['ENTITY_ID'])
    def artilleryAlert(self, arg1):
        self.g_artilleryAlert.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def capturedAsAGoal(self, arg1):
        self.g_capturedAsAGoal.fire(self, arg1)

    @unpack_func_args(['BLOB', 'INT32', 'BOOL'])
    def onEnterPreBattle(self, arg1, arg2, arg3):
        self.g_onEnterPreBattle.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT8'])
    def onLeavePreBattle(self, arg1, arg2):
        self.g_onLeavePreBattle.fire(self, arg1, arg2)

    @unpack_func_args([])
    def createPreBattle(self):
        self.g_createPreBattle.fire(self)

    @unpack_func_args([])
    def leavePreBattle(self):
        self.g_leavePreBattle.fire(self)

    @unpack_func_args(['PLAYER_ID', 'BOOL'])
    def onOwnerChanged(self, arg1, arg2):
        self.g_onOwnerChanged.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB', 'BOOL'])
    def receivePlayerData(self, arg1, arg2):
        self.g_receivePlayerData.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB'])
    def updatePreBattlesInfo(self, arg1):
        self.g_updatePreBattlesInfo.fire(self, arg1)

    @unpack_func_args([])
    def preBattleJoined(self):
        self.g_preBattleJoined.fire(self)

    @unpack_func_args(['INT32'])
    def changePreBattleGrants(self, arg1):
        self.g_changePreBattleGrants.fire(self, arg1)

    @unpack_func_args(['INT16', 'INT16'])
    def onActionFailed(self, arg1, arg2):
        self.g_onActionFailed.fire(self, arg1, arg2)

    @unpack_func_args(['UINT32', 'UINT32', 'BOOL'])
    def onShutdownTime(self, arg1, arg2, arg3):
        self.g_onShutdownTime.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['BLOB'])
    def onBuildingsDataChanged(self, arg1):
        self.g_onBuildingsDataChanged.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def receiveDamageStat(self, arg1):
        self.g_receiveDamageStat.fire(self, arg1)

    @unpack_func_args(['PRE_BATTLE_INVITE_DEF'])
    def inviteToPreBattle(self, arg1):
        self.g_inviteToPreBattle.fire(self, arg1)

    @unpack_func_args(['INT8', 'DB_ID', 'STRING', 'UNICODE_STRING'])
    def onInviteSent(self, arg1, arg2, arg3, arg4):
        self.g_onInviteSent.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT8', 'PLAYER_ID'])
    def onInviteRevoked(self, arg1, arg2):
        self.g_onInviteRevoked.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'OBJECT_ID'])
    def onInviteRejected(self, arg1, arg2):
        self.g_onInviteRejected.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'OBJECT_ID'])
    def onInviteAccepted(self, arg1, arg2):
        self.g_onInviteAccepted.fire(self, arg1, arg2)

    @unpack_func_args(['PLAYER_ID', 'INT8', 'STRING', 'UNICODE_STRING'])
    def rejectInvite(self, arg1, arg2, arg3, arg4):
        self.g_rejectInvite.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['BLOB'])
    def updateCoolDown(self, arg1):
        self.g_updateCoolDown.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'UINT8'])
    def revokeInvite(self, arg1, arg2):
        self.g_revokeInvite.fire(self, arg1, arg2)

    @unpack_func_args(['ENTITY_ID'])
    def startAppearing(self, arg1):
        self.g_startAppearing.fire(self, arg1)

    @unpack_func_args(['ENTITY_ID'])
    def startDissapearing(self, arg1):
        self.g_startDissapearing.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def setIntuitionAngle(self, arg1):
        self.g_setIntuitionAngle.fire(self, arg1)

    @unpack_func_args([])
    def hideIntuitionIndicator(self):
        self.g_hideIntuitionIndicator.fire(self)

    @unpack_func_args(['FLOAT'])
    def ownSmokeCreated(self, arg1):
        self.g_ownSmokeCreated.fire(self, arg1)

    @unpack_func_args(['FLOAT'])
    def clientInsideSmoke(self, arg1):
        self.g_clientInsideSmoke.fire(self, arg1)

    @unpack_func_args([])
    def vehicleLeaveSmoke(self):
        self.g_vehicleLeaveSmoke.fire(self)

    @unpack_func_args([])
    def notifyAboutSmokePenalty(self):
        self.g_notifyAboutSmokePenalty.fire(self)

    @unpack_func_args([])
    def ownSmokeStartsFade(self):
        self.g_ownSmokeStartsFade.fire(self)

    @unpack_func_args(['BOOL', 'FLOAT'])
    def ownSmokeTimeLifeChanges(self, arg1, arg2):
        self.g_ownSmokeTimeLifeChanges.fire(self, arg1, arg2)

    @unpack_func_args(['INT8'])
    def useConsumable(self, arg1):
        self.g_useConsumable.fire(self, arg1)

    @unpack_func_args(['FLOAT'])
    def updateFov(self, arg1):
        self.g_updateFov.fire(self, arg1)

    @unpack_func_args(['UINT16', 'UINT16'])
    def switchTorpedoState(self, arg1, arg2):
        self.g_switchTorpedoState.fire(self, arg1, arg2)

    @unpack_func_args(['INT32'])
    def setSelectedWeapon(self, arg1):
        self.g_setSelectedWeapon.fire(self, arg1)

    @unpack_func_args(['INT32'])
    def setArtilleryAmmo(self, arg1):
        self.g_setArtilleryAmmo.fire(self, arg1)

    @unpack_func_args(['UINT32'])
    def shootTorpedoes(self, arg1):
        self.g_shootTorpedoes.fire(self, arg1)

    @unpack_func_args([])
    def shootGuns(self):
        self.g_shootGuns.fire(self)

    @unpack_func_args([])
    def shootGunsSalvo(self):
        self.g_shootGunsSalvo.fire(self)

    @unpack_func_args([])
    def dontShootGuns(self):
        self.g_dontShootGuns.fire(self)

    @unpack_func_args([])
    def forceTorpedoesReload(self):
        self.g_forceTorpedoesReload.fire(self)

    @unpack_func_args(['VECTOR3'])
    def moveTo(self, arg1):
        self.g_moveTo.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def updateMovFlags(self, arg1):
        self.g_updateMovFlags.fire(self, arg1)

    @unpack_func_args(['INT8', 'INT8', 'TARGET_ID', 'VECTOR3'])
    def setWeaponLock(self, arg1, arg2, arg3, arg4):
        self.g_setWeaponLock.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['VECTOR3', 'INT8'])
    def updateWeaponTargetPos(self, arg1, arg2):
        self.g_updateWeaponTargetPos.fire(self, arg1, arg2)

    @unpack_func_args(['FLOAT'])
    def setCruiseControl(self, arg1):
        self.g_setCruiseControl.fire(self, arg1)

    @unpack_func_args(['FLOAT'])
    def setRudderAngle(self, arg1):
        self.g_setRudderAngle.fire(self, arg1)

    @unpack_func_args([])
    def switchATBA(self):
        self.g_switchATBA.fire(self)

    @unpack_func_args(['INT8', 'INT8', 'GOAL_DEF', 'BOOL'])
    def assignOrder(self, arg1, arg2, arg3, arg4):
        self.g_assignOrder.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT8', 'UINT8', 'GOAL_DEF'])
    def changeOrderGoal(self, arg1, arg2, arg3):
        self.g_changeOrderGoal.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT8', 'UINT8'])
    def squadronRemoveOrder(self, arg1, arg2):
        self.g_squadronRemoveOrder.fire(self, arg1, arg2)

    @unpack_func_args(['INT8'])
    def cancelAllOrders(self, arg1):
        self.g_cancelAllOrders.fire(self, arg1)

    @unpack_func_args([])
    def onClientReady(self):
        self.g_onClientReady.fire(self)

    @unpack_func_args(['UINT8'])
    def dev_switchIdealGunHack(self, arg1):
        self.g_dev_switchIdealGunHack.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def dev_switchIdealATBASelectedGunId(self, arg1):
        self.g_dev_switchIdealATBASelectedGunId.fire(self, arg1)

    @unpack_func_args(['STRING', 'FLOAT'])
    def dev_setFloatCellAppData(self, arg1, arg2):
        self.g_dev_setFloatCellAppData.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB', 'FLOAT'])
    def dev_setFloatShipParam(self, arg1, arg2):
        self.g_dev_setFloatShipParam.fire(self, arg1, arg2)

    @unpack_func_args(['FLOAT'])
    def dev_recreatePhysics(self, arg1):
        self.g_dev_recreatePhysics.fire(self, arg1)

    @unpack_func_args([])
    def dev_bot_spawnSplashAtShootPos(self):
        self.g_dev_bot_spawnSplashAtShootPos.fire(self)

    @unpack_func_args(['UINT64'])
    def checkGamePing(self, arg1):
        self.g_checkGamePing.fire(self, arg1)

    @unpack_func_args(['STRING', 'FLOAT'])
    def dev_setDeathParams(self, arg1, arg2):
        self.g_dev_setDeathParams.fire(self, arg1, arg2)

    @unpack_func_args(['ENTITY_ID'])
    def dev_killEntity(self, arg1):
        self.g_dev_killEntity.fire(self, arg1)

    @unpack_func_args(['STRING', 'FLOAT'])
    def dev_setPhysicParams(self, arg1, arg2):
        self.g_dev_setPhysicParams.fire(self, arg1, arg2)

    @unpack_func_args([])
    def leaveBattle(self):
        self.g_leaveBattle.fire(self)

    @unpack_func_args(['UINT8', 'PLAYER_ID', 'UINT8'])
    def makeEvaluation(self, arg1, arg2, arg3):
        self.g_makeEvaluation.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['PLAYER_ID'])
    def cmdBindToVehicle(self, arg1):
        self.g_cmdBindToVehicle.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'INT32']])
    def cmdSetVision(self, arg1):
        self.g_cmdSetVision.fire(self, arg1)

    @unpack_func_args(['BOOL', 'UINT8', 'UINT32', 'UINT64'])
    def send_CommonCMD(self, arg1, arg2, arg3, arg4):
        self.g_send_CommonCMD.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args([])
    def onClientLoaded(self):
        self.g_onClientLoaded.fire(self)

    @unpack_func_args(['STRING', 'STRING'])
    def chatMessage(self, arg1, arg2):
        self.g_chatMessage.fire(self, arg1, arg2)

    @unpack_func_args(['UINT64'])
    def checkGamePing(self, arg1):
        self.g_checkGamePing.fire(self, arg1)

    @unpack_func_args(['UINT16', 'UINT32', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING'])
    def addBan(self, arg1, arg2, arg3, arg4, arg5):
        self.g_addBan.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT16', 'UNICODE_STRING', 'UNICODE_STRING'])
    def removeBan(self, arg1, arg2, arg3):
        self.g_removeBan.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT32'])
    def dev_earnAchievementInBattle(self, arg1):
        self.g_dev_earnAchievementInBattle.fire(self, arg1)

    @unpack_func_args(['STRING', 'UINT8', 'INT16', 'INT16', 'INT16', 'UINT16', 'STRING', 'STRING'])
    def dev_spawnBot(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_dev_spawnBot.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args([])
    def createPreBattle(self):
        self.g_createPreBattle.fire(self)

    @unpack_func_args(['UINT32', 'UINT32'])
    def joinPreBattle(self, arg1, arg2):
        self.g_joinPreBattle.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'UINT8'])
    def onLeavePreBattle(self, arg1, arg2):
        self.g_onLeavePreBattle.fire(self, arg1, arg2)

    @unpack_func_args([])
    def leavePreBattle(self):
        self.g_leavePreBattle.fire(self)

    @unpack_func_args([])
    def touchAccount(self):
        self.g_touchAccount.fire(self)

    @unpack_func_args([])
    def lock(self):
        self.g_lock.fire(self)

    @unpack_func_args([])
    def unlock(self):
        self.g_unlock.fire(self)

    @unpack_func_args([])
    def dismiss(self):
        self.g_dismiss.fire(self)

    @unpack_func_args(['UINT32'])
    def changeOwner(self, arg1):
        self.g_changeOwner.fire(self, arg1)

    @unpack_func_args(['UINT32'])
    def kick(self, arg1):
        self.g_kick.fire(self, arg1)

    @unpack_func_args([])
    def quitPreBattle(self):
        self.g_quitPreBattle.fire(self)

    @unpack_func_args([])
    def onBecomePlayer(self):
        self.g_onBecomePlayer.fire(self)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT64'])
    def cmdI2(self, arg1, arg2, arg3, arg4):
        self.g_cmdI2.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64'])
    def cmdI1(self, arg1, arg2, arg3):
        self.g_cmdI1.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT64'])
    def requestRejectInvite(self, arg1):
        self.g_requestRejectInvite.fire(self, arg1)

    @unpack_func_args(['UINT32'])
    def sendInvite(self, arg1):
        self.g_sendInvite.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def setInvitationsEnabled(self, arg1):
        self.g_setInvitationsEnabled.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def ownShipId(self):
        return self._ownShipId

    @ownShipId.setter
    def ownShipId(self, value):
        self._ownShipId, = unpack_variables(value, ['ENTITY_ID'])

    @property
    def useATBAandAirDefense(self):
        return self._useATBAandAirDefense

    @useATBAandAirDefense.setter
    def useATBAandAirDefense(self, value):
        self._useATBAandAirDefense, = unpack_variables(value, ['BOOL'])

    @property
    def vehiclePosition(self):
        return self._vehiclePosition

    @vehiclePosition.setter
    def vehiclePosition(self, value):
        self._vehiclePosition, = unpack_variables(value, ['VECTOR3'])

    @property
    def teamId(self):
        return self._teamId

    @teamId.setter
    def teamId(self, value):
        self._teamId, = unpack_variables(value, ['TEAM_ID'])

    @property
    def isBattleStopped(self):
        return self._isBattleStopped

    @isBattleStopped.setter
    def isBattleStopped(self, value):
        self._isBattleStopped, = unpack_variables(value, ['BOOL'])

    @property
    def selectedWeapon(self):
        return self._selectedWeapon

    @selectedWeapon.setter
    def selectedWeapon(self, value):
        self._selectedWeapon, = unpack_variables(value, ['UINT32'])

    @property
    def isFlyMode(self):
        return self._isFlyMode

    @isFlyMode.setter
    def isFlyMode(self, value):
        self._isFlyMode, = unpack_variables(value, ['BOOL'])

    @property
    def intuitionActive(self):
        return self._intuitionActive

    @intuitionActive.setter
    def intuitionActive(self, value):
        self._intuitionActive, = unpack_variables(value, ['INT8'])

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        self._attrs, = unpack_variables(value, ['UINT64'])

    @property
    def isInOfflineMode(self):
        return self._isInOfflineMode

    @isInOfflineMode.setter
    def isInOfflineMode(self, value):
        self._isInOfflineMode, = unpack_variables(value, ['BOOL'])

    @property
    def minefields(self):
        return self._minefields

    @minefields.setter
    def minefields(self, value):
        self._minefields, = unpack_variables(value, [['ARRAY', 'MINEFIELD_STATE']])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)
