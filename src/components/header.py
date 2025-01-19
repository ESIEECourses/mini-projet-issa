from dash import html


def create_header():
    """
        Création du header du site
    
    Returns : 
        html.Div : Layout du header
    """
    return html.Div(
        children=[
            html.A(html.H3("ESIEEVIZ",style={"font-size":"60px"}),href='/home' ,style={"textAlign" : "center", "font-style":"bold","color":"white", "font-family":"Fantasy", "justify-content":"center", "text-decoration":"none"})
        ],
        style={"height":"100px", "background": "rgb(92,9,121)","background": "linear-gradient(180deg, rgba(92,9,121,0.5816701680672269) 15%, rgba(0,191,255,0.5452556022408963) 100%)"}
    )
