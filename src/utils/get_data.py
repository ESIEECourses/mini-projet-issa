import requests

def get_csv():
    """
    Telechargement du jeu de données via un lien et stockage du jeu de données
    dans le dossier data/raw.

    Args :
        Aucun
    """

    link = "https://drive.google.com/uc?export=download&id=1Wiy5411pH-m9aX5nAZzXDXwQhreINqja"   # Lien pour le téléchargement du jeu de données
    file_path = "./data/raw/earthquake.csv"                                                 # Chemin relatif pour déposer le jeu de données
    
    response = requests.get(link)
    
    with open(file_path, "wb") as file :
        file.write(response.content)
    

