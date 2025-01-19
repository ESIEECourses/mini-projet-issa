from ..components.navbar import makeNavBar
from ..components.footer import get_footer
from ..components.header import create_header
from dash import html


def init_home():

    """
    Création et initialisation du layout de la section home
    
    Returns:
    
        dash.Div : Le Layout de la page Home
        
    """

    return html.Div(
        children=[
            create_header(),
            makeNavBar(),
            html.Div(
                children=[
                    html.Br(),
                    html.Br(),
                    html.H2("Bonjour et bienvenue sur ESIEEViz !"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.P(
                        "Nous sommes ravis de vous présenter notre projet qui consistera à vous démontrer une étude sur les différents séismes dans le monde entier"
                    ),
                    html.P(
                        "Ci-dessous veuillez choisir quel types de données vous souhaitez visualiser ⬇️"
                    ),
                    html.Br(),
                ],
                style={"textAlign": "center", "color": "white", "height": "370px"},
            ),
            html.Br(),
            html.Br(),
            html.H2(
                "Nos différentes analyses 📈",
                style={"text-align": "center", "color": "white"},
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H2("Les différents histogrammes 📊"),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.A("Pour les voir cliquez ici", href="/histograms",style={"background-color":"black", "text-decoration":"none",
                                "padding":"15px", "color":"white", "background": "rgb(9,7,21)",
                                "background": "linear-gradient(90deg, rgba(9,27,121,0.5816701680672269) 15%, rgba(0,106,255,0.5452556022408963) 100%)",
                                "border-radius":"20px"}),
                        ],
                        style={
                            "text-align": "center",
                            "width": "45%",
                            "border": "2px solid black",
                            "background": "linear-gradient(0deg, rgba(213,167,33,0.5816701680672269) 15%, rgba(255,0,11,0.5452556022408963) 100%)",
                            "color": "white",
                            "border-radius": "30px",
                            "height": "350px",
                            "font-family": "Poppins",
                        },
                    ),
                    html.Div(
                        children=[
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H2(
                                "Les cartes modélisant les séismes dans le monde 🗺️"
                            ),
                            html.Br(),
                            html.Br(),
                            html.A("Pour les voir cliquez ici", href="/maps",style={"background-color":"black", "text-decoration":"none",
                                "padding":"15px", "color":"white", "background": "rgb(9,7,21)",
                                "background": "linear-gradient(90deg, rgba(9,27,121,0.5816701680672269) 15%, rgba(0,106,255,0.5452556022408963) 100%)",
                                "border-radius":"20px"}),
                        ],
                        style={
                            "text-align": "center",
                            "width": "45%",
                            "border": "2px solid black",
                            "background": "linear-gradient(0deg, rgba(136,208,49,0.6264880952380952) 32%, rgba(68,40,156,0.6629026610644257) 62%)",
                            "color": "white",
                            "border-radius": "30px",
                            "height": "350px",
                            "font-family": "Poppins",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "justify-content": "space-around",
                    "align-items": "center",
                    "margin-top": "20px",
                },
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            get_footer(),
        ],
        style={
            "background": "rgb(9,7,21)",
            "background": "linear-gradient(90deg, rgba(9,27,121,0.5816701680672269) 15%, rgba(0,106,255,0.5452556022408963) 100%)",
        },
    )
