#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Sector_Vehicle(object):
    
    g_sector_onEnterSector = EventHook()
    
    g_sector_onLeaveSector = EventHook()
    
    g_sector_onEnemySectorCaptured = EventHook()
    
    g_sector_onSectorShooting = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['OBJECT_ID', 'UINT8', 'UINT8', 'UINT8', 'BOOL', 'FLOAT32', 'FLOAT32', 'UINT8'])
    def sector_onEnterSector(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_sector_onEnterSector.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['UINT8', 'UINT8'])
    def sector_onLeaveSector(self, arg1, arg2):
        self.g_sector_onLeaveSector.fire(self, arg1, arg2)

    @unpack_func_args([])
    def sector_onEnemySectorCaptured(self):
        self.g_sector_onEnemySectorCaptured.fire(self)

    @unpack_func_args(['UINT8'])
    def sector_onSectorShooting(self, arg1):
        self.g_sector_onSectorShooting.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)