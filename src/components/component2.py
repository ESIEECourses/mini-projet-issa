import plotly.graph_objects as go
import pandas as pd
from dash import html

import dash_leaflet as dl
import folium
from folium.plugins import HeatMap

csv_path = "./data/cleaned/earthquake-cleaned.csv"
df = pd.read_csv(csv_path, delimiter=";", on_bad_lines="skip", engine="python")

# Séparation de la latitude et longitude
df[["Latitude", "Longitude"]] = df["ICoordinates"].str.split(",", expand=True)
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")


def render_folium_map_seism():
    """
    Création d'une HeatMap sur les lieux des séismes.

    Returns:

        html.IFrame : HeatMap sur les lieux des désastres.
    """

    df_filtered = df.dropna(subset=["Latitude", "Longitude"])

    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")

    heat_data = [
        [row["Latitude"], row["Longitude"], row["Earthquake : Deaths"]]
        for _, row in df_filtered.iterrows()
    ]
    HeatMap(heat_data, name="Heatmap des morts dus aux séismes").add_to(m)

    folium_map_html = m.get_root().render()

    return html.Div(
        [
            html.Iframe(
                srcDoc=folium_map_html,
                style={"width": "100%", "height": "600px", "border": "none"},
            )
        ]
    )


def render_leaflet_map_seism():
    """
    Création d'une carte avec marqueurs sur les lieux des séismes.

    Returns:

        dl.Map : Carte avec indication du nombre de morts.
    """
    # Filtrer les lignes avec des coordonnées valides
    df_filtered = df.dropna(subset=["Latitude", "Longitude"])

    # Créer des marqueurs pour chaque point
    markers = [
        dl.CircleMarker(
            center=[row["Latitude"], row["Longitude"]],
            radius=min(row["Earthquake : Deaths"] / 30, 20),
            color="red",
            fill=True,
            fillColor="blue",
            fillOpacity=0.3,
            children=[
                dl.Tooltip(
                    f"Pays: {row['Country']}, Nombre de morts: {row['Earthquake : Deaths']}"
                )
            ],
        )
        for _, row in df_filtered.iterrows()
    ]

    return html.Div(
        [
            dl.Map(
                center=[20, 0],
                zoom=2,
                children=[
                    dl.TileLayer(
                        url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
                    ),
                    *markers,
                ],
                style={"width": "100%", "height": "600px"},
            )
        ]
    )
