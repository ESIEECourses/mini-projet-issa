import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from dash import html, dcc  # Utilisation des imports modernes

# Chemin vers le fichier CSV
csv_path = "../../data/cleaned/earthquake-cleaned.csv"
df = pd.read_csv(
    csv_path,
    delimiter=";",  # Spécifier explicitement le séparateur
    on_bad_lines="skip",  # Ignorer les lignes problématiques
    engine="python"
)

# Séparation de la latitude et longitude
df[['Latitude', 'Longitude']] = df['ICoordinates'].str.split(',', expand=True)
df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

def render_choropleth_map_seism():
    # Regrouper les données par pays
    data_by_country = df.groupby("Country").agg(
        {"Earthquake : Deaths": "sum"}
    ).reset_index()
    
    # Création de la carte choroplèthe
    fig = px.choropleth(
        data_by_country,
        locations="Country",
        locationmode="country names",
        color="Earthquake : Deaths",
        hover_name="Country",
        color_continuous_scale="Reds",
        title="Nombre de morts par pays dus aux séismes"
    )
    
    # Retourner le composant Dash
    return html.Div(
        [
            html.H3(
                "Carte choroplèthe des séismes",
                style={"textAlign": "center", "color": "white", "font-style": "italic"}
            ),
            dcc.Graph(id="choropleth-map", figure=fig, config={"responsive": True})
        ]
    )
