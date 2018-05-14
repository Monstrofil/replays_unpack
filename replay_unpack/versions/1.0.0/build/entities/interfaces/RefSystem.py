#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class RefSystem(object):
    
    g_refSystem_applyContribution = EventHook()
    
    g_refSystem_addReferral = EventHook()
    
    g_refSystem_delReferral = EventHook()
    
    g_refSystem_onUpdateReferralInfo = EventHook()
    
    g_refSystem_onUpdateReferrerInfo = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['MAILBOX', 'INT32', 'STRING', 'DB_ID', 'STRING', 'DB_ID', 'PYTHON'])
    def refSystem_applyContribution(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_refSystem_applyContribution.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

    @unpack_func_args(['MAILBOX', 'INT32', 'DB_ID', 'PYTHON'])
    def refSystem_addReferral(self, arg1, arg2, arg3, arg4):
        self.g_refSystem_addReferral.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['MAILBOX', 'INT32', 'DB_ID'])
    def refSystem_delReferral(self, arg1, arg2, arg3):
        self.g_refSystem_delReferral.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['MAILBOX', 'INT32', 'DB_ID', 'PYTHON'])
    def refSystem_onUpdateReferralInfo(self, arg1, arg2, arg3, arg4):
        self.g_refSystem_onUpdateReferralInfo.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['MAILBOX', 'INT32', 'DB_ID', 'PYTHON'])
    def refSystem_onUpdateReferrerInfo(self, arg1, arg2, arg3, arg4):
        self.g_refSystem_onUpdateReferrerInfo.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)