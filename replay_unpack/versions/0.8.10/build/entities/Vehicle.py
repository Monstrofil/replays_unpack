#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from interfaces.VisionOwner import VisionOwner
from interfaces.AtbaOwner import AtbaOwner
from interfaces.AirDefenceOwner import AirDefenceOwner
from interfaces.DebugDrawEntity import DebugDrawEntity
from interfaces.HitLocationManagerOwner import HitLocationManagerOwner
from interfaces.AviationOwner import AviationOwner
from interfaces.BuoyancyOwner import BuoyancyOwner
from interfaces.WeatherOwner import WeatherOwner
from interfaces.ModelOwner import ModelOwner



class Vehicle(VisionOwner, AtbaOwner, AirDefenceOwner, DebugDrawEntity, HitLocationManagerOwner, AviationOwner, BuoyancyOwner, WeatherOwner, ModelOwner):
    
    g_startOfflineBattle = EventHook()
    
    g_onConsumableInterrupted = EventHook()
    
    g_setAmmoArtilleryGun = EventHook()
    
    g_setAmmoTorpedoTube = EventHook()
    
    g_setAmmoTorpedoTubes = EventHook()
    
    g_startTorpedoTubeReload = EventHook()
    
    g_setShotDecals = EventHook()
    
    g_receiveDamagesOnShip = EventHook()
    
    g_consumableUsed = EventHook()
    
    g_setArtilleryGunsDefaultYawsPitchsTo = EventHook()
    
    g_syncMyTorpedoTube = EventHook()
    
    g_syncMyArtilleryGun = EventHook()
    
    g_syncArtilleryGun = EventHook()
    
    g_syncTorpedoTube = EventHook()
    
    g_syncTorpedoState = EventHook()
    
    g_kill = EventHook()
    
    g_forceSink = EventHook()
    
    g_bodySinkPartLurched = EventHook()
    
    g_shootTorpedo = EventHook()
    
    g_shootGuns = EventHook()
    
    g_syncShipCracks = EventHook()
    
    g_makeShipCracksActive = EventHook()
    
    g_makeShipCracks = EventHook()
    
    g_setReloadingStateTorpedoes = EventHook()
    
    g_setReloadingStateArtillery = EventHook()
    
    g_setConsumables = EventHook()
    
    g_setSqsConsumables = EventHook()
    
    g_stopVarys = EventHook()
    
    g_onShotDecal = EventHook()
    
    g_receiveMirrorDamage = EventHook()
    
    g_offlineSetAI = EventHook()
    
    g_offlineRecieveMovementRoute = EventHook()
    
    g_forceReloadTorpedoes = EventHook()
    
    g_uniqueTriggerActivated = EventHook()
    
    g_onConsumableEnabled = EventHook()
    
    g_updateRudderAngles = EventHook()
    
    g_updateDeepRudderAngles = EventHook()
    
    g_setModifierCoefArtilleryReload = EventHook()
    
    g_setModifierCoefTorpedoesReload = EventHook()
    
    g_setOneTimeArtilleryReload = EventHook()
    
    g_setOneTimeTorpedoesReload = EventHook()
    
    g_onReseted = EventHook()
    
    g_setAirDefenseState = EventHook()
    
    g_onPrioritySectorSet = EventHook()
    
    g_onNextPrioritySectorSet = EventHook()
    
    g_teleport = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._isOnForsage = 0.0

        self._regenCrewHpLimit = '0.0'

        self._buoyancy = None

        self._targetLocalPos = None

        self._torpedoLocalPos = None

        self._weaponLockFlags = 0.0

        self._owner = None

        self._shipConfig = None

        self._crewModifiersCompactParams = None

        self._teamId = None

        self._uiEnabled = None

        self._isAlive = 'True'

        self._selectedWeapon = 0.0

        self._serverSpeedRaw = None

        self._speedSignDir = None

        self._enginePower = None

        self._isInOfflineMode = None

        self._ignoreMapBorders = None

        self._debugText = None

        self._isBot = 'False'

        self._miscsPresetsStatus = None

        self._draught = None

        self._isFogHornOn = None

        self._additionalGMMaxDistCoeff = '1.0'

        self._blockedControls = None

        self._isInvisible = None


        # MRO fix

        VisionOwner.__init__(self)

        AtbaOwner.__init__(self)

        AirDefenceOwner.__init__(self)

        DebugDrawEntity.__init__(self)

        HitLocationManagerOwner.__init__(self)

        AviationOwner.__init__(self)

        BuoyancyOwner.__init__(self)

        WeatherOwner.__init__(self)

        ModelOwner.__init__(self)

        self._properties = getattr(self, '_properties', [])
        for item in [
            (8, 'isOnForsage'),
            (32, 'regenCrewHpLimit'),
            (32, 'buoyancy'),
            (16, 'targetLocalPos'),
            (16, 'torpedoLocalPos'),
            (16, 'weaponLockFlags'),
            (32, 'owner'),
            (10000000000, 'shipConfig'),
            (128, 'crewModifiersCompactParams'),
            (8, 'teamId'),
            (8, 'uiEnabled'),
            (8, 'isAlive'),
            (32, 'selectedWeapon'),
            (16, 'serverSpeedRaw'),
            (8, 'speedSignDir'),
            (8, 'enginePower'),
            (8, 'isInOfflineMode'),
            (8, 'ignoreMapBorders'),
            (10000000000, 'debugText'),
            (8, 'isBot'),
            (10000000000, 'miscsPresetsStatus'),
            (32, 'draught'),
            (8, 'isFogHornOn'),
            (32, 'additionalGMMaxDistCoeff'),
            (8, 'blockedControls'),
            (8, 'isInvisible'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (1, 'startOfflineBattle'),
            (9, 'onConsumableInterrupted'),
            (9, 'setAmmoArtilleryGun'),
            (17, 'setAmmoTorpedoTube'),
            (17, 'setAmmoTorpedoTubes'),
            (9, 'startTorpedoTubeReload'),
            (10000000001, 'setShotDecals'),
            (10000000002, 'receiveDamagesOnShip'),
            (41, 'consumableUsed'),
            (9, 'setArtilleryGunsDefaultYawsPitchsTo'),
            (169, 'syncMyTorpedoTube'),
            (10000000001, 'syncMyArtilleryGun'),
            (105, 'syncArtilleryGun'),
            (137, 'syncTorpedoTube'),
            (65, 'syncTorpedoState'),
            (369, 'kill'),
            (33, 'forceSink'),
            (33, 'bodySinkPartLurched'),
            (201, 'shootTorpedo'),
            (17, 'shootGuns'),
            (10000000001, 'syncShipCracks'),
            (1, 'makeShipCracksActive'),
            (10000000002, 'makeShipCracks'),
            (10000000002, 'setReloadingStateTorpedoes'),
            (10000000002, 'setReloadingStateArtillery'),
            (10000000001, 'setConsumables'),
            (10000000001, 'setSqsConsumables'),
            (1, 'stopVarys'),
            (65, 'onShotDecal'),
            (33, 'receiveMirrorDamage'),
            (33, 'offlineSetAI'),
            (10000000001, 'offlineRecieveMovementRoute'),
            (1, 'forceReloadTorpedoes'),
            (1, 'uniqueTriggerActivated'),
            (17, 'onConsumableEnabled'),
            (33, 'updateRudderAngles'),
            (33, 'updateDeepRudderAngles'),
            (33, 'setModifierCoefArtilleryReload'),
            (33, 'setModifierCoefTorpedoesReload'),
            (33, 'setOneTimeArtilleryReload'),
            (33, 'setOneTimeTorpedoesReload'),
            (1, 'onReseted'),
            (10000000001, 'setAirDefenseState'),
            (41, 'onPrioritySectorSet'),
            (9, 'onNextPrioritySectorSet'),
            (129, 'teleport'),
            
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

# method size: 1
    @unpack_func_args([])
    def startOfflineBattle(self):
        self.g_startOfflineBattle.fire(self)
# method size: 9
    @unpack_func_args(['UINT8'])
    def onConsumableInterrupted(self, arg1):
        self.g_onConsumableInterrupted.fire(self, arg1)
# method size: 9
    @unpack_func_args(['UINT8'])
    def setAmmoArtilleryGun(self, arg1):
        self.g_setAmmoArtilleryGun.fire(self, arg1)
# method size: 17
    @unpack_func_args(['UINT8', 'UINT8'])
    def setAmmoTorpedoTube(self, arg1, arg2):
        self.g_setAmmoTorpedoTube.fire(self, arg1, arg2)
# method size: 17
    @unpack_func_args(['UINT8', 'UINT8'])
    def setAmmoTorpedoTubes(self, arg1, arg2):
        self.g_setAmmoTorpedoTubes.fire(self, arg1, arg2)
# method size: 9
    @unpack_func_args(['UINT8'])
    def startTorpedoTubeReload(self, arg1):
        self.g_startTorpedoTubeReload.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args([['ARRAY', 'UINT64']])
    def setShotDecals(self, arg1):
        self.g_setShotDecals.fire(self, arg1)
# method size: 10000000002
    @unpack_func_args([['ARRAY', 'DAMAGES']])
    def receiveDamagesOnShip(self, arg1):
        self.g_receiveDamagesOnShip.fire(self, arg1)
# method size: 41
    @unpack_func_args(['INT8', 'FLOAT32'])
    def consumableUsed(self, arg1, arg2):
        self.g_consumableUsed.fire(self, arg1, arg2)
# method size: 9
    @unpack_func_args(['BOOL'])
    def setArtilleryGunsDefaultYawsPitchsTo(self, arg1):
        self.g_setArtilleryGunsDefaultYawsPitchsTo.fire(self, arg1)
# method size: 169
    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL', 'FLOAT32', 'INT32'])
    def syncMyTorpedoTube(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_syncMyTorpedoTube.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)
# method size: 10000000001
    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL', 'FLOAT32', ['ARRAY', 'STRING']])
    def syncMyArtilleryGun(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_syncMyArtilleryGun.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)
# method size: 105
    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL'])
    def syncArtilleryGun(self, arg1, arg2, arg3, arg4):
        self.g_syncArtilleryGun.fire(self, arg1, arg2, arg3, arg4)
# method size: 137
    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL', 'INT32'])
    def syncTorpedoTube(self, arg1, arg2, arg3, arg4, arg5):
        self.g_syncTorpedoTube.fire(self, arg1, arg2, arg3, arg4, arg5)
# method size: 65
    @unpack_func_args(['UINT32', 'UINT32'])
    def syncTorpedoState(self, arg1, arg2):
        self.g_syncTorpedoState.fire(self, arg1, arg2)
# method size: 369
    @unpack_func_args(['INT8', 'UINT32', 'UINT32', 'FLOAT', 'UINT8', 'VECTOR2', 'VECTOR3', 'VECTOR3'])
    def kill(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_kill.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def forceSink(self, arg1):
        self.g_forceSink.fire(self, arg1)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def bodySinkPartLurched(self, arg1):
        self.g_bodySinkPartLurched.fire(self, arg1)
# method size: 201
    @unpack_func_args(['INT32', 'VECTOR3', 'INT32', 'INT32', 'BOOL'])
    def shootTorpedo(self, arg1, arg2, arg3, arg4, arg5):
        self.g_shootTorpedo.fire(self, arg1, arg2, arg3, arg4, arg5)
# method size: 17
    @unpack_func_args(['UINT16'])
    def shootGuns(self, arg1):
        self.g_shootGuns.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB', 'BLOB'])
    def syncShipCracks(self, arg1, arg2):
        self.g_syncShipCracks.fire(self, arg1, arg2)
# method size: 1
    @unpack_func_args([])
    def makeShipCracksActive(self):
        self.g_makeShipCracksActive.fire(self)
# method size: 10000000002
    @unpack_func_args(['INT8', 'BLOB'])
    def makeShipCracks(self, arg1, arg2):
        self.g_makeShipCracks.fire(self, arg1, arg2)
# method size: 10000000002
    @unpack_func_args(['BLOB'])
    def setReloadingStateTorpedoes(self, arg1):
        self.g_setReloadingStateTorpedoes.fire(self, arg1)
# method size: 10000000002
    @unpack_func_args(['BLOB'])
    def setReloadingStateArtillery(self, arg1):
        self.g_setReloadingStateArtillery.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def setConsumables(self, arg1):
        self.g_setConsumables.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['PLANE_ID', 'BLOB'])
    def setSqsConsumables(self, arg1, arg2):
        self.g_setSqsConsumables.fire(self, arg1, arg2)
# method size: 1
    @unpack_func_args([])
    def stopVarys(self):
        self.g_stopVarys.fire(self)
# method size: 65
    @unpack_func_args(['UINT64'])
    def onShotDecal(self, arg1):
        self.g_onShotDecal.fire(self, arg1)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def receiveMirrorDamage(self, arg1):
        self.g_receiveMirrorDamage.fire(self, arg1)
# method size: 33
    @unpack_func_args(['UINT32'])
    def offlineSetAI(self, arg1):
        self.g_offlineSetAI.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args([['ARRAY', 'VECTOR3']])
    def offlineRecieveMovementRoute(self, arg1):
        self.g_offlineRecieveMovementRoute.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def forceReloadTorpedoes(self):
        self.g_forceReloadTorpedoes.fire(self)
# method size: 1
    @unpack_func_args([])
    def uniqueTriggerActivated(self):
        self.g_uniqueTriggerActivated.fire(self)
# method size: 17
    @unpack_func_args(['UINT8', 'BOOL'])
    def onConsumableEnabled(self, arg1, arg2):
        self.g_onConsumableEnabled.fire(self, arg1, arg2)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def updateRudderAngles(self, arg1):
        self.g_updateRudderAngles.fire(self, arg1)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def updateDeepRudderAngles(self, arg1):
        self.g_updateDeepRudderAngles.fire(self, arg1)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def setModifierCoefArtilleryReload(self, arg1):
        self.g_setModifierCoefArtilleryReload.fire(self, arg1)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def setModifierCoefTorpedoesReload(self, arg1):
        self.g_setModifierCoefTorpedoesReload.fire(self, arg1)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def setOneTimeArtilleryReload(self, arg1):
        self.g_setOneTimeArtilleryReload.fire(self, arg1)
# method size: 33
    @unpack_func_args(['FLOAT'])
    def setOneTimeTorpedoesReload(self, arg1):
        self.g_setOneTimeTorpedoesReload.fire(self, arg1)
# method size: 1
    @unpack_func_args([])
    def onReseted(self):
        self.g_onReseted.fire(self)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def setAirDefenseState(self, arg1):
        self.g_setAirDefenseState.fire(self, arg1)
# method size: 41
    @unpack_func_args(['INT8', 'FLOAT'])
    def onPrioritySectorSet(self, arg1, arg2):
        self.g_onPrioritySectorSet.fire(self, arg1, arg2)
# method size: 9
    @unpack_func_args(['INT8'])
    def onNextPrioritySectorSet(self, arg1):
        self.g_onNextPrioritySectorSet.fire(self, arg1)
# method size: 129
    @unpack_func_args(['VECTOR3', 'FLOAT'])
    def teleport(self, arg1, arg2):
        self.g_teleport.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 8
    @property
    def isOnForsage(self):
        return self._isOnForsage

    @isOnForsage.setter
    def isOnForsage(self, value):
        self._isOnForsage, = unpack_variables(value, ['BOOL'])
# property size: 32
    @property
    def regenCrewHpLimit(self):
        return self._regenCrewHpLimit

    @regenCrewHpLimit.setter
    def regenCrewHpLimit(self, value):
        self._regenCrewHpLimit, = unpack_variables(value, ['FLOAT32'])
# property size: 32
    @property
    def buoyancy(self):
        return self._buoyancy

    @buoyancy.setter
    def buoyancy(self, value):
        self._buoyancy, = unpack_variables(value, ['FLOAT32'])
# property size: 16
    @property
    def targetLocalPos(self):
        return self._targetLocalPos

    @targetLocalPos.setter
    def targetLocalPos(self, value):
        self._targetLocalPos, = unpack_variables(value, ['UINT16'])
# property size: 16
    @property
    def torpedoLocalPos(self):
        return self._torpedoLocalPos

    @torpedoLocalPos.setter
    def torpedoLocalPos(self, value):
        self._torpedoLocalPos, = unpack_variables(value, ['UINT16'])
# property size: 16
    @property
    def weaponLockFlags(self):
        return self._weaponLockFlags

    @weaponLockFlags.setter
    def weaponLockFlags(self, value):
        self._weaponLockFlags, = unpack_variables(value, ['UINT16'])
# property size: 32
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner, = unpack_variables(value, ['ENTITY_ID'])
# property size: 10000000000
    @property
    def shipConfig(self):
        return self._shipConfig

    @shipConfig.setter
    def shipConfig(self, value):
        self._shipConfig, = unpack_variables(value, ['SHIP_CONFIG'])
# property size: 128
    @property
    def crewModifiersCompactParams(self):
        return self._crewModifiersCompactParams

    @crewModifiersCompactParams.setter
    def crewModifiersCompactParams(self, value):
        self._crewModifiersCompactParams, = unpack_variables(value, ['CREW_MODIFIERS_COMPACT_PARAMS'])
# property size: 8
    @property
    def teamId(self):
        return self._teamId

    @teamId.setter
    def teamId(self, value):
        self._teamId, = unpack_variables(value, ['TEAM_ID'])
# property size: 8
    @property
    def uiEnabled(self):
        return self._uiEnabled

    @uiEnabled.setter
    def uiEnabled(self, value):
        self._uiEnabled, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def isAlive(self):
        return self._isAlive

    @isAlive.setter
    def isAlive(self, value):
        self._isAlive, = unpack_variables(value, ['BOOL'])
# property size: 32
    @property
    def selectedWeapon(self):
        return self._selectedWeapon

    @selectedWeapon.setter
    def selectedWeapon(self, value):
        self._selectedWeapon, = unpack_variables(value, ['UINT32'])
# property size: 16
    @property
    def serverSpeedRaw(self):
        return self._serverSpeedRaw

    @serverSpeedRaw.setter
    def serverSpeedRaw(self, value):
        self._serverSpeedRaw, = unpack_variables(value, ['UINT16'])
# property size: 8
    @property
    def speedSignDir(self):
        return self._speedSignDir

    @speedSignDir.setter
    def speedSignDir(self, value):
        self._speedSignDir, = unpack_variables(value, ['INT8'])
# property size: 8
    @property
    def enginePower(self):
        return self._enginePower

    @enginePower.setter
    def enginePower(self, value):
        self._enginePower, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def isInOfflineMode(self):
        return self._isInOfflineMode

    @isInOfflineMode.setter
    def isInOfflineMode(self, value):
        self._isInOfflineMode, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def ignoreMapBorders(self):
        return self._ignoreMapBorders

    @ignoreMapBorders.setter
    def ignoreMapBorders(self, value):
        self._ignoreMapBorders, = unpack_variables(value, ['BOOL'])
# property size: 10000000000
    @property
    def debugText(self):
        return self._debugText

    @debugText.setter
    def debugText(self, value):
        self._debugText, = unpack_variables(value, [['ARRAY', 'ENTITY_DEBUG_TEXT']])
# property size: 8
    @property
    def isBot(self):
        return self._isBot

    @isBot.setter
    def isBot(self, value):
        self._isBot, = unpack_variables(value, ['BOOL'])
# property size: 10000000000
    @property
    def miscsPresetsStatus(self):
        return self._miscsPresetsStatus

    @miscsPresetsStatus.setter
    def miscsPresetsStatus(self, value):
        self._miscsPresetsStatus, = unpack_variables(value, [['ARRAY', 'STRING']])
# property size: 32
    @property
    def draught(self):
        return self._draught

    @draught.setter
    def draught(self, value):
        self._draught, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def isFogHornOn(self):
        return self._isFogHornOn

    @isFogHornOn.setter
    def isFogHornOn(self, value):
        self._isFogHornOn, = unpack_variables(value, ['BOOL'])
# property size: 32
    @property
    def additionalGMMaxDistCoeff(self):
        return self._additionalGMMaxDistCoeff

    @additionalGMMaxDistCoeff.setter
    def additionalGMMaxDistCoeff(self, value):
        self._additionalGMMaxDistCoeff, = unpack_variables(value, ['FLOAT32'])
# property size: 8
    @property
    def blockedControls(self):
        return self._blockedControls

    @blockedControls.setter
    def blockedControls(self, value):
        self._blockedControls, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def isInvisible(self):
        return self._isInvisible

    @isInvisible.setter
    def isInvisible(self, value):
        self._isInvisible, = unpack_variables(value, ['BOOL'])


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