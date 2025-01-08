from ..components.navbar import makeNavBar
from ..components.footer import get_footer
from dash import html


def init_home():

    return html.Div(
        children=[
            makeNavBar(),
            html.H1("Bonjour et bienvenue sur la page d'accueil !",style={"margin-bottom" : "50px"}),
            html.Br(),
            html.H3("Voici ci-dessous les différentes visualisation des données : ", style={"margin-bottom":"60px"}),
            html.Div(children=[
                html.A(html.P("Voir les histogrammes cliquez ici")),
            ],style={"margin":"7em", "border" : "2px solid black", "border-radius":"20px", "background-color":"black", "padding":"100px"}),
            get_footer(),
        ]
    )