from src.pages import init_home

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout =html.Div(children=[
        init_home()
    ],style={"background-color": "#ccc4c4"}
)


if __name__ == '__main__':
    app.run(debug=True)

