import os
from dash import Dash, html, dcc, Input, Output
import numpy as np
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.figure_factory as ff

debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True

# Application du theme LUX de Bootstrap
app = Dash(external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)
app.title='Finances'

# Datasets imports 
apple_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
prices_df = px.data.stocks()
gapminder_df =  px.data.gapminder()

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
            html.H1("Le marché financier de Apple", className='text-center'),
            html.Hr(),
            dcc.Graph(
                id='apple_graph', 
                figure=go.Figure(
                    [
                        go.Scatter(
                            x=apple_df['Date'], 
                            y=apple_df['AAPL.High']
                        ), 
                    ]
                )
            ), 
        ]
    elif(pathname == '/prices'):
        return [
            html.H1('Graphe des prix du marché', className='text-center'), 
            html.Hr(),
            html.P("Selectionnez un marché ", className='lead fs-6'),
            dcc.Dropdown(
                id='marche', 
                options = ['AMZN', 'GOOG', 'AAPL', 'FB', 'NFLX', 'MSFT'] , 
                value='AMZN', 
                clearable=False
            ), 
            dcc.Graph(id="prices_graph"),            
        ]
    elif(pathname == '/slide'):
        return [
            html.H1('Graphe avec slides', className='text-center'), 
            html.Hr(),
            dcc.Graph(id='slide'), 
            dcc.Slider(
                gapminder_df['year'].min(), 
                gapminder_df['year'].max(), 
                step=None, 
                value=gapminder_df['year'].min(), 
                marks={str(year):str(year) for year in gapminder_df['year'].unique()}, 
                id='year-slider'
            )
        ]
    elif(pathname == '/about'): 
        return [
            html.H1('A propos de moi', className='text-center'), 
            html.Hr(),
            html.Blockquote(
                children=[
                    html.P("Crée dans le cadre de l'apprentissage de Dash - Plotly"), 
                    html.Figcaption("Rushclin Takam", className='blockquote-footer'),
                ], 
                className='blockquote'
            ), 
            html.Ul(
                children=[
                    html.Li("Prise en main de Dash", className='list-item'),
                    html.Li("Installation de dash_bootstrap_components"),
                    html.Li("Mise en place d'un Layout"),
                    html.Li("Ajout des liens  hypertexts dans l'application"),
                    html.Li("Changement de l'apparence de Bootstrap en choisissant son thème"),
                    html.Li("Creation des graphes avec dash_core_component"),
                    html.Li("Utilisation minimale de Docker"),
                    html.Li("Utilisation des callback pour donner du dynamisme à l'application"),
                ], 
                className='list'
            )
        ]
    elif(pathname == '/histogram'): 
        return [
            html.H1('Graphe avec des histogrammes', className='text-center'), 
            html.Hr(),
            dcc.Graph(
                id='histogram', 
            )
        ]
    # Au cas ou l'utilisateur aie entré une url invalide, on lui renvois la page 404
    return dbc.Alert("Oups... La page n'a pas été trouvée. 😴️", color='danger', className='text-center')
    
# Callback pour le rendu de la ligne d'histogramme des prix. 
@app.callback(
    Output('prices_graph', 'figure'), 
    Input('marche', 'value')
)
def render_prices_graph(marche): 
    fig = px.line(prices_df, x='date', y=marche)
    return fig

# Callback pour rendre le composant avac des Slide
@app.callback(
    Output('slide', 'figure'), 
    Input('year-slider', 'value')
)
def render_graph_1(year): 
    filtered_df = gapminder_df[gapminder_df.year == year]
    fig = px.histogram(filtered_df, x='lifeExp', color='continent')
    return fig  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8050", debug=debug)
