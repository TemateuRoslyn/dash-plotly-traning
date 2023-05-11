from dash import Dash
import dash_bootstrap_components as dbc

from layout.layout import Layout
from callbacks.callbacks import Callbacks


class App:
    def __init__(self):
        print("============= INIT APP")
        self.layout = Layout()
        self.app = Dash(
            __name__,
            external_stylesheets=[
                dbc.themes.SOLAR
            ],
            suppress_callback_exceptions=True
        )
        self.callbacks = Callbacks(self.app)

    def run_app(self):
        self.app.layout = self.layout.render()

        self.app.run_server(
            debug=True,
            port=8089
        )


# RUN THE APP
if __name__ == '__main__':
    print("============= APP IS RUNNING ON PORT 8089")
    App().run_app()
