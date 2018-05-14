#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Harm(object):
    
    g_harm_receiveShot = EventHook()
    
    g_harm_receiveExplosion = EventHook()
    
    g_harm_receivePressure = EventHook()
    
    g_harm_receiveRamming = EventHook()
    
    g_harm_receiveMiss = EventHook()
    
    g_harm_receiveCeilingHit = EventHook()
    
    g_harm_receiveAttackResults = EventHook()
    
    g_harm_onCombatEquipmentShootingStarted = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['ATTACKER_INFO', 'SHOT_ID', 'INT32', 'UINT8', 'FLOAT32', 'VECTOR3', 'VECTOR3', ['ARRAY', 'FLOAT32', 2], ['ARRAY', ['ARRAY', 'FLOAT32', 4]], 'FLOAT32', ['ARRAY', 'FLOAT32']])
    def harm_receiveShot(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_harm_receiveShot.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['ATTACKER_INFO', 'SHOT_ID', 'INT32', 'VECTOR3', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'UINT8'])
    def harm_receiveExplosion(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_harm_receiveExplosion.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['BOOL', 'OBJECT_ID', 'FLOAT32'])
    def harm_receivePressure(self, arg1, arg2, arg3):
        self.g_harm_receivePressure.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'FLOAT32', 'FLOAT32', 'UINT8', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'BOOL'])
    def harm_receiveRamming(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_harm_receiveRamming.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['SHOT_ID', 'UINT16'])
    def harm_receiveMiss(self, arg1, arg2):
        self.g_harm_receiveMiss.fire(self, arg1, arg2)

    @unpack_func_args(['SHOT_ID', 'VECTOR3'])
    def harm_receiveCeilingHit(self, arg1, arg2):
        self.g_harm_receiveCeilingHit.fire(self, arg1, arg2)

    @unpack_func_args(['ATTACK_RESULTS'])
    def harm_receiveAttackResults(self, arg1):
        self.g_harm_receiveAttackResults.fire(self, arg1)

    @unpack_func_args(['UINT8', 'VECTOR3', 'FLOAT32', ['ARRAY', 'SHOT_ID']])
    def harm_onCombatEquipmentShootingStarted(self, arg1, arg2, arg3, arg4):
        self.g_harm_onCombatEquipmentShootingStarted.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)