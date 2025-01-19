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
        ],
        style={'border-radius': '15px', 'background-color': 'white', 'padding': '10px'}
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
        title="",
        labels={"Ms Magnitude": "Magnitude", "count": "Nombre de séismes"},
        template="plotly_white"
    )
    return html.Div(
        [
            html.H3("Histogramme des tsunamis et magnitude",style={"textAlign": "center", "color":"white"}),
            dcc.Graph(id="histogram", figure=fig, config={"responsive": True})
        ],
        style={'border-radius': '15px', 'background-color': 'white', 'padding': '10px'}
    )

def histogram_magnitude_bycountry():
    fig = px.histogram(
        df,
        x="Country",
        color="Flag Tsunami",
        title="",
        labels={"Country": "Pays", "count": "Nombre de séismes"},
        template="plotly_white"
    )
    fig.update_layout(
        #width=1400,  # Largeur de la figure
        height=700,  # Hauteur de la figure
        yaxis_title="Nombre de séismes",
    )

    return html.Div(
        [
            dcc.Graph(id="histogram", figure=fig, config={"responsive": True})
        ],
        style={'border-radius': '15px', 'background-color': 'white', 'padding': '10px'}
    )

def histogram_death_magnitude():
    fig = px.histogram(
        df,
        x="Ms Magnitude",
        y="Earthquake : Deaths",
        color="Flag Tsunami",
        title="",
        labels={"Magnitude": "magnitude", "count": "Nombres de séismes"},
        template="plotly_white"
    )
    fig.update_layout(
        #width=1400,  # Largeur de la figure
        height=600,  # Hauteur de la figure
        xaxis_title="Magnitudes",
        yaxis_title="Cumul des décès",
    )

    return html.Div(
        [
            dcc.Graph(id="histogram", figure=fig, config={"responsive": True})
        ],
        style={'border-radius': '15px', 'background-color': 'white', 'padding': '10px'}
    )
     
def scatter_magnitud_seism():
    
    filtered_df = df[(df['Earthquake : Deaths'] > 25000) & (df['Ms Magnitude'] > 5)]    
    
    fig = px.pie(filtered_df, values='Earthquake : Deaths', names='Country',
                 title='',
                 template='gridon',
                 hole=0.15)
    
    return html.Div(
        [
            dcc.Graph(id="pie-chart", figure=fig),
        ],
        style={'border-radius': '15px', 'background-color': 'white', 'padding': '10px'}    
    )
    
def scatter_seism():
    filtered_df = df[(df['Earthquake : Deaths'] > 50000)]
    
    fig = px.scatter(filtered_df, x="Ms Magnitude", y="Earthquake : Deaths", color="Country",
                     title='Magnitude vs Earthquake Deaths',template='seaborn')
    
    # Retourner le composant Dash
    return html.Div(
        [
            dcc.Graph(id="scatter-plot", figure=fig)
        ],
        style={'border-radius': '15px', 'background-color': 'white', 'padding': '10px'}    
    )