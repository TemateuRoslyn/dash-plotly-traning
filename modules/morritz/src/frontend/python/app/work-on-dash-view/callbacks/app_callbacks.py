from dash.dependencies import Input, Output
import dash_html_components as html

from layouts.graph_layout import *


# callback pour le rendu de la premiere Tabs (fenetre de navigation du body)
def tabs_callback(app):
    @app.callback(
        Output("app-content", "children"),
        [Input("app-tabs", "value")]
    )
    def render_tab_content(tab_switch):
        if tab_switch == "tab1":
            return 
        return (
            html.Div(
                id="status-container",
                children=[
                    html.Div(
                        id="graphs-container",
                        children=[
                            html.Div(id='line_chart', className='',
                                      children=render_fig(id="line",title="Line Chart")),
                            html.Div(id='pie_chart', className='',
                                      children=render_fig(id="pie",title="Pie Chart")),
                            html.Div(id='box_chart', className='',
                                      children=render_fig(id="box",title="Box Chart"))
                        ],
                    ),
                ],
            )
        )