from ..components.navbar import makeNavBar
from ..components.footer import get_footer
from ..components.header import create_header
from ..components.component1 import (
    render_histogram_seism_by_country,
    render_histogram_seism_by_year,
    render_histogram_seism_combine,
    histogram_death_magnitude,
    histogram_magnitude_bycountry,
)
from ..components.component2 import render_choropleth_map_seism
from dash import html


def init_home():

    return html.Div(
        children=[
            create_header(),
            makeNavBar(),
            html.Br(),
            html.H3(
                children="Hello dash", style={"textAlign": "center", "color": "black"}
            ),
            html.Br(),
            html.H3(
                children="How are you today ?",
                style={"textAlign": "center", "color": "black"},
            ),
            html.Br(),
            html.Div(
                children=[
                    render_histogram_seism_by_country(),
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "20px",
                    "background-color": "black",
                    "padding": "100px",
                },
            ),
            html.Div(
                children=[
                    render_histogram_seism_by_year(),
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "20px",
                    "background-color": "black",
                    "padding": "100px",
                },
            ),
            html.Div(
                children=[
                    render_histogram_seism_combine(),
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "20px",
                    "background-color": "black",
                    "padding": "100px",
                },
            ),
            html.Div(
                children=[histogram_magnitude_bycountry()],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "20px",
                    "background-color": "black",
                    "padding": "100px",
                },
            ),
            html.Div(
                children=[render_choropleth_map_seism()],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "20px",
                    "background-color": "black",
                    "padding": "100px",
                },
            ),
            html.Div(
                children=[histogram_death_magnitude()],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "20px",
                    "background-color": "black",
                    "padding": "100px",
                },
            ),
            get_footer(),
        ],
        style={"background-color": "#ccc4c4"},
    )
