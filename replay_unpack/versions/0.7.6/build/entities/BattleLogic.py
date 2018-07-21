#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class BattleLogic(object):
    
    g_playEffectOnce = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._battleType = None

        self._duration = None

        self._timeLeft = None

        self._battleStage = None

        self._scenarioPhase = None

        self._state = None

        self._debugText = None

        self._uiInfo = None

        self._prerequisiteShips = None

        self._prerequisiteEffects = None

        self._prerequisiteWeathers = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (16, 'battleType'),
            (16, 'duration'),
            (16, 'timeLeft'),
            (8, 'battleStage'),
            (8, 'scenarioPhase'),
            (10000000000, 'state'),
            (10000000000, 'debugText'),
            (10000000000, 'uiInfo'),
            (10000000000, 'prerequisiteShips'),
            (10000000000, 'prerequisiteEffects'),
            (10000000000, 'prerequisiteWeathers'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (10000000001, 'playEffectOnce'),
            
        ])
        # sort methods by size
        self._methods.sort(key=itemgetter(0))
        return

    @property
    def attributesMap(self):
        d = {}
        for i, (_, name) in enumerate(self._properties):
            d[i] = name
        return d

    @property
    def methodsMap(self):
        d = {}
        for i, (_, name) in enumerate(self._methods):
            d[i] = name
        return d

    ####################################
    #      METHODS
    ####################################

# method size: 10000000001
    @unpack_func_args(['STRING', 'VECTOR3', 'FLOAT'])
    def playEffectOnce(self, arg1, arg2, arg3):
        self.g_playEffectOnce.fire(self, arg1, arg2, arg3)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 16
    @property
    def battleType(self):
        return self._battleType

    @battleType.setter
    def battleType(self, value):
        self._battleType, = unpack_variables(value, ['UINT16'])
# property size: 16
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration, = unpack_variables(value, ['UINT16'])
# property size: 16
    @property
    def timeLeft(self):
        return self._timeLeft

    @timeLeft.setter
    def timeLeft(self, value):
        self._timeLeft, = unpack_variables(value, ['UINT16'])
# property size: 8
    @property
    def battleStage(self):
        return self._battleStage

    @battleStage.setter
    def battleStage(self, value):
        self._battleStage, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def scenarioPhase(self):
        return self._scenarioPhase

    @scenarioPhase.setter
    def scenarioPhase(self, value):
        self._scenarioPhase, = unpack_variables(value, ['UINT8'])
# property size: 10000000000
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state, = unpack_variables(value, ['BATTLE_LOGIC_STATE'])
# property size: 10000000000
    @property
    def debugText(self):
        return self._debugText

    @debugText.setter
    def debugText(self, value):
        self._debugText, = unpack_variables(value, [['ARRAY', 'BATTLE_LOGIC_DEBUG_TEXT']])
# property size: 10000000000
    @property
    def uiInfo(self):
        return self._uiInfo

    @uiInfo.setter
    def uiInfo(self, value):
        self._uiInfo, = unpack_variables(value, ['BATTLE_LOGIC_UI_INFO'])
# property size: 10000000000
    @property
    def prerequisiteShips(self):
        return self._prerequisiteShips

    @prerequisiteShips.setter
    def prerequisiteShips(self, value):
        self._prerequisiteShips, = unpack_variables(value, [['ARRAY', 'PREREQUISITE_SHIP']])
# property size: 10000000000
    @property
    def prerequisiteEffects(self):
        return self._prerequisiteEffects

    @prerequisiteEffects.setter
    def prerequisiteEffects(self, value):
        self._prerequisiteEffects, = unpack_variables(value, [['ARRAY', 'STRING']])
# property size: 10000000000
    @property
    def prerequisiteWeathers(self):
        return self._prerequisiteWeathers

    @prerequisiteWeathers.setter
    def prerequisiteWeathers(self, value):
        self._prerequisiteWeathers, = unpack_variables(value, [['ARRAY', 'GAMEPARAMS_ID']])


    def get_summary(self):
        print '~' * 60
        print 'Entity name: ', self.__class__.__name__
        print 'Total entity client properties: {:>5}'.format(len(self._properties))
        print 'Total entity client methods: {:>5}'.format(len(self._methods))

        print
        print 'Listing entity properties:'
        print '{:>4} {:>40}'.format('idx', 'property name')
        for i, p in self.attributesMap.items():
            print '{:>4} {:>40}'.format(i, p)

        print
        print 'Listing entity methods:'
        print '{:>4} {:>40}'.format('idx', 'method name')
        for i, p in self.methodsMap.items():
            print '{:>4} {:>40}'.format(i, p)
        print '~' * 60
        print
        print


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)