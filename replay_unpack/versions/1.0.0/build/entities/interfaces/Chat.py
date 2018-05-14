#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Chat(object):
    
    g_joinChatChannel = EventHook()
    
    g_leaveChatChannel = EventHook()
    
    g_onChatAction = EventHook()
    
    g_onUserChatChannelCreated = EventHook()
    
    g_chatCommandFromClient = EventHook()
    
    g_chatCommand = EventHook()
    
    g_inviteCommand = EventHook()
    
    g_ackCommand = EventHook()
    
    g_keepAlive = EventHook()
    
    g_onChatAction = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['OBJECT_ID', 'STRING'])
    def joinChatChannel(self, arg1, arg2):
        self.g_joinChatChannel.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID'])
    def leaveChatChannel(self, arg1):
        self.g_leaveChatChannel.fire(self, arg1)

    @unpack_func_args(['CHAT_ACTION_DATA'])
    def onChatAction(self, arg1):
        self.g_onChatAction.fire(self, arg1)

    @unpack_func_args(['MAILBOX', 'PYTHON'])
    def onUserChatChannelCreated(self, arg1, arg2):
        self.g_onUserChatChannelCreated.fire(self, arg1, arg2)

    @unpack_func_args(['INT64', 'UINT8', 'OBJECT_ID', 'INT64', 'INT16', 'STRING', 'STRING'])
    def chatCommandFromClient(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_chatCommandFromClient.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['MAILBOX', 'INT64', 'UINT8', 'OBJECT_ID', 'INT64', 'INT16', 'STRING', 'STRING'])
    def chatCommand(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_chatCommand.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['INT64', 'UINT8', 'INT8', 'STRING', 'INT64', 'INT16', 'STRING', 'STRING'])
    def inviteCommand(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_inviteCommand.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['INT64', 'UINT8', 'FLOAT64', 'INT64', 'INT64'])
    def ackCommand(self, arg1, arg2, arg3, arg4, arg5):
        self.g_ackCommand.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['OBJECT_ID', 'INT16'])
    def keepAlive(self, arg1, arg2):
        self.g_keepAlive.fire(self, arg1, arg2)

    @unpack_func_args(['CHAT_ACTION_DATA'])
    def onChatAction(self, arg1):
        self.g_onChatAction.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)