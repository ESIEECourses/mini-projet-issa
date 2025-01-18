import dash_bootstrap_components as dbc


def makeNavBar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Accueil", href="/")),
            dbc.NavItem(dbc.NavLink("Histogrammes", href="/histograms")),
            dbc.NavItem(dbc.NavLink("Cartes", href="#")),
            dbc.NavItem(dbc.NavLink("À Propos", href="/about")),
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