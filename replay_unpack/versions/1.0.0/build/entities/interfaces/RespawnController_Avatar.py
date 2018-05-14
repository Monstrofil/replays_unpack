#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class RespawnController_Avatar(object):
    
    g_respawnController_requestRespawnGroupChange = EventHook()
    
    g_respawnController_chooseVehicleForRespawn = EventHook()
    
    g_respawnController_performRespawn = EventHook()
    
    g_respawnController_redrawVehicleOnRespawn = EventHook()
    
    g_respawnController_explodeVehicleBeforeRespawn = EventHook()
    
    g_respawnController_updateRespawnVehicles = EventHook()
    
    g_respawnController_updateRespawnCooldowns = EventHook()
    
    g_respawnController_updateRespawnInfo = EventHook()
    
    g_respawnController_updateVehicleLimits = EventHook()
    
    g_respawnController_onTeamLivesRestored = EventHook()
    
    g_respawnController_updatePlayerLives = EventHook()
    
    g_redrawVehicleOnRespawn = EventHook()
    
    g_explodeVehicleBeforeRespawn = EventHook()
    
    g_updateRespawnVehicles = EventHook()
    
    g_updateRespawnCooldowns = EventHook()
    
    g_updateRespawnInfo = EventHook()
    
    g_updateVehicleLimits = EventHook()
    
    g_updatePlayerLives = EventHook()
    
    g_onTeamLivesRestored = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8'])
    def respawnController_requestRespawnGroupChange(self, arg1):
        self.g_respawnController_requestRespawnGroupChange.fire(self, arg1)

    @unpack_func_args(['UINT16'])
    def respawnController_chooseVehicleForRespawn(self, arg1):
        self.g_respawnController_chooseVehicleForRespawn.fire(self, arg1)

    @unpack_func_args([])
    def respawnController_performRespawn(self):
        self.g_respawnController_performRespawn.fire(self)

    @unpack_func_args(['OBJECT_ID', 'STRING', 'STRING'])
    def respawnController_redrawVehicleOnRespawn(self, arg1, arg2, arg3):
        self.g_respawnController_redrawVehicleOnRespawn.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID'])
    def respawnController_explodeVehicleBeforeRespawn(self, arg1):
        self.g_respawnController_explodeVehicleBeforeRespawn.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'RESPAWN_AVAILABLE_VEHICLE']])
    def respawnController_updateRespawnVehicles(self, arg1):
        self.g_respawnController_updateRespawnVehicles.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'RESPAWN_COOLDOWN_ITEM']])
    def respawnController_updateRespawnCooldowns(self, arg1):
        self.g_respawnController_updateRespawnCooldowns.fire(self, arg1)

    @unpack_func_args(['RESPAWN_INFO'])
    def respawnController_updateRespawnInfo(self, arg1):
        self.g_respawnController_updateRespawnInfo.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'RESPAWN_LIMITED_VEHICLES']])
    def respawnController_updateVehicleLimits(self, arg1):
        self.g_respawnController_updateVehicleLimits.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'UINT8']])
    def respawnController_onTeamLivesRestored(self, arg1):
        self.g_respawnController_onTeamLivesRestored.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def respawnController_updatePlayerLives(self, arg1):
        self.g_respawnController_updatePlayerLives.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'STRING', 'STRING'])
    def redrawVehicleOnRespawn(self, arg1, arg2, arg3):
        self.g_redrawVehicleOnRespawn.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID'])
    def explodeVehicleBeforeRespawn(self, arg1):
        self.g_explodeVehicleBeforeRespawn.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'RESPAWN_AVAILABLE_VEHICLE']])
    def updateRespawnVehicles(self, arg1):
        self.g_updateRespawnVehicles.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'RESPAWN_COOLDOWN_ITEM']])
    def updateRespawnCooldowns(self, arg1):
        self.g_updateRespawnCooldowns.fire(self, arg1)

    @unpack_func_args(['RESPAWN_INFO'])
    def updateRespawnInfo(self, arg1):
        self.g_updateRespawnInfo.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'RESPAWN_LIMITED_VEHICLES']])
    def updateVehicleLimits(self, arg1):
        self.g_updateVehicleLimits.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def updatePlayerLives(self, arg1):
        self.g_updatePlayerLives.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'UINT8']])
    def onTeamLivesRestored(self, arg1):
        self.g_onTeamLivesRestored.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)