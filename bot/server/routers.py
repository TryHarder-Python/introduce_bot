from server.views import check_data_handler


def setup_routes(app):
    app.router.add_post('/', check_data_handler, name='check_data_handler')
