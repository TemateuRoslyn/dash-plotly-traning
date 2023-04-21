from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash import Dash

# import des librairies
from layouts.graph_layout import render_fig
from graphs.graph_data import *
from layouts.app_layout import *
from callbacks.callbacks import load_callbacks


app = Dash(__name__, suppress_callback_exceptions=True)


# definition du squelette de l'application
app.layout = html.Div(
    id="big-app-container",
    children=[
        dcc.Interval(
            id="interval",
            disabled=False,
            n_intervals=0,
            interval=1000,
            max_intervals=-1
        ),
        build_banner(app=app),
        html.Div(
            id="app-container",
            children=[
                # Insertion des deux Tabs (pas leurs contenus)
                build_tabs(),
                # la div qui contiendra l'application
                html.Div(id="app-content"),
            ],
        ),
        generate_modal(),
    ],
)



if __name__ == "__main__":
    load_callbacks(app=app)
    app.run_server(debug=True)