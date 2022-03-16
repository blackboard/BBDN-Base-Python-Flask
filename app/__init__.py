"""
app.__init__
------------
Application factory
"""
import os

import admin
from flask import Flask


def init_app() -> Flask:
    """

    :return:
    """
    from app import api
    from app import models
    from app.api import routes

    app = Flask(__name__)
    models.init_app(app)
    routes.init_app(app)
    api.init_app(app)
    admin.init_app(app)
    return app


def create_app(config=None):
    """

    :param config:
    :return:
    """
    app = init_app()
    # load default configuration
    app.config.from_object("config.settings")
    # load environment configuration
    if "FLASK_CONF" in os.environ:
        app.config.from_envvar("FLASK_CONF")
    # load app specified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith(".py"):
            app.config.from_pyfile(config)
    return app
