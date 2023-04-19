from services.APIRequest import APIRequest
from callbacks.render_page import RenderPageCallback


class Callbacks:
    def __init__(self, app):
        RenderPageCallback(app).register()
