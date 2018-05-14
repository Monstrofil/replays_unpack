#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class BomberController(object):
    
    g_bomberController_addBomber = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['ATTACKER_INFO', 'VECTOR3', 'VECTOR2', ['ARRAY', 'VECTOR2', 2], 'FLOAT32', 'FLOAT32', ['ARRAY', 'FLOAT32', 2], 'FLOAT32', 'FLOAT32', ['ARRAY', 'FLOAT32'], ['ARRAY', 'FLOAT32'], ['ARRAY', 'BOOL'], 'FLOAT32', 'UINT16', 'INT32', 'UINT8', ['ARRAY', 'FLOAT32', 2], 'FLOAT32', 'FLOAT64'])
    def bomberController_addBomber(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19):
        self.g_bomberController_addBomber.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)