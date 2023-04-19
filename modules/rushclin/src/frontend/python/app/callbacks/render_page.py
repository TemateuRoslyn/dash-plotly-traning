from dash import html, Input, Output


class RenderPageCallback:
    def __init__(self, app) -> None:
        self.app = app

    def register(self):
        @self.app.callback(
            Output("app-content", "children"),
            Input("app-tabs", "value"),
        )
        def register_pages(tab_switch):
            if tab_switch == "settings":
                return [html.H1('Bonjour petit Rushclin')]
            else:
                return [html.H1('Bonsoit grand Takam')]
