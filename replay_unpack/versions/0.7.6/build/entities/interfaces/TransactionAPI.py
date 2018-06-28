#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class TransactionAPI(object):
    
    g_onTransactionReceive = EventHook()
    
    g_onTransactionSync = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._lastGeneratedTransactionNumber = 0.0


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def onTransactionReceive(self):
        self.g_onTransactionReceive.fire(self)

    @unpack_func_args([])
    def onTransactionSync(self):
        self.g_onTransactionSync.fire(self)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def lastGeneratedTransactionNumber(self):
        return self._lastGeneratedTransactionNumber

    @lastGeneratedTransactionNumber.setter
    def lastGeneratedTransactionNumber(self, value):
        self._lastGeneratedTransactionNumber, = unpack_variables(value, ['UINT16'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)