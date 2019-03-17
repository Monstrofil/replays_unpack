#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #


from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from .interfaces.AccountReady import AccountReady
except:
    from AccountReady import AccountReady



class EntityLookuper(AccountReady):
    
    g_getSuperMBox = EventHook()
    
    g_putSuperMBox = EventHook()
    
    g_lookUpEntityByIDOrName = EventHook()
    
    g_createEntityByIDOrName = EventHook()
    
    g_createEntityAnywhere = EventHook()
    
    g_getNicknameByIDReq = EventHook()
    
    g_getUserlistByDBIDReq = EventHook()
    
    g_getUserlistByNameReq = EventHook()
    
    g_putSQLResult = EventHook()
    
    g_onCreateEntityAnywhere = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        AccountReady.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['MAILBOX', 'UINT64'])
    def getSuperMBox(self, arg1, arg2):
        self.g_getSuperMBox.fire(self, arg1, arg2)

    @unpack_func_args(['MAILBOX', 'MAILBOX', 'UINT8', 'UINT64'])
    def putSuperMBox(self, arg1, arg2, arg3, arg4):
        self.g_putSuperMBox.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['MAILBOX', 'STRING', 'DB_ID', 'STRING', 'UINT8', 'UINT64'])
    def lookUpEntityByIDOrName(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_lookUpEntityByIDOrName.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['MAILBOX', 'STRING', 'DB_ID', 'STRING', 'UINT64'])
    def createEntityByIDOrName(self, arg1, arg2, arg3, arg4, arg5):
        self.g_createEntityByIDOrName.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['MAILBOX', 'STRING', 'PYTHON', 'UINT64'])
    def createEntityAnywhere(self, arg1, arg2, arg3, arg4):
        self.g_createEntityAnywhere.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['DB_ID', 'UINT64'])
    def getNicknameByIDReq(self, arg1, arg2):
        self.g_getNicknameByIDReq.fire(self, arg1, arg2)

    @unpack_func_args(['DB_ID_LIST', 'UINT64'])
    def getUserlistByDBIDReq(self, arg1, arg2):
        self.g_getUserlistByDBIDReq.fire(self, arg1, arg2)

    @unpack_func_args(['STRING', 'UINT32', 'UINT64'])
    def getUserlistByNameReq(self, arg1, arg2, arg3):
        self.g_getUserlistByNameReq.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['BLOB', 'UINT64'])
    def putSQLResult(self, arg1, arg2):
        self.g_putSQLResult.fire(self, arg1, arg2)

    @unpack_func_args(['MAILBOX', 'UINT64'])
    def onCreateEntityAnywhere(self, arg1, arg2):
        self.g_onCreateEntityAnywhere.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)