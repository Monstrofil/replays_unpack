#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class BootcampAccount(object):
    
    g_finishBootcamp = EventHook()
    
    g_onBootcampEnqueued = EventHook()
    
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
            (0, 'finishBootcamp'),
            (128, 'onBootcampEnqueued'),
            
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


    # method size: 0
    @unpack_func_args([])
    def finishBootcamp(self):
        self.g_finishBootcamp.fire(self)

    # method size: 128
    @unpack_func_args(['UINT64', 'UINT32', 'INT32'])
    def onBootcampEnqueued(self, arg1, arg2, arg3):
        self.g_onBootcampEnqueued.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)