import dash_bootstrap_components as dbc


def makeNavBar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="#")),
            dbc.NavItem(dbc.NavLink("Histogram", href="#")),
            dbc.NavItem(dbc.NavLink("Map", href="#")),
        ],
        brand_href="./header",
        color="black",
        dark=True,
        className="justify-content-center",
        style={
            "border-radius":"15px",
            "height":"75px", 
            "margin-top":"-5px",
            "align-items": "center",
        },

    )
    return navbar