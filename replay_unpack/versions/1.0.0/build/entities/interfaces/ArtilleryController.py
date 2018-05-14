#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ArtilleryController(object):
    
    g_artilleryController_addArtilleryPreparation = EventHook()
    
    g_artilleryController_addArtillery = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['ATTACKER_INFO', 'VECTOR3', 'VECTOR3', ['ARRAY', 'FLOAT32', 2], ['ARRAY', 'FLOAT32', 2], 'FLOAT32', 'FLOAT32', 'FLOAT32', ['ARRAY', 'FLOAT32', 2], ['ARRAY', 'FLOAT32', 2], ['ARRAY', 'UINT16', 2], 'INT32', ['ARRAY', 'FLOAT32', 2], 'FLOAT64'])
    def artilleryController_addArtilleryPreparation(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14):
        self.g_artilleryController_addArtilleryPreparation.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)

    @unpack_func_args(['ATTACKER_INFO', 'VECTOR3', 'VECTOR3', ['ARRAY', 'FLOAT32', 2], ['ARRAY', 'FLOAT32', 2], 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'UINT16', 'FLOAT32', 'INT32', ['ARRAY', 'FLOAT32', 2], 'FLOAT64'])
    def artilleryController_addArtillery(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
        self.g_artilleryController_addArtillery.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)