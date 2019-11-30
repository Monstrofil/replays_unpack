# coding=utf-8
import glob
import os
from ddt import ddt, data, unpack
from unittest import TestCase, main

from replay_parser import ReplayParser

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
REPLAYS = glob.glob(os.path.join(BASE_DIR, 'data', 'random_replays', '*/*.wowsreplay'))


@ddt
class TestRandomReplays(TestCase):

    @data(*REPLAYS)
    def test_parse_replay(self, replay_path):
        parser = ReplayParser(replay_path, strict=True)
        result = parser.get_info()
        self.assertNotEqual(None, result['hidden'])
        self.assertEqual(None, result['error'])


if __name__ == '__main__':
    main()
