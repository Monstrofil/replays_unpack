#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ProtectionZone_Vehicle(object):
    
    g_protectionZone_onEnterProtectionZone = EventHook()
    
    g_protectionZone_onLeaveProtectionZone = EventHook()
    
    g_protectionZone_onProtectionZoneShooting = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8'])
    def protectionZone_onEnterProtectionZone(self, arg1):
        self.g_protectionZone_onEnterProtectionZone.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def protectionZone_onLeaveProtectionZone(self, arg1):
        self.g_protectionZone_onLeaveProtectionZone.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def protectionZone_onProtectionZoneShooting(self, arg1):
        self.g_protectionZone_onProtectionZoneShooting.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)