#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountAdmin(object):
    
    g_accountAdmin_addRemoveRareAchievements = EventHook()
    
    g_accountAdmin_changeFairPlay = EventHook()
    
    g_accountAdmin_delRestriction = EventHook()
    
    g_accountAdmin_excludeFromFairPlay = EventHook()
    
    g_accountAdmin_exportToWeb = EventHook()
    
    g_accountAdmin_lockVehicleType = EventHook()
    
    g_accountAdmin_resetDailyLimits = EventHook()
    
    g_accountAdmin_resetWalletAssets = EventHook()
    
    g_accountAdmin_resetWalletIDs = EventHook()
    
    g_accountAdmin_restoreAccountFromPoint = EventHook()
    
    g_accountAdmin_setAutoBanTime = EventHook()
    
    g_accountAdmin_setFinPassword = EventHook()
    
    g_accountAdmin_setLoginPriority = EventHook()
    
    g_accountAdmin_setNextBanLevel = EventHook()
    
    g_accountAdmin_setPlayLimits = EventHook()
    
    g_accountAdmin_setRestriction = EventHook()
    
    g_accountAdmin_setType = EventHook()
    
    g_accountAdmin_syncWallet = EventHook()
    
    g_accountAdmin_unlockVehicleType = EventHook()
    
    g_accountAdmin_wipe = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['MAILBOX', 'INT32', ['ARRAY', 'INT32'], 'INT32', 'UINT32'])
    def accountAdmin_addRemoveRareAchievements(self, arg1, arg2, arg3, arg4, arg5):
        self.g_accountAdmin_addRemoveRareAchievements.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['MAILBOX', 'INT32', 'STRING', 'INT32', 'INT32', 'UINT32', 'INT32', 'UINT32'])
    def accountAdmin_changeFairPlay(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_accountAdmin_changeFairPlay.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['MAILBOX', 'INT32', 'UINT8', 'UINT64', 'INT32', 'UINT32'])
    def accountAdmin_delRestriction(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountAdmin_delRestriction.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['MAILBOX', 'INT32', 'BOOL', 'INT32', 'UINT32'])
    def accountAdmin_excludeFromFairPlay(self, arg1, arg2, arg3, arg4, arg5):
        self.g_accountAdmin_excludeFromFairPlay.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args([])
    def accountAdmin_exportToWeb(self):
        self.g_accountAdmin_exportToWeb.fire(self)

    @unpack_func_args(['MAILBOX', 'INT32', 'PYTHON', 'PYTHON', 'INT32', 'UINT32'])
    def accountAdmin_lockVehicleType(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountAdmin_lockVehicleType.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['MAILBOX', 'INT32', ['ARRAY', 'UINT8'], 'INT32', 'UINT32'])
    def accountAdmin_resetDailyLimits(self, arg1, arg2, arg3, arg4, arg5):
        self.g_accountAdmin_resetDailyLimits.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['MAILBOX', 'INT32', 'INT64', 'INT64', 'UINT32', 'INT32', 'UINT32'])
    def accountAdmin_resetWalletAssets(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_accountAdmin_resetWalletAssets.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['MAILBOX', 'INT32', 'UINT64', 'UINT64', 'INT32', 'UINT32'])
    def accountAdmin_resetWalletIDs(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountAdmin_resetWalletIDs.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['MAILBOX', 'INT32', 'UINT64', 'PYTHON', ['ARRAY', 'UINT64'], 'UINT64', 'UINT32', 'UINT64', 'UINT64', 'INT32', 'UINT32', 'PYTHON', 'PYTHON'])
    def accountAdmin_restoreAccountFromPoint(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
        self.g_accountAdmin_restoreAccountFromPoint.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)

    @unpack_func_args(['MAILBOX', 'INT32', 'UINT32', 'INT32', 'UINT32'])
    def accountAdmin_setAutoBanTime(self, arg1, arg2, arg3, arg4, arg5):
        self.g_accountAdmin_setAutoBanTime.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['MAILBOX', 'INT32', 'STRING', 'STRING', 'BOOL', 'INT32', 'UINT32'])
    def accountAdmin_setFinPassword(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_accountAdmin_setFinPassword.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['MAILBOX', 'INT32', ['ARRAY', 'STRING'], ['ARRAY', 'STRING'], 'INT32', 'UINT32'])
    def accountAdmin_setLoginPriority(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountAdmin_setLoginPriority.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['MAILBOX', 'INT32', 'STRING', 'UINT8', 'INT32', 'UINT32'])
    def accountAdmin_setNextBanLevel(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountAdmin_setNextBanLevel.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['MAILBOX', 'INT32', 'INT32', 'STRING', 'INT32', 'STRING', 'INT32', 'UINT32'])
    def accountAdmin_setPlayLimits(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_accountAdmin_setPlayLimits.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['MAILBOX', 'INT32', 'UINT8', 'STRING', 'UINT32', 'UINT32', 'UINT32', 'UINT16', 'STRING', 'INT32', 'UINT32'])
    def accountAdmin_setRestriction(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        self.g_accountAdmin_setRestriction.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

    @unpack_func_args(['MAILBOX', 'INT32', 'INT16', 'INT16', 'INT32', 'UINT32'])
    def accountAdmin_setType(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountAdmin_setType.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args([])
    def accountAdmin_syncWallet(self):
        self.g_accountAdmin_syncWallet.fire(self)

    @unpack_func_args(['MAILBOX', 'INT32', 'PYTHON', 'PYTHON', 'INT32', 'UINT32'])
    def accountAdmin_unlockVehicleType(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_accountAdmin_unlockVehicleType.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['MAILBOX', 'INT32', 'BOOL', 'INT32', 'UINT32'])
    def accountAdmin_wipe(self, arg1, arg2, arg3, arg4, arg5):
        self.g_accountAdmin_wipe.fire(self, arg1, arg2, arg3, arg4, arg5)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)