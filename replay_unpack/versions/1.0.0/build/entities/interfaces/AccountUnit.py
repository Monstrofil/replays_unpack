#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountUnit(object):
    
    g_accountUnit_processUnitMgrRepublish = EventHook()
    
    g_accountUnit_sendSquadInvitations = EventHook()
    
    g_accountUnit_sendUnitUpdate = EventHook()
    
    g_accountUnit_onUnitChangedLeader = EventHook()
    
    g_accountUnit_onUnitArenaCreated = EventHook()
    
    g_accountUnit_onSquadPlayerAdded = EventHook()
    
    g_accountUnit_setQueueingTime = EventHook()
    
    g_accountUnit_onUnitJoin = EventHook()
    
    g_accountUnit_onUnitLeave = EventHook()
    
    g_accountUnit_onUnitCall = EventHook()
    
    g_accountUnit_onUnitNotify = EventHook()
    
    g_accountUnit_sendExternalNotify = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def accountUnit_processUnitMgrRepublish(self):
        self.g_accountUnit_processUnitMgrRepublish.fire(self)

    @unpack_func_args(['INT64', ['ARRAY', 'DB_ID'], 'STRING'])
    def accountUnit_sendSquadInvitations(self, arg1, arg2, arg3):
        self.g_accountUnit_sendSquadInvitations.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT64', 'STRING', 'STRING'])
    def accountUnit_sendUnitUpdate(self, arg1, arg2, arg3):
        self.g_accountUnit_sendUnitUpdate.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['MAILBOX', 'BOOL'])
    def accountUnit_onUnitChangedLeader(self, arg1, arg2):
        self.g_accountUnit_onUnitChangedLeader.fire(self, arg1, arg2)

    @unpack_func_args(['MAILBOX', 'UINT64', 'UINT8', 'OBJECT_ID', 'UINT8', 'INT32', 'PYTHON', 'PYTHON', 'PYTHON'])
    def accountUnit_onUnitArenaCreated(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_accountUnit_onUnitArenaCreated.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['BOOL'])
    def accountUnit_onSquadPlayerAdded(self, arg1):
        self.g_accountUnit_onSquadPlayerAdded.fire(self, arg1)

    @unpack_func_args(['INT64'])
    def accountUnit_setQueueingTime(self, arg1):
        self.g_accountUnit_setQueueingTime.fire(self, arg1)

    @unpack_func_args(['INT64', 'MAILBOX', 'INT32', 'PYTHON'])
    def accountUnit_onUnitJoin(self, arg1, arg2, arg3, arg4):
        self.g_accountUnit_onUnitJoin.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT64', 'INT32', 'UINT64'])
    def accountUnit_onUnitLeave(self, arg1, arg2, arg3):
        self.g_accountUnit_onUnitLeave.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT64', 'INT32', 'UINT64', 'STRING', 'PYTHON'])
    def accountUnit_onUnitCall(self, arg1, arg2, arg3, arg4, arg5):
        self.g_accountUnit_onUnitCall.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT64', 'INT32', 'PYTHON'])
    def accountUnit_onUnitNotify(self, arg1, arg2, arg3):
        self.g_accountUnit_onUnitNotify.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'STRING', 'PYTHON'])
    def accountUnit_sendExternalNotify(self, arg1, arg2, arg3):
        self.g_accountUnit_sendExternalNotify.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)