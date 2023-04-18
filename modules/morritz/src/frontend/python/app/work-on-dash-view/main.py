# importation des libraries de notre application
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
import dash

# inclusion des meta donnees de notre application
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,'./assets/style.css'], suppress_callback_exceptions=True, use_pages=True)
app.title='Merritz'


# point d'entrer de l'application + routage vers les differentes pages qui se trouvent dans /pages
# la zone de navigation (barre de navigation) est egalement definis ici
app.layout = html.Div(children=[
    html.Div(
        dbc.NavbarSimple(
            children=[
                dbc.NavLink(html.Button(id='', className='btn btn-outline-light btn-lg btn-sm', children=[
                    f"{page['name']}"
                ]), href=page["relative_path"], active="exact")
                for page in dash.page_registry.values()
            ],
            brand=html.Div(id='', className='', children=[
                html.H1(id='', className='fs-4', children='MANUFACTURING SPC DASHBOARD'),
                html.Label(id='', className='fs-6', children='Process Control an Exception Reporting')
            ]),
            color="dark",
            dark=True,
        ),
    ),

	dash.page_container
])

if __name__ == '__main__':
	app.run_server(host="0.0.0.0", port="4000", debug=True)