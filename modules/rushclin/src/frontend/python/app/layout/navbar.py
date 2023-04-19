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
                    value='accelerometre',
                    className='custum-tabs mx-5 mb-2',
                    children=[
                        dcc.Tab(
                            id='setting_tab',
                            label='Accelerometres',
                            value='accelerometre',
                            className="custom-tab text-uppercase",
                            selected_className="custom-tab--selected",
                        ),
                        dcc.Tab(
                            id="control_tab",
                            label="Capteurs",
                            value="capteur",
                            className="custom-tab text-uppercase",
                            selected_className="custom-tab--selected",
                        ),
                    ],
                )
            ],
        )
