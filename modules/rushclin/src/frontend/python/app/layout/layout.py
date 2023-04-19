import dash_bootstrap_components as dbc
from layout.navbar import Navbar
from layout.header import Header
from dash import html, dcc


class Layout:
    def __init__(self):
        print("============= INIT LAYOUT")
        self.navbar = Navbar()
        self.header = Header()

    def render(self):
        return dbc.Container(
            fluid=True,
            children=[
                self.header.render(),
                html.Hr(),
                self.navbar.render(),
                html.Div(
                    id='app-content',
                    className='mx-5'
                ),
                dcc.Interval(
                    id='interval-component',
                    interval=1*1000,
                    n_intervals=0
                )
            ],
            id='app-container'
        )
