from dash import Input, Output
from services.accelerometre1_service import Accelerometre1Service


class Accelerometre:
    def __init__(self, app):
        self.app = app
        self.accelerometre1 = Accelerometre1Service()

    def register(self):
        @self.app.callback(
            Output("acc-1", "label"),
            Output("acc-1", "value"),
            Input("interval-component", "n_intervals"),
        )
        def update_accelerometre(n):
            data = self.accelerometre1.get_next()
            if data is not None:
                label = data['capteur_name']
                value = data['time ']
                return [label, value]
            else:
                print('Data is none')
                return ['Label', 0]
