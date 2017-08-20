#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.Entity import Entity
from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class DebugDrawEntity(object):
    
    g_debugExec = EventHook()
    
    g_drawDebugLine = EventHook()
    
    g_drawDebugCircle = EventHook()
    
    g_drawDebugCross = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['STRING', 'BLOB'])
    def debugExec(self, arg1, arg2):
        self.g_debugExec.fire(self, arg1, arg2)

    @unpack_func_args(['VECTOR3', 'VECTOR3', 'UINT32', 'UINT32'])
    def drawDebugLine(self, arg1, arg2, arg3, arg4):
        self.g_drawDebugLine.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['VECTOR3', 'FLOAT32', 'UINT32', 'UINT32'])
    def drawDebugCircle(self, arg1, arg2, arg3, arg4):
        self.g_drawDebugCircle.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['VECTOR3', 'FLOAT32', 'UINT32', 'UINT32'])
    def drawDebugCross(self, arg1, arg2, arg3, arg4):
        self.g_drawDebugCross.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)