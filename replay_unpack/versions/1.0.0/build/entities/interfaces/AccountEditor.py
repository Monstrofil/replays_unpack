#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountEditor(object):
    
    g_onAccountPropertiesChanged = EventHook()
    
    g_receiveProperties = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT32', 'INT32'])
    def onAccountPropertiesChanged(self, arg1, arg2):
        self.g_onAccountPropertiesChanged.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'DB_ID', 'INT32', 'PYTHON'])
    def receiveProperties(self, arg1, arg2, arg3, arg4):
        self.g_receiveProperties.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)