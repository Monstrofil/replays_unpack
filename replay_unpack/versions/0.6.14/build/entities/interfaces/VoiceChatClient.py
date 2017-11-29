#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class VoiceChatClient(object):
    
    g_loginVoiceChat = EventHook()
    
    g_joinVoiceChat = EventHook()
    
    g_signedCommandToClient = EventHook()
    
    g_receiveSignedCommand = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def loginVoiceChat(self):
        self.g_loginVoiceChat.fire(self)

    @unpack_func_args([])
    def joinVoiceChat(self):
        self.g_joinVoiceChat.fire(self)

    @unpack_func_args(['BLOB'])
    def signedCommandToClient(self, arg1):
        self.g_signedCommandToClient.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def receiveSignedCommand(self, arg1):
        self.g_receiveSignedCommand.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)