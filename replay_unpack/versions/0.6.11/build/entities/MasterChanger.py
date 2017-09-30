#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #


from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.AccountReady import AccountReady
except:
    from AccountReady import AccountReady



class MasterChanger(AccountReady):
    
    g_onKickedFromServer = EventHook()
    
    g_onCheckGamePing = EventHook()
    
    g_onChangeShutdown = EventHook()
    
    g_checkGamePing = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._countBattles = None

        self._lastBattleFinish = None


        # MRO fix

        AccountReady.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def onKickedFromServer(self):
        self.g_onKickedFromServer.fire(self)

    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)

    @unpack_func_args(['UINT8', 'UINT32'])
    def onChangeShutdown(self, arg1, arg2):
        self.g_onChangeShutdown.fire(self, arg1, arg2)

    @unpack_func_args([])
    def checkGamePing(self):
        self.g_checkGamePing.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def countBattles(self):
        return self._countBattles

    @countBattles.setter
    def countBattles(self, value):
        self._countBattles, = unpack_variables(value, ['UINT8'])

    @property
    def lastBattleFinish(self):
        return self._lastBattleFinish

    @lastBattleFinish.setter
    def lastBattleFinish(self, value):
        self._lastBattleFinish, = unpack_variables(value, ['UINT32'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)