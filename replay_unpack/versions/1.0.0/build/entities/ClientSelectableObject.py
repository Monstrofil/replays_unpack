#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook

from def_generator.decorators import unpack_func_args, unpack_variables




class ClientSelectableObject(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._modelName = None

        self._selectionId = None

        self._mouseOverSoundName = None

        self._clickSoundName = None

        self._edgeMode = 0.0


        # MRO fix

        return

    ####################################
    #      METHODS
    ####################################



    ####################################
    #       PROPERTIES
    ####################################


    @property
    def modelName(self):
        return self._modelName

    @modelName.setter
    def modelName(self, value):
        self._modelName, = unpack_variables(value, ['STRING'])

    @property
    def selectionId(self):
        return self._selectionId

    @selectionId.setter
    def selectionId(self, value):
        self._selectionId, = unpack_variables(value, ['STRING'])

    @property
    def mouseOverSoundName(self):
        return self._mouseOverSoundName

    @mouseOverSoundName.setter
    def mouseOverSoundName(self, value):
        self._mouseOverSoundName, = unpack_variables(value, ['STRING'])

    @property
    def clickSoundName(self):
        return self._clickSoundName

    @clickSoundName.setter
    def clickSoundName(self, value):
        self._clickSoundName, = unpack_variables(value, ['STRING'])

    @property
    def edgeMode(self):
        return self._edgeMode

    @edgeMode.setter
    def edgeMode(self, value):
        self._edgeMode, = unpack_variables(value, ['UINT8'])


    def __repr__(self):
        return "<{}> {}".format(self.__class__.__name__, self.__dict__)