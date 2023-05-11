from dash import html
import dash_bootstrap_components as dbc

from components.sparkline_graph import SparkLine


class Capteurs:
    def __init__(self):
        self.sparkline_graph = SparkLine()

    def render(self):
        return html.Div(
            [
                dbc.Row([
                    html.H1("Liste des capteurs actifs",
                            className='my-5 text-center fs-5 fw-bold text-uppercase text-white'),
                ]),
                dbc.Row(
                    [
                        dbc.Col(id='capteur-sparkline-graph'),
                        dbc.Col(id='capteur-sparkline-graph-1'),
                    ]
                )
            ]
        )
