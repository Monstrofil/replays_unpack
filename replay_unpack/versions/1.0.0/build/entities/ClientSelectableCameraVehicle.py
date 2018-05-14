#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ClientSelectableCameraVehicle(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._modelName = None

        self._vehicleGunPitch = None

        self._vehicleTurretYaw = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################



    ####################################
    #       PROPERTIES
    ####################################


    @property
    def modelName(self):
        return self._modelName

    @modelName.setter
    def modelName(self, value):
        self._modelName, = unpack_variables(value, ['STRING'])

    @property
    def vehicleGunPitch(self):
        return self._vehicleGunPitch

    @vehicleGunPitch.setter
    def vehicleGunPitch(self, value):
        self._vehicleGunPitch, = unpack_variables(value, ['FLOAT32'])

    @property
    def vehicleTurretYaw(self):
        return self._vehicleTurretYaw

    @vehicleTurretYaw.setter
    def vehicleTurretYaw(self, value):
        self._vehicleTurretYaw, = unpack_variables(value, ['FLOAT32'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)