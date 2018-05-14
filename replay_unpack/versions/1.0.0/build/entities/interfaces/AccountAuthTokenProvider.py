#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountAuthTokenProvider(object):
    
    g_requestToken = EventHook()
    
    g_accountAuthTokenProvider_setToken = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT16', 'UINT8'])
    def requestToken(self, arg1, arg2):
        self.g_requestToken.fire(self, arg1, arg2)

    @unpack_func_args(['INT64', 'INT32'])
    def accountAuthTokenProvider_setToken(self, arg1, arg2):
        self.g_accountAuthTokenProvider_setToken.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)