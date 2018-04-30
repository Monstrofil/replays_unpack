#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AviationOwner(object):
    
    g_assignOrder = EventHook()
    
    g_changeOrderGoal = EventHook()
    
    g_squadronRemoveOrder = EventHook()
    
    g_cancelCurrentOrder = EventHook()
    
    g_cancelAllOrders = EventHook()
    
    g_dev_killPlane = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT8', 'INT8', 'GOAL_DEF', 'BOOL', 'BOOL'])
    def assignOrder(self, arg1, arg2, arg3, arg4, arg5):
        self.g_assignOrder.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['INT8', 'UINT8', 'GOAL_DEF', 'BOOL'])
    def changeOrderGoal(self, arg1, arg2, arg3, arg4):
        self.g_changeOrderGoal.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT8', 'UINT8', 'BOOL'])
    def squadronRemoveOrder(self, arg1, arg2, arg3):
        self.g_squadronRemoveOrder.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT8', 'BOOL'])
    def cancelCurrentOrder(self, arg1, arg2):
        self.g_cancelCurrentOrder.fire(self, arg1, arg2)

    @unpack_func_args(['INT8', 'BOOL'])
    def cancelAllOrders(self, arg1, arg2):
        self.g_cancelAllOrders.fire(self, arg1, arg2)

    @unpack_func_args([])
    def dev_killPlane(self):
        self.g_dev_killPlane.fire(self)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)