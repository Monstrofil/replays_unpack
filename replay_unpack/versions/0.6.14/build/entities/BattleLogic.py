#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class BattleLogic(object):
    
    g_playEffectOnce = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._battleType = None

        self._timeLeft = None

        self._battleStage = None

        self._scenarioPhase = None

        self._state = None

        self._debugText = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['STRING', 'VECTOR3', 'FLOAT'])
    def playEffectOnce(self, arg1, arg2, arg3):
        self.g_playEffectOnce.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def battleType(self):
        return self._battleType

    @battleType.setter
    def battleType(self, value):
        self._battleType, = unpack_variables(value, ['UINT16'])

    @property
    def timeLeft(self):
        return self._timeLeft

    @timeLeft.setter
    def timeLeft(self, value):
        self._timeLeft, = unpack_variables(value, ['UINT16'])

    @property
    def battleStage(self):
        return self._battleStage

    @battleStage.setter
    def battleStage(self, value):
        self._battleStage, = unpack_variables(value, ['UINT8'])

    @property
    def scenarioPhase(self):
        return self._scenarioPhase

    @scenarioPhase.setter
    def scenarioPhase(self, value):
        self._scenarioPhase, = unpack_variables(value, ['UINT8'])

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state, = unpack_variables(value, ['BATTLE_LOGIC_STATE'])

    @property
    def debugText(self):
        return self._debugText

    @debugText.setter
    def debugText(self, value):
        self._debugText, = unpack_variables(value, [['ARRAY', 'BATTLE_LOGIC_DEBUG_TEXT']])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)