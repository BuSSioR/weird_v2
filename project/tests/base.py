from flask_testing import TestCase
from project import create_app
app = create_app()


class BaseTestCase(TestCase):
    '''Expose method to create app in testing
    config'''
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app
