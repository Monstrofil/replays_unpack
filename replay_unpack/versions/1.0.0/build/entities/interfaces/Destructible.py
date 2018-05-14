#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Destructible(object):
    
    g_receiveAndTakeOverProjectile = EventHook()
    
    g_receiveExplosion = EventHook()
    
    g_receiveRamming = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'UINT8', 'VECTOR3', 'VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32', 'ATTACKER_INFO', 'SHOT_ID', 'INT32', 'UINT8', 'UINT8', ['ARRAY', 'MAILBOX'], ['ARRAY', 'FLOAT32', 2], 'FLOAT32', 'FLOAT64', 'VECTOR3', 'VECTOR3', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT64'])
    def receiveAndTakeOverProjectile(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23):
        self.g_receiveAndTakeOverProjectile.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23)

    @unpack_func_args(['VECTOR3', 'FLOAT32', 'FLOAT32', ['ARRAY', ['ARRAY', 'FLOAT32', 3]], 'ATTACKER_INFO', 'SHOT_ID', 'INT32'])
    def receiveExplosion(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_receiveExplosion.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['UINT16', 'UINT8', 'FLOAT32', 'FLOAT32', 'ATTACKER_INFO'])
    def receiveRamming(self, arg1, arg2, arg3, arg4, arg5):
        self.g_receiveRamming.fire(self, arg1, arg2, arg3, arg4, arg5)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)