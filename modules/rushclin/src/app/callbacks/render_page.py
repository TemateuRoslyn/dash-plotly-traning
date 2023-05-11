from dash import Input, Output

from pages.capteurs import Capteurs
from pages.accelerometres import Accelerometres
from pages.comparateur import Comparateur


class RenderPageCallback:
    def __init__(self, app) -> None:
        self.app = app
        self.capteurs = Capteurs()
        self.accelerometres = Accelerometres()
        self.comparateurs = Comparateur()

    def register(self):
        @self.app.callback(
            Output("app-content", "children"),
            Input("app-tabs", "value"),
        )
        def register_pages(tab_switch):
            if tab_switch == "accelerometre":
                return self.accelerometres.render()
            elif tab_switch == 'comparateur':
                return self.comparateurs.render()
            else:
                return self.capteurs.render()
