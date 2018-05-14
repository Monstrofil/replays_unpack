#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class SectorBase_Vehicle(object):
    
    g_sectorBase_receivePoints = EventHook()
    
    g_sectorBase_onCaptured = EventHook()
    
    g_sectorBase_onAction = EventHook()
    
    g_sectorBase_onCapturePointsBlocked = EventHook()
    
    g_sectorBase_onCapturePointsBlockedComplete = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'FLOAT32'])
    def sectorBase_receivePoints(self, arg1, arg2):
        self.g_sectorBase_receivePoints.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'FLOAT32', 'BOOL'])
    def sectorBase_onCaptured(self, arg1, arg2, arg3):
        self.g_sectorBase_onCaptured.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT8', 'FLOAT32'])
    def sectorBase_onAction(self, arg1, arg2, arg3):
        self.g_sectorBase_onAction.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'FLOAT32'])
    def sectorBase_onCapturePointsBlocked(self, arg1, arg2):
        self.g_sectorBase_onCapturePointsBlocked.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8'])
    def sectorBase_onCapturePointsBlockedComplete(self, arg1):
        self.g_sectorBase_onCapturePointsBlockedComplete.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)