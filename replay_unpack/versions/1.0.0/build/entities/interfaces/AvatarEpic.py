#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AvatarEpic(object):
    
    g_welcomeToSector = EventHook()
    
    g_onStepRepairPointAction = EventHook()
    
    g_onSectorBaseAction = EventHook()
    
    g_enteringProtectionZone = EventHook()
    
    g_leavingProtectionZone = EventHook()
    
    g_protectionZoneShooting = EventHook()
    
    g_onSectorShooting = EventHook()
    
    g_onXPUpdated = EventHook()
    
    g_showDestructibleShotResults = EventHook()
    
    g_onDestructibleDestroyed = EventHook()
    
    g_enableFrontLineDevInfo = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'UINT8', 'UINT8', 'BOOL', 'FLOAT32', 'FLOAT32'])
    def welcomeToSector(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_welcomeToSector.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'FLOAT32', 'UINT16'])
    def onStepRepairPointAction(self, arg1, arg2, arg3, arg4):
        self.g_onStepRepairPointAction.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'UINT8', 'FLOAT32'])
    def onSectorBaseAction(self, arg1, arg2, arg3):
        self.g_onSectorBaseAction.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8'])
    def enteringProtectionZone(self, arg1):
        self.g_enteringProtectionZone.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def leavingProtectionZone(self, arg1):
        self.g_leavingProtectionZone.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def protectionZoneShooting(self, arg1):
        self.g_protectionZoneShooting.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def onSectorShooting(self, arg1):
        self.g_onSectorShooting.fire(self, arg1)

    @unpack_func_args(['INT16'])
    def onXPUpdated(self, arg1):
        self.g_onXPUpdated.fire(self, arg1)

    @unpack_func_args(['UINT8', 'INT32'])
    def showDestructibleShotResults(self, arg1, arg2):
        self.g_showDestructibleShotResults.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'OBJECT_ID'])
    def onDestructibleDestroyed(self, arg1, arg2):
        self.g_onDestructibleDestroyed.fire(self, arg1, arg2)

    @unpack_func_args(['BOOL'])
    def enableFrontLineDevInfo(self, arg1):
        self.g_enableFrontLineDevInfo.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)