#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountPrebattle(object):
    
    g_accountPrebattle_onPrebattleJoined = EventHook()
    
    g_accountPrebattle_onPrebattleJoinFailure = EventHook()
    
    g_accountPrebattle_onPrebattleLeft = EventHook()
    
    g_accountPrebattle_onKickedFromPrebattle = EventHook()
    
    g_accountPrebattle_onPrebattleResponse = EventHook()
    
    g_accountPrebattle_onPrebattleVehicleChanged = EventHook()
    
    g_accountPrebattle_createTraining = EventHook()
    
    g_accountPrebattle_createDevPrebattle = EventHook()
    
    g_accountPrebattle_createEpicDevPrebattle = EventHook()
    
    g_accountPrebattle_sendPrebattleInvites = EventHook()
    
    g_accountPrebattle_receivePrebattleRoster = EventHook()
    
    g_accountPrebattle_updatePrebattle = EventHook()
    
    g_accountPrebattle_addPrebattleInvite = EventHook()
    
    g_accountPrebattle_onSendPrebattleInvites = EventHook()
    
    g_accountPrebattle_updateGroup = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['OBJECT_ID', 'UINT8', 'UINT32'])
    def accountPrebattle_onPrebattleJoined(self, arg1, arg2, arg3):
        self.g_accountPrebattle_onPrebattleJoined.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID', 'UINT8'])
    def accountPrebattle_onPrebattleJoinFailure(self, arg1, arg2):
        self.g_accountPrebattle_onPrebattleJoinFailure.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID'])
    def accountPrebattle_onPrebattleLeft(self, arg1):
        self.g_accountPrebattle_onPrebattleLeft.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'UINT8'])
    def accountPrebattle_onKickedFromPrebattle(self, arg1, arg2):
        self.g_accountPrebattle_onKickedFromPrebattle.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'INT16', 'BOOL', 'STRING', 'INT32'])
    def accountPrebattle_onPrebattleResponse(self, arg1, arg2, arg3, arg4, arg5):
        self.g_accountPrebattle_onPrebattleResponse.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['OBJECT_ID', 'INT8', 'INT32', 'INT32'])
    def accountPrebattle_onPrebattleVehicleChanged(self, arg1, arg2, arg3, arg4):
        self.g_accountPrebattle_onPrebattleVehicleChanged.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'INT32', 'BOOL', 'STRING'])
    def accountPrebattle_createTraining(self, arg1, arg2, arg3, arg4):
        self.g_accountPrebattle_createTraining.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT8', 'INT32', 'INT32', 'STRING'])
    def accountPrebattle_createDevPrebattle(self, arg1, arg2, arg3, arg4):
        self.g_accountPrebattle_createDevPrebattle.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'STRING'])
    def accountPrebattle_createEpicDevPrebattle(self, arg1, arg2):
        self.g_accountPrebattle_createEpicDevPrebattle.fire(self, arg1, arg2)

    @unpack_func_args([['ARRAY', 'INT64'], 'STRING'])
    def accountPrebattle_sendPrebattleInvites(self, arg1, arg2):
        self.g_accountPrebattle_sendPrebattleInvites.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'PYTHON'])
    def accountPrebattle_receivePrebattleRoster(self, arg1, arg2):
        self.g_accountPrebattle_receivePrebattleRoster.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'STRING'])
    def accountPrebattle_updatePrebattle(self, arg1, arg2, arg3):
        self.g_accountPrebattle_updatePrebattle.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID', 'INT32', 'PREBATTLE_INVITE'])
    def accountPrebattle_addPrebattleInvite(self, arg1, arg2, arg3):
        self.g_accountPrebattle_addPrebattleInvite.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['DB_ID', 'STRING', 'DB_ID', 'STRING', 'UINT64', 'UINT8'])
    def accountPrebattle_onSendPrebattleInvites(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountPrebattle_onSendPrebattleInvites.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['OBJECT_ID', 'UINT8'])
    def accountPrebattle_updateGroup(self, arg1, arg2):
        self.g_accountPrebattle_updateGroup.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)