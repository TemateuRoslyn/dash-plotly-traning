import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go
import dash_daq as daq

import pandas as pd

# Fonction utiliser pour generer la nav-bar
def build_banner(app):
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("Sensitive Captor Data"),
                    html.H6("Control des temperatures"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.A(
                        html.Button(children="BUTTON"),
                        href="#",
                    ),
                    html.Button(
                        id="learn-more-button", children="BUTTON 1", n_clicks=0
                    ),
                    html.A(
                        # on utilise la methode get_xxx pour recuperer l'image de dash dans le repertoire /assets
                        html.Img(id="logo", src='https://banner2.cleanpng.com/20180629/fb/kisspng-computer-icons-sensor-radio-frequency-identificati-rfid-5b36d528a281e7.5870295415303201686656.jpg'),
                        href="#",
                    ),
                ],
            ),
        ],
    )


# Definition des bar de navigation dans le body, on utilise dash core components
def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custom-tabs",
                children=[
                    # Premiere Tabs
                    dcc.Tab(
                        id="Specs-tab",
                        label="Specification des parametres",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    # Seconde Tabs
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Dashboard des cartes de controles",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )


# Fonction qui genere le contenue du menu pop-up
def generate_modal():
    return html.Div(
        id="markdown",
        className="modal",
        children=(
            html.Div(
                id="markdown-container",
                className="markdown-container",
                children=[
                    html.Div(
                        className="close-container",
                        children=html.Button(
                            "Fermer",
                            id="markdown_close",
                            n_clicks=0,
                            className="closeButton",
                        ),
                    ),
                    html.Div(
                        className="markdown-text",
                        children=dcc.Markdown(
                            children=(
                                """Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perferendis magni itaque aspernatur minima sit doloribus quod molestiae officia illo architecto hic perspiciatis quia iusto accusantium adipisci facilis, voluptatem saepe nostrum?
                                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perferendis magni itaque aspernatur minima sit doloribus quod molestiae officia illo architecto hic perspiciatis quia iusto accusantium adipisci facilis, voluptatem saepe nostrum?
                                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perferendis magni itaque aspernatur minima sit doloribus quod molestiae officia illo architecto hic perspiciatis quia iusto accusantium adipisci facilis, voluptatem saepe nostrum?
                                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perferendis magni itaque aspernatur minima sit doloribus quod molestiae officia illo architecto hic perspiciatis quia iusto accusantium adipisci facilis, voluptatem saepe nostrum?
                    """
                            )
                        ),
                    ),
                ],
            )
        ),
    )