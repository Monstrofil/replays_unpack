#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.Entity import Entity
from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


class ReplayLeech(Entity):
    
    g_onCheckGamePing = EventHook()
    
    g_replayFromBeginning = EventHook()
    
    g_syncChunk = EventHook()
    
    g_checkGamePing = EventHook()
    
    g_onBecomePlayer = EventHook()
    
    def __init__(self):

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def replayFromBeginning(self, arg1):
        self.g_replayFromBeginning.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def syncChunk(self, arg1):
        self.g_syncChunk.fire(self, arg1)

    @unpack_func_args([])
    def checkGamePing(self):
        self.g_checkGamePing.fire(self)

    @unpack_func_args([])
    def onBecomePlayer(self):
        self.g_onBecomePlayer.fire(self)


    ####################################
    #       PROPERTIES
    ####################################

