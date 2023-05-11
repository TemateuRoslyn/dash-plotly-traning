import plotly.figure_factory as ff
import plotly.graph_objs as go
from dash import dcc


class ComparateurGraph:
    def __init__(self) -> None:
        pass

    def render(self, id, datas, labels, colors):
        fig = dcc.Graph(
            id=id,
            figure=ff.create_distplot(
                datas, labels, colors=colors,
                bin_size=.2, show_rug=False
            )
        )
        return fig
