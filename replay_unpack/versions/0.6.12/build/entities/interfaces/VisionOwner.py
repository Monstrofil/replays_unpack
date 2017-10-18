#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class VisionOwner(object):
    
    g_isInvisible = EventHook()
    
    g_onVisibilityChanged = EventHook()
    
    g_removeFromVision = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def isInvisible(self):
        self.g_isInvisible.fire(self)

    @unpack_func_args(['ENTITY_ID', 'UINT8'])
    def onVisibilityChanged(self, arg1, arg2):
        self.g_onVisibilityChanged.fire(self, arg1, arg2)

    @unpack_func_args(['ENTITY_ID'])
    def removeFromVision(self, arg1):
        self.g_removeFromVision.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)