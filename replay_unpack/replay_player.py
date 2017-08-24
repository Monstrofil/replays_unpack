#!/usr/bin/python
# coding=utf-8
import struct

from replay_unpack.base.BigWorld import BigWorld
from build import entities as entities
from build._entities_list import g_entitiesList
from packets import Map, BasePlayerCreate, CellPlayerCreate, Entity, Position, EntityMethod, EntityProperty
from sentry import client

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
                    except struct.error:
                        client.captureException()

        if isinstance(packet.data, EntityProperty):
            entity = self._bigworld.entities[packet.data.objectID]
            if hasattr(entity, 'attributesMap'):
                attribute_name = entity.attributesMap.get(packet.data.messageId, None)
                if attribute_name:
                    try:
                        setattr(entity, attribute_name, packet.data.data.value.decode('hex'))
                    except struct.error:
                        client.captureException()

    def get_info(self):
        return self._bigworld.battle_controller.get_info()