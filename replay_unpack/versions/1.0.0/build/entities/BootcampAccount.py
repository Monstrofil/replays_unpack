#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class BootcampAccount(object):
    
    g_completeBootcampLesson = EventHook()
    
    g_saveBootcampCheckpoint = EventHook()
    
    g_changeBootcampLessonBonus = EventHook()
    
    g_requestBootcampQuit = EventHook()
    
    g_onBootcampEnqueued = EventHook()
    
    g_setParent = EventHook()
    
    g_resetBootcamp = EventHook()
    
    g_setToken = EventHook()
    
    g_finishBootcamp = EventHook()
    
    g_onBootcampEnqueued = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._markForDelete = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8'])
    def completeBootcampLesson(self, arg1):
        self.g_completeBootcampLesson.fire(self, arg1)

    @unpack_func_args(['STRING', 'UINT8'])
    def saveBootcampCheckpoint(self, arg1, arg2):
        self.g_saveBootcampCheckpoint.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8'])
    def changeBootcampLessonBonus(self, arg1):
        self.g_changeBootcampLessonBonus.fire(self, arg1)

    @unpack_func_args(['UINT32'])
    def requestBootcampQuit(self, arg1):
        self.g_requestBootcampQuit.fire(self, arg1)

    @unpack_func_args(['INT32', 'UINT64'])
    def onBootcampEnqueued(self, arg1, arg2):
        self.g_onBootcampEnqueued.fire(self, arg1, arg2)

    @unpack_func_args(['MAILBOX'])
    def setParent(self, arg1):
        self.g_setParent.fire(self, arg1)

    @unpack_func_args([])
    def resetBootcamp(self):
        self.g_resetBootcamp.fire(self)

    @unpack_func_args(['INT64', 'INT32'])
    def setToken(self, arg1, arg2):
        self.g_setToken.fire(self, arg1, arg2)

    @unpack_func_args([])
    def finishBootcamp(self):
        self.g_finishBootcamp.fire(self)

    @unpack_func_args(['UINT64', 'UINT32', 'INT32'])
    def onBootcampEnqueued(self, arg1, arg2, arg3):
        self.g_onBootcampEnqueued.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def markForDelete(self):
        return self._markForDelete

    @markForDelete.setter
    def markForDelete(self, value):
        self._markForDelete, = unpack_variables(value, ['BOOL'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)