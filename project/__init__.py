from flask import Flask, jsonify
from project.api.weird import encoder_blueprint
import os
import logging
from project.services.weird_words import WeirdText
from project.api.errors import PayloadException
w_conventer = WeirdText()


def create_app(script_info=None):
    """Initialize application with settings"""
    app = Flask(__name__)

    # setting up app config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # set up routes
    app.register_blueprint(encoder_blueprint)
    # set up logging
    if app.config['ENV'] == 'production':
        gunicorn_logger = logging.getLogger('gunicorn.warning')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    # registers errors
    @app.errorhandler(PayloadException)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app
