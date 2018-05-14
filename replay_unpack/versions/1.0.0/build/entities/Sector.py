#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class Sector(object):
    
    g_start = EventHook()
    
    g_reset = EventHook()
    
    g_open = EventHook()
    
    g_transition = EventHook()
    
    g_stop = EventHook()
    
    g_harm_receiveAttackResults = EventHook()
    
    g_smartDestroy = EventHook()
    
    g_showBomb = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._arena = None

        self._arenaBase = None

        self._arenaTypeID = None

        self._groupID = None

        self._sectorID = 1.0

        self._playerGroup = None

        self._IDInPlayerGroup = None

        self._lengthX = '0.0'

        self._lengthZ = '0.0'

        self._team = None

        self._state = None

        self._initialState = None

        self._transitionTime = '1.0'

        self._endOfTransitionPeriod = '-1.0'

        self._mainDirection = 0.0

        self._isActive = 'False'

        self._cp = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def start(self):
        self.g_start.fire(self)

    @unpack_func_args([])
    def reset(self):
        self.g_reset.fire(self)

    @unpack_func_args([])
    def open(self):
        self.g_open.fire(self)

    @unpack_func_args([])
    def transition(self):
        self.g_transition.fire(self)

    @unpack_func_args([])
    def stop(self):
        self.g_stop.fire(self)

    @unpack_func_args(['ATTACK_RESULTS'])
    def harm_receiveAttackResults(self, arg1):
        self.g_harm_receiveAttackResults.fire(self, arg1)

    @unpack_func_args([])
    def smartDestroy(self):
        self.g_smartDestroy.fire(self)

    @unpack_func_args(['VECTOR3'])
    def showBomb(self, arg1):
        self.g_showBomb.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def arena(self):
        return self._arena

    @arena.setter
    def arena(self, value):
        self._arena, = unpack_variables(value, ['MAILBOX'])

    @property
    def arenaBase(self):
        return self._arenaBase

    @arenaBase.setter
    def arenaBase(self, value):
        self._arenaBase, = unpack_variables(value, ['MAILBOX'])

    @property
    def arenaTypeID(self):
        return self._arenaTypeID

    @arenaTypeID.setter
    def arenaTypeID(self, value):
        self._arenaTypeID, = unpack_variables(value, ['INT32'])

    @property
    def groupID(self):
        return self._groupID

    @groupID.setter
    def groupID(self, value):
        self._groupID, = unpack_variables(value, ['UINT8'])

    @property
    def sectorID(self):
        return self._sectorID

    @sectorID.setter
    def sectorID(self, value):
        self._sectorID, = unpack_variables(value, ['UINT8'])

    @property
    def playerGroup(self):
        return self._playerGroup

    @playerGroup.setter
    def playerGroup(self, value):
        self._playerGroup, = unpack_variables(value, ['UINT8'])

    @property
    def IDInPlayerGroup(self):
        return self._IDInPlayerGroup

    @IDInPlayerGroup.setter
    def IDInPlayerGroup(self, value):
        self._IDInPlayerGroup, = unpack_variables(value, ['UINT8'])

    @property
    def lengthX(self):
        return self._lengthX

    @lengthX.setter
    def lengthX(self, value):
        self._lengthX, = unpack_variables(value, ['FLOAT32'])

    @property
    def lengthZ(self):
        return self._lengthZ

    @lengthZ.setter
    def lengthZ(self, value):
        self._lengthZ, = unpack_variables(value, ['FLOAT32'])

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team, = unpack_variables(value, ['UINT8'])

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state, = unpack_variables(value, ['UINT8'])

    @property
    def initialState(self):
        return self._initialState

    @initialState.setter
    def initialState(self, value):
        self._initialState, = unpack_variables(value, ['UINT8'])

    @property
    def transitionTime(self):
        return self._transitionTime

    @transitionTime.setter
    def transitionTime(self, value):
        self._transitionTime, = unpack_variables(value, ['FLOAT32'])

    @property
    def endOfTransitionPeriod(self):
        return self._endOfTransitionPeriod

    @endOfTransitionPeriod.setter
    def endOfTransitionPeriod(self, value):
        self._endOfTransitionPeriod, = unpack_variables(value, ['FLOAT32'])

    @property
    def mainDirection(self):
        return self._mainDirection

    @mainDirection.setter
    def mainDirection(self, value):
        self._mainDirection, = unpack_variables(value, ['UINT8'])

    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, value):
        self._isActive, = unpack_variables(value, ['BOOL'])

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp, = unpack_variables(value, ['PYTHON'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)