import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.express as px
import pandas as pd

#on charge le fichier boostrap depuis dbc,mais il faut etre
#connecte pour cela
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
                title="Merritz")

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Accueil", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page1", active="exact"),
                dbc.NavLink("Table", href="/table", active="exact"),
            ],
            brand="Titre",
            color="primary",
            dark=True,
        ),
        dbc.Container(id="page-content", className="pt-4"),
    ]
)

table = html.Table(title="Un tableau",id='', className='table table-hover', children=[
    html.Thead(id='', className='', children=[
        html.Tr(id='', className='', children=[
            html.Th(id='', scope="col", children='Entete'),
            html.Th(id='', scope="col", children='Entete'),
            html.Th(id='', scope="col", children='Entete'),
            html.Th(id='', scope="col", children='Entete')
        ])
    ]),
    html.Tbody(id='', className='', children=[
        html.Tr(id='', className='table-active', children=[
            html.Th(id='', scope="row", className='', children='titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='table-primary', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='table-secondary', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='table-succes', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='table-danger', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='table-warning', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='table-info', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='table-light', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ]),
        html.Tr(id='', className='table-dark', children=[
            html.Th(id='', scope="row", className='', children='Titre'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue'),
            html.Td(id='', className='', children='contenue')
        ])
    ])
])

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


fig = px.scatter(df, x="Fruits", y="prix", color="ville")
fig1 = px.bar(df, x="Fruits", y="prix", color="ville", barmode="group")
fig2 = px.histogram(df, x="Fruits", y="prix", color="ville", 
                    marginal="rug", hover_data=df.columns)
fig3 = px.area(df, x="Fruits", y="prix", color="ville", line_group="prix")

figList = [fig,fig1,fig2,fig3]

graph = html.Div(children=[
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


#debut de l'action de callback,
#Output represente l'element cibler par la consequence d'un callback,
#Input represente l'element d'entrer qui genere un evenement sur le DOM,
#et cause un callback
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
#fonction associer au callback
def render_page_content(pathname):
    if pathname == "/":
        return graph
    elif pathname == "/page-1":
        return html.P("apres un callback effectuer sur la navigation page 1,redirection du contenue")
    elif pathname == "/table":
        return table
    # On capture les pages indisponibles dans finally
    #Si les etapes precedentes ne sont pas verifier, faire ce qui suit
    return html.Div(
        [
            html.H1("404: Oups, Page inexistante...", className="text-danger"),
            html.Br(),
            #le 'f' devant une chaine specifie qu'elle doit etre compiler avant un rendu
            html.P(f"Le chemin {pathname} n'a pas ete reconnue..."),
        ],
        className="p-3 bg-light rounded-3",
    )

@app.callback(
    Output("example-graph","figure"),
    Input("btn","n_clicks")
)
def changeDiagram(n_clicks):
    print(figList[n_clicks % len(figList)])
    return figList[n_clicks % len(figList)]

if __name__ == "__main__":
    app.run_server(debug=True,port=4000)
