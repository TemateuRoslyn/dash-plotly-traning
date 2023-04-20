from dash import dcc
import plotly.graph_objs as go
import numpy as np
np.random.seed(1)


class SparkLine:
    def __init__(self) -> None:
        self.N = 100
        self.random_x = np.linspace(0, 1, self.N)
        self.random_y = np.random.randn(self.N)

    def render(self, id, x, y, name="Graph"):
        if x is None:
            x = self.random_x
        if y is None:
            y = self.random_y
        fig = dcc.Graph(
            config={
                "staticPlot": False,
                "editable": False,
                "displayModeBar": False,
            },
            id=id,
            figure=go.Figure(
                {
                    "data": [
                        {
                            "x": x,
                            "y": y,
                            "mode": "lines+markers",
                            "name": name,
                            "line": {"color": "#f4d44d"},
                        }
                    ],
                    "layout": {
                        "xaxis": dict(
                            showline=False, showgrid=False, zeroline=False
                        ),
                        "yaxis": dict(
                            showgrid=False, showline=False, zeroline=False
                        ),
                        "autosize": True,
                        "margin": dict(l=20, r=20, t=20, b=20),
                        "showlegend": True,
                        "paper_bgcolor": "rgba(0,0,0,0)",
                        "plot_bgcolor": "rgba(0,0,0,0)",
                        "font": {"color": "white"},
                        "height": 300
                    },
                }
            ),
            className='p-0 bg-dark'
        )

        return fig
