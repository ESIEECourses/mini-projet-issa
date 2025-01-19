from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

csv_path = "./data/cleaned/earthquake-cleaned.csv"
df = pd.read_csv(
    csv_path,
    delimiter=";",
    on_bad_lines="skip",
    engine="python"
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
        height=600,
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
    
    total_deaths = df["Earthquake : Deaths"].sum()
    total_deaths = "{:,.0f}".format(total_deaths).replace(",", " ")
    
    return html.Div(
        [
            html.H4("Nombre de Séismes / Tsunami en fonction des pays",style={"color":"white","text-align":"center"}),
            html.H5("(Tsunami : oui ou non)", style={"color":"white","text-align":"center"}),
            html.P(f"Le nombre total de morts dus aux séismes est de : {total_deaths} millions de personnes", style={"text-align":"center"}),
            dcc.Graph(id="pie-chart", figure=fig),
        ],
        style={'border-radius': '15px', 'background-color': 'white', 'padding': '10px'}    
    )
    
def scatter_seism():
    filtered_df = df[(df['Earthquake : Deaths'] > 50000)]
    
    fig = px.scatter(filtered_df, x="Ms Magnitude", y="Earthquake : Deaths", color="Country",
                     title='Magnitude vs Earthquake Deaths',template='seaborn')
    
    return html.Div(
        [
            dcc.Graph(id="scatter-plot", figure=fig)
        ],
        style={'border-radius': '15px', 'background-color': 'white', 'padding': '10px'}    
    )