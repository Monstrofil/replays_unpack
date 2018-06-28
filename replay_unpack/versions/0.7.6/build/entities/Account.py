#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.AccountEditor import AccountEditor
except:
    from AccountEditor import AccountEditor

try:
    from interfaces.BattleStarter import BattleStarter
except:
    from BattleStarter import BattleStarter

try:
    from interfaces.WalletOwner import WalletOwner
except:
    from WalletOwner import WalletOwner

try:
    from interfaces.AccountPData import AccountPData
except:
    from AccountPData import AccountPData

try:
    from interfaces.EntityLookuper import EntityLookuper
except:
    from EntityLookuper import EntityLookuper

try:
    from interfaces.VoiceChatClient import VoiceChatClient
except:
    from VoiceChatClient import VoiceChatClient

try:
    from interfaces.StatsPublisher import StatsPublisher
except:
    from StatsPublisher import StatsPublisher

try:
    from interfaces.TransactionAPI import TransactionAPI
except:
    from TransactionAPI import TransactionAPI



class Account(AccountEditor, BattleStarter, WalletOwner, AccountPData, EntityLookuper, VoiceChatClient, StatsPublisher, TransactionAPI):
    
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
    
    g_reciveCountFreePreBattles = EventHook()
    
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
    
    g_curVersion_Release_0_7_6_0_346043 = EventHook()
    
    g_initActions = EventHook()
    
    g_updateActionsProgress = EventHook()
    
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
    
    g_onPVEOperationCompleted = EventHook()
    
    g_onPVESeasonCompleted = EventHook()
    
    g_onUpdateSplitCurrency = EventHook()
    
    g_onUpdateAbuseStatus = EventHook()
    
    g_receiveIngameNews = EventHook()
    
    g_receiveWebEvents = EventHook()
    
    g_receivePromo = EventHook()
    
    g_getAccountData = EventHook()
    
    g_getAccountPrices = EventHook()
    
    g_requestGameParams = EventHook()
    
    g_syncGameParams = EventHook()
    
    g_onClientReady = EventHook()
    
    g_onStreamReceived = EventHook()
    
    g_cmdEmpty = EventHook()
    
    g_cmdI1 = EventHook()
    
    g_cmdI2 = EventHook()
    
    g_cmdI3 = EventHook()
    
    g_cmdI4 = EventHook()
    
    g_cmdI3S1 = EventHook()
    
    g_cmdI4S1 = EventHook()
    
    g_cmdI5 = EventHook()
    
    g_cmdI5S1 = EventHook()
    
    g_cmdI6S1 = EventHook()
    
    g_cmdI6S2 = EventHook()
    
    g_cmdI7S1 = EventHook()
    
    g_cmdI8S1 = EventHook()
    
    g_cmdI9S1 = EventHook()
    
    g_cmdI7S2 = EventHook()
    
    g_cmdS1 = EventHook()
    
    g_cmdB1 = EventHook()
    
    g_cmdS2 = EventHook()
    
    g_cmdI1S1 = EventHook()
    
    g_cmdI1S2 = EventHook()
    
    g_cmdI1S3 = EventHook()
    
    g_cmdI1S4 = EventHook()
    
    g_cmdI2S1 = EventHook()
    
    g_cmdI2S2 = EventHook()
    
    g_cmdI2S3 = EventHook()
    
    g_cmdI2S4 = EventHook()
    
    g_cmdI2S5 = EventHook()
    
    g_cmdS1I1 = EventHook()
    
    g_cmdU1 = EventHook()
    
    g_cmdU1S1 = EventHook()
    
    g_cmdI2U7 = EventHook()
    
    g_cmdI7S1R1 = EventHook()
    
    g_cmdT1 = EventHook()
    
    g_cmdD1 = EventHook()
    
    g_chatMessage = EventHook()
    
    g_dev_bot_setTestBattleParams = EventHook()
    
    g_dev_onSurveyClear = EventHook()
    
    g_checkGamePing = EventHook()
    
    g_sendStatData = EventHook()
    
    g_sendSurveyResults = EventHook()
    
    g_newTraces = EventHook()
    
    g_dev_resetDailyLimits = EventHook()
    
    g_dev_resetAbuse = EventHook()
    
    g_dev_resetRecidivism = EventHook()
    
    g_dev_resetAbuseRating = EventHook()
    
    g_executeTransactionCl = EventHook()
    
    g_dev_restoreAccountFromPoint = EventHook()
    
    g_dev_exportAccountToWeb = EventHook()
    
    g_dev_receiveExternalNotification = EventHook()
    
    g_dev_setAbuseStatus = EventHook()
    
    g_dev_setAbuseRecidivism = EventHook()
    
    g_dev_setAbuseRating = EventHook()
    
    g_testInvoice = EventHook()
    
    g_tryGiveClientToReplayConnectionHandler = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        AccountEditor.__init__(self)

        BattleStarter.__init__(self)

        WalletOwner.__init__(self)

        AccountPData.__init__(self)

        EntityLookuper.__init__(self)

        VoiceChatClient.__init__(self)

        StatsPublisher.__init__(self)

        TransactionAPI.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def onAccountReallyCreated(self):
        self.g_onAccountReallyCreated.fire(self)

    @unpack_func_args(['BLOB'])
    def onGetBuyList(self, arg1):
        self.g_onGetBuyList.fire(self, arg1)

    @unpack_func_args([])
    def receiveUIStatisticsServiceInfo(self):
        self.g_receiveUIStatisticsServiceInfo.fire(self)

    @unpack_func_args(['BLOB', 'BLOB', 'BOOL'])
    def onGetMapsList(self, arg1, arg2, arg3):
        self.g_onGetMapsList.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['BLOB'])
    def onUpdatePrice(self, arg1):
        self.g_onUpdatePrice.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def onGetDisabledMapsList(self, arg1):
        self.g_onGetDisabledMapsList.fire(self, arg1)

    @unpack_func_args(['BOOL'])
    def getNationForTutorial(self, arg1):
        self.g_getNationForTutorial.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def updateAttributes(self, arg1):
        self.g_updateAttributes.fire(self, arg1)

    @unpack_func_args(['STRING'])
    def changeName(self, arg1):
        self.g_changeName.fire(self, arg1)

    @unpack_func_args(['INT32', 'FLOAT'])
    def onResting(self, arg1, arg2):
        self.g_onResting.fire(self, arg1, arg2)

    @unpack_func_args(['FLOAT', 'INT32'])
    def onChangeAOGASPenalty(self, arg1, arg2):
        self.g_onChangeAOGASPenalty.fire(self, arg1, arg2)

    @unpack_func_args(['INT32'])
    def onTotalUsersCountUpdate(self, arg1):
        self.g_onTotalUsersCountUpdate.fire(self, arg1)

    @unpack_func_args(['INT16', 'UINT16', 'UINT16', 'UINT16'])
    def onGameRoomStateInit(self, arg1, arg2, arg3, arg4):
        self.g_onGameRoomStateInit.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'UINT8', 'STRING'])
    def onPassiveSeekingSet(self, arg1, arg2, arg3):
        self.g_onPassiveSeekingSet.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT16'])
    def reciveCountFreePreBattles(self, arg1):
        self.g_reciveCountFreePreBattles.fire(self, arg1)

    @unpack_func_args(['PRE_BATTLE_INVITE_DEF'])
    def inviteToPreBattle(self, arg1):
        self.g_inviteToPreBattle.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'UINT8'])
    def revokeInvite(self, arg1, arg2):
        self.g_revokeInvite.fire(self, arg1, arg2)

    @unpack_func_args(['PLAYER_ID', 'INT8', 'STRING', 'UNICODE_STRING'])
    def rejectInvite(self, arg1, arg2, arg3, arg4):
        self.g_rejectInvite.fire(self, arg1, arg2, arg3, arg4)

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

    @unpack_func_args(['BLOB', 'INT32', 'BOOL'])
    def enterPreBattle(self, arg1, arg2, arg3):
        self.g_enterPreBattle.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32'])
    def changePreBattleGrants(self, arg1):
        self.g_changePreBattleGrants.fire(self, arg1)

    @unpack_func_args(['UINT8', 'UINT32', 'UINT8'])
    def onPreBattleCountdown(self, arg1, arg2, arg3):
        self.g_onPreBattleCountdown.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT8'])
    def leavePreBattle(self, arg1, arg2):
        self.g_leavePreBattle.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'BLOB'])
    def leaveBattleSession(self, arg1, arg2):
        self.g_leaveBattleSession.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB', 'COUNTDOWN_INFO', 'INT32', 'BOOL'])
    def enterTrainingRoom(self, arg1, arg2, arg3, arg4):
        self.g_enterTrainingRoom.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT8'])
    def setTrainingRoomDisabled(self, arg1):
        self.g_setTrainingRoomDisabled.fire(self, arg1)

    @unpack_func_args(['PRE_BATTLE_ID', 'BLOB', 'BOOL', 'INT32'])
    def receivePreBattlePlayerData(self, arg1, arg2, arg3, arg4):
        self.g_receivePreBattlePlayerData.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['PLAYER_ID'])
    def onOwnerChanged(self, arg1):
        self.g_onOwnerChanged.fire(self, arg1)

    @unpack_func_args(['UINT32'])
    def receiveSelectedQueueType(self, arg1):
        self.g_receiveSelectedQueueType.fire(self, arg1)

    @unpack_func_args(['UINT16'])
    def onGetActiveShipIndex(self, arg1):
        self.g_onGetActiveShipIndex.fire(self, arg1)

    @unpack_func_args(['DB_ID', 'STRING', 'STRING', 'STRING', 'STRING'])
    def onChatMessage(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onChatMessage.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['INT16', 'INT16'])
    def onActionFailed(self, arg1, arg2):
        self.g_onActionFailed.fire(self, arg1, arg2)

    @unpack_func_args([['ARRAY', 'RANK_BATTLES_DENY_REASON']])
    def onRankBattleFailed(self, arg1):
        self.g_onRankBattleFailed.fire(self, arg1)

    @unpack_func_args(['UINT32', 'UINT8', 'BLOB'])
    def onDisconnectedFromServer(self, arg1, arg2, arg3):
        self.g_onDisconnectedFromServer.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'SHIP_ID', 'BLOB'])
    def onEnqueued(self, arg1, arg2, arg3):
        self.g_onEnqueued.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8'])
    def onDequeued(self, arg1):
        self.g_onDequeued.fire(self, arg1)

    @unpack_func_args([])
    def onPrepareingForBattle(self):
        self.g_onPrepareingForBattle.fire(self)

    @unpack_func_args(['UINT8', 'BLOB'])
    def onQueueInfoReceived(self, arg1, arg2):
        self.g_onQueueInfoReceived.fire(self, arg1, arg2)

    @unpack_func_args(['DB_ID', 'INT32', 'UINT8'])
    def receiveToken(self, arg1, arg2, arg3):
        self.g_receiveToken.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING'])
    def dev_logConsole(self, arg1):
        self.g_dev_logConsole.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)

    @unpack_func_args(['BOOL'])
    def setTrace(self, arg1):
        self.g_setTrace.fire(self, arg1)

    @unpack_func_args([])
    def curVersion_Release_0_7_6_0_346043(self):
        self.g_curVersion_Release_0_7_6_0_346043.fire(self)

    @unpack_func_args(['STRING', 'STRING'])
    def initActions(self, arg1, arg2):
        self.g_initActions.fire(self, arg1, arg2)

    @unpack_func_args(['STRING'])
    def updateActionsProgress(self, arg1):
        self.g_updateActionsProgress.fire(self, arg1)

    @unpack_func_args([])
    def onStartSyncSSE(self):
        self.g_onStartSyncSSE.fire(self)

    @unpack_func_args(['UINT32'])
    def setServerTime(self, arg1):
        self.g_setServerTime.fire(self, arg1)

    @unpack_func_args(['INT32'])
    def setMaskStat(self, arg1):
        self.g_setMaskStat.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def receiveChanges(self, arg1):
        self.g_receiveChanges.fire(self, arg1)

    @unpack_func_args(['SHIP_ID', 'UINT8'])
    def receiveShipLock(self, arg1, arg2):
        self.g_receiveShipLock.fire(self, arg1, arg2)

    @unpack_func_args(['SHIP_ID', 'BLOB'])
    def receiveShipBattleLock(self, arg1, arg2):
        self.g_receiveShipBattleLock.fire(self, arg1, arg2)

    @unpack_func_args(['SHIP_ID'])
    def receiveActiveShip(self, arg1):
        self.g_receiveActiveShip.fire(self, arg1)

    @unpack_func_args(['UINT32', 'STRING', 'BLOB'])
    def onStreamComplete(self, arg1, arg2, arg3):
        self.g_onStreamComplete.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT32', 'BLOB'])
    def receiveTransactionState(self, arg1, arg2):
        self.g_receiveTransactionState.fire(self, arg1, arg2)

    @unpack_func_args(['RANK_BATTLES_PLAYER_INFO', ['ARRAY', 'INT8']])
    def onGetRankBattlesPlayerInfo(self, arg1, arg2):
        self.g_onGetRankBattlesPlayerInfo.fire(self, arg1, arg2)

    @unpack_func_args(['UINT32', 'UINT8'])
    def onGetRankBattlesStage(self, arg1, arg2):
        self.g_onGetRankBattlesStage.fire(self, arg1, arg2)

    @unpack_func_args(['BOOL', 'UINT8', 'UINT32'])
    def onChangeShutdown(self, arg1, arg2, arg3):
        self.g_onChangeShutdown.fire(self, arg1, arg2, arg3)

    @unpack_func_args([])
    def transactionLockEnd(self):
        self.g_transactionLockEnd.fire(self)

    @unpack_func_args(['STRING', 'STRING'])
    def receiveNotification(self, arg1, arg2):
        self.g_receiveNotification.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB'])
    def receiveLockData(self, arg1):
        self.g_receiveLockData.fire(self, arg1)

    @unpack_func_args(['UINT32'])
    def getToken(self, arg1):
        self.g_getToken.fire(self, arg1)

    @unpack_func_args([])
    def forceReplayRecording(self):
        self.g_forceReplayRecording.fire(self)

    @unpack_func_args(['UINT32', 'UINT32', 'BOOL'])
    def onShutdownTime(self, arg1, arg2, arg3):
        self.g_onShutdownTime.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING', 'UINT8', 'BOOL'])
    def onChangeLootbox(self, arg1, arg2, arg3):
        self.g_onChangeLootbox.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['BLOB'])
    def onGetLootboxRewards(self, arg1):
        self.g_onGetLootboxRewards.fire(self, arg1)

    @unpack_func_args(['CAMPAIGN_TASK_ID'])
    def onActivateTask(self, arg1):
        self.g_onActivateTask.fire(self, arg1)

    @unpack_func_args(['CAMPAIGN_TASK_ID', 'UINT8'])
    def onDeactivateTask(self, arg1, arg2):
        self.g_onDeactivateTask.fire(self, arg1, arg2)

    @unpack_func_args(['CAMPAIGN_TASK_ID', 'UINT8', 'UINT16', ['ARRAY', 'UINT32']])
    def onTakeReward(self, arg1, arg2, arg3, arg4):
        self.g_onTakeReward.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['CAMPAIGN_TASK_ID'])
    def onUnlockTask(self, arg1):
        self.g_onUnlockTask.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def onPostBattleUpdate(self, arg1):
        self.g_onPostBattleUpdate.fire(self, arg1)

    @unpack_func_args(['UINT32', 'UINT16', ['ARRAY', 'UINT32']])
    def onUpdateMissionProgress(self, arg1, arg2, arg3):
        self.g_onUpdateMissionProgress.fire(self, arg1, arg2, arg3)

    @unpack_func_args([['ARRAY', 'UINT32'], ['ARRAY', 'UINT32']])
    def onUpdateActiveCampaigns(self, arg1, arg2):
        self.g_onUpdateActiveCampaigns.fire(self, arg1, arg2)

    @unpack_func_args(['UINT32', 'UINT8'])
    def onUpdateCampaignState(self, arg1, arg2):
        self.g_onUpdateCampaignState.fire(self, arg1, arg2)

    @unpack_func_args(['UINT32', 'UINT32', ['ARRAY', 'UINT32']])
    def onActivateMission(self, arg1, arg2, arg3):
        self.g_onActivateMission.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['BOOL'])
    def onUpdateBalanceStatus(self, arg1):
        self.g_onUpdateBalanceStatus.fire(self, arg1)

    @unpack_func_args(['BOOL'])
    def onUpdateWalletStatus(self, arg1):
        self.g_onUpdateWalletStatus.fire(self, arg1)

    @unpack_func_args(['UINT32', 'UINT8'])
    def onGetClanBattlesStage(self, arg1, arg2):
        self.g_onGetClanBattlesStage.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB'])
    def syncPreBattleDef(self, arg1):
        self.g_syncPreBattleDef.fire(self, arg1)

    @unpack_func_args(['UINT32', 'UINT8', 'UINT32', 'UINT32', 'UINT32', 'UINT32'])
    def onGetPVEBattlesStage(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_onGetPVEBattlesStage.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['UINT32', 'STRING', 'BOOL'])
    def receivePVESelectedOperation(self, arg1, arg2, arg3):
        self.g_receivePVESelectedOperation.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT32', 'STRING', ['ARRAY', 'UINT32']])
    def onPVEOperationCompleted(self, arg1, arg2, arg3):
        self.g_onPVEOperationCompleted.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'STRING', 'UINT32'])
    def onPVESeasonCompleted(self, arg1, arg2, arg3):
        self.g_onPVESeasonCompleted.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT32', 'UINT32', 'UINT32', 'UINT32'])
    def onUpdateSplitCurrency(self, arg1, arg2, arg3, arg4):
        self.g_onUpdateSplitCurrency.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['BLOB'])
    def onUpdateAbuseStatus(self, arg1):
        self.g_onUpdateAbuseStatus.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def receiveIngameNews(self, arg1):
        self.g_receiveIngameNews.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def receiveWebEvents(self, arg1):
        self.g_receiveWebEvents.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def receivePromo(self, arg1):
        self.g_receivePromo.fire(self, arg1)

    @unpack_func_args(['STRING', 'STRING', 'STRING', 'UINT32'])
    def getAccountData(self, arg1, arg2, arg3, arg4):
        self.g_getAccountData.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args([['ARRAY', 'STRING']])
    def getAccountPrices(self, arg1):
        self.g_getAccountPrices.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'STRING']])
    def requestGameParams(self, arg1):
        self.g_requestGameParams.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'UINT32']])
    def syncGameParams(self, arg1):
        self.g_syncGameParams.fire(self, arg1)

    @unpack_func_args(['STRING'])
    def onClientReady(self, arg1):
        self.g_onClientReady.fire(self, arg1)

    @unpack_func_args(['UINT16', 'BOOL', 'UINT32', 'UINT32', 'INT32', 'INT32'])
    def onStreamReceived(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_onStreamReceived.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['UINT8', 'UINT8'])
    def cmdEmpty(self, arg1, arg2):
        self.g_cmdEmpty.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64'])
    def cmdI1(self, arg1, arg2, arg3):
        self.g_cmdI1.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT64'])
    def cmdI2(self, arg1, arg2, arg3, arg4):
        self.g_cmdI2.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT64', 'INT64'])
    def cmdI3(self, arg1, arg2, arg3, arg4, arg5):
        self.g_cmdI3.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT64', 'INT32', 'INT32'])
    def cmdI4(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_cmdI4.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT64', 'INT32', 'UNICODE_STRING'])
    def cmdI3S1(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_cmdI3S1.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT64', 'INT32', 'INT32', 'UNICODE_STRING'])
    def cmdI4S1(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_cmdI4S1.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT64', 'UINT32', 'UINT32', 'UINT32'])
    def cmdI5(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_cmdI5.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'UINT32', 'INT32', 'INT32', 'INT32', 'UNICODE_STRING'])
    def cmdI5S1(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_cmdI5S1.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['UINT8', 'UINT8', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UNICODE_STRING'])
    def cmdI6S1(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_cmdI6S1.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['UINT8', 'UINT8', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI6S2(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
        self.g_cmdI6S2.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)

    @unpack_func_args(['UINT8', 'UINT8', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'INT32', 'UINT32', 'UINT32', 'UNICODE_STRING'])
    def cmdI7S1(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
        self.g_cmdI7S1.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)

    @unpack_func_args(['UINT8', 'UINT8', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT64', 'UINT32', 'UNICODE_STRING'])
    def cmdI8S1(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_cmdI8S1.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['UINT8', 'UINT8', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'INT32', 'UINT32', 'UINT32', 'UINT64', 'UINT32', 'UNICODE_STRING'])
    def cmdI9S1(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
        self.g_cmdI9S1.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)

    @unpack_func_args(['UINT8', 'UINT8', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UINT32', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI7S2(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_cmdI7S2.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['UINT8', 'UINT8', 'UNICODE_STRING'])
    def cmdS1(self, arg1, arg2, arg3):
        self.g_cmdS1.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT8', 'BLOB'])
    def cmdB1(self, arg1, arg2, arg3):
        self.g_cmdB1.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT8', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdS2(self, arg1, arg2, arg3, arg4):
        self.g_cmdS2.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'UNICODE_STRING'])
    def cmdI1S1(self, arg1, arg2, arg3, arg4):
        self.g_cmdI1S1.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI1S2(self, arg1, arg2, arg3, arg4, arg5):
        self.g_cmdI1S2.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT8', 'UINT8', 'INT32', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI1S3(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_cmdI1S3.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI1S4(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_cmdI1S4.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT64', 'UNICODE_STRING'])
    def cmdI2S1(self, arg1, arg2, arg3, arg4, arg5):
        self.g_cmdI2S1.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT32', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI2S2(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_cmdI2S2.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT32', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI2S3(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_cmdI2S3.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT32', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI2S4(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_cmdI2S4.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['UINT8', 'UINT8', 'INT64', 'INT32', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING', 'UNICODE_STRING'])
    def cmdI2S5(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_cmdI2S5.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['UINT8', 'UINT8', 'UNICODE_STRING', 'INT32'])
    def cmdS1I1(self, arg1, arg2, arg3, arg4):
        self.g_cmdS1I1.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'UINT8', 'DB_ID_LIST'])
    def cmdU1(self, arg1, arg2, arg3):
        self.g_cmdU1.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT8', 'DB_ID_LIST', 'UNICODE_STRING'])
    def cmdU1S1(self, arg1, arg2, arg3, arg4):
        self.g_cmdU1S1.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'UINT8', 'INT32', 'INT32', ['ARRAY', 'INT32'], ['ARRAY', 'INT32'], ['ARRAY', 'INT32'], ['ARRAY', 'INT32'], ['ARRAY', 'INT32'], ['ARRAY', 'INT32'], ['ARRAY', 'INT32']])
    def cmdI2U7(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_cmdI2U7.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['UINT8', 'UINT8', 'SHIP_ID', 'INT32', 'INT32', 'INT32', 'INT32', 'INT32', 'INT32', 'UNICODE_STRING', 'SHIP_RESTRICTIONS'])
    def cmdI7S1R1(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_cmdI7S1R1.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['UINT8', 'UINT8', 'TRAINING_ROOM_PROPERTIES'])
    def cmdT1(self, arg1, arg2, arg3):
        self.g_cmdT1.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT8', ['ARRAY', 'GAMEPARAMS_ID']])
    def cmdD1(self, arg1, arg2, arg3):
        self.g_cmdD1.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING', 'STRING'])
    def chatMessage(self, arg1, arg2):
        self.g_chatMessage.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB'])
    def dev_bot_setTestBattleParams(self, arg1):
        self.g_dev_bot_setTestBattleParams.fire(self, arg1)

    @unpack_func_args([])
    def dev_onSurveyClear(self):
        self.g_dev_onSurveyClear.fire(self)

    @unpack_func_args(['UINT64'])
    def checkGamePing(self, arg1):
        self.g_checkGamePing.fire(self, arg1)

    @unpack_func_args(['CLIENT_STAT_INFO'])
    def sendStatData(self, arg1):
        self.g_sendStatData.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'UINT8'], 'INT64', 'INT64'])
    def sendSurveyResults(self, arg1, arg2, arg3):
        self.g_sendSurveyResults.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING'])
    def newTraces(self, arg1):
        self.g_newTraces.fire(self, arg1)

    @unpack_func_args([])
    def dev_resetDailyLimits(self):
        self.g_dev_resetDailyLimits.fire(self)

    @unpack_func_args([])
    def dev_resetAbuse(self):
        self.g_dev_resetAbuse.fire(self)

    @unpack_func_args([])
    def dev_resetRecidivism(self):
        self.g_dev_resetRecidivism.fire(self)

    @unpack_func_args([])
    def dev_resetAbuseRating(self):
        self.g_dev_resetAbuseRating.fire(self)

    @unpack_func_args(['UINT32', 'BLOB', 'INT32'])
    def executeTransactionCl(self, arg1, arg2, arg3):
        self.g_executeTransactionCl.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING', 'INT16'])
    def dev_restoreAccountFromPoint(self, arg1, arg2):
        self.g_dev_restoreAccountFromPoint.fire(self, arg1, arg2)

    @unpack_func_args(['BOOL'])
    def dev_exportAccountToWeb(self, arg1):
        self.g_dev_exportAccountToWeb.fire(self, arg1)

    @unpack_func_args(['UINT16'])
    def dev_receiveExternalNotification(self, arg1):
        self.g_dev_receiveExternalNotification.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def dev_setAbuseStatus(self, arg1):
        self.g_dev_setAbuseStatus.fire(self, arg1)

    @unpack_func_args(['STRING', 'FLOAT'])
    def dev_setAbuseRecidivism(self, arg1, arg2):
        self.g_dev_setAbuseRecidivism.fire(self, arg1, arg2)

    @unpack_func_args(['FLOAT'])
    def dev_setAbuseRating(self, arg1):
        self.g_dev_setAbuseRating.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def testInvoice(self, arg1):
        self.g_testInvoice.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def tryGiveClientToReplayConnectionHandler(self, arg1):
        self.g_tryGiveClientToReplayConnectionHandler.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)