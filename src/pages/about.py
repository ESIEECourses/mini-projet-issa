from dash import html
from ..components.navbar import makeNavBar
from ..components.footer import get_footer
from ..components.header import create_header

def init_about():
    return html.Div([
        create_header(),
        makeNavBar(),
        get_footer(),
    ])