import dash_core_components as dcc
import dash_html_components as html
from graphs.graph_data import *
from graphs.line import *

def render_fig(id,title):
    df = load_data()
    return ([
        html.H1(id='', className='', children=title),
        dcc.Graph(id=id,figure=line_graph(df=df))
    ])