import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='Ceci est une page d\'analyse'),
	html.Div([
        "Selectionner une ville que vous aimez: ",
        dcc.RadioItems(['Dschang', 'Douala','Bafoussam'],
        'Ouest Cameroun',
        id='analytics-input')
    ]),
	html.Br(),
    html.Div(id='analytics-output'),
])


@callback(
    Output(component_id='analytics-output', component_property='children'),
    Input(component_id='analytics-input', component_property='value')
)
def update_city_selected(input_value):
    return f'Vous aimez la ville de: {input_value}'