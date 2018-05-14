#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class VehicleObserver(object):
    
    g_switchObserverFPVControlMode = EventHook()
    
    g_setRemoteCamera = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._observerFPVControlMode = None

        self._remoteCamera = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8'])
    def switchObserverFPVControlMode(self, arg1):
        self.g_switchObserverFPVControlMode.fire(self, arg1)

    @unpack_func_args(['REMOTE_CAMERA_DATA'])
    def setRemoteCamera(self, arg1):
        self.g_setRemoteCamera.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def observerFPVControlMode(self):
        return self._observerFPVControlMode

    @observerFPVControlMode.setter
    def observerFPVControlMode(self, value):
        self._observerFPVControlMode, = unpack_variables(value, ['UINT8'])

    @property
    def remoteCamera(self):
        return self._remoteCamera

    @remoteCamera.setter
    def remoteCamera(self, value):
        self._remoteCamera, = unpack_variables(value, ['REMOTE_CAMERA_DATA'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)