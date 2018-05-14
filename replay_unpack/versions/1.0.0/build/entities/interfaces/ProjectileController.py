#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ProjectileController(object):
    
    g_projectileController_takeOverProjectile = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['ATTACKER_INFO', 'SHOT_ID', 'INT32', 'UINT8', 'UINT8', ['ARRAY', 'MAILBOX'], ['ARRAY', 'FLOAT32', 2], 'FLOAT32', 'FLOAT64', 'VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT64'])
    def projectileController_takeOverProjectile(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16):
        self.g_projectileController_takeOverProjectile.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)