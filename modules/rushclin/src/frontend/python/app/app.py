import os
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True

# Application du theme LUX de Bootstrap
app = Dash(external_stylesheets=[dbc.themes.LUX])
app.title='Finances'

# Style du sidebar
SIDEBAR_STYLE = {
    "position": 'fixed', 
    'top': 0, 
    'left': 0,
    'bottom': 0, 
    'width': '16rem', 
    'padding': '2rem 1rem', 
    'background-color': '#f1f1f1' 
}

# Content Style 
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

navlinks = dbc.Nav(
    [
        dbc.NavLink("Marché financier de Apple", href='/', active='exact'), 
        dbc.NavLink("Analyse des prix", href='/prices', active='exact'), 
        dbc.NavLink("Histogramme", href='/histogram', active='exact'), 
        dbc.NavLink("Graphe avec slide", href='/slide', active='exact'), 
        dbc.NavLink("A Propos", href='/about', active='exact'), 
    ], 
    vertical=True,
    pills=True,
)

sidebar = html.Div(
    [
        html.H2("Finance", className='display-6'), 
        html.Hr(), 
        html.P("Courbes de finances ", className='lead my-3 fs-6'), 
        navlinks
    ], 
    style=SIDEBAR_STYLE
)

content = html.Div(
    id='page-content', 
    children=[], 
    style=CONTENT_STYLE
)

server = app.server

app.layout = dbc.Container(
    html.Div(
        [
            dcc.Location(id='url'), 
            sidebar, 
            content
        ]
    )
)

@app.callback( 
    Output('page-content', 'children'),
    [Input('url', 'pathname')] 
)
def render_page_content(pathname):
    if(pathname == '/'): 
        return [

        ]
    elif(pathname == '/prices'):
        return [
      
        ]
    elif(pathname == '/slide'):
        return [

        ]
    elif(pathname == '/about'): 
        return [
            html.H1('A propos de moi', className='text-center'), 
            html.Hr(),
        ]
    elif(pathname == '/histogram'): 
        return [
            
        ]
    # Au cas ou l'utilisateur aie entré une url invalide, on lui renvois la page 404
    return dbc.Alert("Oups... La page n'a pas été trouvée. 😴️", color='danger', className='text-center')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8050", debug=debug)
