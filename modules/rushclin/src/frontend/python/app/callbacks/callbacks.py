from callbacks.render_page import RenderPageCallback
from callbacks.interval_callback import IntervalCallback


class Callbacks:
    def __init__(self, app):
        RenderPageCallback(app).register()
        IntervalCallback(app).register()
