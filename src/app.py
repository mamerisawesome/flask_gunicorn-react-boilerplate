"""
Create Flask app

Attach necessary configurations and define error pages

:author: Matt Finnell <mattfinnell@github.com>
"""

# Flask framework
from flask import Flask, abort
from flask_cors import CORS

# Werkzeug utilities
from werkzeug.utils import find_modules, import_string

# Project specific utilities
import src.utils as utils

def create_app(config):
    """
    Initialize Flask app

    :param config: configuration for flask
    :returns app: Flask app
    """
    # Create unconfigured flask application
    app = Flask(config.APP_NAME)
    cors = CORS(app)

    # Configure flask application
    app.config.from_object(config)

    # register functions are like set-methods for databases, etc.
    registration_functions = [
        register_error_pages,
        # register_database,
        # register_context_processors,
    ]

    # attach databases, plugins, etc to application context
    for r in registration_functions:
        r(app)

    return app

def register_error_pages(app):
    """
    Handle error pages defined by HTTP status codes at https://httpstatuses.com/

    :param app: Flask app
    """
    class Error(object):
        def __init__(self, error_code, error_title):
            self.code = error_code
            self.title = error_title

    @app.errorhandler(400)
    def bad_request(e):
        abort(400)

    @app.errorhandler(401)
    def unauthorized(e):
        abort(401)

    @app.errorhandler(403)
    def forbidden(e):
        abort(403)

    @app.errorhandler(404)
    def page_not_found(e):
        abort(404)

    @app.errorhandler(418)
    def teapot(e):  # for the lols
        abort(418)

    @app.errorhandler(500)
    def server_error(e):
        abort(500)

    @app.errorhandler(502)
    def bad_gateway(e):
        abort(502)

    @app.errorhandler(503)
    def gateway_timeout(e):
        abort(503)
