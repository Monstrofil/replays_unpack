#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Login(object):
    
    g_onKickedFromServer = EventHook()
    
    g_receiveLoginQueueNumber = EventHook()
    
    g_onEnqueued = EventHook()
    
    g_onQueueTurn = EventHook()
    
    g_onAccountClientReleased = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._accountDBID_s = None

        self._loginPriority = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT32'])
    def onKickedFromServer(self, arg1):
        self.g_onKickedFromServer.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def receiveLoginQueueNumber(self, arg1):
        self.g_receiveLoginQueueNumber.fire(self, arg1)

    @unpack_func_args(['STRING', 'UINT64'])
    def onEnqueued(self, arg1, arg2):
        self.g_onEnqueued.fire(self, arg1, arg2)

    @unpack_func_args([])
    def onQueueTurn(self):
        self.g_onQueueTurn.fire(self)

    @unpack_func_args(['MAILBOX'])
    def onAccountClientReleased(self, arg1):
        self.g_onAccountClientReleased.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def accountDBID_s(self):
        return self._accountDBID_s

    @accountDBID_s.setter
    def accountDBID_s(self, value):
        self._accountDBID_s, = unpack_variables(value, ['STRING'])

    @property
    def loginPriority(self):
        return self._loginPriority

    @loginPriority.setter
    def loginPriority(self, value):
        self._loginPriority, = unpack_variables(value, ['UINT32'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)