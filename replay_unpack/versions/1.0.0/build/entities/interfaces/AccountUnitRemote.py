#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountUnitRemote(object):
    
    g_accountUnitRemote_create = EventHook()
    
    g_accountUnitRemote_createEx = EventHook()
    
    g_accountUnitRemote_join = EventHook()
    
    g_accountUnitRemote_joinEx = EventHook()
    
    g_accountUnitRemote_doCmd = EventHook()
    
    g_accountUnitRemote_sendInvites = EventHook()
    
    g_accountUnitRemote_setRosterSlots = EventHook()
    
    g_accountUnitRemote_validateVehicleList = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT32', 'INT32', 'INT32'])
    def accountUnitRemote_create(self, arg1, arg2, arg3):
        self.g_accountUnitRemote_create.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'INT32', 'PYTHON'])
    def accountUnitRemote_createEx(self, arg1, arg2, arg3):
        self.g_accountUnitRemote_createEx.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'UINT64', 'INT32'])
    def accountUnitRemote_join(self, arg1, arg2, arg3):
        self.g_accountUnitRemote_join.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'INT32', 'PYTHON'])
    def accountUnitRemote_joinEx(self, arg1, arg2, arg3):
        self.g_accountUnitRemote_joinEx.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'INT32', 'OBJECT_ID', 'UINT64', 'INT32', 'STRING'])
    def accountUnitRemote_doCmd(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountUnitRemote_doCmd.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['INT32', 'UINT64', ['ARRAY', 'DB_ID'], 'STRING'])
    def accountUnitRemote_sendInvites(self, arg1, arg2, arg3, arg4):
        self.g_accountUnitRemote_sendInvites.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'UINT64', ['ARRAY', 'INT32'], ['ARRAY', 'STRING']])
    def accountUnitRemote_setRosterSlots(self, arg1, arg2, arg3, arg4):
        self.g_accountUnitRemote_setRosterSlots.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'PYTHON'])
    def accountUnitRemote_validateVehicleList(self, arg1, arg2):
        self.g_accountUnitRemote_validateVehicleList.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)