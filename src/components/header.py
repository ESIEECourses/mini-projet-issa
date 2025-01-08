from dash import Dash, html
import dash_bootstrap_components as dbc
from .component1 import render_histogram_seism_by_country, render_histogram_seism_by_year, render_histogram_seism_combine, histogram_magnitude_bycountry, histogram_death_magnitude
from .component2 import render_choropleth_map_seism
from .footer import get_footer

def makeNavBar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="#")),
            dbc.NavItem(dbc.NavLink("Histogram", href="#")),
            dbc.NavItem(dbc.NavLink("Map", href="#")),
        ],
        brand_href="./header",
        color="black",
        dark=True,
        className="justify-content-center",
        style={
            "border-radius":"15px",
            "height":"75px", 
            "margin-top":"-5px",
            "justify-content": "center",  # Centre les éléments horizontalement
            "align-items": "center"
                
        },

    )
    return navbar

def create_header():
    return html.Div(
        children=[
            html.A(html.H3("ESIEEVIZ",style={"font-size":"60px"}),style={"textAlign" : "center", "font-style":"bold","color":"white", "font-family":"Fantasy", "justify-content":"center"})
        ],
        style={"background-color":"#1c03ff", "height":"95px"}
    )
