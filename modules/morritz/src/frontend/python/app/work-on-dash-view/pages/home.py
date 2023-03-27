import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__, path='/')



# Style a utiliser pour la navigation
contentLinkActive = "border-bottom border-primary border-5 mb-0"
contentLinkOff = "border border-0 mb-0"



# Un simple tableau bootstrap utiliser dans l'application
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




layout = html.Div(id='', className='', children=[
    html.Div(id='', className='d-flex mt-2', children=[
        html.Div(id='', className='flex-fill text-center me-3  bg-dark', children=[
            "SPECIFICATIONS SETTINGS",
            html.Hr(id='', className=contentLinkActive, children=[])
        ]),
        html.Div(id='', className='flex-fill text-center ms-3  bg-dark', children=[
            "CONTROL CHARTS DASHBORD",
            html.Hr(id='', className=contentLinkActive, children=[])
        ])
    ]),
    html.Div(id='', className='', children=[
        table
    ])
])