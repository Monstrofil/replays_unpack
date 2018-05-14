#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class SessionTracker(object):
    
    g_sessionTracker_processSessionTrackerData = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['MAILBOX', 'INT32', 'UINT8', 'STRING'])
    def sessionTracker_processSessionTrackerData(self, arg1, arg2, arg3, arg4):
        self.g_sessionTracker_processSessionTrackerData.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)