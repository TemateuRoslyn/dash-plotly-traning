import dash_bootstrap_components as dbc
from dash import html, dcc


class Navbar:
    def __init__(self):
        print("============= INIT NAVBAR")

    def render(self):
        return html.Div(
            id='tabs',
            className='tabs',
            children=[
                dcc.Tabs(
                    id='app-tabs',
                    value='graphes',
                    className='custum-tabs mx-5 mb-2',
                    children=[
                        dcc.Tab(
                            id='setting_tab',
                            label='paramètres',
                            value='settings',
                            className="custom-tab text-uppercase",
                            selected_className="custom-tab--selected",
                        ),
                        dcc.Tab(
                            id="control_tab",
                            label="graphes de contrôle",
                            value="graphes",
                            className="custom-tab text-uppercase",
                            selected_className="custom-tab--selected",
                        ),
                    ],
                )
            ],
        )
