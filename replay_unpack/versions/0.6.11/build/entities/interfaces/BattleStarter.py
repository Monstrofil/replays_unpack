#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #


from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class BattleStarter(object):
    
    g_onEnqueued = EventHook()
    
    g_onDequeued = EventHook()
    
    g_onStartBattle = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'SHIP_ID', ['ARRAY', 'INT8'], 'PYTHON', 'BOOL'])
    def onEnqueued(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onEnqueued.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT8'])
    def onDequeued(self, arg1):
        self.g_onDequeued.fire(self, arg1)

    @unpack_func_args(['PYTHON'])
    def onStartBattle(self, arg1):
        self.g_onStartBattle.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)