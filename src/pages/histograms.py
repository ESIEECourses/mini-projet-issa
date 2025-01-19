from ..components.navbar import makeNavBar
from ..components.footer import get_footer
from ..components.header import create_header
from ..components.component1 import (
    render_histogram_seism_by_country,
    render_histogram_seism_by_year,
    render_histogram_seism_combine,
    histogram_death_magnitude,
    histogram_magnitude_bycountry,
    scatter_magnitud_seism,
    scatter_seism,
)
from dash import html


def init_histogram():
    return html.Div(
        children=[
            create_header(),
            makeNavBar(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H2(
                "Bienvenue sur la page Histogrammes !", style={"textAlign": "center", "color": "white"}
            ),
            html.Br(),
            html.P(
                "Explorez ci-dessous nos différentes représentations graphiques de nos analyses.",
                style={"textAlign": "center", "color": "white"},
            ),
            html.Br(),
            html.Br(),
            html.Div(
              children=[
                html.H4("Diagramme circulaire : Répartition des décès par pays",style={"color":"white","text-align":"center"}),
                html.H5("(pour les séismes de magnitude > 5 et les pays de plus de 25 000 décès)",style={"color":"white","text-align":"center"}),
                html.Br(),
               scatter_magnitud_seism(),   
              ],
              style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "100px",
                    "background-color": "#800F47",
                    "padding": "100px",
                    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset",
                },
            ),
            html.Div(
              children=[
                html.H4("Nuage de points : Décès par pays en fonction des différentes magnitudes.",style={"color":"white","text-align":"center"}),
                html.H5("(Magnitude supérieure à 5)",style={"color":"white","text-align":"center"}),
                html.Br(),
               scatter_seism(),   
              ],
              style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "100px",
                    "background-color": "#520C6C",
                    "padding": "100px",
                    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset",
                },
            ),
            html.Div(
                children=[
                    html.H4("Diagramme : Nombre de séismes / Tsunamis en fonction des magnitudes",style={"color":"white","text-align":"center"}),
                    html.H5("(Tsunami : oui ou non)",style={"color":"white","text-align":"center"}),
                    html.Br(),
                    render_histogram_seism_combine(),
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "100px",
                    "background-color": "black",
                    "padding": "100px",
                },
            ),
            html.Div(
                children=[
                    html.H4("Histogramme : Nombre de Séismes / Tsunami en fonction des pays",style={"color":"white","text-align":"center"}),
                    html.H5("(Tsunami : oui ou non)", style={"color":"white","text-align":"center"}),
                    html.Br(),                
                    histogram_magnitude_bycountry()
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "100px",
                    "background-color": "#1027BD",
                    "padding": "100px",
                    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset",
                    
                },
            ),
            html.Div(
                children=[
                    html.H4("Histogramme : Cumul de Décès en fonction de la magnitude", style={"color":"white","text-align":"center"}),
                    html.H5("(Tsunami : oui ou non)", style={"color":"white","text-align":"center"}),
                    html.Br(),
                    histogram_death_magnitude()
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "100px",
                    "background-color": "grey",
                    "padding": "100px",
                    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset",

                },
            ),
            get_footer(),
        ],
        style={"background": "rgb(9,7,21)","background": "linear-gradient(90deg, rgba(9,27,121,0.5816701680672269) 15%, rgba(0,106,255,0.5452556022408963) 100%)"},
    )