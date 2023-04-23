import dash_bootstrap_components as dbc
from dash import html


class Comparateur:
    def __init__(self) -> None:
        pass

    def render(self):
        return html.Div(
            [
                dbc.Row([
                    html.H1("Liste des comparateurs actifs",
                            className='my-5 text-center fs-5 fw-bold text-uppercase text-white'),
                ]),
            ]
        )
