#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class RecoveryMechanic_Vehicle(object):
    
    g_recoveryMechanic_onActivate = EventHook()
    
    g_recoveryMechanic_onDeactivate = EventHook()
    
    g_recoveryMechanic_startRecovering = EventHook()
    
    g_recoveryMechanic_stopRecovering = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def recoveryMechanic_onActivate(self):
        self.g_recoveryMechanic_onActivate.fire(self)

    @unpack_func_args([])
    def recoveryMechanic_onDeactivate(self):
        self.g_recoveryMechanic_onDeactivate.fire(self)

    @unpack_func_args([])
    def recoveryMechanic_startRecovering(self):
        self.g_recoveryMechanic_startRecovering.fire(self)

    @unpack_func_args([])
    def recoveryMechanic_stopRecovering(self):
        self.g_recoveryMechanic_stopRecovering.fire(self)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)