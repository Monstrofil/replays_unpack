#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class StepRepairPoint(object):
    
    g_changeOwnerTeam = EventHook()
    
    g_setCooldownAfterRepair = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._initTeam = 0.0

        self._team = 0.0

        self._pointsPerStep = 100.0

        self._repairTime = '1.0'

        self._secondsCooldownPerStep = '10.0'

        self._baseSecondsCooldownAfterRepair = '120.0'

        self._percentageShellsPerStep = 10.0

        self._radius = '25.0'


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT8'])
    def changeOwnerTeam(self, arg1):
        self.g_changeOwnerTeam.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'FLOAT32', 'BOOL'])
    def setCooldownAfterRepair(self, arg1, arg2, arg3):
        self.g_setCooldownAfterRepair.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def initTeam(self):
        return self._initTeam

    @initTeam.setter
    def initTeam(self, value):
        self._initTeam, = unpack_variables(value, ['UINT8'])

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])

    @property
    def pointsPerStep(self):
        return self._pointsPerStep

    @pointsPerStep.setter
    def pointsPerStep(self, value):
        self._pointsPerStep, = unpack_variables(value, ['INT16'])

    @property
    def repairTime(self):
        return self._repairTime

    @repairTime.setter
    def repairTime(self, value):
        self._repairTime, = unpack_variables(value, ['FLOAT32'])

    @property
    def secondsCooldownPerStep(self):
        return self._secondsCooldownPerStep

    @secondsCooldownPerStep.setter
    def secondsCooldownPerStep(self, value):
        self._secondsCooldownPerStep, = unpack_variables(value, ['FLOAT32'])

    @property
    def baseSecondsCooldownAfterRepair(self):
        return self._baseSecondsCooldownAfterRepair

    @baseSecondsCooldownAfterRepair.setter
    def baseSecondsCooldownAfterRepair(self, value):
        self._baseSecondsCooldownAfterRepair, = unpack_variables(value, ['FLOAT32'])

    @property
    def percentageShellsPerStep(self):
        return self._percentageShellsPerStep

    @percentageShellsPerStep.setter
    def percentageShellsPerStep(self, value):
        self._percentageShellsPerStep, = unpack_variables(value, ['UINT8'])

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius, = unpack_variables(value, ['FLOAT32'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)