from callbacks.app_callbacks import *
from callbacks.graph_callback import *

def load_callbacks(app):
    line_graph_update(app=app)
    pie_graph_update(app=app)
    tabs_callback(app=app)