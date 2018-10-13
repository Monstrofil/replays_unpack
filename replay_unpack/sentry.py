#!/usr/bin/python
# coding=utf-8
import logging

from raven import Client, setup_logging
from raven.handlers.logging import SentryHandler

DSN = 'https://1c55b1f4826242f9a137740d26c50a54:ee2dd20c52934bd48662a80f3d96dc5e@sentry.io/205092'

client = Client(DSN)
handler = SentryHandler(client)
handler.setLevel(logging.WARNING)
setup_logging(handler)
