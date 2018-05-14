#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables


try:
    from interfaces.VehicleAI import VehicleAI
except:
    from VehicleAI import VehicleAI

try:
    from interfaces.TeamBase_Vehicle import TeamBase_Vehicle
except:
    from TeamBase_Vehicle import TeamBase_Vehicle

try:
    from interfaces.SectorBase_Vehicle import SectorBase_Vehicle
except:
    from SectorBase_Vehicle import SectorBase_Vehicle

try:
    from interfaces.RepairBase_Vehicle import RepairBase_Vehicle
except:
    from RepairBase_Vehicle import RepairBase_Vehicle

try:
    from interfaces.VehicleObserver import VehicleObserver
except:
    from VehicleObserver import VehicleObserver

try:
    from interfaces.BattleFeedback import BattleFeedback
except:
    from BattleFeedback import BattleFeedback

try:
    from interfaces.Harm import Harm
except:
    from Harm import Harm

try:
    from interfaces.Sector_Vehicle import Sector_Vehicle
except:
    from Sector_Vehicle import Sector_Vehicle

try:
    from interfaces.ProtectionZone_Vehicle import ProtectionZone_Vehicle
except:
    from ProtectionZone_Vehicle import ProtectionZone_Vehicle

try:
    from interfaces.StepRepairPoint_Vehicle import StepRepairPoint_Vehicle
except:
    from StepRepairPoint_Vehicle import StepRepairPoint_Vehicle

try:
    from interfaces.DestructibleEntity_Vehicle import DestructibleEntity_Vehicle
except:
    from DestructibleEntity_Vehicle import DestructibleEntity_Vehicle

try:
    from interfaces.DefenderBonusController_Vehicle import DefenderBonusController_Vehicle
except:
    from DefenderBonusController_Vehicle import DefenderBonusController_Vehicle

try:
    from interfaces.RecoveryMechanic_Vehicle import RecoveryMechanic_Vehicle
except:
    from RecoveryMechanic_Vehicle import RecoveryMechanic_Vehicle

try:
    from interfaces.RespawnController_Vehicle import RespawnController_Vehicle
except:
    from RespawnController_Vehicle import RespawnController_Vehicle

try:
    from interfaces.SmokeController_Vehicle import SmokeController_Vehicle
except:
    from SmokeController_Vehicle import SmokeController_Vehicle

try:
    from interfaces.InspireController_Vehicle import InspireController_Vehicle
except:
    from InspireController_Vehicle import InspireController_Vehicle



class Vehicle(VehicleAI, TeamBase_Vehicle, SectorBase_Vehicle, RepairBase_Vehicle, VehicleObserver, BattleFeedback, Harm, Sector_Vehicle, ProtectionZone_Vehicle, StepRepairPoint_Vehicle, DestructibleEntity_Vehicle, DefenderBonusController_Vehicle, RecoveryMechanic_Vehicle, RespawnController_Vehicle, SmokeController_Vehicle, InspireController_Vehicle):
    
    g_onHealthChanged = EventHook()
    
    g_showShooting = EventHook()
    
    g_showDamageFromShot = EventHook()
    
    g_showDamageFromExplosion = EventHook()
    
    g_showAmmoBayEffect = EventHook()
    
    g_onPushed = EventHook()
    
    g_onStaticCollision = EventHook()
    
    g_showRammingEffect = EventHook()
    
    g_updatePrebattleID = EventHook()
    
    g_moveWith = EventHook()
    
    g_trackWorldPointWithGun = EventHook()
    
    g_trackRelativePointWithGun = EventHook()
    
    g_stopTrackingWithGun = EventHook()
    
    g_trackVehicleWithGun = EventHook()
    
    g_changeSetting = EventHook()
    
    g_sendVisibilityDevelopmentInfo = EventHook()
    
    g_shoot = EventHook()
    
    g_teleportTo = EventHook()
    
    g_replenishAmmo = EventHook()
    
    g_setDevelopmentFeature = EventHook()
    
    g_receiveFakeShot = EventHook()
    
    g_setAvatar = EventHook()
    
    g_registerObserver = EventHook()
    
    g_sendFinalStats = EventHook()
    
    g_onClientConnected = EventHook()
    
    g_onBattleRunning = EventHook()
    
    g_sendStateToOwnClient = EventHook()
    
    g_receiveHitAssistBonus = EventHook()
    
    g_onEnemyVehicleShot = EventHook()
    
    g_scheduleExtraCheck = EventHook()
    
    g_onObservedByEnemy = EventHook()
    
    g_onDetectedByEnemy = EventHook()
    
    g_onConcealedFromEnemy = EventHook()
    
    g_onStopObservationByEnemy = EventHook()
    
    g_updateVehicleAmmo = EventHook()
    
    g_onFlagAction = EventHook()
    
    g_receiveAssistsFromArena = EventHook()
    
    g_receiveFirstDetectionFromArena = EventHook()
    
    g_sendPositionsToClient = EventHook()
    
    g_requestDamagedDevicesFromFor = EventHook()
    
    g_sendDamagedDevicesTo = EventHook()
    
    g_setHonorTitle = EventHook()
    
    g_receiveTaggedDestructibleKill = EventHook()
    
    g_setOnFireByExplosion = EventHook()
    
    g_onReceiveSpatialData = EventHook()
    
    g_onResourceAbsorbed = EventHook()
    
    g_setInsideResourcePoint = EventHook()
    
    g_grantWinPoints = EventHook()
    
    g_activateGasAttack = EventHook()
    
    g_pauseMechanics = EventHook()
    
    g_startOrUpdateExtraFromOutside = EventHook()
    
    g_damageByEquipment = EventHook()
    
    g_updateOwnClientRTT = EventHook()
    
    g_receiveVisibilityUpdate = EventHook()
    
    g_requestVisibilityLists = EventHook()
    
    g_createCellNearHere = EventHook()
    
    g_onCreateCellSuccess = EventHook()
    
    g_receiveFinalStats = EventHook()
    
    g_setAvatar = EventHook()
    
    g_sendFinalStats = EventHook()
    
    g_smartDestroy = EventHook()
    
    g_logAimMetrics = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._isStrafing = None

        self._steeringAngle = None

        self._physicsMode = None

        self._siegeState = None

        self._gunAnglesPacked = None

        self._publicInfo = None

        self._health = None

        self._isCrewActive = None

        self._engineMode = None

        self._damageStickers = None

        self._publicStateModifiers = None

        self._compDescr = None

        self._stunInfo = None

        self._status = None

        self._invisibility = None

        self._radioDistance = None

        self._circularVisionRadius = None

        self._detectedVehicles = None

        self._isObservedByEnemy = None

        self._rammingBonus = None

        self._ammo = None

        self._isClientConnected = None

        self._avatar = None

        self._arenaBase = None

        self._botKind = None

        self._crewCompactDescrs = None

        self._arenaTypeID = None

        self._arenaBonusType = None

        self._tkillRating = None

        self._cp = None

        self._arenaUniqueID = None

        self._accountDBID = None

        self._historyLoggingFlags = None

        self._heatmapLoggingFlags = None

        self._state = None

        self._arena = None

        self._inspiringEffect = None

        self._inspired = None

        self._isSpeedCapturing = None

        self._isBlockingCapture = None


        # MRO fix

        VehicleAI.__init__(self)

        TeamBase_Vehicle.__init__(self)

        SectorBase_Vehicle.__init__(self)

        RepairBase_Vehicle.__init__(self)

        VehicleObserver.__init__(self)

        BattleFeedback.__init__(self)

        Harm.__init__(self)

        Sector_Vehicle.__init__(self)

        ProtectionZone_Vehicle.__init__(self)

        StepRepairPoint_Vehicle.__init__(self)

        DestructibleEntity_Vehicle.__init__(self)

        DefenderBonusController_Vehicle.__init__(self)

        RecoveryMechanic_Vehicle.__init__(self)

        RespawnController_Vehicle.__init__(self)

        SmokeController_Vehicle.__init__(self)

        InspireController_Vehicle.__init__(self)

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['INT16', 'OBJECT_ID', 'UINT8'])
    def onHealthChanged(self, arg1, arg2, arg3):
        self.g_onHealthChanged.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['UINT8'])
    def showShooting(self, arg1):
        self.g_showShooting.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', ['ARRAY', 'UINT64'], 'UINT8', 'UINT8'])
    def showDamageFromShot(self, arg1, arg2, arg3, arg4):
        self.g_showDamageFromShot.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'UINT8', 'UINT8'])
    def showDamageFromExplosion(self, arg1, arg2, arg3, arg4):
        self.g_showDamageFromExplosion.fire(self, arg1, arg2, arg3, arg4)

    @unpack_func_args(['UINT8', 'FLOAT32', 'FLOAT32'])
    def showAmmoBayEffect(self, arg1, arg2, arg3):
        self.g_showAmmoBayEffect.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['FLOAT32', 'FLOAT32'])
    def onPushed(self, arg1, arg2):
        self.g_onPushed.fire(self, arg1, arg2)

    @unpack_func_args(['FLOAT32', 'VECTOR3', 'VECTOR3', 'UINT8', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'INT8', 'UINT16'])
    def onStaticCollision(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_onStaticCollision.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    @unpack_func_args(['FLOAT32', 'VECTOR3'])
    def showRammingEffect(self, arg1, arg2):
        self.g_showRammingEffect.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID'])
    def updatePrebattleID(self, arg1):
        self.g_updatePrebattleID.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def moveWith(self, arg1):
        self.g_moveWith.fire(self, arg1)

    @unpack_func_args(['VECTOR3'])
    def trackWorldPointWithGun(self, arg1):
        self.g_trackWorldPointWithGun.fire(self, arg1)

    @unpack_func_args(['VECTOR3'])
    def trackRelativePointWithGun(self, arg1):
        self.g_trackRelativePointWithGun.fire(self, arg1)

    @unpack_func_args(['FLOAT32', 'FLOAT32'])
    def stopTrackingWithGun(self, arg1, arg2):
        self.g_stopTrackingWithGun.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID'])
    def trackVehicleWithGun(self, arg1):
        self.g_trackVehicleWithGun.fire(self, arg1)

    @unpack_func_args(['UINT8', 'INT32'])
    def changeSetting(self, arg1, arg2):
        self.g_changeSetting.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'VECTOR3'])
    def sendVisibilityDevelopmentInfo(self, arg1, arg2):
        self.g_sendVisibilityDevelopmentInfo.fire(self, arg1, arg2)

    @unpack_func_args(['FLOAT32'])
    def shoot(self, arg1):
        self.g_shoot.fire(self, arg1)

    @unpack_func_args(['VECTOR3', 'FLOAT32'])
    def teleportTo(self, arg1, arg2):
        self.g_teleportTo.fire(self, arg1, arg2)

    @unpack_func_args([])
    def replenishAmmo(self):
        self.g_replenishAmmo.fire(self)

    @unpack_func_args(['STRING', 'INT32', 'STRING'])
    def setDevelopmentFeature(self, arg1, arg2, arg3):
        self.g_setDevelopmentFeature.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['INT32', 'FLOAT32', 'VECTOR3', 'VECTOR3', 'UINT8'])
    def receiveFakeShot(self, arg1, arg2, arg3, arg4, arg5):
        self.g_receiveFakeShot.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['MAILBOX'])
    def setAvatar(self, arg1):
        self.g_setAvatar.fire(self, arg1)

    @unpack_func_args(['MAILBOX', 'BOOL'])
    def registerObserver(self, arg1, arg2):
        self.g_registerObserver.fire(self, arg1, arg2)

    @unpack_func_args(['PYTHON'])
    def sendFinalStats(self, arg1):
        self.g_sendFinalStats.fire(self, arg1)

    @unpack_func_args(['BOOL'])
    def onClientConnected(self, arg1):
        self.g_onClientConnected.fire(self, arg1)

    @unpack_func_args(['BOOL', 'BOOL'])
    def onBattleRunning(self, arg1, arg2):
        self.g_onBattleRunning.fire(self, arg1, arg2)

    @unpack_func_args([])
    def sendStateToOwnClient(self):
        self.g_sendStateToOwnClient.fire(self)

    @unpack_func_args(['OBJECT_ID', 'SHOT_ID', 'UINT16', 'UINT8', 'INT32', 'INT32', 'INT32', 'UINT8', 'UINT8', 'UINT8', 'UINT16', 'BOOL', 'UINT16', 'UINT8'])
    def receiveHitAssistBonus(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14):
        self.g_receiveHitAssistBonus.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)

    @unpack_func_args(['OBJECT_ID', ['ARRAY', 'SHOT_ID'], 'UINT8', 'FLOAT32', 'FLOAT32'])
    def onEnemyVehicleShot(self, arg1, arg2, arg3, arg4, arg5):
        self.g_onEnemyVehicleShot.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['OBJECT_ID', 'FLOAT32'])
    def scheduleExtraCheck(self, arg1, arg2):
        self.g_scheduleExtraCheck.fire(self, arg1, arg2)

    @unpack_func_args([])
    def onObservedByEnemy(self):
        self.g_onObservedByEnemy.fire(self)

    @unpack_func_args(['OBJECT_ID', 'BOOL', 'UINT8'])
    def onDetectedByEnemy(self, arg1, arg2, arg3):
        self.g_onDetectedByEnemy.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['OBJECT_ID'])
    def onConcealedFromEnemy(self, arg1):
        self.g_onConcealedFromEnemy.fire(self, arg1)

    @unpack_func_args([])
    def onStopObservationByEnemy(self):
        self.g_onStopObservationByEnemy.fire(self)

    @unpack_func_args(['INT32', 'UINT16', 'UINT8', 'INT16', 'INT16'])
    def updateVehicleAmmo(self, arg1, arg2, arg3, arg4, arg5):
        self.g_updateVehicleAmmo.fire(self, arg1, arg2, arg3, arg4, arg5)

    @unpack_func_args(['UINT8', 'PYTHON', 'UINT8'])
    def onFlagAction(self, arg1, arg2, arg3):
        self.g_onFlagAction.fire(self, arg1, arg2, arg3)

    @unpack_func_args([['ARRAY', 'UINT8'], ['ARRAY', 'OBJECT_ID']])
    def receiveAssistsFromArena(self, arg1, arg2):
        self.g_receiveAssistsFromArena.fire(self, arg1, arg2)

    @unpack_func_args(['OBJECT_ID', 'UINT8', 'UINT16'])
    def receiveFirstDetectionFromArena(self, arg1, arg2, arg3):
        self.g_receiveFirstDetectionFromArena.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['BOOL'])
    def sendPositionsToClient(self, arg1):
        self.g_sendPositionsToClient.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'MAILBOX'])
    def requestDamagedDevicesFromFor(self, arg1, arg2):
        self.g_requestDamagedDevicesFromFor.fire(self, arg1, arg2)

    @unpack_func_args(['MAILBOX'])
    def sendDamagedDevicesTo(self, arg1):
        self.g_sendDamagedDevicesTo.fire(self, arg1)

    @unpack_func_args(['STRING'])
    def setHonorTitle(self, arg1):
        self.g_setHonorTitle.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def receiveTaggedDestructibleKill(self, arg1):
        self.g_receiveTaggedDestructibleKill.fire(self, arg1)

    @unpack_func_args(['ATTACKER_INFO', 'SHOT_ID'])
    def setOnFireByExplosion(self, arg1, arg2):
        self.g_setOnFireByExplosion.fire(self, arg1, arg2)

    @unpack_func_args([['ARRAY', 'VEHICLE_SPATIAL_INFO']])
    def onReceiveSpatialData(self, arg1):
        self.g_onReceiveSpatialData.fire(self, arg1)

    @unpack_func_args(['UINT16'])
    def onResourceAbsorbed(self, arg1):
        self.g_onResourceAbsorbed.fire(self, arg1)

    @unpack_func_args(['BOOL'])
    def setInsideResourcePoint(self, arg1):
        self.g_setInsideResourcePoint.fire(self, arg1)

    @unpack_func_args(['UINT16'])
    def grantWinPoints(self, arg1):
        self.g_grantWinPoints.fire(self, arg1)

    @unpack_func_args(['FLOAT32'])
    def activateGasAttack(self, arg1):
        self.g_activateGasAttack.fire(self, arg1)

    @unpack_func_args(['UINT64'])
    def pauseMechanics(self, arg1):
        self.g_pauseMechanics.fire(self, arg1)

    @unpack_func_args(['STRING', 'PYTHON'])
    def startOrUpdateExtraFromOutside(self, arg1, arg2):
        self.g_startOrUpdateExtraFromOutside.fire(self, arg1, arg2)

    @unpack_func_args(['INT32', 'BOOL'])
    def damageByEquipment(self, arg1, arg2):
        self.g_damageByEquipment.fire(self, arg1, arg2)

    @unpack_func_args(['FLOAT32'])
    def updateOwnClientRTT(self, arg1):
        self.g_updateOwnClientRTT.fire(self, arg1)

    @unpack_func_args(['OBJECT_ID', 'BOOL', 'BOOL'])
    def receiveVisibilityUpdate(self, arg1, arg2, arg3):
        self.g_receiveVisibilityUpdate.fire(self, arg1, arg2, arg3)

    @unpack_func_args(['MAILBOX'])
    def requestVisibilityLists(self, arg1):
        self.g_requestVisibilityLists.fire(self, arg1)

    @unpack_func_args(['MAILBOX'])
    def createCellNearHere(self, arg1):
        self.g_createCellNearHere.fire(self, arg1)

    @unpack_func_args([])
    def onCreateCellSuccess(self):
        self.g_onCreateCellSuccess.fire(self)

    @unpack_func_args(['STRING'])
    def receiveFinalStats(self, arg1):
        self.g_receiveFinalStats.fire(self, arg1)

    @unpack_func_args(['MAILBOX'])
    def setAvatar(self, arg1):
        self.g_setAvatar.fire(self, arg1)

    @unpack_func_args(['PYTHON'])
    def sendFinalStats(self, arg1):
        self.g_sendFinalStats.fire(self, arg1)

    @unpack_func_args([])
    def smartDestroy(self):
        self.g_smartDestroy.fire(self)

    @unpack_func_args(['PYTHON'])
    def logAimMetrics(self, arg1):
        self.g_logAimMetrics.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def isStrafing(self):
        return self._isStrafing

    @isStrafing.setter
    def isStrafing(self, value):
        self._isStrafing, = unpack_variables(value, ['BOOL'])

    @property
    def steeringAngle(self):
        return self._steeringAngle

    @steeringAngle.setter
    def steeringAngle(self, value):
        self._steeringAngle, = unpack_variables(value, ['FLOAT32'])

    @property
    def physicsMode(self):
        return self._physicsMode

    @physicsMode.setter
    def physicsMode(self, value):
        self._physicsMode, = unpack_variables(value, ['UINT8'])

    @property
    def siegeState(self):
        return self._siegeState

    @siegeState.setter
    def siegeState(self, value):
        self._siegeState, = unpack_variables(value, ['UINT8'])

    @property
    def gunAnglesPacked(self):
        return self._gunAnglesPacked

    @gunAnglesPacked.setter
    def gunAnglesPacked(self, value):
        self._gunAnglesPacked, = unpack_variables(value, ['UINT16'])

    @property
    def publicInfo(self):
        return self._publicInfo

    @publicInfo.setter
    def publicInfo(self, value):
        self._publicInfo, = unpack_variables(value, ['PUBLIC_VEHICLE_INFO'])

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health, = unpack_variables(value, ['INT16'])

    @property
    def isCrewActive(self):
        return self._isCrewActive

    @isCrewActive.setter
    def isCrewActive(self, value):
        self._isCrewActive, = unpack_variables(value, ['BOOL'])

    @property
    def engineMode(self):
        return self._engineMode

    @engineMode.setter
    def engineMode(self, value):
        self._engineMode, = unpack_variables(value, ['ARRAY', ['UINT8'], 2])

    @property
    def damageStickers(self):
        return self._damageStickers

    @damageStickers.setter
    def damageStickers(self, value):
        self._damageStickers, = unpack_variables(value, ['ARRAY', ['UINT64']])

    @property
    def publicStateModifiers(self):
        return self._publicStateModifiers

    @publicStateModifiers.setter
    def publicStateModifiers(self, value):
        self._publicStateModifiers, = unpack_variables(value, ['ARRAY', ['EXTRA_ID']])

    @property
    def compDescr(self):
        return self._compDescr

    @compDescr.setter
    def compDescr(self, value):
        self._compDescr, = unpack_variables(value, ['STRING'])

    @property
    def stunInfo(self):
        return self._stunInfo

    @stunInfo.setter
    def stunInfo(self, value):
        self._stunInfo, = unpack_variables(value, ['STUN_INFO'])

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status, = unpack_variables(value, ['INT8'])

    @property
    def invisibility(self):
        return self._invisibility

    @invisibility.setter
    def invisibility(self, value):
        self._invisibility, = unpack_variables(value, ['FLOAT32'])

    @property
    def radioDistance(self):
        return self._radioDistance

    @radioDistance.setter
    def radioDistance(self, value):
        self._radioDistance, = unpack_variables(value, ['FLOAT32'])

    @property
    def circularVisionRadius(self):
        return self._circularVisionRadius

    @circularVisionRadius.setter
    def circularVisionRadius(self, value):
        self._circularVisionRadius, = unpack_variables(value, ['FLOAT32'])

    @property
    def detectedVehicles(self):
        return self._detectedVehicles

    @detectedVehicles.setter
    def detectedVehicles(self, value):
        self._detectedVehicles, = unpack_variables(value, ['ARRAY', ['OBJECT_ID']])

    @property
    def isObservedByEnemy(self):
        return self._isObservedByEnemy

    @isObservedByEnemy.setter
    def isObservedByEnemy(self, value):
        self._isObservedByEnemy, = unpack_variables(value, ['BOOL'])

    @property
    def rammingBonus(self):
        return self._rammingBonus

    @rammingBonus.setter
    def rammingBonus(self, value):
        self._rammingBonus, = unpack_variables(value, ['FLOAT32'])

    @property
    def ammo(self):
        return self._ammo

    @ammo.setter
    def ammo(self, value):
        self._ammo, = unpack_variables(value, ['ARRAY', ['INT32']])

    @property
    def isClientConnected(self):
        return self._isClientConnected

    @isClientConnected.setter
    def isClientConnected(self, value):
        self._isClientConnected, = unpack_variables(value, ['INT8'])

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar, = unpack_variables(value, ['MAILBOX'])

    @property
    def arenaBase(self):
        return self._arenaBase

    @arenaBase.setter
    def arenaBase(self, value):
        self._arenaBase, = unpack_variables(value, ['MAILBOX'])

    @property
    def botKind(self):
        return self._botKind

    @botKind.setter
    def botKind(self, value):
        self._botKind, = unpack_variables(value, ['UINT8'])

    @property
    def crewCompactDescrs(self):
        return self._crewCompactDescrs

    @crewCompactDescrs.setter
    def crewCompactDescrs(self, value):
        self._crewCompactDescrs, = unpack_variables(value, ['ARRAY', ['STRING']])

    @property
    def arenaTypeID(self):
        return self._arenaTypeID

    @arenaTypeID.setter
    def arenaTypeID(self, value):
        self._arenaTypeID, = unpack_variables(value, ['INT32'])

    @property
    def arenaBonusType(self):
        return self._arenaBonusType

    @arenaBonusType.setter
    def arenaBonusType(self, value):
        self._arenaBonusType, = unpack_variables(value, ['UINT8'])

    @property
    def tkillRating(self):
        return self._tkillRating

    @tkillRating.setter
    def tkillRating(self, value):
        self._tkillRating, = unpack_variables(value, ['FLOAT'])

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, value):
        self._cp, = unpack_variables(value, ['PYTHON'])

    @property
    def arenaUniqueID(self):
        return self._arenaUniqueID

    @arenaUniqueID.setter
    def arenaUniqueID(self, value):
        self._arenaUniqueID, = unpack_variables(value, ['UINT64'])

    @property
    def accountDBID(self):
        return self._accountDBID

    @accountDBID.setter
    def accountDBID(self, value):
        self._accountDBID, = unpack_variables(value, ['DB_ID'])

    @property
    def historyLoggingFlags(self):
        return self._historyLoggingFlags

    @historyLoggingFlags.setter
    def historyLoggingFlags(self, value):
        self._historyLoggingFlags, = unpack_variables(value, ['UINT32'])

    @property
    def heatmapLoggingFlags(self):
        return self._heatmapLoggingFlags

    @heatmapLoggingFlags.setter
    def heatmapLoggingFlags(self, value):
        self._heatmapLoggingFlags, = unpack_variables(value, ['UINT32'])

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state, = unpack_variables(value, ['UINT8'])

    @property
    def arena(self):
        return self._arena

    @arena.setter
    def arena(self, value):
        self._arena, = unpack_variables(value, ['MAILBOX'])

    @property
    def inspiringEffect(self):
        return self._inspiringEffect

    @inspiringEffect.setter
    def inspiringEffect(self, value):
        self._inspiringEffect, = unpack_variables(value, ['INSPIRING_EFFECT'])

    @property
    def inspired(self):
        return self._inspired

    @inspired.setter
    def inspired(self, value):
        self._inspired, = unpack_variables(value, ['INSPIRED'])

    @property
    def isSpeedCapturing(self):
        return self._isSpeedCapturing

    @isSpeedCapturing.setter
    def isSpeedCapturing(self, value):
        self._isSpeedCapturing, = unpack_variables(value, ['BOOL'])

    @property
    def isBlockingCapture(self):
        return self._isBlockingCapture

    @isBlockingCapture.setter
    def isBlockingCapture(self, value):
        self._isBlockingCapture, = unpack_variables(value, ['BOOL'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)