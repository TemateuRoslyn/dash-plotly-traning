





# Cette page n'est pas utile......







#debut de l'action de callback,
#Output represente l'element cibler par la consequence d'un callback,
#Input represente l'element d'entrer qui genere un evenement sur le DOM,
#et cause un callback
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# 
#fonction associer au callback
def render_page_content(pathname):
    if pathname == "/":
        return homeBody
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




# Point d'entrer de l'application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4000", debug=True)
