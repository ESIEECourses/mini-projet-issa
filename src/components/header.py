from dash import Dash, html
import dash_bootstrap_components as dbc


def create_header():
    return html.Div(
        children=[
            html.A(html.H3("ESIEEVIZ",style={"font-size":"60px"}),style={"textAlign" : "center", "font-style":"bold","color":"white", "font-family":"Fantasy", "justify-content":"center"})
        ],
        style={"background-color":"#1c03ff", "height":"95px"}
    )
