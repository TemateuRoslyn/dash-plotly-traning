from callbacks.app_callbacks import *
from callbacks.line_graph_callback import *

def load_callbacks(app):
    line_graph_update(app=app)
    tabs_callback(app=app)