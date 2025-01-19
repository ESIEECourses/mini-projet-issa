from ..components.navbar import makeNavBar
from ..components.footer import get_footer
from ..components.header import create_header
from ..components.component2 import render_folium_map_seism, render_leaflet_map_seism
from dash import html


def init_maps():
    """
    Création et initialisation de la section Cartes avec le chargement de toutes les cartes.

    Returns :

        dash.Div : La page Maps avec toutes les cartes.
    """
    return html.Div(
        children=[
            create_header(),
            makeNavBar(),
            html.Br(),
            html.Br(),
            html.H2(
                "Bienvenue dans la page Cartes !",
                style={"textAlign": "center", "color": "white"},
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.P(
                "Découvrez ci-dessous les analyses menées qui ont étés modélisées sous forme de cartes.",
                style={"textAlign": "center", "color": "white"},
            ),
            html.Br(),
            html.Div(
                children=[
                    html.H3(
                        "HeatMap des différents Séismes impactant les différentes zones",
                        style={"textAlign": "center", "color": "white"},
                    ),
                    html.Br(),
                    render_folium_map_seism(),
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "100px",
                    "background-color": "#800F47",
                    "padding": "90px",
                    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset",
                },
            ),
            html.Div(
                children=[
                    html.H3(
                        "Carte chlorophète des différents séismes dans les zones du mondes",
                        style={"textAlign": "center", "color": "white"},
                    ),
                    html.P(
                        "(Ainsi que les données pour chacun des cercles.)",
                        style={"textAlign": "center", "color": "white"},
                    ),
                    html.Br(),
                    render_leaflet_map_seism(),
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "90px",
                    "background-color": "black",
                    "padding": "100px",
                    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset",
                },
            ),
            get_footer(),
        ],
        style={
            "background": "rgb(9,7,21)",
            "background": "linear-gradient(90deg, rgba(9,27,121,0.5816701680672269) 15%, rgba(0,106,255,0.5452556022408963) 100%)",
        },
    )
