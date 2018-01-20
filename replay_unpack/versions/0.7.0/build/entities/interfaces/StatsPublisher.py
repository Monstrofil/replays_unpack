#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class StatsPublisher(object):
    
    g_receivePublicIntStat = EventHook()
    
    g_receivePublicFloatStat = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def receivePublicIntStat(self):
        self.g_receivePublicIntStat.fire(self)

    @unpack_func_args([])
    def receivePublicFloatStat(self):
        self.g_receivePublicFloatStat.fire(self)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)