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

    application = Flask(__name__)
    models.init_app(application)
    routes.init_app(application)
    api.init_app(application)
    admin.init_app(application)
    return application


def create_app(config=None):
    """

    :param config:
    :return:
    """
    application = init_app()
    # load default configuration
    application.config.from_object("config.settings")
    # load environment configuration
    if "FLASK_CONF" in os.environ:
        application.config.from_envvar("FLASK_CONF")
    # load app specified configuration
    if config is not None:
        if isinstance(config, dict):
            application.config.update(config)
        elif config.endswith(".py"):
            application.config.from_pyfile(config)
    return application
