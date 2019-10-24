import os


class BaseConfig:
    """Base configuration of app"""
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    JSON_AS_ASCII = False
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    ENV='development'

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    ENV='testing'


class ProductionConfig(BaseConfig):
    """Development configuration"""
    DEBUG = False
    ENV='production'
