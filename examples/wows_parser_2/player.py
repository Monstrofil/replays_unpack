# coding=utf-8
import os

from replay_unpack.clients.wows.network.packets import (
    Position
)
from replay_unpack.clients.wows.player import ReplayPlayer as WoWSReplayPlayer


from replay_unpack.core import PrettyPrintObjectMixin

EXPECTED_TYPE = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                b'\x80\xbf\x00\x00\x80\xbf\x00\x00\x80\xbf'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class UnknownPacket(PrettyPrintObjectMixin):

    def __init__(self, stream):
        assert stream.read() == EXPECTED_TYPE


class ReplayPlayer(WoWSReplayPlayer):

    def _get_packets_mapping(self):
        return {
            0x18: UnknownPacket,
        }

    def _process_packet(self, time, packet):

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
