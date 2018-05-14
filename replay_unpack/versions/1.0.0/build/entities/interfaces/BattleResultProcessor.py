#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class BattleResultProcessor(object):
    
    g_battleResultProcessor_onBattleResultsReceived = EventHook()
    
    g_battleResultProcessor_onPlayerLeftArena = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT32', 'STRING'])
    def battleResultProcessor_onBattleResultsReceived(self, arg1, arg2):
        self.g_battleResultProcessor_onBattleResultsReceived.fire(self, arg1, arg2)

    @unpack_func_args(['INT32', 'STRING', 'UINT64', 'PYTHON', 'PYTHON', 'INT32', 'INT64'])
    def battleResultProcessor_onPlayerLeftArena(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.g_battleResultProcessor_onPlayerLeftArena.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)