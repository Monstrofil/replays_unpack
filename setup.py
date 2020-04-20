# coding=utf-8
from setuptools import setup

setup(
    name='World of Warships replays parser',
    version='3.1.0',
    description='Utility which loads .wowsreplay file, "plays" it '
                'in memory and produces results in json format',
    author='Oleksandr Shyshatskyi',
    author_email='shalal545@gmail.com',
    license='MIT',
    packages=['replay_unpack'],
    package_data={'': ['*.py']},
    include_package_data=True,
    scripts=['replay_parser.py'],
)
