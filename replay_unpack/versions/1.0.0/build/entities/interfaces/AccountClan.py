#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountClan(object):
    
    g_accountClan_createClan = EventHook()
    
    g_accountClan_enterLeaveClan = EventHook()
    
    g_accountClan_processUrgentOps = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['MAILBOX', 'INT32', 'DB_ID', 'STRING', 'STRING', 'STRING', 'STRING', 'INT32', 'INT32', 'UINT32'])
    def accountClan_createClan(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
        self.g_accountClan_createClan.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)

    @unpack_func_args(['MAILBOX', 'INT32', 'DB_ID', 'DB_ID', 'UINT8', 'INT32', 'UINT32'])
    def accountClan_enterLeaveClan(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_accountClan_enterLeaveClan.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['STRING'])
    def accountClan_processUrgentOps(self, arg1):
        self.g_accountClan_processUrgentOps.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)