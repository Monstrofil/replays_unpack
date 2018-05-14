#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class RecoveryMechanic_Avatar(object):
    
    g_recoveryMechanic_notifyCannotStartRecovering = EventHook()
    
    g_recoveryMechanic_notifyCancelled = EventHook()
    
    g_recoveryMechanic_updateState = EventHook()
    
    g_notifyCannotStartRecovering = EventHook()
    
    g_notifyCancelled = EventHook()
    
    g_updateState = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def recoveryMechanic_notifyCannotStartRecovering(self):
        self.g_recoveryMechanic_notifyCannotStartRecovering.fire(self)

    @unpack_func_args([])
    def recoveryMechanic_notifyCancelled(self):
        self.g_recoveryMechanic_notifyCancelled.fire(self)

    @unpack_func_args(['BOOL', 'INT32', 'INT32', 'FLOAT32'])
    def recoveryMechanic_updateState(self, arg1, arg2, arg3, arg4):
        self.g_recoveryMechanic_updateState.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args([])
    def notifyCannotStartRecovering(self):
        self.g_notifyCannotStartRecovering.fire(self)

    @unpack_func_args([])
    def notifyCancelled(self):
        self.g_notifyCancelled.fire(self)

    @unpack_func_args(['BOOL', 'INT32', 'INT32', 'FLOAT32'])
    def updateState(self, arg1, arg2, arg3, arg4):
        self.g_updateState.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)