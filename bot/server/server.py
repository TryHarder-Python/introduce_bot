from server.routers import setup_routes


def init_app(app):
    setup_routes(app)
    return app
