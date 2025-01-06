from dash import Dash, html
import dash_bootstrap_components as dbc
from component1 import render_histogram_seism_by_country, render_histogram_seism_by_year, render_histogram_seism_combine, histogram_magnitude_bycountry, histogram_death_magnitude
from component2 import render_choropleth_map_seism
from footer import get_footer

def makeNavBar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.NavItem(dbc.NavLink("Page 2", href="#")),
            dbc.NavItem(dbc.NavLink("Page 3", href="#")),
        ],
        brand="ESIEEViz",
        brand_href="./header",
        color="black",
        dark=True,
        style={"border-radius":"15px", "height":"75px"},
    )
    return navbar



def header():
    app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

    app.layout =html.Div(children=[
        makeNavBar(),
        html.Br(),
        html.H3(children='Hello dash', style={"textAlign" : "center", "color": "black"}),
        html.Br(),
        html.H3(children='How are you today ?', style={"textAlign" : "center", "color": "black"}),
        html.Br(),
        html.Div(children=[
                render_histogram_seism_by_country(),
            ], style={"margin":"7em", "border" : "2px solid black", "border-radius":"20px", "background-color":"black", "padding":"100px"}
        ),
        html.Div(children=[
                render_histogram_seism_by_year(),
            ], style={"margin":"7em", "border" : "2px solid black", "border-radius":"20px", "background-color":"black", "padding":"100px"}
        ),
        html.Div(children=[
                render_histogram_seism_combine(),
            ], style={"margin":"7em", "border" : "2px solid black", "border-radius":"20px", "background-color":"black", "padding":"100px"}
        ),
        html.Div(children=[
            histogram_magnitude_bycountry()
            ], style={"margin":"7em", "border" : "2px solid black", "border-radius":"20px", "background-color":"black", "padding":"100px"}
        ),
        html.Div(children=[
                render_choropleth_map_seism()
            ], style={"margin":"7em", "border" : "2px solid black", "border-radius":"20px", "background-color":"black", "padding":"100px"}
        ),
        html.Div(children=[
                histogram_death_magnitude()
            ], style={"margin":"7em", "border" : "2px solid black", "border-radius":"20px", "background-color":"black", "padding":"100px"}
        ),
        
        get_footer()
    ],style={"background-color": "#779874"})

    if __name__ == '__main__':
        app.run(debug=True)

header()