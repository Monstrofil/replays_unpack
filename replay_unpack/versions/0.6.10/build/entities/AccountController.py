#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.Entity import Entity
from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


class AccountController(Entity):
    
    g_onKickedFromServer = EventHook()
    
    g_onCheckGamePing = EventHook()
    
    g_checkGamePing = EventHook()
    
    def __init__(self):

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def onKickedFromServer(self):
        self.g_onKickedFromServer.fire(self)

    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)

    @unpack_func_args([])
    def checkGamePing(self):
        self.g_checkGamePing.fire(self)


    ####################################
    #       PROPERTIES
    ####################################

