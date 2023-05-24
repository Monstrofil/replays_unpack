# coding=utf-8
import logging
import os
import struct

from replay_unpack.clients.wot.network.packets import (
    Map,
    BasePlayerCreate,
    CellPlayerCreate,
    EntityCreate,
    Position,
    EntityMethod,
    EntityProperty,
    NestedProperty,
    EntityEnter,
    EntityLeave,
    EntityControl,
    PACKETS_MAPPING
)
from replay_unpack.core import Definitions
from replay_unpack.core import (
    Entity,
    PlayerBase,
    NetPacket)
from wot_parser.versions.packets.Test import Test
from wot_parser.versions.packets.Tick import Tick

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class ReplayPlayer(PlayerBase):

    def __init__(self, version):
        self.entities = {}

        super(ReplayPlayer, self).__init__(version)

    def _get_definitions(self, version):
        return Definitions(os.path.join(BASE_DIR, 'versions', version.replace('.', '_')))

    def _get_packets_mapping(self):
        return {
            31: Tick,
            0x20: Test,
            **PACKETS_MAPPING
        }

    def _deserialize_packet(self, packet: NetPacket):
        p = super(ReplayPlayer, self)._deserialize_packet(packet)
        # if p is None:
        #     print('unknown packet %s %s', packet.type, packet.raw_data.read())
        return p

    def _process_packet(self, time, packet):

        if isinstance(packet, Tick):
            print(packet)

        elif isinstance(packet, Test):
            print(packet)

        elif isinstance(packet, Map):
            logging.debug('Welcome to map %s: %s', packet.name, packet.arenaId)

        elif isinstance(packet, BasePlayerCreate):
            # I'm not sure what is the order of cell/base/client player creation
            if packet.entityId in self.entities:
                base_player = self.entities[packet.entityId]
            else:
                base_player = Entity(id_=packet.entityId,
                                     spec=self._definitions.get_entity_def_by_name('Avatar'))

            self.entities[base_player.id] = base_player

        elif isinstance(packet, CellPlayerCreate):
            # I'm not sure what is the order of cell/base/client player creation
            if packet.entityId in self.entities:
                cell_player = self.entities[packet.entityId]
            else:
                cell_player = Entity(id_=packet.entityId,
                                     spec=self._definitions.get_entity_def_by_name('Avatar'))

            # cell is internal, so props are stored in order of xml file
            io = packet.value.io()
            for index, prop in enumerate(cell_player.client_properties_internal):
                cell_player.set_client_property_internal(index, io)
            # TODO: why this assert fails?
            # assert io.read() == b''
            self.entities[cell_player.id] = cell_player

        elif isinstance(packet, EntityEnter):
            self.entities[packet.entityId].is_in_aoi = True

        elif isinstance(packet, EntityLeave):
            self.entities[packet.entityId].is_in_aoi = False

        elif isinstance(packet, EntityCreate):
            entity = Entity(
                id_=packet.entityID,
                spec=self._definitions.get_entity_def_by_index(packet.type))

            values = packet.state.io()
            values_count, = struct.unpack('B', values.read(1))
            for i in range(values_count):
                k = values.read(1)
                idx, = struct.unpack('B', k)
                entity.set_client_property(idx, values)
            assert values.read() == b''
            self.entities[entity.id] = entity

        elif isinstance(packet, Position):
            self.entities[packet.entityId].position = packet.position
            self.entities[packet.entityId].yaw = packet.yaw
            self.entities[packet.entityId].pitch = packet.pitch
            self.entities[packet.entityId].roll = packet.roll

        elif isinstance(packet, EntityMethod):
            entity = self.entities[packet.entityId]
            entity.call_client_method(packet.messageId, packet.data.io())

        elif isinstance(packet, EntityProperty):
            entity = self.entities[packet.objectID]
            entity.set_client_property(packet.messageId, packet.data.io())

        elif isinstance(packet, NestedProperty):
            e = self.entities[packet.entity_id]

            logging.debug('')
            logging.debug('nested property request for id=%s isSlice=%s packet=%s',
                          e.id, packet.is_slice, packet.payload.hex())
            packet.read_and_apply(e)
        elif isinstance(packet, EntityControl):
            logging.info('on control entity %s', packet)
