#!/usr/bin/python
# -*- coding: utf-8 -*-

import configparser
import os


def get_config():
    ENV = os.environ.get('env', 'DEFAULT')
    config = configparser.ConfigParser()
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    config.read(os.path.join(PROJECT_ROOT, 'config.ini'))
    return config[ENV]


cfg = get_config()
