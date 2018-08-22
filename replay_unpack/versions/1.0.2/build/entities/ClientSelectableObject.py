#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

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

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (10000000000, 'modelName'),
            (10000000000, 'selectionId'),
            (10000000000, 'mouseOverSoundName'),
            (10000000000, 'clickSoundName'),
            (8, 'edgeMode'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            
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



    ####################################
    #       PROPERTIES
    ####################################

# property size: 10000000000
    @property
    def modelName(self):
        return self._modelName

    @modelName.setter
    def modelName(self, value):
        self._modelName, = unpack_variables(value, ['STRING'])
# property size: 10000000000
    @property
    def selectionId(self):
        return self._selectionId

    @selectionId.setter
    def selectionId(self, value):
        self._selectionId, = unpack_variables(value, ['STRING'])
# property size: 10000000000
    @property
    def mouseOverSoundName(self):
        return self._mouseOverSoundName

    @mouseOverSoundName.setter
    def mouseOverSoundName(self, value):
        self._mouseOverSoundName, = unpack_variables(value, ['STRING'])
# property size: 10000000000
    @property
    def clickSoundName(self):
        return self._clickSoundName

    @clickSoundName.setter
    def clickSoundName(self, value):
        self._clickSoundName, = unpack_variables(value, ['STRING'])
# property size: 8
    @property
    def edgeMode(self):
        return self._edgeMode

    @edgeMode.setter
    def edgeMode(self, value):
        self._edgeMode, = unpack_variables(value, ['UINT8'])


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