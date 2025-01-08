from dash import html

footer_style = {
    'border': '2px solid #ccc',     # Add a border at the top
    'text-align': 'center',         # Center-align the text
    'padding': '10px',              # Add some padding for spacing
    'background-color': '#302f2f',   # Set a background color
    'color':'white'
}

def get_footer(): 
    footer = html.Footer(
        children=[
            html.H5("Tout droits réservés   |   Issa M.  |   Lucie S."),
            html.P("© ESIEE Paris | Noisy-le-Grand, 93160 | Informatique et Applications"),
        ],
        style=footer_style,
    )
    return footer