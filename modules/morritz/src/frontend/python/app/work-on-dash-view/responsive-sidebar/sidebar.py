import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

app = dash.Dash(
    title="Merritz",
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

# Row et Col sont des composants de dbc, que l'on utilise pour generer un
#header, il s'agit d'un titre et d'une bascule d'affichage et de masquage en
#cas d'evenemant sur l'ecran
sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Merritz", className="display-4")),
        dbc.Col(
            html.Button(
                # on utilise le recourci 'navbar-..' pour generer une bascule dans un span
                html.Span(className="navbar-toggler-icon"),
                className="navbar-toggler",
                # on personalise la couleur de notre bascule en noir
                style={
                    "color": "rgba(0,0,0,.5)",
                    "border-color": "rgba(0,0,0,.1)",
                },
                id="toggle",
            ),
            #on donne a la navbar une largeur automatique
            width="auto",
            # on aligne verticalement les items au centre
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        #on commence par place l'entete de la sidebar
        sidebar_header,
        # on utilise Collapse pour personaliser l'affichage et le masquage
        #de style sur les liens
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Accueil", href="/", active="exact"),
                    dbc.NavLink("Page 1", href="/page1", active="exact"),
                    dbc.NavLink("Page 2", href="/page2", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

#cette balise definit le contenue de notre apps
content = html.Div(id="page-content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


#definition du callback pour le routage
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Bienvenue sur la page d'accueil!")
    elif pathname == "/page1":
        return html.P("Vous etes sur la page 1")
    elif pathname == "/page2":
        return html.P("Vous etes sur la page 2")
    # Gestion des routes non defini
    return html.Div(
        [
            html.H1("404: Oups, Page inexistante...", className="text-danger"),
            html.Br(),
            #le 'f' devant une chaine specifie qu'elle doit etre compiler avant un rendu
            html.P(f"Le chemin {pathname} n'a pas ete reconnue..."),
        ],
        className="p-3 bg-light rounded-3",
    )

#callback pour la gestion de l'affichage de la sidebar en mode
#portrait
@app.callback(
    Output("collapse", "is_open"),
    [Input("toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4001", debug=True)
