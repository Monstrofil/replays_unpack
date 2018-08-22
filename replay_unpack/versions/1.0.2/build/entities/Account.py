#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from interfaces.Chat import Chat
from interfaces.PlayerMessenger_chat2 import PlayerMessenger_chat2
from interfaces.AccountEditor import AccountEditor
from interfaces.TransactionUser import TransactionUser
from interfaces.InterclusterSender import InterclusterSender
from interfaces.ClientCommandsPort import ClientCommandsPort
from interfaces.AccountAdmin import AccountAdmin
from interfaces.AccountClan import AccountClan
from interfaces.AccountAuthTokenProvider import AccountAuthTokenProvider
from interfaces.AccountAuthTokenProviderClient import AccountAuthTokenProviderClient
from interfaces.BattleResultProcessor import BattleResultProcessor
from interfaces.Invitations import Invitations
from interfaces.InvitationsClient import InvitationsClient
from interfaces.Invoicing import Invoicing
from interfaces.AccountPrebattle import AccountPrebattle
from interfaces.AccountSpaProcessor import AccountSpaProcessor
from interfaces.RefSystem import RefSystem
from interfaces.AccountIGRProcessing import AccountIGRProcessing
from interfaces.SessionTracker import SessionTracker
from interfaces.AccountGlobalMapConnector import AccountGlobalMapConnector
from interfaces.AccountSysMessenger import AccountSysMessenger
from interfaces.AccountUnit import AccountUnit
from interfaces.AccountUnitClient import AccountUnitClient
from interfaces.AccountUnitRemote import AccountUnitRemote
from interfaces.AccountUnitAssembler import AccountUnitAssembler
from interfaces.AccountUnitBrowser import AccountUnitBrowser
from interfaces.AccountDebugger import AccountDebugger



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
    
    def __init__(self):
        self.id = None
        self.position = None


        self._requiredVersion_10200 = 'ru_1.0.2_8'

        self._name = None

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

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (10000000000, 'requiredVersion_10200'),
            (10000000000, 'name'),
            (10000000000, 'initialServerSettings'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (10000000001, 'onKickedFromServer'),
            (9, 'onEnqueued'),
            (10000000001, 'onEnqueueFailure'),
            (9, 'onDequeued'),
            (129, 'onTutorialEnqueued'),
            (9, 'onKickedFromQueue'),
            (97, 'onUnitAssemblerSuccess'),
            (1, 'onArenaCreated'),
            (10000000001, 'onIGRTypeChanged'),
            (10000000001, 'onArenaJoinFailure'),
            (33, 'onPrebattleJoined'),
            (9, 'onPrebattleJoinFailure'),
            (1, 'onPrebattleLeft'),
            (9, 'onKickedFromArena'),
            (9, 'onKickedFromPrebattle'),
            (9, 'onCenterIsLongDisconnected'),
            (10000000002, 'showGUI'),
            (10000000001, 'receiveActiveArenas'),
            (65, 'receiveServerStats'),
            (10000000001, 'receiveQueueInfo'),
            (10000000001, 'updatePrebattle'),
            (10000000001, 'update'),
            (1, 'resyncDossiers'),
            (1, 'reloadShop'),
            (10000000001, 'onUnitUpdate'),
            (33, 'onUnitCallOk'),
            (10000000001, 'onUnitNotify'),
            (10000000001, 'onUnitError'),
            (10000000001, 'onUnitBrowserError'),
            (10000000001, 'onUnitBrowserResultsSet'),
            (10000000001, 'onUnitBrowserResultsUpdate'),
            (10000000001, 'onGlobalMapUpdate'),
            (10000000001, 'onGlobalMapReply'),
            (10000000001, 'onSendPrebattleInvites'),
            (10000000001, 'onClanInfoReceived'),
            (10000000001, 'receiveNotification'),
            (65, 'onEntityCheckOutEnqueued'),
            (1, 'onBootcampAccountMigrationComplete'),
            (1, 'chooseBootcampStart'),
            
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

# method size: 10000000001
    @unpack_func_args(['STRING', 'BOOL', 'UINT32'])
    def onKickedFromServer(self, arg1, arg2, arg3):
        self.g_onKickedFromServer.fire(self, arg1, arg2, arg3)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onEnqueued(self, arg1):
        self.g_onEnqueued.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UINT8', 'UINT8', 'STRING'])
    def onEnqueueFailure(self, arg1, arg2, arg3):
        self.g_onEnqueueFailure.fire(self, arg1, arg2, arg3)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onDequeued(self, arg1):
        self.g_onDequeued.fire(self, arg1)
# method size: 129
    @unpack_func_args(['UINT64', 'UINT32', 'INT32'])
    def onTutorialEnqueued(self, arg1, arg2, arg3):
        self.g_onTutorialEnqueued.fire(self, arg1, arg2, arg3)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onKickedFromQueue(self, arg1):
        self.g_onKickedFromQueue.fire(self, arg1)
# method size: 97
    @unpack_func_args(['UINT64', 'INT32'])
    def onUnitAssemblerSuccess(self, arg1, arg2):
        self.g_onUnitAssemblerSuccess.fire(self, arg1, arg2)
# method size: 1
    @unpack_func_args([])
    def onArenaCreated(self):
        self.g_onArenaCreated.fire(self)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def onIGRTypeChanged(self, arg1):
        self.g_onIGRTypeChanged.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UINT8', 'STRING'])
    def onArenaJoinFailure(self, arg1, arg2):
        self.g_onArenaJoinFailure.fire(self, arg1, arg2)
# method size: 33
    @unpack_func_args(['OBJECT_ID'])
    def onPrebattleJoined(self, arg1):
        self.g_onPrebattleJoined.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onPrebattleJoinFailure(self, arg1):
        self.g_onPrebattleJoinFailure.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def onPrebattleLeft(self):
        self.g_onPrebattleLeft.fire(self)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onKickedFromArena(self, arg1):
        self.g_onKickedFromArena.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onKickedFromPrebattle(self, arg1):
        self.g_onKickedFromPrebattle.fire(self, arg1)
# method size: 9
    @unpack_func_args(['BOOL'])
    def onCenterIsLongDisconnected(self, arg1):
        self.g_onCenterIsLongDisconnected.fire(self, arg1)
# method size: 10000000002
    @unpack_func_args(['STRING'])
    def showGUI(self, arg1):
        self.g_showGUI.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args([['ARRAY', 'PUBLIC_ARENA_INFO']])
    def receiveActiveArenas(self, arg1):
        self.g_receiveActiveArenas.fire(self, arg1)
# method size: 65
    @unpack_func_args(['SERVER_STATISTICS'])
    def receiveServerStats(self, arg1):
        self.g_receiveServerStats.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['QUEUE_INFO'])
    def receiveQueueInfo(self, arg1):
        self.g_receiveQueueInfo.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UINT8', 'STRING'])
    def updatePrebattle(self, arg1, arg2):
        self.g_updatePrebattle.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def update(self, arg1):
        self.g_update.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def resyncDossiers(self):
        self.g_resyncDossiers.fire(self)
# method size: 1
    @unpack_func_args([])
    def reloadShop(self):
        self.g_reloadShop.fire(self)
# method size: 10000000001
    @unpack_func_args(['UINT64', 'STRING', 'STRING'])
    def onUnitUpdate(self, arg1, arg2, arg3):
        self.g_onUnitUpdate.fire(self, arg1, arg2, arg3)
# method size: 33
    @unpack_func_args(['INT32'])
    def onUnitCallOk(self, arg1):
        self.g_onUnitCallOk.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['UINT64', 'INT32', 'STRING', 'PYTHON'])
    def onUnitNotify(self, arg1, arg2, arg3, arg4):
        self.g_onUnitNotify.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000001
    @unpack_func_args(['INT32', 'UINT64', 'INT32', 'STRING'])
    def onUnitError(self, arg1, arg2, arg3, arg4):
        self.g_onUnitError.fire(self, arg1, arg2, arg3, arg4)
# method size: 10000000001
    @unpack_func_args(['INT32', 'STRING'])
    def onUnitBrowserError(self, arg1, arg2):
        self.g_onUnitBrowserError.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def onUnitBrowserResultsSet(self, arg1):
        self.g_onUnitBrowserResultsSet.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def onUnitBrowserResultsUpdate(self, arg1):
        self.g_onUnitBrowserResultsUpdate.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['STRING', 'STRING'])
    def onGlobalMapUpdate(self, arg1, arg2):
        self.g_onGlobalMapUpdate.fire(self, arg1, arg2)
# method size: 10000000001
    @unpack_func_args(['UINT64', 'INT32', 'STRING'])
    def onGlobalMapReply(self, arg1, arg2, arg3):
        self.g_onGlobalMapReply.fire(self, arg1, arg2, arg3)
# method size: 10000000001
    @unpack_func_args(['DB_ID', 'STRING', 'DB_ID', 'STRING', 'UINT64', 'UINT8'])
    def onSendPrebattleInvites(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_onSendPrebattleInvites.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)
# method size: 10000000001
    @unpack_func_args(['DB_ID', 'STRING', 'STRING', 'STRING', 'STRING'])
    def onClanInfoReceived(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onClanInfoReceived.fire(self, arg1, arg2, arg3, arg4, arg5)
# method size: 10000000001
    @unpack_func_args(['STRING'])
    def receiveNotification(self, arg1):
        self.g_receiveNotification.fire(self, arg1)
# method size: 65
    @unpack_func_args(['UINT64'])
    def onEntityCheckOutEnqueued(self, arg1):
        self.g_onEntityCheckOutEnqueued.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def onBootcampAccountMigrationComplete(self):
        self.g_onBootcampAccountMigrationComplete.fire(self)
# method size: 1
    @unpack_func_args([])
    def chooseBootcampStart(self):
        self.g_chooseBootcampStart.fire(self)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 10000000000
    @property
    def requiredVersion_10200(self):
        return self._requiredVersion_10200

    @requiredVersion_10200.setter
    def requiredVersion_10200(self, value):
        self._requiredVersion_10200, = unpack_variables(value, ['STRING'])
# property size: 10000000000
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name, = unpack_variables(value, ['STRING'])
# property size: 10000000000
    @property
    def initialServerSettings(self):
        return self._initialServerSettings

    @initialServerSettings.setter
    def initialServerSettings(self, value):
        self._initialServerSettings, = unpack_variables(value, ['PYTHON'])


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