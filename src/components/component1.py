from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

csv_path = "./data/cleaned/earthquake-cleaned.csv"
df = pd.read_csv(
    csv_path,
    delimiter=";",  # Définir explicitement le séparateur (si ce n'est pas la virgule `,`)
    on_bad_lines="skip",  # Pour pandas >= 1.3.0
    engine="python"
)

def render_histogram_seism_by_country():

    if df.empty:
        return html.Div("Aucune donnée disponible pour afficher l'histogramme.", style={"color": "red"})

    fig = px.histogram(
        df,
        x="Country",
        title="Nombre de séismes par pays",
        labels={"Country": "Pays", "count": "Nombre de séismes"},
        template="gridon"
    )
    fig.update_layout(
        yaxis=dict(
            dtick=50  # Pas de 100 pour l'axe des y
        ),
        height=600,  # Hauteur de la figure
    )
    return html.Div(
        [
            html.H3("Histogramme des Séismes par pays", style={"textAlign": "center", "color":"white"}),
            dcc.Graph(id="histogram", figure=fig, config={"responsive": True})
        ]
    )

def render_histogram_seism_by_year():
    fig = px.histogram(
        df,
        x="Year",
        title="Nombre de séismes par années",
        labels={"Year": "Année", "count": "Nombre de séismes"},
        template="plotly"
    )
    
    return html.Div(
        [
            html.H3("Histogramme des seismes par année",style={"textAlign": "center", "color":"white", "font-style":"italic"}),
            dcc.Graph(id="histogram", figure=fig, config={"responsive": True})
        ]
    )

def render_histogram_seism_combine():
    """
        Histogramme concernant la magnitude des séismes en fonction des Tsunamis
    Returns :
        Histogram
    """
    fig = px.histogram(
        df,
        x="Ms Magnitude",
        color="Flag Tsunami",
        title="Nombre de Tsunamis en fonction des magnitudes de séismes",
        labels={"Ms Magnitude": "Magnitude", "count": "Nombre de séismes"},
        template="plotly_white"
    )
    return html.Div(
        [
            html.H3("Histogramme des tsunamis et magnitude",style={"textAlign": "center", "color":"white"}),
            dcc.Graph(id="histogram", figure=fig, config={"responsive": True})
        ]
    )

def histogram_magnitude_bycountry():
    fig = px.histogram(
        df,
        x="Country",
        color="Flag Tsunami",
        title="Nombre de Tsunami en fonction des pays",
        labels={"Country": "Pays", "count": "Nombre de séismes"},
        template="plotly_white"
    )
    fig.update_layout(
        #width=1400,  # Largeur de la figure
        height=800,  # Hauteur de la figure
    )

    return html.Div(
        [
            dcc.Graph(id="histogram", figure=fig, config={"responsive": True})
        ]
    )

def histogram_death_magnitude():
    fig = px.histogram(
        df,
        x="Ms Magnitude",
        y="Earthquake : Deaths",
        color="Flag Tsunami",
        title="Nombre de Décès en fonction de la magnitude",
        labels={"Magnitude": "magnitude", "count": "Décès"},
        template="plotly_white"
    )
    fig.update_layout(
        #width=1400,  # Largeur de la figure
        height=800,  # Hauteur de la figure
    )

    return html.Div(
        [
            dcc.Graph(id="histogram", figure=fig, config={"responsive": True})
        ]
    )
     
def scatter_magnitud_seism():
    
    filtered_df = df[(df['Earthquake : Deaths'] > 50000) & (df['Ms Magnitude'] > 5)]    
    
    fig = px.pie(filtered_df, values='Earthquake : Deaths', names='Country',
                 title='Répartition des décès par pays (pour les séismes de magnitude > 5 et plus de 50 000 décès)',
                 template='gridon',
                 hole=0.15)
    
    return html.Div(
        [
            dcc.Graph(id="pie-chart", figure=fig),
        ]    
    )