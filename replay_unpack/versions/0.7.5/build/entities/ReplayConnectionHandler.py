#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ReplayConnectionHandler(object):
    
    g_onCheckGamePing = EventHook()
    
    g_onShutDownChanged = EventHook()
    
    g_stopReplay = EventHook()
    
    g_checkGamePing = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)

    @unpack_func_args([])
    def onShutDownChanged(self):
        self.g_onShutDownChanged.fire(self)

    @unpack_func_args([])
    def stopReplay(self):
        self.g_stopReplay.fire(self)

    @unpack_func_args(['UINT64'])
    def checkGamePing(self, arg1):
        self.g_checkGamePing.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)