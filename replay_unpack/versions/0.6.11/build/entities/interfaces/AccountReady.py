#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #


from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountReady(object):
    
    g_onAccountReady = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['MAILBOX', 'DB_ID', 'MAILBOX', 'MASTER_ID', 'UINT8', 'UINT64'])
    def onAccountReady(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_onAccountReady.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)