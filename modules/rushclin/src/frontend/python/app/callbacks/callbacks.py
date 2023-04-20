from callbacks.render_page import RenderPageCallback
from callbacks.accelerometre import Accelerometre
from callbacks.capteur_sparkline import CapteurSparkLineCallback


class Callbacks:
    def __init__(self, app):
        RenderPageCallback(app).register()
        Accelerometre(app).register()
        CapteurSparkLineCallback(app).register()
