#!/usr/bin/python
# coding=utf-8
import pickle
from StringIO import StringIO

import struct
from raven import Client
from base.BigWorld import BigWorld
from base.packets.BigWorldPacket import BigWorldPacket
import build.entities as entities
from build._entities_list import g_entitiesList
from replay_decrypt import WoWSReplayDecrypt
from versions.packets import *
__author__ = "Aleksandr Shyshatsky"


client = Client('https://1c55b1f4826242f9a137740d26c50a54:ee2dd20c52934bd48662a80f3d96dc5e@sentry.io/205092')


class ReplayParser(object):
    def __init__(self, replay_path):
        self._replay_path = replay_path
        self._decrypter = WoWSReplayDecrypt(replay_path)
        self._bigworld = BigWorld()

    def get_info(self):
        json_data, replay_data = self._decrypter.get_replay_data()
        io = StringIO(replay_data)

        while io.pos != io.len:
            packet = BigWorldPacket(io)

            if isinstance(packet.data, BasePlayerCreate):
                avatar = entities.Avatar()
                avatar.id = packet.data.entityId
                self._bigworld.entities[packet.data.entityId] = avatar

            if isinstance(packet.data, CellPlayerCreate):
                print packet.data

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

        print self._bigworld.battle_controller.get_info()


ReplayParser(r"C:\Users\shish\AppData\Roaming\Skype\My Skype Received Files\20170811_182113_PBSB517-Nelson_46_Estuary.wowsreplay").get_info()