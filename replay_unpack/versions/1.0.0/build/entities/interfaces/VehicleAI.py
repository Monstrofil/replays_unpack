#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class VehicleAI(object):
    
    g_vehicleAI_autoBotScriptStep = EventHook()
    
    g_vehicleAI_autoBotReroute = EventHook()
    
    g_vehicleAI_onEvent = EventHook()
    
    g_vehicleAI_receiveVehicleID = EventHook()
    
    g_vehicleAI_createAutoBotController = EventHook()
    
    g_vehicleAI_autoBotScriptStep = EventHook()
    
    g_vehicleAI_autoBotScriptCallback = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'PYTHON', ['ARRAY', 'INT32'], ['ARRAY', 'INT32']])
    def vehicleAI_autoBotScriptStep(self, arg1, arg2, arg3, arg4):
        self.g_vehicleAI_autoBotScriptStep.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['STRING', 'PYTHON'])
    def vehicleAI_autoBotReroute(self, arg1, arg2):
        self.g_vehicleAI_autoBotReroute.fire(self, arg1, arg2)

    @unpack_func_args(['STRING', 'STRING'])
    def vehicleAI_onEvent(self, arg1, arg2):
        self.g_vehicleAI_onEvent.fire(self, arg1, arg2)

    @unpack_func_args(['STRING', 'OBJECT_ID'])
    def vehicleAI_receiveVehicleID(self, arg1, arg2):
        self.g_vehicleAI_receiveVehicleID.fire(self, arg1, arg2)

    @unpack_func_args(['STRING', 'PYTHON'])
    def vehicleAI_createAutoBotController(self, arg1, arg2):
        self.g_vehicleAI_createAutoBotController.fire(self, arg1, arg2)

    @unpack_func_args(['PYTHON'])
    def vehicleAI_autoBotScriptStep(self, arg1):
        self.g_vehicleAI_autoBotScriptStep.fire(self, arg1)

    @unpack_func_args(['INT32', 'PYTHON'])
    def vehicleAI_autoBotScriptCallback(self, arg1, arg2):
        self.g_vehicleAI_autoBotScriptCallback.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)