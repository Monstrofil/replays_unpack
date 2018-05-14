#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountUnitClient(object):
    
    g_accountUnitClient_create = EventHook()
    
    g_accountUnitClient_join = EventHook()
    
    g_accountUnitClient_doCmd = EventHook()
    
    g_accountUnitClient_sendInvites = EventHook()
    
    g_accountUnitClient_setRosterSlots = EventHook()
    
    g_accountUnitClient_createEx = EventHook()
    
    g_accountUnitClient_joinEx = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT32', 'INT32', 'INT32'])
    def accountUnitClient_create(self, arg1, arg2, arg3):
        self.g_accountUnitClient_create.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'UINT64', 'INT32'])
    def accountUnitClient_join(self, arg1, arg2, arg3):
        self.g_accountUnitClient_join.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'OBJECT_ID', 'INT32', 'UINT64', 'INT32', 'STRING'])
    def accountUnitClient_doCmd(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountUnitClient_doCmd.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['INT32', 'UINT64', ['ARRAY', 'DB_ID'], 'STRING'])
    def accountUnitClient_sendInvites(self, arg1, arg2, arg3, arg4):
        self.g_accountUnitClient_sendInvites.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'UINT64', ['ARRAY', 'INT32'], ['ARRAY', 'STRING']])
    def accountUnitClient_setRosterSlots(self, arg1, arg2, arg3, arg4):
        self.g_accountUnitClient_setRosterSlots.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'INT32', 'PYTHON'])
    def accountUnitClient_createEx(self, arg1, arg2, arg3):
        self.g_accountUnitClient_createEx.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'INT32', 'PYTHON'])
    def accountUnitClient_joinEx(self, arg1, arg2, arg3):
        self.g_accountUnitClient_joinEx.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)