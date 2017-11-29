#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class SmokeScreen(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._bcRadius = None

        self._points = None

        self._radius = None

        self._height = None

        self._activePointIndex = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################



    ####################################
    #       PROPERTIES
    ####################################


    @property
    def bcRadius(self):
        return self._bcRadius

    @bcRadius.setter
    def bcRadius(self, value):
        self._bcRadius, = unpack_variables(value, ['FLOAT32'])

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points, = unpack_variables(value, [['ARRAY', 'VECTOR2']])

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT32'])

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height, = unpack_variables(value, ['FLOAT32'])

    @property
    def activePointIndex(self):
        return self._activePointIndex

    @activePointIndex.setter
    def activePointIndex(self, value):
        self._activePointIndex, = unpack_variables(value, ['INT8'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)