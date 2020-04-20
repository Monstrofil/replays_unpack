# coding=utf-8
import glob
import os
from unittest import TestCase, main

from ddt import ddt, data

from replay_parser import ReplayParser

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
REPLAYS = glob.glob(os.path.join(BASE_DIR, 'data', 'random_replays', '*/*.wowsreplay')) + \
          glob.glob(os.path.join(BASE_DIR, 'data', 'random_replays', '*/*.wotreplay'))


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
