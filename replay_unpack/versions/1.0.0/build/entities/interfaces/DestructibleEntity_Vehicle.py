#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class DestructibleEntity_Vehicle(object):
    
    g_destructibleEntity_showShotResults = EventHook()
    
    g_destructibleEntity_onDamaged = EventHook()
    
    g_destructibleEntity_onDestroyed = EventHook()
    
    g_destructibleEntity_onDefended = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'INT32'])
    def destructibleEntity_showShotResults(self, arg1, arg2):
        self.g_destructibleEntity_showShotResults.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'INT16'])
    def destructibleEntity_onDamaged(self, arg1, arg2):
        self.g_destructibleEntity_onDamaged.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'BOOL'])
    def destructibleEntity_onDestroyed(self, arg1, arg2):
        self.g_destructibleEntity_onDestroyed.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8'])
    def destructibleEntity_onDefended(self, arg1):
        self.g_destructibleEntity_onDefended.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)