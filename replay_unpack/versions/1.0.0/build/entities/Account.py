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
    from interfaces.AccountEditor import AccountEditor
except:
    from AccountEditor import AccountEditor

try:
    from interfaces.TransactionUser import TransactionUser
except:
    from TransactionUser import TransactionUser

try:
    from interfaces.InterclusterSender import InterclusterSender
except:
    from InterclusterSender import InterclusterSender

try:
    from interfaces.ClientCommandsPort import ClientCommandsPort
except:
    from ClientCommandsPort import ClientCommandsPort

try:
    from interfaces.AccountAdmin import AccountAdmin
except:
    from AccountAdmin import AccountAdmin

try:
    from interfaces.AccountClan import AccountClan
except:
    from AccountClan import AccountClan

try:
    from interfaces.AccountAuthTokenProvider import AccountAuthTokenProvider
except:
    from AccountAuthTokenProvider import AccountAuthTokenProvider

try:
    from interfaces.AccountAuthTokenProviderClient import AccountAuthTokenProviderClient
except:
    from AccountAuthTokenProviderClient import AccountAuthTokenProviderClient

try:
    from interfaces.BattleResultProcessor import BattleResultProcessor
except:
    from BattleResultProcessor import BattleResultProcessor

try:
    from interfaces.Invitations import Invitations
except:
    from Invitations import Invitations

try:
    from interfaces.InvitationsClient import InvitationsClient
except:
    from InvitationsClient import InvitationsClient

try:
    from interfaces.Invoicing import Invoicing
except:
    from Invoicing import Invoicing

try:
    from interfaces.AccountPrebattle import AccountPrebattle
except:
    from AccountPrebattle import AccountPrebattle

try:
    from interfaces.AccountSpaProcessor import AccountSpaProcessor
except:
    from AccountSpaProcessor import AccountSpaProcessor

try:
    from interfaces.RefSystem import RefSystem
except:
    from RefSystem import RefSystem

try:
    from interfaces.AccountIGRProcessing import AccountIGRProcessing
except:
    from AccountIGRProcessing import AccountIGRProcessing

try:
    from interfaces.SessionTracker import SessionTracker
except:
    from SessionTracker import SessionTracker

try:
    from interfaces.AccountGlobalMapConnector import AccountGlobalMapConnector
except:
    from AccountGlobalMapConnector import AccountGlobalMapConnector

try:
    from interfaces.AccountSysMessenger import AccountSysMessenger
except:
    from AccountSysMessenger import AccountSysMessenger

try:
    from interfaces.AccountUnit import AccountUnit
except:
    from AccountUnit import AccountUnit

try:
    from interfaces.AccountUnitClient import AccountUnitClient
except:
    from AccountUnitClient import AccountUnitClient

try:
    from interfaces.AccountUnitRemote import AccountUnitRemote
except:
    from AccountUnitRemote import AccountUnitRemote

try:
    from interfaces.AccountUnitAssembler import AccountUnitAssembler
except:
    from AccountUnitAssembler import AccountUnitAssembler

try:
    from interfaces.AccountUnitBrowser import AccountUnitBrowser
except:
    from AccountUnitBrowser import AccountUnitBrowser

try:
    from interfaces.AccountDebugger import AccountDebugger
except:
    from AccountDebugger import AccountDebugger



class Account(Chat, PlayerMessenger_chat2, AccountEditor, TransactionUser, InterclusterSender, ClientCommandsPort, AccountAdmin, AccountClan, AccountAuthTokenProvider, AccountAuthTokenProviderClient, BattleResultProcessor, Invitations, InvitationsClient, Invoicing, AccountPrebattle, AccountSpaProcessor, RefSystem, AccountIGRProcessing, SessionTracker, AccountGlobalMapConnector, AccountSysMessenger, AccountUnit, AccountUnitClient, AccountUnitRemote, AccountUnitAssembler, AccountUnitBrowser, AccountDebugger):
    
    g_onKickedFromServer = EventHook()
    
    g_onEnqueued = EventHook()
    
    g_onEnqueueFailure = EventHook()
    
    g_onDequeued = EventHook()
    
    g_onTutorialEnqueued = EventHook()
    
    g_onKickedFromQueue = EventHook()
    
    g_onUnitAssemblerSuccess = EventHook()
    
    g_onArenaCreated = EventHook()
    
    g_onIGRTypeChanged = EventHook()
    
    g_onArenaJoinFailure = EventHook()
    
    g_onPrebattleJoined = EventHook()
    
    g_onPrebattleJoinFailure = EventHook()
    
    g_onPrebattleLeft = EventHook()
    
    g_onKickedFromArena = EventHook()
    
    g_onKickedFromPrebattle = EventHook()
    
    g_onCenterIsLongDisconnected = EventHook()
    
    g_showGUI = EventHook()
    
    g_receiveActiveArenas = EventHook()
    
    g_receiveServerStats = EventHook()
    
    g_receiveQueueInfo = EventHook()
    
    g_updatePrebattle = EventHook()
    
    g_update = EventHook()
    
    g_resyncDossiers = EventHook()
    
    g_reloadShop = EventHook()
    
    g_onUnitUpdate = EventHook()
    
    g_onUnitCallOk = EventHook()
    
    g_onUnitNotify = EventHook()
    
    g_onUnitError = EventHook()
    
    g_onUnitBrowserError = EventHook()
    
    g_onUnitBrowserResultsSet = EventHook()
    
    g_onUnitBrowserResultsUpdate = EventHook()
    
    g_onGlobalMapUpdate = EventHook()
    
    g_onGlobalMapReply = EventHook()
    
    g_onSendPrebattleInvites = EventHook()
    
    g_onClanInfoReceived = EventHook()
    
    g_receiveNotification = EventHook()
    
    g_onEntityCheckOutEnqueued = EventHook()
    
    g_onBootcampAccountMigrationComplete = EventHook()
    
    g_chooseBootcampStart = EventHook()
    
    g_onEnqueued = EventHook()
    
    g_onDequeued = EventHook()
    
    g_onTutorialEnqueued = EventHook()
    
    g_onArenaCreated = EventHook()
    
    g_onTutorialCreated = EventHook()
    
    g_onBootcampCreated = EventHook()
    
    g_onKickedFromQueue = EventHook()
    
    g_onKickedFromArena = EventHook()
    
    g_logClientSystem = EventHook()
    
    g_logClientSessionStats = EventHook()
    
    g_logStreamCorruption = EventHook()
    
    g_createAvatar = EventHook()
    
    g_releaseClientForLogin = EventHook()
    
    g_keepAliveFor = EventHook()
    
    g_stopKeepingAlive = EventHook()
    
    g_kickSelf = EventHook()
    
    g_destroyIfNoKeepers = EventHook()
    
    g_destroySelfForPeriphery = EventHook()
    
    g_fetchPrebattleAutoInvites = EventHook()
    
    g_sendPropertiesTo = EventHook()
    
    g_processWalletResponse = EventHook()
    
    g_processWGMoneyResponse = EventHook()
    
    g_extraWriteToDB = EventHook()
    
    g_receiveClanMemberInfo = EventHook()
    
    g_receiveClanMembersListDiff = EventHook()
    
    g_debugRunMethod = EventHook()
    
    g_updateVehDossiersCut = EventHook()
    
    g_updateVehicleDossiers = EventHook()
    
    g_receiveExternalNotification = EventHook()
    
    g_sendExternalNotificationReply = EventHook()
    
    g_setAction = EventHook()
    
    g_onClientDeath = EventHook()
    
    g_onEntityCheckedOut = EventHook()
    
    g_giveClientTo = EventHook()
    
    g_cancelEntityCheckOut = EventHook()
    
    g_onBootcampAccountDestroyed = EventHook()
    
    g_onGameSessionFinish = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._requiredVersion_10100 = 'ru_1.0.1'

        self._name = None

        self._normalizedName = None

        self._globalRating = 0.0

        self._ver = None

        self._accountType = None

        self._attrs = None

        self._premiumExpiryTime = None

        self._autoBanTime = None

        self._clanDBID = None

        self._lastUserMessageID = -1.0

        self._lastSystemMessageID = -1.0

        self._lastInternalSystemMessageID = -1.0

        self._vivoxCredentials = None

        self._jabberCredentials = None

        self._vhID = None

        self._incarnationID = None

        self._peripheryID = None

        self._saveTime = None

        self._lastPlayerActivityTime = None

        self._vehDossiersCutVer = None

        self._vehDossiersVer = None

        self._nextOffloadToPeripheryTime = None

        self._walletID = None

        self._extWalletID = None

        self._pdata = None

        self._bp = None

        self._initialServerSettings = None


        # MRO fix

        Chat.__init__(self)

        PlayerMessenger_chat2.__init__(self)

        AccountEditor.__init__(self)

        TransactionUser.__init__(self)

        InterclusterSender.__init__(self)

        ClientCommandsPort.__init__(self)

        AccountAdmin.__init__(self)

        AccountClan.__init__(self)

        AccountAuthTokenProvider.__init__(self)

        AccountAuthTokenProviderClient.__init__(self)

        BattleResultProcessor.__init__(self)

        Invitations.__init__(self)

        InvitationsClient.__init__(self)

        Invoicing.__init__(self)

        AccountPrebattle.__init__(self)

        AccountSpaProcessor.__init__(self)

        RefSystem.__init__(self)

        AccountIGRProcessing.__init__(self)

        SessionTracker.__init__(self)

        AccountGlobalMapConnector.__init__(self)

        AccountSysMessenger.__init__(self)

        AccountUnit.__init__(self)

        AccountUnitClient.__init__(self)

        AccountUnitRemote.__init__(self)

        AccountUnitAssembler.__init__(self)

        AccountUnitBrowser.__init__(self)

        AccountDebugger.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['STRING', 'BOOL', 'UINT32'])
    def onKickedFromServer(self, arg1, arg2, arg3):
        self.g_onKickedFromServer.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8'])
    def onEnqueued(self, arg1):
        self.g_onEnqueued.fire(self, arg1)

    @unpack_func_args(['UINT8', 'UINT8', 'STRING'])
    def onEnqueueFailure(self, arg1, arg2, arg3):
        self.g_onEnqueueFailure.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8'])
    def onDequeued(self, arg1):
        self.g_onDequeued.fire(self, arg1)

    @unpack_func_args(['UINT64', 'UINT32', 'INT32'])
    def onTutorialEnqueued(self, arg1, arg2, arg3):
        self.g_onTutorialEnqueued.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8'])
    def onKickedFromQueue(self, arg1):
        self.g_onKickedFromQueue.fire(self, arg1)

    @unpack_func_args(['UINT64', 'INT32'])
    def onUnitAssemblerSuccess(self, arg1, arg2):
        self.g_onUnitAssemblerSuccess.fire(self, arg1, arg2)

    @unpack_func_args([])
    def onArenaCreated(self):
        self.g_onArenaCreated.fire(self)

    @unpack_func_args(['STRING'])
    def onIGRTypeChanged(self, arg1):
        self.g_onIGRTypeChanged.fire(self, arg1)

    @unpack_func_args(['UINT8', 'STRING'])
    def onArenaJoinFailure(self, arg1, arg2):
        self.g_onArenaJoinFailure.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID'])
    def onPrebattleJoined(self, arg1):
        self.g_onPrebattleJoined.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def onPrebattleJoinFailure(self, arg1):
        self.g_onPrebattleJoinFailure.fire(self, arg1)

    @unpack_func_args([])
    def onPrebattleLeft(self):
        self.g_onPrebattleLeft.fire(self)

    @unpack_func_args(['UINT8'])
    def onKickedFromArena(self, arg1):
        self.g_onKickedFromArena.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def onKickedFromPrebattle(self, arg1):
        self.g_onKickedFromPrebattle.fire(self, arg1)

    @unpack_func_args(['BOOL'])
    def onCenterIsLongDisconnected(self, arg1):
        self.g_onCenterIsLongDisconnected.fire(self, arg1)

    @unpack_func_args(['STRING'])
    def showGUI(self, arg1):
        self.g_showGUI.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'PUBLIC_ARENA_INFO']])
    def receiveActiveArenas(self, arg1):
        self.g_receiveActiveArenas.fire(self, arg1)

    @unpack_func_args(['SERVER_STATISTICS'])
    def receiveServerStats(self, arg1):
        self.g_receiveServerStats.fire(self, arg1)

    @unpack_func_args(['QUEUE_INFO'])
    def receiveQueueInfo(self, arg1):
        self.g_receiveQueueInfo.fire(self, arg1)

    @unpack_func_args(['UINT8', 'STRING'])
    def updatePrebattle(self, arg1, arg2):
        self.g_updatePrebattle.fire(self, arg1, arg2)

    @unpack_func_args(['STRING'])
    def update(self, arg1):
        self.g_update.fire(self, arg1)

    @unpack_func_args([])
    def resyncDossiers(self):
        self.g_resyncDossiers.fire(self)

    @unpack_func_args([])
    def reloadShop(self):
        self.g_reloadShop.fire(self)

    @unpack_func_args(['UINT64', 'STRING', 'STRING'])
    def onUnitUpdate(self, arg1, arg2, arg3):
        self.g_onUnitUpdate.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32'])
    def onUnitCallOk(self, arg1):
        self.g_onUnitCallOk.fire(self, arg1)

    @unpack_func_args(['UINT64', 'INT32', 'STRING', 'PYTHON'])
    def onUnitNotify(self, arg1, arg2, arg3, arg4):
        self.g_onUnitNotify.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'UINT64', 'INT32', 'STRING'])
    def onUnitError(self, arg1, arg2, arg3, arg4):
        self.g_onUnitError.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'STRING'])
    def onUnitBrowserError(self, arg1, arg2):
        self.g_onUnitBrowserError.fire(self, arg1, arg2)

    @unpack_func_args(['STRING'])
    def onUnitBrowserResultsSet(self, arg1):
        self.g_onUnitBrowserResultsSet.fire(self, arg1)

    @unpack_func_args(['STRING'])
    def onUnitBrowserResultsUpdate(self, arg1):
        self.g_onUnitBrowserResultsUpdate.fire(self, arg1)

    @unpack_func_args(['STRING', 'STRING'])
    def onGlobalMapUpdate(self, arg1, arg2):
        self.g_onGlobalMapUpdate.fire(self, arg1, arg2)

    @unpack_func_args(['UINT64', 'INT32', 'STRING'])
    def onGlobalMapReply(self, arg1, arg2, arg3):
        self.g_onGlobalMapReply.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['DB_ID', 'STRING', 'DB_ID', 'STRING', 'UINT64', 'UINT8'])
    def onSendPrebattleInvites(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_onSendPrebattleInvites.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['DB_ID', 'STRING', 'STRING', 'STRING', 'STRING'])
    def onClanInfoReceived(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onClanInfoReceived.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['STRING'])
    def receiveNotification(self, arg1):
        self.g_receiveNotification.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def onEntityCheckOutEnqueued(self, arg1):
        self.g_onEntityCheckOutEnqueued.fire(self, arg1)

    @unpack_func_args([])
    def onBootcampAccountMigrationComplete(self):
        self.g_onBootcampAccountMigrationComplete.fire(self)

    @unpack_func_args([])
    def chooseBootcampStart(self):
        self.g_chooseBootcampStart.fire(self)

    @unpack_func_args(['UINT8'])
    def onEnqueued(self, arg1):
        self.g_onEnqueued.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def onDequeued(self, arg1):
        self.g_onDequeued.fire(self, arg1)

    @unpack_func_args(['STRING', 'UINT64'])
    def onTutorialEnqueued(self, arg1, arg2):
        self.g_onTutorialEnqueued.fire(self, arg1, arg2)

    @unpack_func_args(['MAILBOX', 'UINT64', 'UINT8', 'OBJECT_ID', 'UINT8', 'INT32', 'PYTHON'])
    def onArenaCreated(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_onArenaCreated.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['MAILBOX', 'UINT64', 'OBJECT_ID', 'UINT8', 'INT32'])
    def onTutorialCreated(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onTutorialCreated.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['MAILBOX', 'UINT64', 'OBJECT_ID', 'UINT8', 'INT32'])
    def onBootcampCreated(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onBootcampCreated.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT8'])
    def onKickedFromQueue(self, arg1):
        self.g_onKickedFromQueue.fire(self, arg1)

    @unpack_func_args(['UINT64', 'UINT8'])
    def onKickedFromArena(self, arg1, arg2):
        self.g_onKickedFromArena.fire(self, arg1, arg2)

    @unpack_func_args(['CLIENT_SYSTEM'])
    def logClientSystem(self, arg1):
        self.g_logClientSystem.fire(self, arg1)

    @unpack_func_args(['CLIENT_STATISTICS'])
    def logClientSessionStats(self, arg1):
        self.g_logClientSessionStats.fire(self, arg1)

    @unpack_func_args(['INT16', 'INT32', 'INT32', 'INT32', 'INT32'])
    def logStreamCorruption(self, arg1, arg2, arg3, arg4, arg5):
        self.g_logStreamCorruption.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['MAILBOX', 'MAILBOX', 'INT32', 'UINT8', 'VECTOR3', 'FLOAT32', 'PYTHON', 'BOOL', 'INT32', ['ARRAY', 'INT32']])
    def createAvatar(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
        self.g_createAvatar.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)

    @unpack_func_args(['MAILBOX', 'PYTHON', 'PYTHON'])
    def releaseClientForLogin(self, arg1, arg2, arg3):
        self.g_releaseClientForLogin.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['MAILBOX', 'INT32', 'UINT8', 'UINT16'])
    def keepAliveFor(self, arg1, arg2, arg3, arg4):
        self.g_keepAliveFor.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8'])
    def stopKeepingAlive(self, arg1):
        self.g_stopKeepingAlive.fire(self, arg1)

    @unpack_func_args(['STRING', 'BOOL', 'UINT32'])
    def kickSelf(self, arg1, arg2, arg3):
        self.g_kickSelf.fire(self, arg1, arg2, arg3)

    @unpack_func_args([])
    def destroyIfNoKeepers(self):
        self.g_destroyIfNoKeepers.fire(self)

    @unpack_func_args(['INT32', 'MAILBOX'])
    def destroySelfForPeriphery(self, arg1, arg2):
        self.g_destroySelfForPeriphery.fire(self, arg1, arg2)

    @unpack_func_args([])
    def fetchPrebattleAutoInvites(self):
        self.g_fetchPrebattleAutoInvites.fire(self)

    @unpack_func_args(['MAILBOX', 'INT32', ['ARRAY', 'STRING']])
    def sendPropertiesTo(self, arg1, arg2, arg3):
        self.g_sendPropertiesTo.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['MAILBOX', 'INT32', 'PYTHON'])
    def processWalletResponse(self, arg1, arg2, arg3):
        self.g_processWalletResponse.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['MAILBOX', 'INT32', 'PYTHON'])
    def processWGMoneyResponse(self, arg1, arg2, arg3):
        self.g_processWGMoneyResponse.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8'])
    def extraWriteToDB(self, arg1):
        self.g_extraWriteToDB.fire(self, arg1)

    @unpack_func_args(['DB_ID', 'DB_ID', 'STRING', 'STRING', 'STRING', 'STRING', 'DB_ID', 'INT32', 'INT32', 'STRING', 'STRING'])
    def receiveClanMemberInfo(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_receiveClanMemberInfo.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['DB_ID', 'STRING'])
    def receiveClanMembersListDiff(self, arg1, arg2):
        self.g_receiveClanMembersListDiff.fire(self, arg1, arg2)

    @unpack_func_args(['STRING', 'PYTHON'])
    def debugRunMethod(self, arg1, arg2):
        self.g_debugRunMethod.fire(self, arg1, arg2)

    @unpack_func_args([])
    def updateVehDossiersCut(self):
        self.g_updateVehDossiersCut.fire(self)

    @unpack_func_args([])
    def updateVehicleDossiers(self):
        self.g_updateVehicleDossiers.fire(self)

    @unpack_func_args(['PYTHON'])
    def receiveExternalNotification(self, arg1):
        self.g_receiveExternalNotification.fire(self, arg1)

    @unpack_func_args(['INT64', 'STRING', 'UINT8'])
    def sendExternalNotificationReply(self, arg1, arg2, arg3):
        self.g_sendExternalNotificationReply.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'PYTHON'])
    def setAction(self, arg1, arg2):
        self.g_setAction.fire(self, arg1, arg2)

    @unpack_func_args([])
    def onClientDeath(self):
        self.g_onClientDeath.fire(self)

    @unpack_func_args(['MAILBOX'])
    def onEntityCheckedOut(self, arg1):
        self.g_onEntityCheckedOut.fire(self, arg1)

    @unpack_func_args(['MAILBOX'])
    def giveClientTo(self, arg1):
        self.g_giveClientTo.fire(self, arg1)

    @unpack_func_args([])
    def cancelEntityCheckOut(self):
        self.g_cancelEntityCheckOut.fire(self)

    @unpack_func_args([])
    def onBootcampAccountDestroyed(self):
        self.g_onBootcampAccountDestroyed.fire(self)

    @unpack_func_args([])
    def onGameSessionFinish(self):
        self.g_onGameSessionFinish.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def requiredVersion_10100(self):
        return self._requiredVersion_10100

    @requiredVersion_10100.setter
    def requiredVersion_10100(self, value):
        self._requiredVersion_10100, = unpack_variables(value, ['STRING'])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name, = unpack_variables(value, ['STRING'])

    @property
    def normalizedName(self):
        return self._normalizedName

    @normalizedName.setter
    def normalizedName(self, value):
        self._normalizedName, = unpack_variables(value, ['STRING'])

    @property
    def globalRating(self):
        return self._globalRating

    @globalRating.setter
    def globalRating(self, value):
        self._globalRating, = unpack_variables(value, ['UINT32'])

    @property
    def ver(self):
        return self._ver

    @ver.setter
    def ver(self, value):
        self._ver, = unpack_variables(value, ['INT16'])

    @property
    def accountType(self):
        return self._accountType

    @accountType.setter
    def accountType(self, value):
        self._accountType, = unpack_variables(value, ['UINT32'])

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        self._attrs, = unpack_variables(value, ['UINT64'])

    @property
    def premiumExpiryTime(self):
        return self._premiumExpiryTime

    @premiumExpiryTime.setter
    def premiumExpiryTime(self, value):
        self._premiumExpiryTime, = unpack_variables(value, ['UINT32'])

    @property
    def autoBanTime(self):
        return self._autoBanTime

    @autoBanTime.setter
    def autoBanTime(self, value):
        self._autoBanTime, = unpack_variables(value, ['UINT32'])

    @property
    def clanDBID(self):
        return self._clanDBID

    @clanDBID.setter
    def clanDBID(self, value):
        self._clanDBID, = unpack_variables(value, ['DB_ID'])

    @property
    def lastUserMessageID(self):
        return self._lastUserMessageID

    @lastUserMessageID.setter
    def lastUserMessageID(self, value):
        self._lastUserMessageID, = unpack_variables(value, ['DB_ID'])

    @property
    def lastSystemMessageID(self):
        return self._lastSystemMessageID

    @lastSystemMessageID.setter
    def lastSystemMessageID(self, value):
        self._lastSystemMessageID, = unpack_variables(value, ['DB_ID'])

    @property
    def lastInternalSystemMessageID(self):
        return self._lastInternalSystemMessageID

    @lastInternalSystemMessageID.setter
    def lastInternalSystemMessageID(self, value):
        self._lastInternalSystemMessageID, = unpack_variables(value, ['DB_ID'])

    @property
    def vivoxCredentials(self):
        return self._vivoxCredentials

    @vivoxCredentials.setter
    def vivoxCredentials(self, value):
        self._vivoxCredentials, = unpack_variables(value, ['STRING'])

    @property
    def jabberCredentials(self):
        return self._jabberCredentials

    @jabberCredentials.setter
    def jabberCredentials(self, value):
        self._jabberCredentials, = unpack_variables(value, ['STRING'])

    @property
    def vhID(self):
        return self._vhID

    @vhID.setter
    def vhID(self, value):
        self._vhID, = unpack_variables(value, ['UINT64'])

    @property
    def incarnationID(self):
        return self._incarnationID

    @incarnationID.setter
    def incarnationID(self, value):
        self._incarnationID, = unpack_variables(value, ['UINT64'])

    @property
    def peripheryID(self):
        return self._peripheryID

    @peripheryID.setter
    def peripheryID(self, value):
        self._peripheryID, = unpack_variables(value, ['INT32'])

    @property
    def saveTime(self):
        return self._saveTime

    @saveTime.setter
    def saveTime(self, value):
        self._saveTime, = unpack_variables(value, ['INT32'])

    @property
    def lastPlayerActivityTime(self):
        return self._lastPlayerActivityTime

    @lastPlayerActivityTime.setter
    def lastPlayerActivityTime(self, value):
        self._lastPlayerActivityTime, = unpack_variables(value, ['INT32'])

    @property
    def vehDossiersCutVer(self):
        return self._vehDossiersCutVer

    @vehDossiersCutVer.setter
    def vehDossiersCutVer(self, value):
        self._vehDossiersCutVer, = unpack_variables(value, ['UINT8'])

    @property
    def vehDossiersVer(self):
        return self._vehDossiersVer

    @vehDossiersVer.setter
    def vehDossiersVer(self, value):
        self._vehDossiersVer, = unpack_variables(value, ['UINT8'])

    @property
    def nextOffloadToPeripheryTime(self):
        return self._nextOffloadToPeripheryTime

    @nextOffloadToPeripheryTime.setter
    def nextOffloadToPeripheryTime(self, value):
        self._nextOffloadToPeripheryTime, = unpack_variables(value, ['INT32'])

    @property
    def walletID(self):
        return self._walletID

    @walletID.setter
    def walletID(self, value):
        self._walletID, = unpack_variables(value, ['UINT64'])

    @property
    def extWalletID(self):
        return self._extWalletID

    @extWalletID.setter
    def extWalletID(self, value):
        self._extWalletID, = unpack_variables(value, ['UINT64'])

    @property
    def pdata(self):
        return self._pdata

    @pdata.setter
    def pdata(self, value):
        self._pdata, = unpack_variables(value, ['STRING'])

    @property
    def bp(self):
        return self._bp

    @bp.setter
    def bp(self, value):
        self._bp, = unpack_variables(value, ['PYTHON'])

    @property
    def initialServerSettings(self):
        return self._initialServerSettings

    @initialServerSettings.setter
    def initialServerSettings(self, value):
        self._initialServerSettings, = unpack_variables(value, ['PYTHON'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)