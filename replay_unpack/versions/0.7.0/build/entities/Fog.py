#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Fog(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._radius = None

        self._force = None

        self._height = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################



    ####################################
    #       PROPERTIES
    ####################################


    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT'])

    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, value):
        self._force, = unpack_variables(value, ['FLOAT'])

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height, = unpack_variables(value, ['FLOAT32'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)