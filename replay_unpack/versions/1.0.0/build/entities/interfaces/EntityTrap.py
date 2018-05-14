#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class EntityTrap(object):
    
    g_start = EventHook()
    
    g_stop = EventHook()
    
    g_smartDestroy = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._arenaBase = None

        self._arena = None

        self._radius = '25.0'

        self._isActive = None

        self._cp = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def start(self):
        self.g_start.fire(self)

    @unpack_func_args([])
    def stop(self):
        self.g_stop.fire(self)

    @unpack_func_args([])
    def smartDestroy(self):
        self.g_smartDestroy.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def arenaBase(self):
        return self._arenaBase

    @arenaBase.setter
    def arenaBase(self, value):
        self._arenaBase, = unpack_variables(value, ['MAILBOX'])

    @property
    def arena(self):
        return self._arena

    @arena.setter
    def arena(self, value):
        self._arena, = unpack_variables(value, ['MAILBOX'])

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT32'])

    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, value):
        self._isActive, = unpack_variables(value, ['BOOL'])

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp, = unpack_variables(value, ['PYTHON'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)