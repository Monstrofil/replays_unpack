#!/usr/bin/python
# coding=utf-8

from distutils.core import setup

setup(name='World of Warships replay unpacker',
      version='1.0',
      author='Oleksandr Shyshatskyi',
      author_email='shalal545@gmail.com',
      packages=['replays_unpack'],
      scripts=['replay_parser.py'])