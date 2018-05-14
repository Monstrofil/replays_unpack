#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountUnitBrowser(object):
    
    g_accountUnitBrowser_subscribe = EventHook()
    
    g_accountUnitBrowser_unsubscribe = EventHook()
    
    g_accountUnitBrowser_recenter = EventHook()
    
    g_accountUnitBrowser_doCmd = EventHook()
    
    g_accountUnitBrowser_onError = EventHook()
    
    g_accountUnitBrowser_onResultsSet = EventHook()
    
    g_accountUnitBrowser_onResultsUpdate = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT16', 'BOOL'])
    def accountUnitBrowser_subscribe(self, arg1, arg2):
        self.g_accountUnitBrowser_subscribe.fire(self, arg1, arg2)

    @unpack_func_args([])
    def accountUnitBrowser_unsubscribe(self):
        self.g_accountUnitBrowser_unsubscribe.fire(self)

    @unpack_func_args(['INT32', 'INT16', 'BOOL'])
    def accountUnitBrowser_recenter(self, arg1, arg2, arg3):
        self.g_accountUnitBrowser_recenter.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32'])
    def accountUnitBrowser_doCmd(self, arg1):
        self.g_accountUnitBrowser_doCmd.fire(self, arg1)

    @unpack_func_args(['INT32', 'STRING'])
    def accountUnitBrowser_onError(self, arg1, arg2):
        self.g_accountUnitBrowser_onError.fire(self, arg1, arg2)

    @unpack_func_args(['STRING'])
    def accountUnitBrowser_onResultsSet(self, arg1):
        self.g_accountUnitBrowser_onResultsSet.fire(self, arg1)

    @unpack_func_args(['STRING'])
    def accountUnitBrowser_onResultsUpdate(self, arg1):
        self.g_accountUnitBrowser_onResultsUpdate.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)