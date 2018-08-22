#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from interfaces.VoiceChatClient import VoiceChatClient
from interfaces.StatsPublisher import StatsPublisher



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

        self._weatherParams = None

        self._privateBattleLogicState = None


        # MRO fix

        VoiceChatClient.__init__(self)

        StatsPublisher.__init__(self)

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (32, 'ownShipId'),
            (8, 'useATBAandAirDefense'),
            (96, 'vehiclePosition'),
            (8, 'teamId'),
            (8, 'isBattleStopped'),
            (32, 'selectedWeapon'),
            (8, 'isFlyMode'),
            (8, 'intuitionActive'),
            (64, 'attrs'),
            (8, 'isInOfflineMode'),
            (10000000000, 'minefields'),
            (576, 'weatherParams'),
            (10000000000, 'privateBattleLogicState'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (9, 'onVisibilityChanged'),
            (97, 'receiveVehicleDeath'),
            (10000000001, 'onConnected'),
            (10000000001, 'receiveShellInfo'),
            (10000000002, 'onGameRoomStateChanged'),
            (10000000001, 'onNewPlayerSpawnedInBattle'),
            (17, 'onBattleEnd'),
            (1, 'onBattleInterrupted'),
            (10000000002, 'receiveShotPack'),
            (10000000001, 'receiveProjectileTrace'),
            (10000000002, 'receiveDamageReport'),
            (25, 'targetLoss'),
            (273, 'receive_addSquadron'),
            (201, 'receive_addMinimapSquadron'),
            (65, 'receive_removeMinimapSquadron'),
            (161, 'receive_updateMinimapSquadronPosition'),
            (233, 'receive_setSquadronActive'),
            (65, 'receive_removeSquadron'),
            (10000000001, 'receive_updateSquadron'),
            (65, 'receive_bombDropped'),
            (137, 'receive_planeDeath'),
            (65, 'receive_squadrounOutOfFuel'),
            (17, 'receive_squadronNotify'),
            (201, 'receive_squadronDropBombs'),
            (25, 'receive_assignOrderStatus'),
            (17, 'receive_squadronChangeState'),
            (17, 'receive_squadronPopOrder'),
            (17, 'receive_lastOrdersCanceled'),
            (17, 'receive_cancelOrder'),
            (10000000001, 'receive_squadronAddOrders'),
            (10000000001, 'receive_squadronChangeOrderGoal'),
            (17, 'receive_squadronClearOrders'),
            (73, 'receive_squadronAttackPlaneState'),
            (73, 'receive_squadronUpdatePassiveAura'),
            (10000000001, 'receive_refresh'),
            (97, 'receive_squadronFormation'),
            (65, 'receive_landSquadron'),
            (137, 'receive_targetID'),
            (10000000001, 'receive_prepareBombing'),
            (161, 'receive_startBombing'),
            (10000000001, 'receive_startTorpedo'),
            (41, 'receive_inDefenceChanged'),
            (10000000002, 'battleLogicAction'),
            (145, 'receive_CommonCMD'),
            (10000000001, 'onChatMessage'),
            (81, 'notifyStartAttackPlane'),
            (81, 'notifyStopAttackPlane'),
            (161, 'onShipCollision'),
            (33, 'onEndShipCollision'),
            (41, 'onDisconnectedFromServer'),
            (10000000002, 'onArenaStateReceived'),
            (10000000001, 'receiveChatHistory'),
            (65, 'onCheckGamePing'),
            (65, 'onCheckCellPing'),
            (10000000001, 'updateMinimapVisionInfo'),
            (9, 'onRibbon'),
            (1, 'onWorldStateReceived'),
            (65, 'onAchievementEarned'),
            (10000000001, 'onBattleAchievementsRestored'),
            (10000000001, 'receiveAvatarInfo'),
            (17, 'onEvaluationAccepted'),
            (33, 'artilleryAlert'),
            (9, 'capturedAsAGoal'),
            (10000000002, 'onEnterPreBattle'),
            (17, 'onLeavePreBattle'),
            (1, 'createPreBattle'),
            (1, 'leavePreBattle'),
            (41, 'onOwnerChanged'),
            (10000000002, 'receivePlayerData'),
            (10000000001, 'updatePreBattlesInfo'),
            (1, 'preBattleJoined'),
            (33, 'changePreBattleGrants'),
            (33, 'onActionFailed'),
            (73, 'onShutdownTime'),
            (10000000001, 'onBuildingsDataChanged'),
            (10000000001, 'receiveDamageStat'),
            (10000000001, 'inviteToPreBattle'),
            (10000000001, 'onInviteSent'),
            (41, 'onInviteRevoked'),
            (41, 'onInviteRejected'),
            (41, 'onInviteAccepted'),
            (10000000001, 'rejectInvite'),
            (10000000001, 'updateCoolDown'),
            (41, 'revokeInvite'),
            (33, 'startAppearing'),
            (33, 'startDissapearing'),
            (9, 'setIntuitionAngle'),
            (1, 'hideIntuitionIndicator'),
            (33, 'ownSmokeCreated'),
            (33, 'clientInsideSmoke'),
            (1, 'vehicleLeaveSmoke'),
            (1, 'notifyAboutSmokePenalty'),
            (1, 'ownSmokeStartsFade'),
            (41, 'ownSmokeTimeLifeChanges'),
            
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

# method size: 9
    @unpack_func_args(['UINT8'])
    def onVisibilityChanged(self, arg1):
        self.g_onVisibilityChanged.fire(self, arg1)
# method size: 97
    @unpack_func_args(['ENTITY_ID', 'ENTITY_ID', 'UINT32'])
    def receiveVehicleDeath(self, arg1, arg2, arg3):
        self.g_receiveVehicleDeath.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def onConnected(self, arg1):
        self.g_onConnected.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['GAMEPARAMS_ID', 'UINT32', 'UINT32', 'ENTITY_ID', 'UINT32', 'UINT32', 'UINT32', 'UINT8', 'UINT8', 'INT16', ['ARRAY', 'UINT32']])
    def receiveShellInfo(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_receiveShellInfo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)
# method size: 10000000002
    @unpack_func_args(['BLOB'])
    def onGameRoomStateChanged(self, arg1):
        self.g_onGameRoomStateChanged.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def onNewPlayerSpawnedInBattle(self, arg1):
        self.g_onNewPlayerSpawnedInBattle.fire(self, arg1)
# method size: 17
    @unpack_func_args(['TEAM_ID', 'UINT8'])
    def onBattleEnd(self, arg1, arg2):
        self.g_onBattleEnd.fire(self, arg1, arg2)
# method size: 1
    @unpack_func_args([])
    def onBattleInterrupted(self):
        self.g_onBattleInterrupted.fire(self)
# method size: 10000000002
    @unpack_func_args([['ARRAY', 'SHOT'], ['ARRAY', 'TORPEDOSHOT'], ['ARRAY', 'SHOTKILL'], ['ARRAY', 'EXPLOSION']])
    def receiveShotPack(self, arg1, arg2, arg3, arg4):
        self.g_receiveShotPack.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000001
    @unpack_func_args(['INT32', 'BLOB', 'ENTITY_ID', 'BOOL'])
    def receiveProjectileTrace(self, arg1, arg2, arg3, arg4):
        self.g_receiveProjectileTrace.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000002
    @unpack_func_args(['BLOB', 'INT16', 'BOOL'])
    def receiveDamageReport(self, arg1, arg2, arg3):
        self.g_receiveDamageReport.fire(self, arg1, arg2, arg3)
# method size: 25
    @unpack_func_args(['UINT8', 'UINT16'])
    def targetLoss(self, arg1, arg2):
        self.g_targetLoss.fire(self, arg1, arg2)
# method size: 273
    @unpack_func_args(['GAMEPARAMS_ID', 'UINT8', 'SQUADRON_STATE'])
    def receive_addSquadron(self, arg1, arg2, arg3):
        self.g_receive_addSquadron.fire(self, arg1, arg2, arg3)
# method size: 201
    @unpack_func_args(['PLANE_ID', 'TEAM_ID', 'GAMEPARAMS_ID', 'VECTOR3'])
    def receive_addMinimapSquadron(self, arg1, arg2, arg3, arg4):
        self.g_receive_addMinimapSquadron.fire(self, arg1, arg2, arg3, arg4)
# method size: 65
    @unpack_func_args(['PLANE_ID'])
    def receive_removeMinimapSquadron(self, arg1):
        self.g_receive_removeMinimapSquadron.fire(self, arg1)
# method size: 161
    @unpack_func_args(['PLANE_ID', 'VECTOR3'])
    def receive_updateMinimapSquadronPosition(self, arg1, arg2):
        self.g_receive_updateMinimapSquadronPosition.fire(self, arg1, arg2)
# method size: 233
    @unpack_func_args(['SQUADRON_STATE'])
    def receive_setSquadronActive(self, arg1):
        self.g_receive_setSquadronActive.fire(self, arg1)
# method size: 65
    @unpack_func_args(['PLANE_ID'])
    def receive_removeSquadron(self, arg1):
        self.g_receive_removeSquadron.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['PLANE_ID', 'FLOAT', 'PLANE_PATH'])
    def receive_updateSquadron(self, arg1, arg2, arg3):
        self.g_receive_updateSquadron.fire(self, arg1, arg2, arg3)
# method size: 65
    @unpack_func_args(['PLANE_ID'])
    def receive_bombDropped(self, arg1):
        self.g_receive_bombDropped.fire(self, arg1)
# method size: 137
    @unpack_func_args(['PLANE_ID', 'UINT8', 'INT64'])
    def receive_planeDeath(self, arg1, arg2, arg3):
        self.g_receive_planeDeath.fire(self, arg1, arg2, arg3)
# method size: 65
    @unpack_func_args(['PLANE_ID'])
    def receive_squadrounOutOfFuel(self, arg1):
        self.g_receive_squadrounOutOfFuel.fire(self, arg1)
# method size: 17
    @unpack_func_args(['INT8', 'INT8'])
    def receive_squadronNotify(self, arg1, arg2):
        self.g_receive_squadronNotify.fire(self, arg1, arg2)
# method size: 201
    @unpack_func_args(['INT8', 'VECTOR3', 'VECTOR3'])
    def receive_squadronDropBombs(self, arg1, arg2, arg3):
        self.g_receive_squadronDropBombs.fire(self, arg1, arg2, arg3)
# method size: 25
    @unpack_func_args(['INT8', 'INT8', 'BOOL'])
    def receive_assignOrderStatus(self, arg1, arg2, arg3):
        self.g_receive_assignOrderStatus.fire(self, arg1, arg2, arg3)
# method size: 17
    @unpack_func_args(['INT8', 'INT8'])
    def receive_squadronChangeState(self, arg1, arg2):
        self.g_receive_squadronChangeState.fire(self, arg1, arg2)
# method size: 17
    @unpack_func_args(['INT8', 'INT8'])
    def receive_squadronPopOrder(self, arg1, arg2):
        self.g_receive_squadronPopOrder.fire(self, arg1, arg2)
# method size: 17
    @unpack_func_args(['INT8', 'UINT8'])
    def receive_lastOrdersCanceled(self, arg1, arg2):
        self.g_receive_lastOrdersCanceled.fire(self, arg1, arg2)
# method size: 17
    @unpack_func_args(['INT8', 'UINT8'])
    def receive_cancelOrder(self, arg1, arg2):
        self.g_receive_cancelOrder.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['INT8', ['ARRAY', 'ORDER_DEF']])
    def receive_squadronAddOrders(self, arg1, arg2):
        self.g_receive_squadronAddOrders.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['INT8', 'UINT8', 'GOAL_DEF'])
    def receive_squadronChangeOrderGoal(self, arg1, arg2, arg3):
        self.g_receive_squadronChangeOrderGoal.fire(self, arg1, arg2, arg3)
# method size: 17
    @unpack_func_args(['INT8', 'INT8'])
    def receive_squadronClearOrders(self, arg1, arg2):
        self.g_receive_squadronClearOrders.fire(self, arg1, arg2)
# method size: 73
    @unpack_func_args(['INT8', 'FLOAT', 'FLOAT'])
    def receive_squadronAttackPlaneState(self, arg1, arg2, arg3):
        self.g_receive_squadronAttackPlaneState.fire(self, arg1, arg2, arg3)
# method size: 73
    @unpack_func_args(['PLANE_ID', 'BOOL'])
    def receive_squadronUpdatePassiveAura(self, arg1, arg2):
        self.g_receive_squadronUpdatePassiveAura.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receive_refresh(self, arg1):
        self.g_receive_refresh.fire(self, arg1)
# method size: 97
    @unpack_func_args(['PLANE_ID', 'INT32'])
    def receive_squadronFormation(self, arg1, arg2):
        self.g_receive_squadronFormation.fire(self, arg1, arg2)
# method size: 65
    @unpack_func_args(['PLANE_ID'])
    def receive_landSquadron(self, arg1):
        self.g_receive_landSquadron.fire(self, arg1)
# method size: 137
    @unpack_func_args(['PLANE_ID', 'PLANE_ID', 'BOOL'])
    def receive_targetID(self, arg1, arg2, arg3):
        self.g_receive_targetID.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['PLANE_ID', 'BOOL', 'BOOL', ['ARRAY', 'VECTOR3']])
    def receive_prepareBombing(self, arg1, arg2, arg3, arg4):
        self.g_receive_prepareBombing.fire(self, arg1, arg2, arg3, arg4)
# method size: 161
    @unpack_func_args(['PLANE_ID', 'VECTOR3'])
    def receive_startBombing(self, arg1, arg2):
        self.g_receive_startBombing.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['PLANE_ID', 'BOOL', 'BOOL', ['ARRAY', 'VECTOR3']])
    def receive_startTorpedo(self, arg1, arg2, arg3, arg4):
        self.g_receive_startTorpedo.fire(self, arg1, arg2, arg3, arg4)
# method size: 41
    @unpack_func_args(['INT32', 'UINT8'])
    def receive_inDefenceChanged(self, arg1, arg2):
        self.g_receive_inDefenceChanged.fire(self, arg1, arg2)
# method size: 10000000002
    @unpack_func_args(['BLOB'])
    def battleLogicAction(self, arg1):
        self.g_battleLogicAction.fire(self, arg1)
# method size: 145
    @unpack_func_args(['BOOL', 'PLAYER_ID', 'UINT8', 'UINT32', 'UINT64'])
    def receive_CommonCMD(self, arg1, arg2, arg3, arg4, arg5):
        self.g_receive_CommonCMD.fire(self, arg1, arg2, arg3, arg4, arg5)
# method size: 10000000001
    @unpack_func_args(['ENTITY_ID', 'STRING', 'STRING', 'STRING'])
    def onChatMessage(self, arg1, arg2, arg3, arg4):
        self.g_onChatMessage.fire(self, arg1, arg2, arg3, arg4)
# method size: 81
    @unpack_func_args(['INT8', 'TARGET_ID', 'INT8'])
    def notifyStartAttackPlane(self, arg1, arg2, arg3):
        self.g_notifyStartAttackPlane.fire(self, arg1, arg2, arg3)
# method size: 81
    @unpack_func_args(['INT8', 'TARGET_ID', 'INT8'])
    def notifyStopAttackPlane(self, arg1, arg2, arg3):
        self.g_notifyStopAttackPlane.fire(self, arg1, arg2, arg3)
# method size: 161
    @unpack_func_args(['ENTITY_ID', 'VECTOR3', 'FLOAT'])
    def onShipCollision(self, arg1, arg2, arg3):
        self.g_onShipCollision.fire(self, arg1, arg2, arg3)
# method size: 33
    @unpack_func_args(['ENTITY_ID'])
    def onEndShipCollision(self, arg1):
        self.g_onEndShipCollision.fire(self, arg1)
# method size: 41
    @unpack_func_args(['UINT32', 'UINT8'])
    def onDisconnectedFromServer(self, arg1, arg2):
        self.g_onDisconnectedFromServer.fire(self, arg1, arg2)
# method size: 10000000002
    @unpack_func_args(['ARENA_STATE'])
    def onArenaStateReceived(self, arg1):
        self.g_onArenaStateReceived.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receiveChatHistory(self, arg1):
        self.g_receiveChatHistory.fire(self, arg1)
# method size: 65
    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)
# method size: 65
    @unpack_func_args(['UINT64'])
    def onCheckCellPing(self, arg1):
        self.g_onCheckCellPing.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['MINIMAPINFO', 'MINIMAPINFO'])
    def updateMinimapVisionInfo(self, arg1, arg2):
        self.g_updateMinimapVisionInfo.fire(self, arg1, arg2)
# method size: 9
    @unpack_func_args(['INT8'])
    def onRibbon(self, arg1):
        self.g_onRibbon.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def onWorldStateReceived(self):
        self.g_onWorldStateReceived.fire(self)
# method size: 65
    @unpack_func_args(['ENTITY_ID', 'UINT32'])
    def onAchievementEarned(self, arg1, arg2):
        self.g_onAchievementEarned.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args([['ARRAY', 'UINT32']])
    def onBattleAchievementsRestored(self, arg1):
        self.g_onBattleAchievementsRestored.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receiveAvatarInfo(self, arg1):
        self.g_receiveAvatarInfo.fire(self, arg1)
# method size: 17
    @unpack_func_args(['UINT8', 'INT8'])
    def onEvaluationAccepted(self, arg1, arg2):
        self.g_onEvaluationAccepted.fire(self, arg1, arg2)
# method size: 33
    @unpack_func_args(['ENTITY_ID'])
    def artilleryAlert(self, arg1):
        self.g_artilleryAlert.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def capturedAsAGoal(self, arg1):
        self.g_capturedAsAGoal.fire(self, arg1)
# method size: 10000000002
    @unpack_func_args(['BLOB', 'INT32', 'BOOL'])
    def onEnterPreBattle(self, arg1, arg2, arg3):
        self.g_onEnterPreBattle.fire(self, arg1, arg2, arg3)
# method size: 17
    @unpack_func_args(['UINT8', 'UINT8'])
    def onLeavePreBattle(self, arg1, arg2):
        self.g_onLeavePreBattle.fire(self, arg1, arg2)
# method size: 1
    @unpack_func_args([])
    def createPreBattle(self):
        self.g_createPreBattle.fire(self)
# method size: 1
    @unpack_func_args([])
    def leavePreBattle(self):
        self.g_leavePreBattle.fire(self)
# method size: 41
    @unpack_func_args(['PLAYER_ID', 'BOOL'])
    def onOwnerChanged(self, arg1, arg2):
        self.g_onOwnerChanged.fire(self, arg1, arg2)
# method size: 10000000002
    @unpack_func_args(['BLOB', 'BOOL'])
    def receivePlayerData(self, arg1, arg2):
        self.g_receivePlayerData.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def updatePreBattlesInfo(self, arg1):
        self.g_updatePreBattlesInfo.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def preBattleJoined(self):
        self.g_preBattleJoined.fire(self)
# method size: 33
    @unpack_func_args(['INT32'])
    def changePreBattleGrants(self, arg1):
        self.g_changePreBattleGrants.fire(self, arg1)
# method size: 33
    @unpack_func_args(['INT16', 'INT16'])
    def onActionFailed(self, arg1, arg2):
        self.g_onActionFailed.fire(self, arg1, arg2)
# method size: 73
    @unpack_func_args(['UINT32', 'UINT32', 'BOOL'])
    def onShutdownTime(self, arg1, arg2, arg3):
        self.g_onShutdownTime.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def onBuildingsDataChanged(self, arg1):
        self.g_onBuildingsDataChanged.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receiveDamageStat(self, arg1):
        self.g_receiveDamageStat.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['PRE_BATTLE_INVITE_DEF'])
    def inviteToPreBattle(self, arg1):
        self.g_inviteToPreBattle.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['INT8', 'DB_ID', 'STRING', 'UNICODE_STRING'])
    def onInviteSent(self, arg1, arg2, arg3, arg4):
        self.g_onInviteSent.fire(self, arg1, arg2, arg3, arg4)
# method size: 41
    @unpack_func_args(['INT8', 'PLAYER_ID'])
    def onInviteRevoked(self, arg1, arg2):
        self.g_onInviteRevoked.fire(self, arg1, arg2)
# method size: 41
    @unpack_func_args(['INT8', 'OBJECT_ID'])
    def onInviteRejected(self, arg1, arg2):
        self.g_onInviteRejected.fire(self, arg1, arg2)
# method size: 41
    @unpack_func_args(['INT8', 'OBJECT_ID'])
    def onInviteAccepted(self, arg1, arg2):
        self.g_onInviteAccepted.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['PLAYER_ID', 'INT8', 'STRING', 'UNICODE_STRING'])
    def rejectInvite(self, arg1, arg2, arg3, arg4):
        self.g_rejectInvite.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def updateCoolDown(self, arg1):
        self.g_updateCoolDown.fire(self, arg1)
# method size: 41
    @unpack_func_args(['OBJECT_ID', 'UINT8'])
    def revokeInvite(self, arg1, arg2):
        self.g_revokeInvite.fire(self, arg1, arg2)
# method size: 33
    @unpack_func_args(['ENTITY_ID'])
    def startAppearing(self, arg1):
        self.g_startAppearing.fire(self, arg1)
# method size: 33
    @unpack_func_args(['ENTITY_ID'])
    def startDissapearing(self, arg1):
        self.g_startDissapearing.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def setIntuitionAngle(self, arg1):
        self.g_setIntuitionAngle.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def hideIntuitionIndicator(self):
        self.g_hideIntuitionIndicator.fire(self)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def ownSmokeCreated(self, arg1):
        self.g_ownSmokeCreated.fire(self, arg1)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def clientInsideSmoke(self, arg1):
        self.g_clientInsideSmoke.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def vehicleLeaveSmoke(self):
        self.g_vehicleLeaveSmoke.fire(self)
# method size: 1
    @unpack_func_args([])
    def notifyAboutSmokePenalty(self):
        self.g_notifyAboutSmokePenalty.fire(self)
# method size: 1
    @unpack_func_args([])
    def ownSmokeStartsFade(self):
        self.g_ownSmokeStartsFade.fire(self)
# method size: 41
    @unpack_func_args(['BOOL', 'FLOAT'])
    def ownSmokeTimeLifeChanges(self, arg1, arg2):
        self.g_ownSmokeTimeLifeChanges.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 32
    @property
    def ownShipId(self):
        return self._ownShipId

    @ownShipId.setter
    def ownShipId(self, value):
        self._ownShipId, = unpack_variables(value, ['ENTITY_ID'])
# property size: 8
    @property
    def useATBAandAirDefense(self):
        return self._useATBAandAirDefense

    @useATBAandAirDefense.setter
    def useATBAandAirDefense(self, value):
        self._useATBAandAirDefense, = unpack_variables(value, ['BOOL'])
# property size: 96
    @property
    def vehiclePosition(self):
        return self._vehiclePosition

    @vehiclePosition.setter
    def vehiclePosition(self, value):
        self._vehiclePosition, = unpack_variables(value, ['VECTOR3'])
# property size: 8
    @property
    def teamId(self):
        return self._teamId

    @teamId.setter
    def teamId(self, value):
        self._teamId, = unpack_variables(value, ['TEAM_ID'])
# property size: 8
    @property
    def isBattleStopped(self):
        return self._isBattleStopped

    @isBattleStopped.setter
    def isBattleStopped(self, value):
        self._isBattleStopped, = unpack_variables(value, ['BOOL'])
# property size: 32
    @property
    def selectedWeapon(self):
        return self._selectedWeapon

    @selectedWeapon.setter
    def selectedWeapon(self, value):
        self._selectedWeapon, = unpack_variables(value, ['UINT32'])
# property size: 8
    @property
    def isFlyMode(self):
        return self._isFlyMode

    @isFlyMode.setter
    def isFlyMode(self, value):
        self._isFlyMode, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def intuitionActive(self):
        return self._intuitionActive

    @intuitionActive.setter
    def intuitionActive(self, value):
        self._intuitionActive, = unpack_variables(value, ['INT8'])
# property size: 64
    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        self._attrs, = unpack_variables(value, ['UINT64'])
# property size: 8
    @property
    def isInOfflineMode(self):
        return self._isInOfflineMode

    @isInOfflineMode.setter
    def isInOfflineMode(self, value):
        self._isInOfflineMode, = unpack_variables(value, ['BOOL'])
# property size: 10000000000
    @property
    def minefields(self):
        return self._minefields

    @minefields.setter
    def minefields(self, value):
        self._minefields, = unpack_variables(value, [['ARRAY', 'MINEFIELD_STATE']])
# property size: 576
    @property
    def weatherParams(self):
        return self._weatherParams

    @weatherParams.setter
    def weatherParams(self, value):
        self._weatherParams, = unpack_variables(value, ['WEATHER_LOGIC_PARAMS'])
# property size: 10000000000
    @property
    def privateBattleLogicState(self):
        return self._privateBattleLogicState

    @privateBattleLogicState.setter
    def privateBattleLogicState(self, value):
        self._privateBattleLogicState, = unpack_variables(value, ['PRIVATE_BATTLE_LOGIC_STATE'])


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