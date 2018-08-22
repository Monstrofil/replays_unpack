#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

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
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (97, 'welcomeToSector'),
            (89, 'onStepRepairPointAction'),
            (49, 'onSectorBaseAction'),
            (9, 'enteringProtectionZone'),
            (9, 'leavingProtectionZone'),
            (9, 'protectionZoneShooting'),
            (9, 'onSectorShooting'),
            (17, 'onXPUpdated'),
            (41, 'showDestructibleShotResults'),
            (41, 'onDestructibleDestroyed'),
            
        ])
        # sort methods by size
        self._methods.sort(key=itemgetter(0))
        return

    @property
    def attributesMap(self):
        d = {}
        for i, (_, name) in enumerate(self._properties):
            d[i] = name
        return d

    @property
    def methodsMap(self):
        d = {}
        for i, (_, name) in enumerate(self._methods):
            d[i] = name
        return d

    ####################################
    #      METHODS
    ####################################

# method size: 97
    @unpack_func_args(['UINT8', 'UINT8', 'UINT8', 'BOOL', 'FLOAT32', 'FLOAT32'])
    def welcomeToSector(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_welcomeToSector.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)
# method size: 89
    @unpack_func_args(['OBJECT_ID', 'UINT8', 'FLOAT32', 'UINT16'])
    def onStepRepairPointAction(self, arg1, arg2, arg3, arg4):
        self.g_onStepRepairPointAction.fire(self, arg1, arg2, arg3, arg4)
# method size: 49
    @unpack_func_args(['UINT8', 'UINT8', 'FLOAT32'])
    def onSectorBaseAction(self, arg1, arg2, arg3):
        self.g_onSectorBaseAction.fire(self, arg1, arg2, arg3)
# method size: 9
    @unpack_func_args(['UINT8'])
    def enteringProtectionZone(self, arg1):
        self.g_enteringProtectionZone.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def leavingProtectionZone(self, arg1):
        self.g_leavingProtectionZone.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def protectionZoneShooting(self, arg1):
        self.g_protectionZoneShooting.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onSectorShooting(self, arg1):
        self.g_onSectorShooting.fire(self, arg1)
# method size: 17
    @unpack_func_args(['INT16'])
    def onXPUpdated(self, arg1):
        self.g_onXPUpdated.fire(self, arg1)
# method size: 41
    @unpack_func_args(['UINT8', 'INT32'])
    def showDestructibleShotResults(self, arg1, arg2):
        self.g_showDestructibleShotResults.fire(self, arg1, arg2)
# method size: 41
    @unpack_func_args(['UINT8', 'OBJECT_ID'])
    def onDestructibleDestroyed(self, arg1, arg2):
        self.g_onDestructibleDestroyed.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def get_summary(self):
        print '~' * 60
        print 'Entity name: ', self.__class__.__name__
        print 'Total entity client properties: {:>5}'.format(len(self._properties))
        print 'Total entity client methods: {:>5}'.format(len(self._methods))

        print
        print 'Listing entity properties:'
        print '{:>4} {:>40}'.format('idx', 'property name')
        for i, p in self.attributesMap.items():
            print '{:>4} {:>40}'.format(i, p)

        print
        print 'Listing entity methods:'
        print '{:>4} {:>40}'.format('idx', 'method name')
        for i, p in self.methodsMap.items():
            print '{:>4} {:>40}'.format(i, p)
        print '~' * 60
        print
        print


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)