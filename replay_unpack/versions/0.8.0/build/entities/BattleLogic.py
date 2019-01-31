#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class BattleLogic(object):
    
    g_onPlayWorldEffect = EventHook()
    
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

        self._prerequisiteData = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        for item in [
            (16, 'battleType'),
            (16, 'duration'),
            (16, 'timeLeft'),
            (8, 'battleStage'),
            (8, 'scenarioPhase'),
            (10000000000, 'state'),
            (10000000000, 'debugText'),
            (10000000000, 'prerequisiteData'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (10000000001, 'onPlayWorldEffect'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._methods:
                continue
            self._methods.append(item)
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
    def onPlayWorldEffect(self, arg1, arg2, arg3):
        self.g_onPlayWorldEffect.fire(self, arg1, arg2, arg3)


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
    def prerequisiteData(self):
        return self._prerequisiteData

    @prerequisiteData.setter
    def prerequisiteData(self, value):
        self._prerequisiteData, = unpack_variables(value, ['PREREQUISITE_DATA'])


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