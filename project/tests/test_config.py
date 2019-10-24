from flask import current_app
from flask_testing import TestCase
from project import create_app
import os

app = create_app()


class TestDevelopmentConfig(TestCase):
    '''Tests development config'''
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] ==
                        os.getenv('SECRET_KEY'))
        self.assertFalse(current_app is None)


class TestTestConfig(TestCase):
    '''Test testing config'''
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] ==
                        os.getenv('SECRET_KEY'))
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
