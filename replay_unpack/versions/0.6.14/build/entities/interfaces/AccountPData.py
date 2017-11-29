#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AccountPData(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._name = ''

        self._normalizedName = None

        self._spaID = None

        self._version = None

        self._accountType = None

        self._attrs = 0.0

        self._level = 0.0

        self._isTeamkiller = 0.0

        self._rank = 0.0

        self._lastGameTime = 0.0

        self._persistentData = None

        self._vhID = None

        self._dataRevision = 1.0

        self._ttkStatus = 0.0

        self.__destroyReason = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################



    ####################################
    #       PROPERTIES
    ####################################


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name, = unpack_variables(value, ['STRING'])

    @property
    def normalizedName(self):
        return self._normalizedName

    @normalizedName.setter
    def normalizedName(self, value):
        self._normalizedName, = unpack_variables(value, ['STRING'])

    @property
    def spaID(self):
        return self._spaID

    @spaID.setter
    def spaID(self, value):
        self._spaID, = unpack_variables(value, ['DB_ID'])

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version, = unpack_variables(value, ['INT16'])

    @property
    def accountType(self):
        return self._accountType

    @accountType.setter
    def accountType(self, value):
        self._accountType, = unpack_variables(value, ['UINT32'])

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        self._attrs, = unpack_variables(value, ['UINT64'])

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level, = unpack_variables(value, ['UINT32'])

    @property
    def isTeamkiller(self):
        return self._isTeamkiller

    @isTeamkiller.setter
    def isTeamkiller(self, value):
        self._isTeamkiller, = unpack_variables(value, ['UINT8'])

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank, = unpack_variables(value, ['UINT32'])

    @property
    def lastGameTime(self):
        return self._lastGameTime

    @lastGameTime.setter
    def lastGameTime(self, value):
        self._lastGameTime, = unpack_variables(value, ['UINT32'])

    @property
    def persistentData(self):
        return self._persistentData

    @persistentData.setter
    def persistentData(self, value):
        self._persistentData, = unpack_variables(value, ['STRING'])

    @property
    def vhID(self):
        return self._vhID

    @vhID.setter
    def vhID(self, value):
        self._vhID, = unpack_variables(value, ['UINT64'])

    @property
    def dataRevision(self):
        return self._dataRevision

    @dataRevision.setter
    def dataRevision(self, value):
        self._dataRevision, = unpack_variables(value, ['UINT64'])

    @property
    def ttkStatus(self):
        return self._ttkStatus

    @ttkStatus.setter
    def ttkStatus(self, value):
        self._ttkStatus, = unpack_variables(value, ['UINT64'])

    @property
    def _destroyReason(self):
        return self.__destroyReason

    @_destroyReason.setter
    def _destroyReason(self, value):
        self.__destroyReason, = unpack_variables(value, ['UINT8'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)