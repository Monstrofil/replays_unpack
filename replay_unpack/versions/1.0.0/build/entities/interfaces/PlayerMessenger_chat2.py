#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class PlayerMessenger_chat2(object):
    
    g_messenger_onActionByServer_chat2 = EventHook()
    
    g_messenger_onActionByClient_chat2 = EventHook()
    
    g_messenger_onActionForClient_chat2 = EventHook()
    
    g_messenger_onActionByServer_chat2 = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['MAILBOX', 'INT16', 'INT32', 'GENERIC_MESSENGER_ARGS_chat2'])
    def messenger_onActionByServer_chat2(self, arg1, arg2, arg3, arg4):
        self.g_messenger_onActionByServer_chat2.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT16', 'UINT16', 'GENERIC_MESSENGER_ARGS_chat2'])
    def messenger_onActionByClient_chat2(self, arg1, arg2, arg3):
        self.g_messenger_onActionByClient_chat2.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['MAILBOX', 'INT16', 'INT32', 'GENERIC_MESSENGER_ARGS_chat2'])
    def messenger_onActionForClient_chat2(self, arg1, arg2, arg3, arg4):
        self.g_messenger_onActionForClient_chat2.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT16', 'UINT16', 'GENERIC_MESSENGER_ARGS_chat2'])
    def messenger_onActionByServer_chat2(self, arg1, arg2, arg3):
        self.g_messenger_onActionByServer_chat2.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)