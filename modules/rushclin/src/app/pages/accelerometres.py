from dash import html
import dash_bootstrap_components as dbc
import dash_daq as daq
from components.accelerometre_card import AccelerometreCard


class Accelerometres:
    def __init__(self):
        self.accelerometre_card = AccelerometreCard()

    def render(self):
        return html.Div(
            [
                dbc.Row([
                    html.H1("Liste des accelerometres actifs",
                            className='my-5 text-center fs-5 fw-bold text-uppercase text-white'),
                ]),
                dbc.Row(
                    [
                        dbc.Col(self.accelerometre_card.render(id='acc-1')),
                        dbc.Col(self.accelerometre_card.render(id='acc-2')),
                        dbc.Col(self.accelerometre_card.render(id='acc-3')),
                        dbc.Col(self.accelerometre_card.render(id='acc-4')),
                    ]
                )
            ]
        )
