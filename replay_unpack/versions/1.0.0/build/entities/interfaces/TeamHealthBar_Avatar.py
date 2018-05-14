#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class TeamHealthBar_Avatar(object):
    
    g_teamHealthBar_updateTeamsHealthPercentage = EventHook()
    
    g_updateTeamsHealthPercentage = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([['ARRAY', 'UINT8']])
    def teamHealthBar_updateTeamsHealthPercentage(self, arg1):
        self.g_teamHealthBar_updateTeamsHealthPercentage.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'UINT8']])
    def updateTeamsHealthPercentage(self, arg1):
        self.g_updateTeamsHealthPercentage.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)