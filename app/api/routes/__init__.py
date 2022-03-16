"""
app.api.routes
-------------------------------------------------------------------
"""
from api.routes.routes import api


def init_app(app):
    """

    :param app:
    :return:
    """
    with app.app_context():
        app.register_blueprint(api, url_prefix="/api")
