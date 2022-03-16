"""
app.admin.routes
----------------

"""
from admin.routes.routes import admin


def init_app(app):
    """

    :param app:
    :return:
    """
    with app.app_context():
        app.register_blueprint(admin, url_prefix="/admin")
