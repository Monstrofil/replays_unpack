#!/usr/bin/python
# coding=utf-8
import logging
from enum import Enum
from io import BytesIO
from typing import Callable, Dict, List, Tuple

from replay_unpack.entity_def.constants import EntityFlags
from replay_unpack.entity_def.data_description.entity_description import EntityDef

__author__ = "Aleksandr Shyshatsky"


class Entity:

    class Type(Enum):
        """
        Enum which represents all possible entity variations
        """
        CLIENT = 1
        CELL = 2
        BASE = 4

    _methods_subscriptions = {
        Type.CLIENT: {},
        Type.CELL: {},
        Type.BASE: {}
    }  # type: Dict[Type, Dict[str, List[Callable]]]
    _properties_subscriptions = {
        Type.CLIENT: {},
        Type.CELL: {},
        Type.BASE: {}
    }  # type: Dict[Type, Dict[str, List[Callable]]]

    def __init__(self, id_: int, spec: EntityDef):
        self.id = id_
        self._spec = spec
        self._methods = spec.client().get_exposed_index_map()

        # we had to store properties values because network protocol
        # supports updating them partly (lists and dicts)
        self.properties = {
            'client': {},
            'cell': {},
            'base': {}
        }

        # position, yaw, pitch, roll
        self.volatiles = spec.volatiles()

        self.client_properties = spec.properties().get_properties_by_flags(
            EntityFlags.ALL_CLIENTS |
            EntityFlags.BASE_AND_CLIENT |
            EntityFlags.OTHER_CLIENTS |
            EntityFlags.OWN_CLIENT |
            EntityFlags.CELL_PUBLIC_AND_OWN |
            EntityFlags.ALL_CLIENTS,
            exposed_index=True
        )
        self.cell_properties = spec.properties().get_properties_by_flags(
            EntityFlags.CELL_PUBLIC_AND_OWN |
            EntityFlags.CELL_PUBLIC |
            EntityFlags.CELL_PRIVATE
        )
        self.base_properties = spec.properties().get_properties_by_flags(
            EntityFlags.BASE |
            EntityFlags.BASE_AND_CLIENT
        )

    @classmethod
    def subscribe_method_call(cls, entity_name: str, method_type: Type, method_name: str, func: Callable):
        """
        Add callbacks that should be triggered when given method called
        """
        if method_name not in cls._methods_subscriptions[method_type]:
            cls._methods_subscriptions[method_type][entity_name + '_' + method_name] = []
        cls._methods_subscriptions[method_type][entity_name + '_' + method_name].append(func)

    @classmethod
    def subscribe_property_change(cls, property_type: Type, name: str, func: Callable):
        """
        Add callbacks that should be triggered when given method called
        """
        if name not in cls._methods_subscriptions[property_type]:
            cls._methods_subscriptions[property_type][name] = []
        cls._methods_subscriptions[property_type][name].append(func)

    def call_client_method(self, exposed_index: int, payload: BytesIO):
        method = self._methods[exposed_index]
        logging.debug('calling %s method %s', self._spec.get_name(), method)

        args, kwargs = method.create_from_stream(payload)
        method_hash = self._spec.get_name() + '_' + method.get_name()
        for func in Entity._methods_subscriptions[self.Type.CLIENT].get(method_hash, []):
            try:
                func(self, *args, **kwargs)
            except TypeError as e:
                logging.error("Failed to call %s with args %s "
                              "and kwargs %s, problem: '%s'", func, args, kwargs, e)
                raise

    def set_client_property(self, exposed_index, payload: BytesIO):
        logging.debug('requested property %s of entity %s', exposed_index, self._spec.get_name())
        prop = self.client_properties[exposed_index]
        logging.debug('setting %s client property %s', self._spec.get_name(), prop)
        self.properties['client'][prop.get_name()] = prop.create_from_stream(payload)

    def set_cell_property(self, internal_index, payload: BytesIO):
        prop = self.cell_properties[internal_index]
        logging.debug('setting %s cell property %s', self._spec.get_name(), prop)
        self.properties['cell'][prop.get_name()] = prop.create_from_stream(payload)

    def set_base_property(self, internal_index, payload: BytesIO):
        prop = self.base_properties[internal_index]
        logging.debug('setting %s base property %s', self._spec.get_name(), prop)
        self.properties['base'][prop.get_name()] = prop.create_from_stream(payload)

    def get_name(self):
        return self._spec.get_name()

    @property
    def position(self) -> Tuple[float, float, float]:
        try:
            return self.volatiles['position']
        except KeyError:
            raise RuntimeError("Entity %s does not have volatile %s" % (self.get_name(), 'position'))

    @position.setter
    def position(self, value: Tuple[float, float, float]):
        self.volatiles['position'] = value

    @property
    def yaw(self) -> float:
        try:
            return self.volatiles['yaw']
        except KeyError:
            raise RuntimeError("Entity %s does not have volatile %s" % (self.get_name(), 'yaw'))

    @yaw.setter
    def yaw(self, value: float):
        self.volatiles['yaw'] = value

    @property
    def pitch(self) -> float:
        try:
            return self.volatiles['pitch']
        except KeyError:
            raise RuntimeError("Entity %s does not have volatile %s" % (self.get_name(), 'pitch'))

    @pitch.setter
    def pitch(self, value: float):
        self.volatiles['pitch'] = value

    @property
    def roll(self) -> float:
        try:
            return self.volatiles['roll']
        except KeyError:
            raise RuntimeError("Entity %s does not have volatile %s" % (self.get_name(), 'roll'))

    @roll.setter
    def roll(self, value: float):
        self.volatiles['roll'] = value

    def __repr__(self):
        return '{}<{}>'.format(self._spec.get_name(), self.id)
