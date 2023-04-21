import plotly.express as px

def chart_graph(df,id):
    if (id == 'line'):
        fig = px.line(
            df,
            x="date",
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
        fig = px.line(
            df,
            x="date",
            y="temperature",
            markers=True,
        )
        return fig