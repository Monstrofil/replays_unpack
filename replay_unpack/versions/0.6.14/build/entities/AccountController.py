#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from .interfaces.WalletProperties import WalletProperties
except:
    from WalletProperties import WalletProperties

try:
    from .interfaces.AccountPData import AccountPData
except:
    from AccountPData import AccountPData

try:
    from .interfaces.EntityLookuper import EntityLookuper
except:
    from EntityLookuper import EntityLookuper



class AccountController(WalletProperties, AccountPData, EntityLookuper):
    
    g_onKickedFromServer = EventHook()
    
    g_onCheckGamePing = EventHook()
    
    g_checkGamePing = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        WalletProperties.__init__(self)

        AccountPData.__init__(self)

        EntityLookuper.__init__(self)

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

    @unpack_func_args([])
    def checkGamePing(self):
        self.g_checkGamePing.fire(self)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)