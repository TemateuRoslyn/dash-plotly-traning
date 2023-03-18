from dash import html, dash, dcc 

app = dash.Dash(_name_)
app.layout = html.Div(children = [
    html.H1('Une grosse demo'),
    html.H2("Un sous titre")

])

app.run_server(debug=True)