import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import requests


def line_graph():
    datas = requests.get("http://127.0.0.1:8000/accelerometre1/next")
    if datas.status_code == requests.codes.ok:
        json_datas = datas.json()
        df = pd.DataFrame(data=json_datas)
        fig = px.line(
            df,
            x="date",
            y="temperature",
            markers=True,
        )

        fig.update_layout(plot_bgcolor='lightgray')
        return fig
    else:
        raise Exception