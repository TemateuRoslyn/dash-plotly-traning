from dash import html
import dash_bootstrap_components as dbc


class Header:
    def __init__(self):
        self.title = html.H4(
            "Dashboard application",
            className="text-white p-0 fs-5 font-weight-bold text-uppercase",
        )
        self.sub_title = html.H5(
            "Une petite description",
            className="text-white p-0 fs-6 h-6",
        )

        self.logo_img = html.Img(
            src="/assets/dash-logo.png",
            style={
                "float": "right",
                "height": 50,
                "padding-left": 10,
                "padding-bottom": 10,
                "padding-top": 10,
            },
        )

        self.link = html.A(
            self.logo_img,
            href="https://plotly.com/dash/",
        )

    def render(self):
        return dbc.Row(
            children=[
                dbc.Col(
                    [
                        dbc.Row([self.title]),
                        dbc.Row([self.sub_title]),
                    ],
                ),
                dbc.Col([self.link])
            ],
            className="my-3 mx-5",
        )
