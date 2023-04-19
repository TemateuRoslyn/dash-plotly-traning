from dash import html, Input, Output

from pages.capteurs import Capteurs
from pages.accelerometres import Accelerometres


class RenderPageCallback:
    def __init__(self, app) -> None:
        self.app = app
        self.capteurs = Capteurs()
        self.accelerometres = Accelerometres()

    def register(self):
        @self.app.callback(
            Output("app-content", "children"),
            Input("app-tabs", "value"),
        )
        def register_pages(tab_switch):
            if tab_switch == "accelerometre":
                return self.accelerometres.render()
            else:
                return self.capteurs.render()
