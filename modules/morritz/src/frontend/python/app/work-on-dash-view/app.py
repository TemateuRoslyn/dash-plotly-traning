from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash import Dash

# import des librairies
from layouts.graph_layout import render_fig
from graphs.graph_data import *


app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        dcc.Interval(
            id="interval",
            disabled=False,
            n_intervals=0,
            interval=1000,
            max_intervals=-1
        ),
        html.H2("Dash Plotly Interface with Python API"),
        html.Div(id='figure', className='', children=render_fig('id',line_graph())
                 )
    ]
)


@app.callback(
    Output("figure", "children"),
    [Input("interval", "n_intervals")]
)
def line_chart(n):
    return render_fig('id',line_graph())


if __name__ == "__main__":
    app.run_server()