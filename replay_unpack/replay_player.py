#!/usr/bin/python
# coding=utf-8
import struct
import logging

from replay_unpack.base.BigWorld import BigWorld
from build import entities as entities
from build._entities_list import g_entitiesList
from packets import Map, BasePlayerCreate, CellPlayerCreate, Entity, Position, EntityMethod, EntityProperty

__author__ = "Aleksandr Shyshatsky"


class ReplayPlayer(object):
    def __init__(self):
        self._bigworld = BigWorld()

    def on_packet(self, packet):
        if isinstance(packet.data, Map):
            self._bigworld.battle_controller.map = packet.data.name

        if isinstance(packet.data, BasePlayerCreate):
            avatar = entities.Avatar()
            avatar.id = packet.data.entityId
            self._bigworld.entities[packet.data.entityId] = avatar

            self._bigworld.battle_controller.player_id = packet.data.entityId

        if isinstance(packet.data, CellPlayerCreate):
            # TODO: what to do with this?
            pass

        if isinstance(packet.data, Entity):
            class_ = getattr(entities, g_entitiesList[packet.data.type])
            entity = class_()
            entity.id = packet.data.entityID

            if hasattr(entity, 'attributesMap'):
                try:
                    values = packet.data.state.io()
                    values_count, = struct.unpack('B', values.read(1))
                    for i in xrange(values_count):
                        k = values.read(1)
                        idx, = struct.unpack('B', k)
                        setattr(entity, entity.attributesMap[idx], values)
                except Exception as e:
                    logging.exception(e.message)

            self._bigworld.entities[packet.data.entityID] = entity

        if isinstance(packet.data, Position):
            self._bigworld.entities[packet.data.entityId].position = packet.data.position
            self._bigworld.entities[packet.data.entityId].rotation = packet.data.rotation

        if isinstance(packet.data, EntityMethod):
            entity = self._bigworld.entities[packet.data.entityId]
            if hasattr(entity, 'methodsMap'):
                method_name = entity.methodsMap.get(packet.data.messageId, None)
                if method_name:
                    try:
                        getattr(entity, method_name)(packet.data.data.value.decode('hex'))
                    except Exception as e:
                        logging.exception(e.message)

        if isinstance(packet.data, EntityProperty):
            entity = self._bigworld.entities[packet.data.objectID]
            if hasattr(entity, 'attributesMap'):
                attribute_name = entity.attributesMap.get(packet.data.messageId, None)
                if attribute_name:
                    try:
                        setattr(entity, attribute_name, packet.data.data.value.decode('hex'))
                    except Exception as e:
                        logging.exception(e.message)

    def get_info(self):
        return self._bigworld.battle_controller.get_info()
