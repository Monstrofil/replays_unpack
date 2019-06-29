#!/usr/bin/python
# coding=utf-8
"""
Demo script that prints summary information about
parsed entities. Can be used for debug purpoces (e.g.
comparing exposed index with client memory values)
"""

from entities import ENTITIES

for entity in ENTITIES:
    entity().get_summary()
