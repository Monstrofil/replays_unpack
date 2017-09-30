#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #


from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.VisionOwner import VisionOwner
except:
    from VisionOwner import VisionOwner

try:
    from interfaces.AtbaOwner import AtbaOwner
except:
    from AtbaOwner import AtbaOwner

try:
    from interfaces.AirDefenceOwner import AirDefenceOwner
except:
    from AirDefenceOwner import AirDefenceOwner

try:
    from interfaces.DebugDrawEntity import DebugDrawEntity
except:
    from DebugDrawEntity import DebugDrawEntity

try:
    from interfaces.HitLocationManagerOwner import HitLocationManagerOwner
except:
    from HitLocationManagerOwner import HitLocationManagerOwner



class Vehicle(VisionOwner, AtbaOwner, AirDefenceOwner, DebugDrawEntity, HitLocationManagerOwner):
    
    g_startOfflineBattle = EventHook()
    
    g_onConsumableInterrupted = EventHook()
    
    g_setAmmoArtilleryGun = EventHook()
    
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
    
    g_stopVarys = EventHook()
    
    g_reflood = EventHook()
    
    g_onShotDecal = EventHook()
    
    g_receiveMirrorDamage = EventHook()
    
    g_offlineSetAI = EventHook()
    
    g_offlineRecieveMovementRoute = EventHook()
    
    g_receiveVisibilityFactors = EventHook()
    
    g_forceReloadTorpedoes = EventHook()
    
    g_onSkillActivated = EventHook()
    
    g_uniqueSkillActivated = EventHook()
    
    g_onClientEnterWorld = EventHook()
    
    g_onClientLeaveWorld = EventHook()
    
    g_suicide = EventHook()
    
    g_dev_teleportShip = EventHook()
    
    g_dev_killPlane = EventHook()
    
    g_dev_flight = EventHook()
    
    g_offlineOnHit = EventHook()
    
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

        self._isAlive = None

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


        # MRO fix

        VisionOwner.__init__(self)

        AtbaOwner.__init__(self)

        AirDefenceOwner.__init__(self)

        DebugDrawEntity.__init__(self)

        HitLocationManagerOwner.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args([])
    def startOfflineBattle(self):
        self.g_startOfflineBattle.fire(self)

    @unpack_func_args(['UINT8'])
    def onConsumableInterrupted(self, arg1):
        self.g_onConsumableInterrupted.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def setAmmoArtilleryGun(self, arg1):
        self.g_setAmmoArtilleryGun.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'UINT64']])
    def setShotDecals(self, arg1):
        self.g_setShotDecals.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'DAMAGES']])
    def receiveDamagesOnShip(self, arg1):
        self.g_receiveDamagesOnShip.fire(self, arg1)

    @unpack_func_args(['INT8', 'FLOAT32'])
    def consumableUsed(self, arg1, arg2):
        self.g_consumableUsed.fire(self, arg1, arg2)

    @unpack_func_args(['BOOL'])
    def setArtilleryGunsDefaultYawsPitchsTo(self, arg1):
        self.g_setArtilleryGunsDefaultYawsPitchsTo.fire(self, arg1)

    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL', 'FLOAT32', 'INT32'])
    def syncMyTorpedoTube(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_syncMyTorpedoTube.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL', 'FLOAT32', ['ARRAY', 'STRING']])
    def syncMyArtilleryGun(self, arg1, arg2, arg3, arg4, arg5, arg6):
        self.g_syncMyArtilleryGun.fire(self, arg1, arg2, arg3, arg4, arg5, arg6)

    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL'])
    def syncArtilleryGun(self, arg1, arg2, arg3, arg4):
        self.g_syncArtilleryGun.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['INT32', 'FLOAT32', 'FLOAT32', 'BOOL', 'INT32'])
    def syncTorpedoTube(self, arg1, arg2, arg3, arg4, arg5):
        self.g_syncTorpedoTube.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT32', 'UINT32'])
    def syncTorpedoState(self, arg1, arg2):
        self.g_syncTorpedoState.fire(self, arg1, arg2)

    @unpack_func_args(['UINT32', 'UINT32', 'UINT32', 'FLOAT', 'UINT8', 'VECTOR2', 'VECTOR3', 'VECTOR3'])
    def kill(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        self.g_kill.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @unpack_func_args(['FLOAT'])
    def forceSink(self, arg1):
        self.g_forceSink.fire(self, arg1)

    @unpack_func_args(['FLOAT'])
    def bodySinkPartLurched(self, arg1):
        self.g_bodySinkPartLurched.fire(self, arg1)

    @unpack_func_args(['INT32', 'VECTOR3', 'INT32', 'INT32', 'BOOL'])
    def shootTorpedo(self, arg1, arg2, arg3, arg4, arg5):
        self.g_shootTorpedo.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT16'])
    def shootGuns(self, arg1):
        self.g_shootGuns.fire(self, arg1)

    @unpack_func_args(['BLOB', 'BLOB'])
    def syncShipCracks(self, arg1, arg2):
        self.g_syncShipCracks.fire(self, arg1, arg2)

    @unpack_func_args([])
    def makeShipCracksActive(self):
        self.g_makeShipCracksActive.fire(self)

    @unpack_func_args(['INT8', 'BLOB'])
    def makeShipCracks(self, arg1, arg2):
        self.g_makeShipCracks.fire(self, arg1, arg2)

    @unpack_func_args(['BLOB'])
    def setReloadingStateTorpedoes(self, arg1):
        self.g_setReloadingStateTorpedoes.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def setReloadingStateArtillery(self, arg1):
        self.g_setReloadingStateArtillery.fire(self, arg1)

    @unpack_func_args(['BLOB'])
    def setConsumables(self, arg1):
        self.g_setConsumables.fire(self, arg1)

    @unpack_func_args([])
    def stopVarys(self):
        self.g_stopVarys.fire(self)

    @unpack_func_args([])
    def reflood(self):
        self.g_reflood.fire(self)

    @unpack_func_args(['UINT64'])
    def onShotDecal(self, arg1):
        self.g_onShotDecal.fire(self, arg1)

    @unpack_func_args(['FLOAT'])
    def receiveMirrorDamage(self, arg1):
        self.g_receiveMirrorDamage.fire(self, arg1)

    @unpack_func_args(['UINT32'])
    def offlineSetAI(self, arg1):
        self.g_offlineSetAI.fire(self, arg1)

    @unpack_func_args([['ARRAY', 'VECTOR3']])
    def offlineRecieveMovementRoute(self, arg1):
        self.g_offlineRecieveMovementRoute.fire(self, arg1)

    @unpack_func_args(['FLOAT', 'FLOAT', 'FLOAT'])
    def receiveVisibilityFactors(self, arg1, arg2, arg3):
        self.g_receiveVisibilityFactors.fire(self, arg1, arg2, arg3)

    @unpack_func_args([])
    def forceReloadTorpedoes(self):
        self.g_forceReloadTorpedoes.fire(self)

    @unpack_func_args(['UINT32'])
    def onSkillActivated(self, arg1):
        self.g_onSkillActivated.fire(self, arg1)

    @unpack_func_args([])
    def uniqueSkillActivated(self):
        self.g_uniqueSkillActivated.fire(self)

    @unpack_func_args([])
    def onClientEnterWorld(self):
        self.g_onClientEnterWorld.fire(self)

    @unpack_func_args([])
    def onClientLeaveWorld(self):
        self.g_onClientLeaveWorld.fire(self)

    @unpack_func_args([])
    def suicide(self):
        self.g_suicide.fire(self)

    @unpack_func_args(['VECTOR3'])
    def dev_teleportShip(self, arg1):
        self.g_dev_teleportShip.fire(self, arg1)

    @unpack_func_args([])
    def dev_killPlane(self):
        self.g_dev_killPlane.fire(self)

    @unpack_func_args([])
    def dev_flight(self):
        self.g_dev_flight.fire(self)

    @unpack_func_args(['ON_HIT_INFO'])
    def offlineOnHit(self, arg1):
        self.g_offlineOnHit.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def isOnForsage(self):
        return self._isOnForsage

    @isOnForsage.setter
    def isOnForsage(self, value):
        self._isOnForsage, = unpack_variables(value, ['BOOL'])

    @property
    def regenCrewHpLimit(self):
        return self._regenCrewHpLimit

    @regenCrewHpLimit.setter
    def regenCrewHpLimit(self, value):
        self._regenCrewHpLimit, = unpack_variables(value, ['FLOAT32'])

    @property
    def buoyancy(self):
        return self._buoyancy

    @buoyancy.setter
    def buoyancy(self, value):
        self._buoyancy, = unpack_variables(value, ['FLOAT32'])

    @property
    def targetLocalPos(self):
        return self._targetLocalPos

    @targetLocalPos.setter
    def targetLocalPos(self, value):
        self._targetLocalPos, = unpack_variables(value, ['UINT16'])

    @property
    def torpedoLocalPos(self):
        return self._torpedoLocalPos

    @torpedoLocalPos.setter
    def torpedoLocalPos(self, value):
        self._torpedoLocalPos, = unpack_variables(value, ['UINT16'])

    @property
    def weaponLockFlags(self):
        return self._weaponLockFlags

    @weaponLockFlags.setter
    def weaponLockFlags(self, value):
        self._weaponLockFlags, = unpack_variables(value, ['UINT16'])

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner, = unpack_variables(value, ['ENTITY_ID'])

    @property
    def shipConfig(self):
        return self._shipConfig

    @shipConfig.setter
    def shipConfig(self, value):
        self._shipConfig, = unpack_variables(value, ['SHIP_CONFIG'])

    @property
    def crewModifiersCompactParams(self):
        return self._crewModifiersCompactParams

    @crewModifiersCompactParams.setter
    def crewModifiersCompactParams(self, value):
        self._crewModifiersCompactParams, = unpack_variables(value, ['CREW_MODIFIERS_COMPACT_PARAMS'])

    @property
    def teamId(self):
        return self._teamId

    @teamId.setter
    def teamId(self, value):
        self._teamId, = unpack_variables(value, ['TEAM_ID'])

    @property
    def isAlive(self):
        return self._isAlive

    @isAlive.setter
    def isAlive(self, value):
        self._isAlive, = unpack_variables(value, ['BOOL'])

    @property
    def selectedWeapon(self):
        return self._selectedWeapon

    @selectedWeapon.setter
    def selectedWeapon(self, value):
        self._selectedWeapon, = unpack_variables(value, ['UINT32'])

    @property
    def serverSpeedRaw(self):
        return self._serverSpeedRaw

    @serverSpeedRaw.setter
    def serverSpeedRaw(self, value):
        self._serverSpeedRaw, = unpack_variables(value, ['UINT8'])

    @property
    def speedSignDir(self):
        return self._speedSignDir

    @speedSignDir.setter
    def speedSignDir(self, value):
        self._speedSignDir, = unpack_variables(value, ['INT8'])

    @property
    def enginePower(self):
        return self._enginePower

    @enginePower.setter
    def enginePower(self, value):
        self._enginePower, = unpack_variables(value, ['UINT8'])

    @property
    def isInOfflineMode(self):
        return self._isInOfflineMode

    @isInOfflineMode.setter
    def isInOfflineMode(self, value):
        self._isInOfflineMode, = unpack_variables(value, ['BOOL'])

    @property
    def ignoreMapBorders(self):
        return self._ignoreMapBorders

    @ignoreMapBorders.setter
    def ignoreMapBorders(self, value):
        self._ignoreMapBorders, = unpack_variables(value, ['BOOL'])

    @property
    def debugText(self):
        return self._debugText

    @debugText.setter
    def debugText(self, value):
        self._debugText, = unpack_variables(value, [['ARRAY', 'ENTITY_DEBUG_TEXT']])

    @property
    def isBot(self):
        return self._isBot

    @isBot.setter
    def isBot(self, value):
        self._isBot, = unpack_variables(value, ['BOOL'])

    @property
    def miscsPresetsStatus(self):
        return self._miscsPresetsStatus

    @miscsPresetsStatus.setter
    def miscsPresetsStatus(self, value):
        self._miscsPresetsStatus, = unpack_variables(value, [['ARRAY', 'STRING']])

    @property
    def draught(self):
        return self._draught

    @draught.setter
    def draught(self, value):
        self._draught, = unpack_variables(value, ['FLOAT32'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)