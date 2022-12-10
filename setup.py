# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='World of Warships replays parser',
    version='3.3.3',
    description='Utility which loads .wowsreplay file, "plays" it '
                'in memory and produces results in json format',
    author='Oleksandr Shyshatskyi',
    author_email='shalal545@gmail.com',
    license='MIT',
    packages=find_packages(include='replay_unpack.*'),
    package_data={'': ['*.py', '**/scripts/**/*.def', '**/scripts/**/**/*.def', '**/scripts/**/*.xml', '**/scripts/*.xml']},
    include_package_data=True,
    scripts=['replay_parser.py'],
)
