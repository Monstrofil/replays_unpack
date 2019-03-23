#!/usr/bin/python
# coding=utf-8
import importlib
import os
import struct
import logging
from io import BytesIO

from replay_unpack.entity_def.definitions import Definitions

from replay_unpack.battle_controller import IBattleController
from replay_unpack.entity import Entity

logging.basicConfig(level=logging.DEBUG)

from .packets import (
    Map,
    BasePlayerCreate,
    CellPlayerCreate,
    EntityCreate,
    Position,
    EntityMethod,
    EntityProperty,
    NestedProperty
)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class ReplayPlayer(object):
    def __init__(self, version: str):
        self._battle_controller = self._get_controller(version)
        self._definitions = Definitions(os.path.join(BASE_DIR, 'versions/' + version.replace('.', '_')))

    def _get_controller(self, version) -> IBattleController:
        """
        Get real controller class by game version.
        """
        try:
            module = importlib.import_module('.versions.%s' % version.replace('.', '_'), package=__package__)
        except ImportError:
            raise RuntimeError("version %s is not supported currently" % version)

        try:
            conrtoller = module.BattleController()
        except AttributeError:
            raise AssertionError("battle controller for version %s "
                                 "should contain BattleController class" % version)
        return conrtoller

    def on_packet(self, packet):
        if isinstance(packet.data, Map):
            self._battle_controller.map = packet.data.name

        elif isinstance(packet.data, BasePlayerCreate):
            avatar = Entity(id_=packet.data.entityId,
                            spec=self._definitions.get_entity_def_by_name('Avatar'))
            self._battle_controller.create_entity(avatar)
            self._battle_controller.on_player_enter_world(packet.data.entityId)

            # I'm not sure what is the order of cell/base/client player creation
            if packet.data.entityId in self._battle_controller.entities:
                base_player = self._battle_controller.entities[packet.data.entityId]
            else:
                base_player = Entity(id_=packet.data.entityId,
                                     spec=self._definitions.get_entity_def_by_name('Avatar'))

            # base is internal, so props are stored in order of xml file
            for index, prop in enumerate(base_player.base_properties):
                base_player.set_base_property(index, BytesIO(packet.data.value.value))
            self._battle_controller.create_entity(base_player)

        elif isinstance(packet.data, CellPlayerCreate):
            # I'm not sure what is the order of cell/base/client player creation
            if packet.data.entityId in self._battle_controller.entities:
                cell_player = self._battle_controller.entities[packet.data.entityId]
            else:
                cell_player = Entity(id_=packet.data.entityId,
                                     spec=self._definitions.get_entity_def_by_name('Avatar'))

            # cell is internal, so props are stored in order of xml file
            for index, prop in enumerate(cell_player.cell_properties):
                cell_player.set_cell_property(index, packet.data.value.io())
            self._battle_controller.create_entity(cell_player)

        elif isinstance(packet.data, EntityCreate):
            entity = Entity(
                id_=packet.data.entityID,
                spec=self._definitions.get_entity_def_by_index(packet.data.type))

            values = packet.data.state.io()
            values_count, = struct.unpack('B', values.read(1))
            for i in range(values_count):
                k = values.read(1)
                idx, = struct.unpack('B', k)
                entity.set_client_property(idx, values)

            self._battle_controller.create_entity(entity)

        elif isinstance(packet.data, Position):
            self._battle_controller.entities[packet.data.entityId].position = packet.data.position
            self._battle_controller.entities[packet.data.entityId].yaw = packet.data.yaw
            self._battle_controller.entities[packet.data.entityId].pitch = packet.data.pitch
            self._battle_controller.entities[packet.data.entityId].roll = packet.data.roll

        elif isinstance(packet.data, EntityMethod):
            entity = self._battle_controller.entities[packet.data.entityId]
            entity.call_client_method(packet.data.messageId, packet.data.data.io())

        elif isinstance(packet.data, EntityProperty):
            entity = self._battle_controller.entities[packet.data.objectID]
            entity.set_client_property(packet.data.messageId, packet.data.data.io())

        elif isinstance(packet.data, NestedProperty):
            e = self._battle_controller.entities[packet.data.entity_id]

            logging.debug('')
            logging.debug('nested property request for id=%s isSlice=%s data=%s',
                          e.id, packet.data.is_slice, packet.data.payload.hex())
            packet.data.read_and_apply(e)

    def get_info(self):
        return self._battle_controller.get_info()
