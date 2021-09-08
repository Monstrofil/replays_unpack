# coding=utf-8
import os

from replay_unpack.clients.wows.network.packets import (
    Position
)
from replay_unpack.clients.wows.player import ReplayPlayer as WoWSReplayPlayer

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class ReplayPlayer(WoWSReplayPlayer):

    def _process_packet(self, packet):
        if isinstance(packet, Position):
            print('Entity %s had position %s; new position is %s' % (
                packet.entityId,
                self._battle_controller.entities[packet.entityId].position,
                packet.position
            ))

            self._battle_controller.entities[packet.entityId].position = packet.position
            self._battle_controller.entities[packet.entityId].yaw = packet.yaw
            self._battle_controller.entities[packet.entityId].pitch = packet.pitch
            self._battle_controller.entities[packet.entityId].roll = packet.roll

        super(ReplayPlayer, self)._process_packet(packet)
