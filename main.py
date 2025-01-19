from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from src.utils import retirerColonnesEtNettoyer, get_csv

# Téléchargement du fichier CSV en ligne
get_csv()
# Nettoyage du fichier CSV
retirerColonnesEtNettoyer()


from src.pages import init_home, init_histogram, init_maps

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')  
    ],
    style={"background-color": "#ccc4c4"}
)


# Callback pour afficher la page en fonction de l'URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """
    Affichage de la page qui est sélectionnée dans la navbar.

    Args:
        pathname (str): Le chemin de la page spécifiée.
    """
    if pathname == '/histograms':
        return init_histogram()
    elif pathname == '/maps':
        return init_maps()
    else:
        return init_home()


if __name__ == '__main__':
    app.run(debug=True)