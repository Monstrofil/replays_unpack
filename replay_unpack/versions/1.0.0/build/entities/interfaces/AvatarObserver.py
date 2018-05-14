#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AvatarObserver(object):
    
    g_switchObserverFPV = EventHook()
    
    g_switchObserverFPVControlMode = EventHook()
    
    g_setRemoteCamera = EventHook()
    
    g_setNumOfObservers = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._remoteCamera = None

        self._isObserverFPV = None

        self._observerFPVControlMode = None

        self._numOfObservers = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['BOOL'])
    def switchObserverFPV(self, arg1):
        self.g_switchObserverFPV.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def switchObserverFPVControlMode(self, arg1):
        self.g_switchObserverFPVControlMode.fire(self, arg1)

    @unpack_func_args(['REMOTE_CAMERA_DATA'])
    def setRemoteCamera(self, arg1):
        self.g_setRemoteCamera.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def setNumOfObservers(self, arg1):
        self.g_setNumOfObservers.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def remoteCamera(self):
        return self._remoteCamera

    @remoteCamera.setter
    def remoteCamera(self, value):
        self._remoteCamera, = unpack_variables(value, ['REMOTE_CAMERA_DATA'])

    @property
    def isObserverFPV(self):
        return self._isObserverFPV

    @isObserverFPV.setter
    def isObserverFPV(self, value):
        self._isObserverFPV, = unpack_variables(value, ['BOOL'])

    @property
    def observerFPVControlMode(self):
        return self._observerFPVControlMode

    @observerFPVControlMode.setter
    def observerFPVControlMode(self, value):
        self._observerFPVControlMode, = unpack_variables(value, ['UINT8'])

    @property
    def numOfObservers(self):
        return self._numOfObservers

    @numOfObservers.setter
    def numOfObservers(self, value):
        self._numOfObservers, = unpack_variables(value, ['UINT8'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)