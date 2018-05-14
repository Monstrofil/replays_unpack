#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountDebugger(object):
    
    g_accountDebugger_runDebugTask = EventHook()
    
    g_accountDebugger_registerDebugTaskResult = EventHook()
    
    g_accountDebugger_sendDebugTaskResultChunk = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['STRING'])
    def accountDebugger_runDebugTask(self, arg1):
        self.g_accountDebugger_runDebugTask.fire(self, arg1)

    @unpack_func_args(['INT64', 'INT32', 'INT64'])
    def accountDebugger_registerDebugTaskResult(self, arg1, arg2, arg3):
        self.g_accountDebugger_registerDebugTaskResult.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT64', 'INT64', 'STRING'])
    def accountDebugger_sendDebugTaskResultChunk(self, arg1, arg2, arg3):
        self.g_accountDebugger_sendDebugTaskResultChunk.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)