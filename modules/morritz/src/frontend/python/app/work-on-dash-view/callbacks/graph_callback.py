from dash.dependencies import Input, Output
from layouts.graph_layout import render_fig
from graphs.graph_data import *
from graphs.chart import *

# callbacks de rechargement des differents graphics de l'application

def line_graph_update(app):
    @app.callback(
        Output("line_chart", "children"),
        [Input("interval", "n_intervals")]
    )
    def line_chart(n):
        return render_fig(id="line",title="Line Chart")
    
def pie_graph_update(app):
    @app.callback(
        Output("pie_chart", "children"),
        [Input("interval", "n_intervals")]
    )
    def line_chart(n):
        return render_fig(id="pie",title="Scatter Chart")


def scatter_graph_update(app):
    @app.callback(
        Output("scatter_chart", "children"),
        [Input("interval", "n_intervals")]
    )
    def line_chart(n):
        return render_fig(id="scatter",title="Scatter Chart")