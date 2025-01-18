from src.pages import init_home, init_about,init_histogram

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),  
        html.Div(id='page-content') 
    ],
    style={"background-color": "#ccc4c4"}
)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/about':
        return init_about()
    elif pathname == '/histograms':
        return init_histogram()
    else:
        return init_home()  

# Lancer l'application
if __name__ == '__main__':
    app.run(debug=True)

