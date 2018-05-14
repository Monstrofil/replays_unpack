#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class BattleFeedback(object):
    
    g_battleFeedback_onBattleEvent = EventHook()
    
    g_battleFeedback_onDeath = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'OBJECT_ID', 'UINT32', 'BOOL'])
    def battleFeedback_onBattleEvent(self, arg1, arg2, arg3, arg4):
        self.g_battleFeedback_onBattleEvent.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'UINT8'])
    def battleFeedback_onDeath(self, arg1, arg2):
        self.g_battleFeedback_onDeath.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)