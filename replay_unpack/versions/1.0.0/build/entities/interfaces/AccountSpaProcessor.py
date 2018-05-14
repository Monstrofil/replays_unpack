#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountSpaProcessor(object):
    
    g_accountSPA_processSpaAttributes = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['MAILBOX', 'INT32', 'INT32', 'PYTHON'])
    def accountSPA_processSpaAttributes(self, arg1, arg2, arg3, arg4):
        self.g_accountSPA_processSpaAttributes.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)