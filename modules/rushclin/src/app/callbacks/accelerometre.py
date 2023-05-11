from dash import Input, Output
from services.accelerometre1_service import Accelerometre1Service


class Accelerometre:
    def __init__(self, app):
        self.app = app
        self.accelerometre1 = Accelerometre1Service()

    def register(self):
        @self.app.callback(
            Output("acc-1", "label"),
            Output("acc-2", "label"),
            Output("acc-3", "label"),
            Output("acc-4", "label"),
            Output("acc-1", "value"),
            Output("acc-2", "value"),
            Output("acc-3", "value"),
            Output("acc-4", "value"),
            Input("interval-component", "n_intervals"),
        )
        def update_accelerometre(n):
            data = self.accelerometre1.get_next()
            if data is not None:
                label = data['capteur_name']
                value = data['time ']
                return [label, 'Capteur No 2', 'Capteur No 3', 'Capteur No 4', value, value*.5, value*1.5, value*.3]
            else:
                print('Data is None')
                return ['Label 1', 'Label 2', 'Label 3', 'Label 4', 0, 0, 0, 0]
