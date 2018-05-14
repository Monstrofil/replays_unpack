#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class RespawnController_Vehicle(object):
    
    g_respawnController_respawnScheduled = EventHook()
    
    g_respawnController_stopRespawn = EventHook()
    
    g_respawnController_suspendRespawn = EventHook()
    
    g_respawnController_respawn = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def respawnController_respawnScheduled(self):
        self.g_respawnController_respawnScheduled.fire(self)

    @unpack_func_args([])
    def respawnController_stopRespawn(self):
        self.g_respawnController_stopRespawn.fire(self)

    @unpack_func_args([])
    def respawnController_suspendRespawn(self):
        self.g_respawnController_suspendRespawn.fire(self)

    @unpack_func_args(['RESPAWN_INFO_VEHICLE', ['ARRAY', 'MAILBOX']])
    def respawnController_respawn(self, arg1, arg2):
        self.g_respawnController_respawn.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)