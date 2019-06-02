#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from interfaces.AccountCMDs import AccountCMDs
from interfaces.AccountEditor import AccountEditor
from interfaces.BattleStarterClient import BattleStarterClient
from interfaces.WalletOwner import WalletOwner
from interfaces.AccountPData import AccountPData
from interfaces.EntityHelperAPI import EntityHelperAPI
from interfaces.VoiceChatClient import VoiceChatClient
from interfaces.StatsPublisher import StatsPublisher
from interfaces.TransactionAPI import TransactionAPI



class Account(AccountCMDs, AccountEditor, BattleStarterClient, WalletOwner, AccountPData, EntityHelperAPI, VoiceChatClient, StatsPublisher, TransactionAPI):
    
    g_onAccountReallyCreated = EventHook()
    
    g_onGetBuyList = EventHook()
    
    g_receiveUIStatisticsServiceInfo = EventHook()
    
    g_onGetMapsList = EventHook()
    
    g_onUpdatePrice = EventHook()
    
    g_onGetDisabledMapsList = EventHook()
    
    g_getNationForTutorial = EventHook()
    
    g_updateAttributes = EventHook()
    
    g_changeName = EventHook()
    
    g_onResting = EventHook()
    
    g_onChangeAOGASPenalty = EventHook()
    
    g_onTotalUsersCountUpdate = EventHook()
    
    g_onGameRoomStateInit = EventHook()
    
    g_onPassiveSeekingSet = EventHook()
    
    g_inviteToPreBattle = EventHook()
    
    g_revokeInvite = EventHook()
    
    g_rejectInvite = EventHook()
    
    g_onInviteSent = EventHook()
    
    g_onInviteRevoked = EventHook()
    
    g_onInviteRejected = EventHook()
    
    g_onInviteAccepted = EventHook()
    
    g_enterPreBattle = EventHook()
    
    g_changePreBattleGrants = EventHook()
    
    g_onPreBattleCountdown = EventHook()
    
    g_leavePreBattle = EventHook()
    
    g_leaveBattleSession = EventHook()
    
    g_enterTrainingRoom = EventHook()
    
    g_setTrainingRoomDisabled = EventHook()
    
    g_receivePreBattlePlayerData = EventHook()
    
    g_onOwnerChanged = EventHook()
    
    g_receiveSelectedQueueType = EventHook()
    
    g_onGetActiveShipIndex = EventHook()
    
    g_onChatMessage = EventHook()
    
    g_onActionFailed = EventHook()
    
    g_onRankBattleFailed = EventHook()
    
    g_onDisconnectedFromServer = EventHook()
    
    g_onEnqueued = EventHook()
    
    g_onDequeued = EventHook()
    
    g_onPrepareingForBattle = EventHook()
    
    g_onQueueInfoReceived = EventHook()
    
    g_receiveToken = EventHook()
    
    g_dev_logConsole = EventHook()
    
    g_onCheckGamePing = EventHook()
    
    g_setTrace = EventHook()
    
    g_curVersion_release_8_4_0_1549228 = EventHook()
    
    g_updateSSEProgress = EventHook()
    
    g_onStartSyncSSE = EventHook()
    
    g_setServerTime = EventHook()
    
    g_setMaskStat = EventHook()
    
    g_receiveChanges = EventHook()
    
    g_receiveShipLock = EventHook()
    
    g_receiveShipBattleLock = EventHook()
    
    g_receiveActiveShip = EventHook()
    
    g_onStreamComplete = EventHook()
    
    g_receiveTransactionState = EventHook()
    
    g_onGetRankBattlesPlayerInfo = EventHook()
    
    g_onGetRankBattlesStage = EventHook()
    
    g_onChangeShutdown = EventHook()
    
    g_transactionLockEnd = EventHook()
    
    g_receiveNotification = EventHook()
    
    g_receiveLockData = EventHook()
    
    g_getToken = EventHook()
    
    g_forceReplayRecording = EventHook()
    
    g_onShutdownTime = EventHook()
    
    g_onChangeLootbox = EventHook()
    
    g_onGetLootboxRewards = EventHook()
    
    g_onActivateTask = EventHook()
    
    g_onDeactivateTask = EventHook()
    
    g_onTakeReward = EventHook()
    
    g_onUnlockTask = EventHook()
    
    g_onPostBattleUpdate = EventHook()
    
    g_onUpdateMissionProgress = EventHook()
    
    g_onUpdateActiveCampaigns = EventHook()
    
    g_onUpdateCampaignState = EventHook()
    
    g_onActivateMission = EventHook()
    
    g_onUpdateBalanceStatus = EventHook()
    
    g_onUpdateWalletStatus = EventHook()
    
    g_onGetClanBattlesStage = EventHook()
    
    g_syncPreBattleDef = EventHook()
    
    g_onGetPVEBattlesStage = EventHook()
    
    g_receivePVESelectedOperation = EventHook()
    
    g_receiveEventSelectedOperation = EventHook()
    
    g_onPVEOperationCompleted = EventHook()
    
    g_onPVESeasonCompleted = EventHook()
    
    g_onUpdateSplitCurrency = EventHook()
    
    g_onUpdateAbuseStatus = EventHook()
    
    g_receiveIngameNews = EventHook()
    
    g_receiveWebEvents = EventHook()
    
    g_receivePromo = EventHook()
    
    g_receiveArcEventOffer = EventHook()
    
    g_onArcEventSideChosen = EventHook()
    
    g_onArcEventOfferApplied = EventHook()
    
    g_onGetArcEventProgress = EventHook()
    
    g_onGetArcEventModifiers = EventHook()
    
    g_onLoyaltyChanged = EventHook()
    
    g_receiveActiveAlmanacs = EventHook()
    
    g_receiveAlmanacUpdate = EventHook()
    
    g_onAlmanacCompleted = EventHook()
    
    g_onOpenLootboxesStarted = EventHook()
    
    g_sendOpenedLootboxCount = EventHook()
    
    g_setEmailBind = EventHook()
    
    g_receiveActiveRoster = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        AccountCMDs.__init__(self)

        AccountEditor.__init__(self)

        BattleStarterClient.__init__(self)

        WalletOwner.__init__(self)

        AccountPData.__init__(self)

        EntityHelperAPI.__init__(self)

        VoiceChatClient.__init__(self)

        StatsPublisher.__init__(self)

        TransactionAPI.__init__(self)

        self._properties = getattr(self, '_properties', [])
        for item in [
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (1, 'onAccountReallyCreated'),
            (10000000001, 'onGetBuyList'),
            (10000000001, 'receiveUIStatisticsServiceInfo'),
            (10000000001, 'onGetMapsList'),
            (10000000001, 'onUpdatePrice'),
            (10000000001, 'onGetDisabledMapsList'),
            (9, 'getNationForTutorial'),
            (65, 'updateAttributes'),
            (10000000001, 'changeName'),
            (65, 'onResting'),
            (65, 'onChangeAOGASPenalty'),
            (33, 'onTotalUsersCountUpdate'),
            (65, 'onGameRoomStateInit'),
            (10000000001, 'onPassiveSeekingSet'),
            (10000000001, 'inviteToPreBattle'),
            (41, 'revokeInvite'),
            (10000000001, 'rejectInvite'),
            (10000000001, 'onInviteSent'),
            (41, 'onInviteRevoked'),
            (41, 'onInviteRejected'),
            (41, 'onInviteAccepted'),
            (10000000001, 'enterPreBattle'),
            (33, 'changePreBattleGrants'),
            (49, 'onPreBattleCountdown'),
            (17, 'leavePreBattle'),
            (10000000001, 'leaveBattleSession'),
            (10000000001, 'enterTrainingRoom'),
            (9, 'setTrainingRoomDisabled'),
            (10000000001, 'receivePreBattlePlayerData'),
            (33, 'onOwnerChanged'),
            (33, 'receiveSelectedQueueType'),
            (17, 'onGetActiveShipIndex'),
            (10000000001, 'onChatMessage'),
            (33, 'onActionFailed'),
            (10000000001, 'onRankBattleFailed'),
            (10000000001, 'onDisconnectedFromServer'),
            (10000000001, 'onEnqueued'),
            (9, 'onDequeued'),
            (1, 'onPrepareingForBattle'),
            (10000000001, 'onQueueInfoReceived'),
            (105, 'receiveToken'),
            (10000000001, 'dev_logConsole'),
            (65, 'onCheckGamePing'),
            (9, 'setTrace'),
            (1, 'curVersion_release_8_4_0_1549228'),
            (10000000001, 'updateSSEProgress'),
            (1, 'onStartSyncSSE'),
            (33, 'setServerTime'),
            (33, 'setMaskStat'),
            (10000000001, 'receiveChanges'),
            (41, 'receiveShipLock'),
            (10000000001, 'receiveShipBattleLock'),
            (33, 'receiveActiveShip'),
            (10000000001, 'onStreamComplete'),
            (10000000001, 'receiveTransactionState'),
            (10000000001, 'onGetRankBattlesPlayerInfo'),
            (41, 'onGetRankBattlesStage'),
            (49, 'onChangeShutdown'),
            (1, 'transactionLockEnd'),
            (10000000001, 'receiveNotification'),
            (10000000001, 'receiveLockData'),
            (33, 'getToken'),
            (1, 'forceReplayRecording'),
            (73, 'onShutdownTime'),
            (10000000001, 'onChangeLootbox'),
            (10000000001, 'onGetLootboxRewards'),
            (33, 'onActivateTask'),
            (41, 'onDeactivateTask'),
            (10000000001, 'onTakeReward'),
            (33, 'onUnlockTask'),
            (10000000001, 'onPostBattleUpdate'),
            (10000000001, 'onUpdateMissionProgress'),
            (10000000001, 'onUpdateActiveCampaigns'),
            (41, 'onUpdateCampaignState'),
            (10000000001, 'onActivateMission'),
            (9, 'onUpdateBalanceStatus'),
            (9, 'onUpdateWalletStatus'),
            (41, 'onGetClanBattlesStage'),
            (10000000001, 'syncPreBattleDef'),
            (169, 'onGetPVEBattlesStage'),
            (10000000001, 'receivePVESelectedOperation'),
            (33, 'receiveEventSelectedOperation'),
            (10000000001, 'onPVEOperationCompleted'),
            (10000000001, 'onPVESeasonCompleted'),
            (129, 'onUpdateSplitCurrency'),
            (10000000001, 'onUpdateAbuseStatus'),
            (9, 'receiveIngameNews'),
            (10000000001, 'receiveWebEvents'),
            (10000000001, 'receivePromo'),
            (9, 'receiveArcEventOffer'),
            (9, 'onArcEventSideChosen'),
            (17, 'onArcEventOfferApplied'),
            (169, 'onGetArcEventProgress'),
            (65, 'onGetArcEventModifiers'),
            (41, 'onLoyaltyChanged'),
            (10000000001, 'receiveActiveAlmanacs'),
            (10000000002, 'receiveAlmanacUpdate'),
            (17, 'onAlmanacCompleted'),
            (17, 'onOpenLootboxesStarted'),
            (17, 'sendOpenedLootboxCount'),
            (9, 'setEmailBind'),
            (10000000001, 'receiveActiveRoster'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._methods:
                continue
            self._methods.append(item)
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

# method size: 1
    @unpack_func_args([])
    def onAccountReallyCreated(self):
        self.g_onAccountReallyCreated.fire(self)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def onGetBuyList(self, arg1):
        self.g_onGetBuyList.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UNICODE_STRING', 'INT64'])
    def receiveUIStatisticsServiceInfo(self, arg1, arg2):
        self.g_receiveUIStatisticsServiceInfo.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['BLOB', 'BLOB', 'BOOL'])
    def onGetMapsList(self, arg1, arg2, arg3):
        self.g_onGetMapsList.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def onUpdatePrice(self, arg1):
        self.g_onUpdatePrice.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def onGetDisabledMapsList(self, arg1):
        self.g_onGetDisabledMapsList.fire(self, arg1)
# method size: 9
    @unpack_func_args(['BOOL'])
    def getNationForTutorial(self, arg1):
        self.g_getNationForTutorial.fire(self, arg1)
# method size: 65
    @unpack_func_args(['UINT64'])
    def updateAttributes(self, arg1):
        self.g_updateAttributes.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def changeName(self, arg1):
        self.g_changeName.fire(self, arg1)
# method size: 65
    @unpack_func_args(['INT32', 'FLOAT'])
    def onResting(self, arg1, arg2):
        self.g_onResting.fire(self, arg1, arg2)
# method size: 65
    @unpack_func_args(['FLOAT', 'INT32'])
    def onChangeAOGASPenalty(self, arg1, arg2):
        self.g_onChangeAOGASPenalty.fire(self, arg1, arg2)
# method size: 33
    @unpack_func_args(['INT32'])
    def onTotalUsersCountUpdate(self, arg1):
        self.g_onTotalUsersCountUpdate.fire(self, arg1)
# method size: 65
    @unpack_func_args(['INT16', 'UINT16', 'UINT16', 'UINT16'])
    def onGameRoomStateInit(self, arg1, arg2, arg3, arg4):
        self.g_onGameRoomStateInit.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000001
    @unpack_func_args(['UINT8', 'UINT8', 'STRING'])
    def onPassiveSeekingSet(self, arg1, arg2, arg3):
        self.g_onPassiveSeekingSet.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['PRE_BATTLE_INVITE_DEF'])
    def inviteToPreBattle(self, arg1):
        self.g_inviteToPreBattle.fire(self, arg1)
# method size: 41
    @unpack_func_args(['OBJECT_ID', 'UINT8'])
    def revokeInvite(self, arg1, arg2):
        self.g_revokeInvite.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['PLAYER_ID', 'INT8', 'STRING', 'UNICODE_STRING'])
    def rejectInvite(self, arg1, arg2, arg3, arg4):
        self.g_rejectInvite.fire(self, arg1, arg2, arg3, arg4)
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
    @unpack_func_args(['BLOB', 'INT32', 'BOOL'])
    def enterPreBattle(self, arg1, arg2, arg3):
        self.g_enterPreBattle.fire(self, arg1, arg2, arg3)
# method size: 33
    @unpack_func_args(['INT32'])
    def changePreBattleGrants(self, arg1):
        self.g_changePreBattleGrants.fire(self, arg1)
# method size: 49
    @unpack_func_args(['UINT8', 'UINT32', 'UINT8'])
    def onPreBattleCountdown(self, arg1, arg2, arg3):
        self.g_onPreBattleCountdown.fire(self, arg1, arg2, arg3)
# method size: 17
    @unpack_func_args(['UINT8', 'UINT8'])
    def leavePreBattle(self, arg1, arg2):
        self.g_leavePreBattle.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['UINT8', 'BLOB'])
    def leaveBattleSession(self, arg1, arg2):
        self.g_leaveBattleSession.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['BLOB', 'COUNTDOWN_INFO', 'INT32', 'BOOL'])
    def enterTrainingRoom(self, arg1, arg2, arg3, arg4):
        self.g_enterTrainingRoom.fire(self, arg1, arg2, arg3, arg4)
# method size: 9
    @unpack_func_args(['INT8'])
    def setTrainingRoomDisabled(self, arg1):
        self.g_setTrainingRoomDisabled.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['PRE_BATTLE_ID', 'BLOB', 'BOOL', 'INT32'])
    def receivePreBattlePlayerData(self, arg1, arg2, arg3, arg4):
        self.g_receivePreBattlePlayerData.fire(self, arg1, arg2, arg3, arg4)
# method size: 33
    @unpack_func_args(['PLAYER_ID'])
    def onOwnerChanged(self, arg1):
        self.g_onOwnerChanged.fire(self, arg1)
# method size: 33
    @unpack_func_args(['UINT32'])
    def receiveSelectedQueueType(self, arg1):
        self.g_receiveSelectedQueueType.fire(self, arg1)
# method size: 17
    @unpack_func_args(['UINT16'])
    def onGetActiveShipIndex(self, arg1):
        self.g_onGetActiveShipIndex.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['DB_ID', 'STRING', 'STRING', 'STRING', 'STRING'])
    def onChatMessage(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onChatMessage.fire(self, arg1, arg2, arg3, arg4, arg5)
# method size: 33
    @unpack_func_args(['INT16', 'INT16'])
    def onActionFailed(self, arg1, arg2):
        self.g_onActionFailed.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args([['ARRAY', 'RANK_BATTLES_DENY_REASON']])
    def onRankBattleFailed(self, arg1):
        self.g_onRankBattleFailed.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UINT32', 'UINT8', 'BLOB'])
    def onDisconnectedFromServer(self, arg1, arg2, arg3):
        self.g_onDisconnectedFromServer.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['UINT8', 'SHIP_ID', 'BLOB'])
    def onEnqueued(self, arg1, arg2, arg3):
        self.g_onEnqueued.fire(self, arg1, arg2, arg3)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onDequeued(self, arg1):
        self.g_onDequeued.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def onPrepareingForBattle(self):
        self.g_onPrepareingForBattle.fire(self)
# method size: 10000000001
    @unpack_func_args(['UINT8', 'BLOB'])
    def onQueueInfoReceived(self, arg1, arg2):
        self.g_onQueueInfoReceived.fire(self, arg1, arg2)
# method size: 105
    @unpack_func_args(['DB_ID', 'INT32', 'UINT8'])
    def receiveToken(self, arg1, arg2, arg3):
        self.g_receiveToken.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def dev_logConsole(self, arg1):
        self.g_dev_logConsole.fire(self, arg1)
# method size: 65
    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)
# method size: 9
    @unpack_func_args(['BOOL'])
    def setTrace(self, arg1):
        self.g_setTrace.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def curVersion_release_8_4_0_1549228(self):
        self.g_curVersion_release_8_4_0_1549228.fire(self)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def updateSSEProgress(self, arg1):
        self.g_updateSSEProgress.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def onStartSyncSSE(self):
        self.g_onStartSyncSSE.fire(self)
# method size: 33
    @unpack_func_args(['UINT32'])
    def setServerTime(self, arg1):
        self.g_setServerTime.fire(self, arg1)
# method size: 33
    @unpack_func_args(['INT32'])
    def setMaskStat(self, arg1):
        self.g_setMaskStat.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['MSGPACK_BLOB'])
    def receiveChanges(self, arg1):
        self.g_receiveChanges.fire(self, arg1)
# method size: 41
    @unpack_func_args(['SHIP_ID', 'UINT8'])
    def receiveShipLock(self, arg1, arg2):
        self.g_receiveShipLock.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['SHIP_ID', 'MSGPACK_BLOB'])
    def receiveShipBattleLock(self, arg1, arg2):
        self.g_receiveShipBattleLock.fire(self, arg1, arg2)
# method size: 33
    @unpack_func_args(['SHIP_ID'])
    def receiveActiveShip(self, arg1):
        self.g_receiveActiveShip.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UINT32', 'STRING', 'BLOB'])
    def onStreamComplete(self, arg1, arg2, arg3):
        self.g_onStreamComplete.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['UINT32', 'MSGPACK_BLOB'])
    def receiveTransactionState(self, arg1, arg2):
        self.g_receiveTransactionState.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['RANK_BATTLES_PLAYER_INFO', ['ARRAY', 'INT8']])
    def onGetRankBattlesPlayerInfo(self, arg1, arg2):
        self.g_onGetRankBattlesPlayerInfo.fire(self, arg1, arg2)
# method size: 41
    @unpack_func_args(['UINT32', 'UINT8'])
    def onGetRankBattlesStage(self, arg1, arg2):
        self.g_onGetRankBattlesStage.fire(self, arg1, arg2)
# method size: 49
    @unpack_func_args(['BOOL', 'UINT8', 'UINT32'])
    def onChangeShutdown(self, arg1, arg2, arg3):
        self.g_onChangeShutdown.fire(self, arg1, arg2, arg3)
# method size: 1
    @unpack_func_args([])
    def transactionLockEnd(self):
        self.g_transactionLockEnd.fire(self)
# method size: 10000000001
    @unpack_func_args(['STRING', 'STRING'])
    def receiveNotification(self, arg1, arg2):
        self.g_receiveNotification.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receiveLockData(self, arg1):
        self.g_receiveLockData.fire(self, arg1)
# method size: 33
    @unpack_func_args(['UINT32'])
    def getToken(self, arg1):
        self.g_getToken.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def forceReplayRecording(self):
        self.g_forceReplayRecording.fire(self)
# method size: 73
    @unpack_func_args(['UINT32', 'UINT32', 'BOOL'])
    def onShutdownTime(self, arg1, arg2, arg3):
        self.g_onShutdownTime.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['STRING', 'UINT8', 'BOOL'])
    def onChangeLootbox(self, arg1, arg2, arg3):
        self.g_onChangeLootbox.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def onGetLootboxRewards(self, arg1):
        self.g_onGetLootboxRewards.fire(self, arg1)
# method size: 33
    @unpack_func_args(['CAMPAIGN_TASK_ID'])
    def onActivateTask(self, arg1):
        self.g_onActivateTask.fire(self, arg1)
# method size: 41
    @unpack_func_args(['CAMPAIGN_TASK_ID', 'UINT8'])
    def onDeactivateTask(self, arg1, arg2):
        self.g_onDeactivateTask.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['CAMPAIGN_TASK_ID', 'UINT8', 'UINT16', ['ARRAY', 'UINT32']])
    def onTakeReward(self, arg1, arg2, arg3, arg4):
        self.g_onTakeReward.fire(self, arg1, arg2, arg3, arg4)
# method size: 33
    @unpack_func_args(['CAMPAIGN_TASK_ID'])
    def onUnlockTask(self, arg1):
        self.g_onUnlockTask.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def onPostBattleUpdate(self, arg1):
        self.g_onPostBattleUpdate.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UINT32', 'UINT16', ['ARRAY', 'UINT32']])
    def onUpdateMissionProgress(self, arg1, arg2, arg3):
        self.g_onUpdateMissionProgress.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args([['ARRAY', 'UINT32'], ['ARRAY', 'UINT32']])
    def onUpdateActiveCampaigns(self, arg1, arg2):
        self.g_onUpdateActiveCampaigns.fire(self, arg1, arg2)
# method size: 41
    @unpack_func_args(['UINT32', 'UINT8'])
    def onUpdateCampaignState(self, arg1, arg2):
        self.g_onUpdateCampaignState.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['UINT32', 'UINT32', ['ARRAY', 'UINT32']])
    def onActivateMission(self, arg1, arg2, arg3):
        self.g_onActivateMission.fire(self, arg1, arg2, arg3)
# method size: 9
    @unpack_func_args(['BOOL'])
    def onUpdateBalanceStatus(self, arg1):
        self.g_onUpdateBalanceStatus.fire(self, arg1)
# method size: 9
    @unpack_func_args(['BOOL'])
    def onUpdateWalletStatus(self, arg1):
        self.g_onUpdateWalletStatus.fire(self, arg1)
# method size: 41
    @unpack_func_args(['UINT32', 'UINT8'])
    def onGetClanBattlesStage(self, arg1, arg2):
        self.g_onGetClanBattlesStage.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def syncPreBattleDef(self, arg1):
        self.g_syncPreBattleDef.fire(self, arg1)
# method size: 169
    @unpack_func_args(['UINT32', 'UINT8', 'UINT32', 'UINT32', 'UINT32', 'UINT32'])
    def onGetPVEBattlesStage(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_onGetPVEBattlesStage.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)
# method size: 10000000001
    @unpack_func_args(['UINT32', 'STRING', 'BOOL'])
    def receivePVESelectedOperation(self, arg1, arg2, arg3):
        self.g_receivePVESelectedOperation.fire(self, arg1, arg2, arg3)
# method size: 33
    @unpack_func_args(['UINT32'])
    def receiveEventSelectedOperation(self, arg1):
        self.g_receiveEventSelectedOperation.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UINT32', 'STRING', ['ARRAY', 'UINT32']])
    def onPVEOperationCompleted(self, arg1, arg2, arg3):
        self.g_onPVEOperationCompleted.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['UINT8', 'STRING', 'UINT32'])
    def onPVESeasonCompleted(self, arg1, arg2, arg3):
        self.g_onPVESeasonCompleted.fire(self, arg1, arg2, arg3)
# method size: 129
    @unpack_func_args(['UINT32', 'UINT32', 'UINT32', 'UINT32'])
    def onUpdateSplitCurrency(self, arg1, arg2, arg3, arg4):
        self.g_onUpdateSplitCurrency.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000001
    @unpack_func_args(['MSGPACK_BLOB'])
    def onUpdateAbuseStatus(self, arg1):
        self.g_onUpdateAbuseStatus.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def receiveIngameNews(self, arg1):
        self.g_receiveIngameNews.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receiveWebEvents(self, arg1):
        self.g_receiveWebEvents.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receivePromo(self, arg1):
        self.g_receivePromo.fire(self, arg1)
# method size: 9
    @unpack_func_args(['INT8'])
    def receiveArcEventOffer(self, arg1):
        self.g_receiveArcEventOffer.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onArcEventSideChosen(self, arg1):
        self.g_onArcEventSideChosen.fire(self, arg1)
# method size: 17
    @unpack_func_args(['UINT8', 'UINT8'])
    def onArcEventOfferApplied(self, arg1, arg2):
        self.g_onArcEventOfferApplied.fire(self, arg1, arg2)
# method size: 169
    @unpack_func_args(['INT8', 'UINT32', ['ARRAY', 'UINT32', 2], 'UINT32', 'UINT32'])
    def onGetArcEventProgress(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onGetArcEventProgress.fire(self, arg1, arg2, arg3, arg4, arg5)
# method size: 65
    @unpack_func_args([['ARRAY', 'FLOAT', 2]])
    def onGetArcEventModifiers(self, arg1):
        self.g_onGetArcEventModifiers.fire(self, arg1)
# method size: 41
    @unpack_func_args(['UINT8', 'UINT32'])
    def onLoyaltyChanged(self, arg1, arg2):
        self.g_onLoyaltyChanged.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receiveActiveAlmanacs(self, arg1):
        self.g_receiveActiveAlmanacs.fire(self, arg1)
# method size: 10000000002
    @unpack_func_args(['BLOB'])
    def receiveAlmanacUpdate(self, arg1):
        self.g_receiveAlmanacUpdate.fire(self, arg1)
# method size: 17
    @unpack_func_args(['UINT16'])
    def onAlmanacCompleted(self, arg1):
        self.g_onAlmanacCompleted.fire(self, arg1)
# method size: 17
    @unpack_func_args(['UINT16'])
    def onOpenLootboxesStarted(self, arg1):
        self.g_onOpenLootboxesStarted.fire(self, arg1)
# method size: 17
    @unpack_func_args(['UINT16'])
    def sendOpenedLootboxCount(self, arg1):
        self.g_sendOpenedLootboxCount.fire(self, arg1)
# method size: 9
    @unpack_func_args(['BOOL'])
    def setEmailBind(self, arg1):
        self.g_setEmailBind.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def receiveActiveRoster(self, arg1):
        self.g_receiveActiveRoster.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



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