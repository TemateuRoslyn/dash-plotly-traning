from dash import Dash, dash, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc

from layout.layout import Layout


class App:
    def __init__(self):
        print("============= INIT APP")
        self.layout = Layout()
        self.title = 'DASHBOARD APP'

    def run_app(self):
        app = Dash(
            __name__,
            external_stylesheets=[
                dbc.themes.SOLAR
            ]
        )

        app.layout = self.layout.render()
        app.title = self.title

        # CALLBACKS METHODS

        @app.callback(
            Output("app-content", "children"),
            Input("app-tabs", "value"),
        )
        def render_pages(tab_switch):
            if tab_switch == "settings":
                return [html.H1('Bonjour petit Rushclin')]
            else:
                return [html.H1('Bonsoit grand Takam')]

        app.run_server(
            debug=True,
            port=8089
        )


# RUN THE APP
if __name__ == '__main__':
    print("============= APP IS RUNNING ON PORT 8089")
    App().run_app()
