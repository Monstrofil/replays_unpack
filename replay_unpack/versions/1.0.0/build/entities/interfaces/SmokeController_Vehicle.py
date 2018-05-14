#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class SmokeController_Vehicle(object):
    
    g_smokeController_onEnterSmoke = EventHook()
    
    g_smokeController_onLeaveSmoke = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT32', 'FLOAT32'])
    def smokeController_onEnterSmoke(self, arg1, arg2):
        self.g_smokeController_onEnterSmoke.fire(self, arg1, arg2)

    @unpack_func_args(['UINT32'])
    def smokeController_onLeaveSmoke(self, arg1):
        self.g_smokeController_onLeaveSmoke.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)