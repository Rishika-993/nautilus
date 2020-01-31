#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import sys
import pathlib
import logging

NAME = pathlib.Path(__file__).parent.name
VERSION = "1.0.0"
SCRAPER = f"{NAME} {VERSION}"

ROOT_DIR = pathlib.Path(__file__).parent


class LessThanFilter(logging.Filter):
    def __init__(self, exclusive_maximum, name=""):
        super(LessThanFilter, self).__init__(name)
        self.max_level = exclusive_maximum

    def filter(self, record):
        """ non-zero return means we log this message """
        return 1 if record.levelno < self.max_level else 0


logger = logging.getLogger("youtube-scraper")
logger.setLevel(logging.NOTSET)
log_format = "[%(asctime)s] %(levelname)s:%(message)s"

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(logging.Formatter(log_format))
stdout_handler.addFilter(LessThanFilter(logging.WARNING))
stdout_handler.setLevel(logging.DEBUG)
logger.addHandler(stdout_handler)

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setFormatter(logging.Formatter(log_format))
stderr_handler.setLevel(logging.WARNING)
logger.addHandler(stderr_handler)