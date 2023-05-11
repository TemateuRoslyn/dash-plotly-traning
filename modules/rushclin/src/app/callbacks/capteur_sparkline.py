from dash import Output, Input, State
from services.accelerometre1_service import Accelerometre1Service
from components.sparkline_graph import SparkLine


class CapteurSparkLineCallback:
    def __init__(self, app):
        self.app = app
        self.capteur_service = Accelerometre1Service()
        self.Y1 = []
        self.Y2 = []
        self.X = []
        self.X = [0 for i in range(5)]
        self.sparkline = SparkLine()

    def register(self):
        @self.app.callback(
            Output("capteur-sparkline-graph", "children"),
            Output("capteur-sparkline-graph-1", "children"),
            Input("interval-component", "n_intervals"),
        )
        def update_capteur(n):
            data = self.capteur_service.get_next()
            if data is not None:
                value = data['time ']
                self.Y1.append(value)
                self.Y2.append((value*.5)-20)
                return [
                    self.sparkline.render(
                        id='sprk-1', x=None, y=self.Y1, name='Capteur 1'),
                    self.sparkline.render(
                        id='sprk-2', x=None, y=self.Y2, name='Capteur 2')
                ]
            else:
                print("Data is None")
                return []
