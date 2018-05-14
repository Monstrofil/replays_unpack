#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountUnitAssembler(object):
    
    g_accountUnitAssembler_acceptAutoSearch = EventHook()
    
    g_accountUnitAssembler_createEx = EventHook()
    
    g_accountUnitAssembler_joinEx = EventHook()
    
    g_accountUnitAssembler_onNeedToJoinToUnitMgr = EventHook()
    
    g_accountUnitAssembler_onAddAutoAssembledAccount = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT32', 'INT64'])
    def accountUnitAssembler_acceptAutoSearch(self, arg1, arg2):
        self.g_accountUnitAssembler_acceptAutoSearch.fire(self, arg1, arg2)

    @unpack_func_args(['INT32', 'INT32', 'PYTHON'])
    def accountUnitAssembler_createEx(self, arg1, arg2, arg3):
        self.g_accountUnitAssembler_createEx.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'INT32', 'PYTHON'])
    def accountUnitAssembler_joinEx(self, arg1, arg2, arg3):
        self.g_accountUnitAssembler_joinEx.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['MAILBOX', 'INT8', 'UINT16', 'INT32'])
    def accountUnitAssembler_onNeedToJoinToUnitMgr(self, arg1, arg2, arg3, arg4):
        self.g_accountUnitAssembler_onNeedToJoinToUnitMgr.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT32', 'PYTHON', 'BOOL'])
    def accountUnitAssembler_onAddAutoAssembledAccount(self, arg1, arg2, arg3):
        self.g_accountUnitAssembler_onAddAutoAssembledAccount.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)