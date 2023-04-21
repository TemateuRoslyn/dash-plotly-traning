from dash.dependencies import Input, Output
from layouts.graph_layout import render_fig
from graphs.graph_data import *
from graphs.line import *

def line_graph_update(app):
    @app.callback(
        Output("line_chart", "children"),
        [Input("interval", "n_intervals")]
    )
    def line_chart(n):
        return render_fig(id="line",title="Line Chart")