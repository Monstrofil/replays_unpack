#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ProtectionZoneController_Avatar(object):
    
    g_protectionZone_enteringProtectionZone = EventHook()
    
    g_protectionZone_leavingProtectionZone = EventHook()
    
    g_protectionZone_protectionZoneShooting = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8'])
    def protectionZone_enteringProtectionZone(self, arg1):
        self.g_protectionZone_enteringProtectionZone.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def protectionZone_leavingProtectionZone(self, arg1):
        self.g_protectionZone_leavingProtectionZone.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def protectionZone_protectionZoneShooting(self, arg1):
        self.g_protectionZone_protectionZoneShooting.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)