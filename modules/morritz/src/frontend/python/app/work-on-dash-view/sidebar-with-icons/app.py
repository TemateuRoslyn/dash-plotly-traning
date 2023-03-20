from dash import Dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

LOGO = "./assets/logo.png"

app = Dash(
    title="Merritz",
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src=LOGO, style={"width": "3rem"}),
                html.H2("Merritz"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Accueil")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-calendar-alt me-2"),
                        html.Span("Calendrier"),
                    ],
                    href="/calendrier",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-envelope-open-text me-2"),
                        html.Span("Messages"),
                    ],
                    href="/messages",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

content = html.Div(id="page-content", className="content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# gestion du routage
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Bienvenue sur l'accueil")
    elif pathname == "/calendrier":
        return html.P("Un calendrier pas visible... HI HI HI")
    elif pathname == "/messages":
        return html.P("Vous voulez m'envoyer un message?")
    # route non definis
    return html.Div(
        [
            html.H1("404: Oups,non definie...", className="text-danger"),
            html.Hr(),
            html.P(f"Le chemin {pathname} est non reconnue..."),
        ],
        className="p-3 bg-light rounded-3",
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4002", debug=True)
