#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ClientCommandsPort(object):
    
    g_doCmdStr = EventHook()
    
    g_doCmdInt3 = EventHook()
    
    g_doCmdInt4 = EventHook()
    
    g_doCmdInt2Str = EventHook()
    
    g_doCmdIntArr = EventHook()
    
    g_doCmdIntStr = EventHook()
    
    g_doCmdIntStrArr = EventHook()
    
    g_doCmdIntArrStrArr = EventHook()
    
    g_onCmdResponse = EventHook()
    
    g_onCmdResponseExt = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT16', 'INT16', 'STRING'])
    def doCmdStr(self, arg1, arg2, arg3):
        self.g_doCmdStr.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT16', 'INT16', 'INT64', 'INT64', 'INT64'])
    def doCmdInt3(self, arg1, arg2, arg3, arg4, arg5):
        self.g_doCmdInt3.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['INT16', 'INT16', 'INT64', 'INT64', 'INT32', 'INT32'])
    def doCmdInt4(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_doCmdInt4.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['INT16', 'INT16', 'INT64', 'INT64', 'STRING'])
    def doCmdInt2Str(self, arg1, arg2, arg3, arg4, arg5):
        self.g_doCmdInt2Str.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['INT16', 'INT16', ['ARRAY', 'INT32']])
    def doCmdIntArr(self, arg1, arg2, arg3):
        self.g_doCmdIntArr.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT16', 'INT16', 'INT64', 'STRING'])
    def doCmdIntStr(self, arg1, arg2, arg3, arg4):
        self.g_doCmdIntStr.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT16', 'INT16', 'INT64', ['ARRAY', 'STRING']])
    def doCmdIntStrArr(self, arg1, arg2, arg3, arg4):
        self.g_doCmdIntStrArr.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT16', 'INT16', ['ARRAY', 'INT64'], ['ARRAY', 'STRING']])
    def doCmdIntArrStrArr(self, arg1, arg2, arg3, arg4):
        self.g_doCmdIntArrStrArr.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT16', 'INT16', 'STRING'])
    def onCmdResponse(self, arg1, arg2, arg3):
        self.g_onCmdResponse.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT16', 'INT16', 'STRING', 'STRING'])
    def onCmdResponseExt(self, arg1, arg2, arg3, arg4):
        self.g_onCmdResponseExt.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)