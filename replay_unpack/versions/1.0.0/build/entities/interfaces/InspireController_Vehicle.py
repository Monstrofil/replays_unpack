#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class InspireController_Vehicle(object):
    
    g_inspireController_startInspire = EventHook()
    
    g_inspireController_onInspireEntered = EventHook()
    
    g_inspireController_onInspireLeft = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT16', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32'])
    def inspireController_startInspire(self, arg1, arg2, arg3, arg4, arg5):
        self.g_inspireController_startInspire.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['OBJECT_ID', 'FLOAT32'])
    def inspireController_onInspireEntered(self, arg1, arg2):
        self.g_inspireController_onInspireEntered.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'FLOAT32'])
    def inspireController_onInspireLeft(self, arg1, arg2):
        self.g_inspireController_onInspireLeft.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)