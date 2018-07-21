#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

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

        self._stunInfo = None

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

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (8, 'isStrafing'),
            (32, 'steeringAngle'),
            (8, 'physicsMode'),
            (8, 'siegeState'),
            (16, 'gunAnglesPacked'),
            (10000000000, 'publicInfo'),
            (16, 'health'),
            (8, 'isCrewActive'),
            (16, 'engineMode'),
            (10000000000, 'damageStickers'),
            (10000000000, 'publicStateModifiers'),
            (64, 'stunInfo'),
            (10000000000, 'inspiringEffect'),
            (10000000000, 'inspired'),
            (8, 'isSpeedCapturing'),
            (8, 'isBlockingCapture'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (56, 'onHealthChanged'),
            (8, 'showShooting'),
            (10000000000, 'showDamageFromShot'),
            (144, 'showDamageFromExplosion'),
            (72, 'showAmmoBayEffect'),
            (64, 'onPushed'),
            (352, 'onStaticCollision'),
            (128, 'showRammingEffect'),
            
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


    # method size: 56
    @unpack_func_args(['INT16', 'OBJECT_ID', 'UINT8'])
    def onHealthChanged(self, arg1, arg2, arg3):
        self.g_onHealthChanged.fire(self, arg1, arg2, arg3)

    # method size: 8
    @unpack_func_args(['UINT8'])
    def showShooting(self, arg1):
        self.g_showShooting.fire(self, arg1)

    # method size: 10000000000
    @unpack_func_args(['OBJECT_ID', ['ARRAY', 'UINT64'], 'UINT8', 'UINT8'])
    def showDamageFromShot(self, arg1, arg2, arg3, arg4):
        self.g_showDamageFromShot.fire(self, arg1, arg2, arg3, arg4)

    # method size: 144
    @unpack_func_args(['OBJECT_ID', 'VECTOR3', 'UINT8', 'UINT8'])
    def showDamageFromExplosion(self, arg1, arg2, arg3, arg4):
        self.g_showDamageFromExplosion.fire(self, arg1, arg2, arg3, arg4)

    # method size: 72
    @unpack_func_args(['UINT8', 'FLOAT32', 'FLOAT32'])
    def showAmmoBayEffect(self, arg1, arg2, arg3):
        self.g_showAmmoBayEffect.fire(self, arg1, arg2, arg3)

    # method size: 64
    @unpack_func_args(['FLOAT32', 'FLOAT32'])
    def onPushed(self, arg1, arg2):
        self.g_onPushed.fire(self, arg1, arg2)

    # method size: 352
    @unpack_func_args(['FLOAT32', 'VECTOR3', 'VECTOR3', 'UINT8', 'FLOAT32', 'FLOAT32', 'FLOAT32', 'INT8', 'UINT16'])
    def onStaticCollision(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        self.g_onStaticCollision.fire(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

    # method size: 128
    @unpack_func_args(['FLOAT32', 'VECTOR3'])
    def showRammingEffect(self, arg1, arg2):
        self.g_showRammingEffect.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################


    # property size: 8
    @property
    def isStrafing(self):
        return self._isStrafing

    @isStrafing.setter
    def isStrafing(self, value):
        self._isStrafing, = unpack_variables(value, ['BOOL'])

    # property size: 32
    @property
    def steeringAngle(self):
        return self._steeringAngle

    @steeringAngle.setter
    def steeringAngle(self, value):
        self._steeringAngle, = unpack_variables(value, ['FLOAT32'])

    # property size: 8
    @property
    def physicsMode(self):
        return self._physicsMode

    @physicsMode.setter
    def physicsMode(self, value):
        self._physicsMode, = unpack_variables(value, ['UINT8'])

    # property size: 8
    @property
    def siegeState(self):
        return self._siegeState

    @siegeState.setter
    def siegeState(self, value):
        self._siegeState, = unpack_variables(value, ['UINT8'])

    # property size: 16
    @property
    def gunAnglesPacked(self):
        return self._gunAnglesPacked

    @gunAnglesPacked.setter
    def gunAnglesPacked(self, value):
        self._gunAnglesPacked, = unpack_variables(value, ['UINT16'])

    # property size: 10000000000
    @property
    def publicInfo(self):
        return self._publicInfo

    @publicInfo.setter
    def publicInfo(self, value):
        self._publicInfo, = unpack_variables(value, ['PUBLIC_VEHICLE_INFO'])

    # property size: 16
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health, = unpack_variables(value, ['INT16'])

    # property size: 8
    @property
    def isCrewActive(self):
        return self._isCrewActive

    @isCrewActive.setter
    def isCrewActive(self, value):
        self._isCrewActive, = unpack_variables(value, ['BOOL'])

    # property size: 16
    @property
    def engineMode(self):
        return self._engineMode

    @engineMode.setter
    def engineMode(self, value):
        self._engineMode, = unpack_variables(value, [['ARRAY', 'UINT8', 2]])

    # property size: 10000000000
    @property
    def damageStickers(self):
        return self._damageStickers

    @damageStickers.setter
    def damageStickers(self, value):
        self._damageStickers, = unpack_variables(value, [['ARRAY', 'UINT64']])

    # property size: 10000000000
    @property
    def publicStateModifiers(self):
        return self._publicStateModifiers

    @publicStateModifiers.setter
    def publicStateModifiers(self, value):
        self._publicStateModifiers, = unpack_variables(value, [['ARRAY', 'EXTRA_ID']])

    # property size: 64
    @property
    def stunInfo(self):
        return self._stunInfo

    @stunInfo.setter
    def stunInfo(self, value):
        self._stunInfo, = unpack_variables(value, ['STUN_INFO'])

    # property size: 10000000000
    @property
    def inspiringEffect(self):
        return self._inspiringEffect

    @inspiringEffect.setter
    def inspiringEffect(self, value):
        self._inspiringEffect, = unpack_variables(value, ['INSPIRING_EFFECT'])

    # property size: 10000000000
    @property
    def inspired(self):
        return self._inspired

    @inspired.setter
    def inspired(self, value):
        self._inspired, = unpack_variables(value, ['INSPIRED'])

    # property size: 8
    @property
    def isSpeedCapturing(self):
        return self._isSpeedCapturing

    @isSpeedCapturing.setter
    def isSpeedCapturing(self, value):
        self._isSpeedCapturing, = unpack_variables(value, ['BOOL'])

    # property size: 8
    @property
    def isBlockingCapture(self):
        return self._isBlockingCapture

    @isBlockingCapture.setter
    def isBlockingCapture(self, value):
        self._isBlockingCapture, = unpack_variables(value, ['BOOL'])


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)