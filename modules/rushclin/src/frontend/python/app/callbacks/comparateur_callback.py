from dash import Input, Output

from services.comparateur1_service import Comparateur1Service
from services.comparateur2_service import Comparateur2Service
from components.comparateur_graph import ComparateurGraph


class ComparateurCallbacks:
    def __init__(self, app) -> None:
        self.app = app
        self.comparateur_graph = ComparateurGraph()
        self.comparateur1Service = Comparateur1Service()
        self.comparateur2Service = Comparateur2Service()
        self.X1 = []
        self.X2 = []
        self.LABELS = []
        self.COLORS = ['#A56CC1', '#A6ACEC',]

    def register(self):
        @self.app.callback(
            Output('comparateur-1', 'children'),
            Input("interval-component", "n_intervals"),
        )
        def update_comparateur(n):
            data1 = self.comparateur1Service.get_next()
            data2 = self.comparateur2Service.get_next()

            # print(data1, data2)
            if data1 and data2 is not None:
                # return self.comparateur_graph.render(
                #     id="cmp-1", datas=[self.X1, self.X2], labels=['Lab 1', 'Lab 2'], colors=self.COLORS)
                return []
            else:
                print("No Datas to render")
                return []
