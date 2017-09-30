#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.Entity import Entity
from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class AtbaOwner(object):
    
    g_shootATBAGuns = EventHook()
    
    g_dev_switchIdealATBASelectedGunId = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._atbaTargets = None


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################


    @unpack_func_args(['UINT32'])
    def shootATBAGuns(self, arg1):
        self.g_shootATBAGuns.fire(self, arg1)

    @unpack_func_args(['UINT8'])
    def dev_switchIdealATBASelectedGunId(self, arg1):
        self.g_dev_switchIdealATBASelectedGunId.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################


    @property
    def atbaTargets(self):
        return self._atbaTargets

    @atbaTargets.setter
    def atbaTargets(self, value):
        self._atbaTargets, = unpack_variables(value, ['ATBA_TARGETS'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)