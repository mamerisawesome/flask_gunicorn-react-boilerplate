"""
Define test environment

:author: Matt Finnell <mattfinnell@github.com>
"""

import os

class Config(object):
    APP_NAME = "TEST APPLICATION"
    DEBUG = True
    CORS_HEADERS = "Content-Type"

    DEVELOPMENT = True
    TESTING = False
    STAGING = False
    PRODUCTION = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True

class StagingConfig(Config):
    STAGING = True

class ProductionConfig(Config):
    PRODUCTION = True
    DEBUG = False
