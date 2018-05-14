#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class DefenderBonusController_Vehicle(object):
    
    g_defenderBonus_onOwnSectorCaptured = EventHook()
    
    g_defenderBonus_onOwnDestructibleDestroyed = EventHook()
    
    g_defenderBonus_onPlayerGroupChanged = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def defenderBonus_onOwnSectorCaptured(self):
        self.g_defenderBonus_onOwnSectorCaptured.fire(self)

    @unpack_func_args([])
    def defenderBonus_onOwnDestructibleDestroyed(self):
        self.g_defenderBonus_onOwnDestructibleDestroyed.fire(self)

    @unpack_func_args([])
    def defenderBonus_onPlayerGroupChanged(self):
        self.g_defenderBonus_onPlayerGroupChanged.fire(self)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)