# coding=utf-8
import logging
import struct
from io import BytesIO
from replay_unpack.core import (
    Entity
)
from replay_unpack.core.network.player import ControlledPlayerBase
from .helper import get_definitions, get_controller
from .network.packets import (
    BasePlayerCreate,
    Position,
    EntityMethod,
    EntityProperty,
    NestedProperty,
    EntityEnter,
    EntityLeave,
    Version,
    PACKETS_MAPPING
)

last_gap = 0
last_negative = 0xffffffff
class ReplayPlayer(ControlledPlayerBase):

    def _get_definitions(self, version):
        try:
            return get_definitions('_'.join(version[:4]))
        except RuntimeError:
            return get_definitions('_'.join(version[:3]))

    def _get_controller(self, version):
        try:
            return get_controller('_'.join(version[:4]))
        except RuntimeError:
            return get_controller('_'.join(version[:3]))

    def _get_packets_mapping(self, version):
        return PACKETS_MAPPING

    def _process_packet(self, time, packet):

        if isinstance(packet, Version):
            logging.debug('Game version: %s', packet.version)

        elif isinstance(packet, BasePlayerCreate):
            # I'm not sure what is the order of cell/base/client player creation
            if packet.entityId in self._battle_controller.entities:
                base_player = self._battle_controller.entities[packet.entityId]
            else:
                base_player = Entity(id_=packet.entityId,
                                     spec=self._definitions.get_entity_def_by_name('Avatar'))

            # base is internal, so props are stored in order of xml file
            io = BytesIO(packet.value.value)
            for index, prop in enumerate(base_player.base_properties):
                base_player.set_base_property(index, io)

            self._battle_controller.create_entity(base_player)
            self._battle_controller.on_player_enter_world(packet.entityId)

