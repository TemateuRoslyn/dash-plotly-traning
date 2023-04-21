from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash import Dash
import plotly.express as px
import pandas as pd
import requests

x_axis = [0]
def render_page_content():
    datas = requests.get("http://127.0.0.1:8000/accelerometre1/next")
    if datas.status_code == requests.codes.ok:
        json_datas = datas.json()
        df = pd.DataFrame(data=json_datas)
        df_val = df.values[0]
        # print(df.columns[1])
        # exit()
        fig = px.line(
            df,
            x="date",
            y="temperature"
        )
        return ([
            dcc.Graph(id="line",figure=fig)
        ])
    else:
        raise Exception


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
        html.Div(id='figure', className='', children=render_page_content()
                 )
    ]
)


@app.callback(
    Output("figure", "children"),
    [Input("interval", "n_intervals")]
)
def line_chart(n):
    return render_page_content()


if __name__ == "__main__":
    app.run_server()