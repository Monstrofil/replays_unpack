#!/usr/bin/python
# coding=utf-8
import struct
import logging
from StringIO import StringIO

from replay_unpack import PlayerPosition
from replay_unpack import Unknown
from replay_unpack.base.BigWorld import BigWorld
from build import entities as entities
from build._entities_list import g_entitiesList
from packets import (
    Map,
    BasePlayerCreate,
    CellPlayerCreate,
    Entity,
    Position,
    EntityMethod,
    EntityProperty,
    NestedProperty
)

__author__ = "Aleksandr Shyshatsky"


class ReplayPlayer(object):
    def __init__(self):
        self._bigworld = BigWorld()

    def on_packet(self, packet):
        if isinstance(packet.data, Map):
            self._bigworld.battle_controller.map = packet.data.name

        elif isinstance(packet.data, BasePlayerCreate):
            avatar = entities.Avatar()
            avatar.id = packet.data.entityId
            self._bigworld.entities[packet.data.entityId] = avatar
            self._bigworld.battle_controller.player_id = packet.data.entityId

            # TODO: see comments in CellPlayerCreate section

        elif isinstance(packet.data, CellPlayerCreate):
            # TODO: rework this part
            # e = self._bigworld.entities.setdefault(
            #     packet.data.entityId, entities.Avatar())
            # e.id = packet.data.entityId
            # io = StringIO(packet.data.value.value.decode('hex'))
            # for _, name in e._properties:
            #     # TODO: stupid hack, need to rework properties system
            #     # we should be able to separate CELL and BASE properties
            #     if name == 'attrs':
            #         continue
            #     setattr(e, name, io)
            pass

        elif isinstance(packet.data, Entity):
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

        elif isinstance(packet.data, Position):
            self._bigworld.entities[packet.data.entityId].position = packet.data.position
            self._bigworld.entities[packet.data.entityId].rotation = packet.data.rotation

        elif isinstance(packet.data, PlayerPosition):
            try:
                if packet.data.entityId2 != (0,):
                    # This is a link packet
                    self._bigworld.entities[packet.data.entityId1[0]].position = self._bigworld.entities[packet.data.entityId2[0]].position
                elif packet.data.entityId1 != (0,) and packet.data.entityId2 == (0,):
                    self._bigworld.entities[packet.data.entityId1[0]].position = packet.data.position
                    self._bigworld.entities[packet.data.entityId1[0]].rotation = packet.data.rotation
            except KeyError as e:
                # entity not yet created
                pass

        elif isinstance(packet.data, EntityMethod):
            entity = self._bigworld.entities[packet.data.entityId]
            if hasattr(entity, 'methodsMap'):
                try:
                    method_name = entity.methodsMap[packet.data.messageId]
                    with open('record.rec', 'a+') as f:
                        f.write('\r'+' ' + str(int(packet.time*100)) +' '+method_name+' ')
                except KeyError:
                    logging.exception('Unable to detect method name %s:%s', packet.data.messageId, entity.__class__)
                else:
                    try:
                        getattr(entity, method_name)(packet.data.data.value.decode('hex'))
                    except Exception as e:
                        logging.exception(e.message)

        elif isinstance(packet.data, EntityProperty):
            entity = self._bigworld.entities[packet.data.objectID]
            if hasattr(entity, 'attributesMap'):
                try:
                    attribute_name = entity.attributesMap[packet.data.messageId]
                except KeyError:
                    logging.exception('Unable to detect property name %s:%s', packet.data.messageId, entity.__class__)
                else:
                    try:
                        setattr(entity, attribute_name, packet.data.data.value.decode('hex'))
                    except Exception as e:
                        logging.exception(e.message)

        elif isinstance(packet.data, NestedProperty):
            e = self._bigworld.entities[packet.data.entity_id]

            logging.debug('')
            logging.debug('nested property request for id=%s isSlice=%s data=%s',
                          e.id, packet.data.is_slice, packet.data.payload.encode('hex'))
            try:
                packet.data.read_and_apply(e)
            except Exception:
                logging.error("Something really bad happened", exc_info=True)

        elif isinstance(packet.data, Unknown):
            return

        else:
            pass

        pass

    def get_info(self):
        return self._bigworld.battle_controller.get_info()
