from dash import html
import dash_bootstrap_components as dbc


class Accelerometres:
    def __init__(self):
        pass

    def render(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        html.H1('La liste des accelerometres actifs')
                    ]
                )
            ]
        )
