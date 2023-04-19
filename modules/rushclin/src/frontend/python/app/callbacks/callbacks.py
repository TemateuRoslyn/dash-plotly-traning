from dash import html, Input, Output


class Callbacks:
    def __init__(self, app):
        self.app = app
        self.register_callback()

    def register_callback(self):
        @self.app.callback(
            Output("app-content", "children"),
            Input("app-tabs", "value"),
        )
        def render_pages(tab_switch):
            if tab_switch == "settings":
                return [html.H1('Bonjour petit Rushclin')]
            else:
                return [html.H1('Bonsoit grand Takam')]
