"""
api/__init__.py
-------------------------------------------------------------------
"""
from api import routes


def init_app(app):
    """

    :param app:
    :return:
    """
    routes.init_app(app)
