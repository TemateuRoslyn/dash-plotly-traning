from dash import html, Input, Output
from services.accelerometre1_service import Accelerometre1Service


class IntervalCallback:
    def __init__(self, app) -> None:
        self.app = app
        self.accelerometre1 = Accelerometre1Service()

    def register(self):
        @self.app.callback(
            Output("timer", "children"),
            Input("interval-component", "n_intervals"),
        )
        def make_interval(n):
            data = self.accelerometre1.get_next()
            if (data is not None):
                print(data)
            else:
                print('Errerur de requette')

            return [
                html.H1("Interval : "+str(n))
            ]
