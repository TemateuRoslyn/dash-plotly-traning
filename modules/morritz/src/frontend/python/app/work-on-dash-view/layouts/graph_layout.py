import dash_core_components as dcc

def render_fig(id,fig):
    return ([
        dcc.Graph(id=id,figure=fig)
    ])