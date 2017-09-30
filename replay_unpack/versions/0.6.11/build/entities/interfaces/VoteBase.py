#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #


from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class VoteBase(object):
    
    g_tryStartVote = EventHook()
    
    g_onStartVote = EventHook()
    
    g_onVoteStartFail = EventHook()
    
    g_vote = EventHook()
    
    g_tryCancel = EventHook()
    
    g_onVoteUpdate = EventHook()
    
    g_onVoteUpdate = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8', 'BLOB'])
    def tryStartVote(self, arg1, arg2):
        self.g_tryStartVote.fire(self, arg1, arg2)

    @unpack_func_args(['UINT32', 'UINT64', 'UINT8', 'UINT32', 'BOOL'])
    def onStartVote(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onStartVote.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT8', 'UINT16', 'PYTHON'])
    def onVoteStartFail(self, arg1, arg2, arg3):
        self.g_onVoteStartFail.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT32', 'UINT8'])
    def vote(self, arg1, arg2, arg3):
        self.g_vote.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8', 'UINT32'])
    def tryCancel(self, arg1, arg2):
        self.g_tryCancel.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'BLOB'])
    def onVoteUpdate(self, arg1, arg2):
        self.g_onVoteUpdate.fire(self, arg1, arg2)

    @unpack_func_args(['UINT8', 'BLOB'])
    def onVoteUpdate(self, arg1, arg2):
        self.g_onVoteUpdate.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)