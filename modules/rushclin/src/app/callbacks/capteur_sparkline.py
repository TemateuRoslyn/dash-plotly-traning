from dash import Output, Input, State
from services.accelerometre1_service import Accelerometre1Service
from components.sparkline_graph import SparkLine
from datetime import datetime, timedelta
from services.redis_service import RedisServices

UPDATE_INTERVAL = 1


class CapteurSparkLineCallback:
    def __init__(self, app):
        self.app = app
        self.capteur_service = Accelerometre1Service()
        self.Y1 = []
        self.Y2 = []
        self.X = []
        self.sparkline = SparkLine()
        self.redis = RedisServices()

    def register(self):
        @self.app.callback(
            Output("capteur-sparkline-graph", "children"),
            Output("capteur-sparkline-graph-1", "children"),
            Input("interval-component", "n_intervals"),
        )
        def update_capteur(n):
            data = self.redis.get_data("acc-1")
            self.capteur_service.get_next()
            self.X = [
                datetime.now() + timedelta(seconds=i * UPDATE_INTERVAL)
                for i in range(n + 1)
            ]

            if data is not None:
                value = data["time "]
                self.Y1.append(value)
                self.Y2.append((value * 0.5) - 20)
                return [
                    self.sparkline.render(
                        id="sprk-1", x=self.X, y=self.Y1[-60:], name="Capteur 1"
                    ),
                    self.sparkline.render(
                        id="sprk-2", x=None, y=self.Y2[-60:], name="Capteur 2"
                    ),
                ]

            print("Data is None")
            return []
