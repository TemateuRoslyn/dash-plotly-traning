import dash
import pandas as pd
from dash import html, dcc
import plotly.express as px
from dash import Input, Output, dcc, html


dash.register_page(__name__)

# Templates pour la representation des graphes dans l'application
layout = html.Div(children=[
    html.H1(children='Mytest on Dash'),

    html.Div(children='''
        Presentation des prix de quelques fruits dans les villes camerounaises
    '''),
    html.Button(id='btn', className='btn btn-info', children=[
        '''Next graph style'''
    ], n_clicks=0),
    dcc.Graph(
        id='example-graph'
    )
])


# Un datagramme de donnees utiliser pour dessiner les differents graphes
df = pd.DataFrame({
    "Fruits": ["Pommes", "Oranges", "Bananes", "pommes", "Oranges",
            "Bananes", "Pommes", "Oranges", "Bananes", "Pommes", 
            "Oranges", "Bananes"],
    "prix": [400, 150, 225, 254, 444, 545, 765, 409, 692, 950, 300, 275],
    "ville": [
        "Dschang", "Bafoussam", "Bouda", "Badjoun", "Bangangte", 
        "Baham", "Douala", "Kribi", "Mbepanda", "Fomopea", "Bafia",
        "Tongolo"]
})


# Une enumeration de quelques graphiques
fig = px.scatter(df, x="Fruits", y="prix", color="ville")
fig1 = px.bar(df, x="Fruits", y="prix", color="ville", barmode="group")
fig2 = px.histogram(df, x="Fruits", y="prix", color="ville", 
                    marginal="rug", hover_data=df.columns)
fig3 = px.area(df, x="Fruits", y="prix", color="ville", line_group="prix")

# Encapsulation des graphes dans une liste
figList = [fig,fig1,fig2,fig3]


# Callback pour gerer l'affichage des figures sous formes de slide
@dash.callback(
    Output("example-graph","figure"),
    Input("btn","n_clicks")
)
# 
# Fonction associer au callback de slide
def changeDiagram(n_clicks):
    print(figList[n_clicks % len(figList)])
    return figList[n_clicks % len(figList)]