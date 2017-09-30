#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.Entity import Entity
from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.EntityLookuper import EntityLookuper
except:
    from EntityLookuper import EntityLookuper



class Login(EntityLookuper):
    
    g_onKickedFromServer = EventHook()
    
    g_receiveLoginQueueNumber = EventHook()
    
    g_checkGamePing = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._accountDBID_s = None


        # MRO fix

        EntityLookuper.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def onKickedFromServer(self):
        self.g_onKickedFromServer.fire(self)

    @unpack_func_args([])
    def receiveLoginQueueNumber(self):
        self.g_receiveLoginQueueNumber.fire(self)

    @unpack_func_args([])
    def checkGamePing(self):
        self.g_checkGamePing.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def accountDBID_s(self):
        return self._accountDBID_s

    @accountDBID_s.setter
    def accountDBID_s(self, value):
        self._accountDBID_s, = unpack_variables(value, ['STRING'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)