#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class TeamBase_Vehicle(object):
    
    g_teamBase_receivePoints = EventHook()
    
    g_teamBase_onCaptured = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'FLOAT32'])
    def teamBase_receivePoints(self, arg1, arg2):
        self.g_teamBase_receivePoints.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'FLOAT32', 'BOOL'])
    def teamBase_onCaptured(self, arg1, arg2, arg3):
        self.g_teamBase_onCaptured.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)