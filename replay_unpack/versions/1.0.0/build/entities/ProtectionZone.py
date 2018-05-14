#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ProtectionZone(object):
    
    g_start = EventHook()
    
    g_reset = EventHook()
    
    g_stop = EventHook()
    
    g_harm_receiveAttackResults = EventHook()
    
    g_smartDestroy = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._arena = None

        self._arenaBase = None

        self._zoneID = 1.0

        self._lengthX = '300.0'

        self._lengthZ = '500.0'

        self._team = 0.0

        self._maxStayTime = '5.0'

        self._numberOfTurrets = 2.0

        self._minTurretShootInterval = '2.0'

        self._minShootingTime = '15.0'

        self._shotDuration = '1.0'

        self._shotRadius = '5.0'

        self._shotShellNation = 'germany'

        self._shotShellName = 'protection_zone_artillery_shell'

        self._shotPiercingPower = '45.'

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
    def stop(self):
        self.g_stop.fire(self)

    @unpack_func_args(['ATTACK_RESULTS'])
    def harm_receiveAttackResults(self, arg1):
        self.g_harm_receiveAttackResults.fire(self, arg1)

    @unpack_func_args([])
    def smartDestroy(self):
        self.g_smartDestroy.fire(self)


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
    def zoneID(self):
        return self._zoneID

    @zoneID.setter
    def zoneID(self, value):
        self._zoneID, = unpack_variables(value, ['UINT8'])

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
    def maxStayTime(self):
        return self._maxStayTime

    @maxStayTime.setter
    def maxStayTime(self, value):
        self._maxStayTime, = unpack_variables(value, ['FLOAT32'])

    @property
    def numberOfTurrets(self):
        return self._numberOfTurrets

    @numberOfTurrets.setter
    def numberOfTurrets(self, value):
        self._numberOfTurrets, = unpack_variables(value, ['UINT8'])

    @property
    def minTurretShootInterval(self):
        return self._minTurretShootInterval

    @minTurretShootInterval.setter
    def minTurretShootInterval(self, value):
        self._minTurretShootInterval, = unpack_variables(value, ['FLOAT32'])

    @property
    def minShootingTime(self):
        return self._minShootingTime

    @minShootingTime.setter
    def minShootingTime(self, value):
        self._minShootingTime, = unpack_variables(value, ['FLOAT32'])

    @property
    def shotDuration(self):
        return self._shotDuration

    @shotDuration.setter
    def shotDuration(self, value):
        self._shotDuration, = unpack_variables(value, ['FLOAT32'])

    @property
    def shotRadius(self):
        return self._shotRadius

    @shotRadius.setter
    def shotRadius(self, value):
        self._shotRadius, = unpack_variables(value, ['FLOAT32'])

    @property
    def shotShellNation(self):
        return self._shotShellNation

    @shotShellNation.setter
    def shotShellNation(self, value):
        self._shotShellNation, = unpack_variables(value, ['STRING'])

    @property
    def shotShellName(self):
        return self._shotShellName

    @shotShellName.setter
    def shotShellName(self, value):
        self._shotShellName, = unpack_variables(value, ['STRING'])

    @property
    def shotPiercingPower(self):
        return self._shotPiercingPower

    @shotPiercingPower.setter
    def shotPiercingPower(self, value):
        self._shotPiercingPower, = unpack_variables(value, ['FLOAT32'])

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