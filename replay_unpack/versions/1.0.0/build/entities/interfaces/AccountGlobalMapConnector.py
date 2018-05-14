#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountGlobalMapConnector(object):
    
    g_accountGlobalMapConnector_callGlobalMapMethod = EventHook()
    
    g_accountGlobalMapConnector_onGlobalMapUpdate = EventHook()
    
    g_accountGlobalMapConnector_onGlobalMapReply = EventHook()
    
    g_accountGlobalMapConnector_onSpecBattleRoundEnd = EventHook()
    
    g_accountGlobalMapConnector_onSpecBattleEnd = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT64', 'INT32', 'INT64', 'STRING'])
    def accountGlobalMapConnector_callGlobalMapMethod(self, arg1, arg2, arg3, arg4):
        self.g_accountGlobalMapConnector_callGlobalMapMethod.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['STRING', 'STRING'])
    def accountGlobalMapConnector_onGlobalMapUpdate(self, arg1, arg2):
        self.g_accountGlobalMapConnector_onGlobalMapUpdate.fire(self, arg1, arg2)

    @unpack_func_args(['UINT64', 'INT32', 'STRING'])
    def accountGlobalMapConnector_onGlobalMapReply(self, arg1, arg2, arg3):
        self.g_accountGlobalMapConnector_onGlobalMapReply.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['STRING'])
    def accountGlobalMapConnector_onSpecBattleRoundEnd(self, arg1):
        self.g_accountGlobalMapConnector_onSpecBattleRoundEnd.fire(self, arg1)

    @unpack_func_args(['STRING'])
    def accountGlobalMapConnector_onSpecBattleEnd(self, arg1):
        self.g_accountGlobalMapConnector_onSpecBattleEnd.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)