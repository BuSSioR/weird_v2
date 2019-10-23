import os


class BaseConfig:
    """Base configuration of app"""
    TESTING = False
    SECRET_KEY = 'c873eeb1326e6bf2c2d066acc771347e'
    JSON_AS_ASCII = False
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Development configuration"""
    DEBUG = False
