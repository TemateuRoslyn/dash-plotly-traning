from callbacks.render_page import RenderPageCallback
from callbacks.accelerometre import Accelerometre


class Callbacks:
    def __init__(self, app):
        RenderPageCallback(app).register()
        Accelerometre(app).register()
