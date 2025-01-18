from ..components.navbar import makeNavBar
from ..components.footer import get_footer
from ..components.header import create_header
from ..components.component1 import (
    render_histogram_seism_by_country,
    render_histogram_seism_by_year,
    render_histogram_seism_combine,
    histogram_death_magnitude,
    histogram_magnitude_bycountry,
    scatter_magnitud_seism,
)
from dash import html


def init_histogram():
    return html.Div(
        children=[
            create_header(),
            makeNavBar(),
            html.Br(),
            html.H3(
                children="Hello histograms", style={"textAlign": "center", "color": "black"}
            ),
            html.Br(),
            html.H3(
                children="How are you today ?",
                style={"textAlign": "center", "color": "black"},
            ),
            html.Br(),
            html.Br(),
            html.Div(
              children=[
               scatter_magnitud_seism(),   
              ],
              style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "100px",
                    "background-color": "#1C56F1",
                    "padding": "100px",
                    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset",
                },
            ),
            html.Br(),
            html.Br(),
            html.Div(
                children=[
                    render_histogram_seism_by_country(),
                ],
                style={
                    "margin": "7em",
                    "border": "2px solid black",
                    "border-radius": "100px",
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
        style={"background": "rgb(9,7,21)","background": "linear-gradient(90deg, rgba(9,27,121,0.5816701680672269) 15%, rgba(0,106,255,0.5452556022408963) 100%)"},
    )