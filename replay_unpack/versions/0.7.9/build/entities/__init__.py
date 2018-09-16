#!/usr/bin/python
# coding=utf-8

from Avatar import Avatar
from Vehicle import Vehicle
from Account import Account
from SmokeScreen import SmokeScreen
from Fog import Fog
from OfflineEntity import OfflineEntity
from Login import Login
from Building import Building
from AccountController import AccountController
from MasterChanger import MasterChanger
from BattleLogic import BattleLogic
from ReplayLeech import ReplayLeech
from ReplayConnectionHandler import ReplayConnectionHandler


# import user plugins (override auto-generated models)
try:
    from plugins import *
except ImportError:
    pass

ENTITIES = [Avatar, Vehicle, Account, SmokeScreen, Fog, OfflineEntity, Login, Building, AccountController, MasterChanger, BattleLogic, ReplayLeech, ReplayConnectionHandler, ]