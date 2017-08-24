#!/usr/bin/python
# coding=utf-8
import json

import sys
from StringIO import StringIO

from replay_unpack.replay_parser import ReplayParser

__author__ = "Aleksandr Shyshatsky"


def silence_stdout_until_process_exit():
    """
    Upon process exit, Sentry sometimes prints:

        Sentry is attempting to send 1 pending error messages
        Waiting up to 10 seconds
        Press Ctrl-C to quit

    This causes us to get emails from cron which are useless noise, since the
    exceptions end up in sentry anyway. "Real" exceptions print to stderr, not
    stdout, so this shouldn't silence anything important.

    See also this issue: https://github.com/getsentry/raven-python/issues/904
    """
    sys.stdout = StringIO()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=str, required=True)

    namespace = parser.parse_args()
    print json.dumps(ReplayParser(namespace.replay).get_info(), indent=1)
    silence_stdout_until_process_exit()
