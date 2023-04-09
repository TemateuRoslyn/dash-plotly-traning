from dash import dash, html, Output, Input, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SOLAR],
)
app.title = "Dashboard"


# Composants
def render_header():
    title = html.H4(
        "DASHBOARD",
        style={
            "marginTop": 5,
            "marginLeft": "10px",
        },
        className="text-white",
    )
    sub_title = html.H5(
        "Une petite description.",
        style={"marginLeft": "10px"},
        className="text-white",
    )
    logo_image = html.Img(
        src=app.get_asset_url("dash-logo.png"),
        style={
            "float": "right",
            "height": 50,
            "padding": 10,
        },
        className="mt-3",
    )
    link = html.A(
        logo_image,
        href="https://plotly.com/dash/",
    )

    return dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Row([title]),
                    dbc.Row([sub_title]),
                ]
            ),
            dbc.Col(link),
        ],
        className="my-1",
    )


def render_tab_1():
    return [
        html.Div(
            [
                html.Div(
                    [
                        html.P(
                            "Utilisez cette interface pour le parametrage du Dashboard"
                        )
                    ],
                    id="",
                    className="mt-5",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Label(
                                    id="select",
                                    children="Selectionnez la metrique",
                                    className="mb-3",
                                ),
                                html.Br(),
                                dcc.Dropdown(
                                    options=[
                                        "Facebook",
                                        "WhatsApp",
                                        "Telegram",
                                    ],
                                    id="select",
                                ),
                            ],
                            md=4,
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    generate_row(
                                        "specification",
                                        {
                                            "borderBottom": "solid 2px #f1f1f1",
                                            "height": "2rem",
                                        },
                                        {
                                            "id": "m_header_1",
                                            "children": html.Div("Specification"),
                                        },
                                        {
                                            "id": "m_header_2",
                                            "children": html.Div("Valeur"),
                                        },
                                        {
                                            "id": "m_header_3",
                                            "children": html.Div("Nouvelle valeur"),
                                        },
                                    ),
                                ),
                                html.Div(
                                    [
                                        generate_row(
                                            "row_1",
                                            {
                                                "marginTop": "10px",
                                                "marginBottom": "10px",
                                            },
                                            {
                                                "id": "m_header_1",
                                                "children": html.Div("Specification 1"),
                                            },
                                            {
                                                "id": "m_header_1",
                                                "children": html.Div("20"),
                                            },
                                            {
                                                "id": "m_header_1",
                                                "children": html.Div(
                                                    dcc.Input(
                                                        value=1,
                                                        type="number",
                                                        className="p-1",
                                                    )
                                                ),
                                            },
                                        )
                                    ]
                                ),
                            ],
                            md=8,
                            className="px-5",
                        ),
                    ],
                ),
            ],
            className="px-5",
        )
    ]


def render_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custum-tabs",
                children=[
                    dcc.Tab(
                        id="setting_tab",
                        label="PARAMETRAGES DU DASHBOARD",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="control_tab",
                        label="GRAPHES DE CONTRôLE",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            ),
        ],
    )


def render_side_bar_graph():
    return html.Div(
        id="",
        children=[
            html.Div(
                [
                    html.P("ID"),
                    daq.LEDDisplay(
                        id="",
                        value="1704",
                        color="#92e0d3",
                        backgroundColor="#1e2130",
                        size=50,
                    ),
                ],
                className="custum_card mb-5",
            ),
            html.Div(
                [
                    html.P("FREQUENCE"),
                    daq.Gauge(
                        id="",
                        max=2,
                        min=0,
                        showCurrentValue=True,
                    ),
                ],
                className="custum_card mb-5",
            ),
            html.Div(
                [
                    daq.StopButton(
                        id="",
                        size=100,
                        n_clicks=0,
                    )
                ],
                id="",
            ),
        ],
        className="bg-dark p-3",
    )


def render_header_list():
    return generate_row(
        "header_list",
        {"height": "3rem", "margin": "1rem 0"},
        {"id": "m_header_1", "children": html.Div("Parametres")},
        {"id": "m_header_2", "children": html.Div("Total")},
        {"id": "m_header_3", "children": html.Div("Evolution")},
    )


def generate_row(id, style, col1, col2, col3):
    if style is None:
        style = {"height": "8rem", "width": "100%"}
    return dbc.Row(
        children=[
            dbc.Col(
                id=col1["id"],
                children=col1["children"],
            ),
            dbc.Col(
                id=col2["id"],
                children=col2["children"],
            ),
            dbc.Col(
                id=col3["id"],
                children=col3["children"],
            ),
        ],
        id=id,
        style=style,
    )


def render_content_top():
    return html.Div(
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        [
                            html.Div(
                                ["Graphe de contrôle de metrique"],
                                className="px-3 text-capitalize text-muted",
                            ),
                            html.Hr(),
                            html.Div(
                                id="",
                                children=[
                                    render_header_list(),
                                    html.Div(
                                        [
                                            "Les elements ici",
                                        ],
                                        id="",
                                    ),
                                ],
                                className="px-3",
                            ),
                        ],
                        md=8,
                        className="bg-dark p-2",
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                ["Les parametres"],
                                className="px-3 text-capitalize text-muted",
                            ),
                            html.Hr(),
                            dcc.Graph(
                                id="",
                                figure={
                                    "data": [
                                        {
                                            "labels": [],
                                            "values": [],
                                            "type": "pie",
                                            "marker": {
                                                "line": {"color": "white", "width": 1}
                                            },
                                            "hoverinfo": "label",
                                            "textinfo": "label",
                                        }
                                    ],
                                    "layout": {
                                        "margin": dict(l=20, r=20, t=20, b=20),
                                        "showlegend": True,
                                        "paper_bgcolor": "rgba(0,0,0,0)",
                                        "plot_bgcolor": "rgba(0,0,0,0)",
                                        "font": {"color": "white"},
                                        "autosize": True,
                                    },
                                },
                            ),
                        ],
                        md=4,
                        className="bg-dark p-2",
                    ),
                ],
                id="",
            )
        ],
        className="px-3",
    )


app.layout = dbc.Container(
    fluid=True,
    children=[
        render_header(),
        html.Hr(),
        render_tabs(),
        html.Div(
            id="app-content",
        ),
    ],
    id="app-container",
)


@app.callback(
    [Output("app-content", "children")],
    [Input("app-tabs", "value")],
)
def render_tab_content(tab_switch):
    if tab_switch == "tab1":
        return render_tab_1()
    return [
        dbc.Row(
            [
                dbc.Col(
                    [
                        render_side_bar_graph(),
                    ],
                    md=3,
                ),
                dbc.Col(
                    [
                        html.Div(
                            id="graph_container",
                            children=[
                                render_content_top(),
                            ],
                        ),
                    ],
                    md=9,
                ),
            ],
            id="",
            className="mt-3",
        )
    ]


app.run_server(debug=True, port=8050)