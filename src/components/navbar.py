import dash_bootstrap_components as dbc


def makeNavBar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.NavItem(dbc.NavLink("More pages", href="#")),
            dbc.NavItem(dbc.NavLink("Page 2", href="#")),
            dbc.NavItem(dbc.NavLink("Page 3", href="#")),
        ],
        brand="Navbar Oké",
        brand_href="#",
        color="primary",
        dark=True,
    )
    return navbar

makeNavBar()