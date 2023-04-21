import plotly.express as px

# fonction a utiliser pour le rendu des graphiques
def chart_graph(df,id):
    if (id == 'line'):
        fig = px.line(
            df,
            x="time",
            y="temperature",
            markers=True,
        )

        fig.update_layout(plot_bgcolor='lightgray')
        return fig
    elif (id == 'pie'):
        fig = px.pie(
            df,
            values='temperature',
            names='code',
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        return fig
    else:
        fig = px.scatter(
            df,
            x="time",
            y="temperature",
            color="code",
            hover_name="code"
        )
        return fig