import plotly.express as px

def line_graph(df):
    fig = px.line(
        df,
        x="date",
        y="temperature",
        markers=True,
    )

    fig.update_layout(plot_bgcolor='lightgray')
    return fig