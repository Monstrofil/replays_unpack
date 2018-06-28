#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AirDefenceOwner(object):
    
    g_setAntiAirMode = EventHook()
    
    g_setEnabledUniversalAura = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._airDefenseTargetId = None

        self._airDefenseDispRadius = '0.0'

        self._isAntiAirMode = 0.0

        self._antiAirAuras = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['BOOL'])
    def setAntiAirMode(self, arg1):
        self.g_setAntiAirMode.fire(self, arg1)

    @unpack_func_args(['BOOL'])
    def setEnabledUniversalAura(self, arg1):
        self.g_setEnabledUniversalAura.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def airDefenseTargetId(self):
        return self._airDefenseTargetId

    @airDefenseTargetId.setter
    def airDefenseTargetId(self, value):
        self._airDefenseTargetId, = unpack_variables(value, [['ARRAY', 'PLANE_ID']])

    @property
    def airDefenseDispRadius(self):
        return self._airDefenseDispRadius

    @airDefenseDispRadius.setter
    def airDefenseDispRadius(self, value):
        self._airDefenseDispRadius, = unpack_variables(value, ['FLOAT32'])

    @property
    def isAntiAirMode(self):
        return self._isAntiAirMode

    @isAntiAirMode.setter
    def isAntiAirMode(self, value):
        self._isAntiAirMode, = unpack_variables(value, ['BOOL'])

    @property
    def antiAirAuras(self):
        return self._antiAirAuras

    @antiAirAuras.setter
    def antiAirAuras(self, value):
        self._antiAirAuras, = unpack_variables(value, [['ARRAY', 'AIR_DEFENCE_AURA']])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)