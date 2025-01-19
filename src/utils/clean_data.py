import csv
import pandas as pd

def retirerColonnesEtNettoyer():

    """
    Retire les colonnes indésirables et applique un nettoyage spécifiques aux données, 
    puis écrit les données nettoyées dans un nouveau fichier.

    Args:
        input_file (str): Chemin du fichier CSV d'entrée.
        output_file (str): Chemin du fichier CSV de sortie.
        colonnes_a_retirer (list): Liste des colonnes à retirer.
    """

    input_file = './data/raw/earthquake.csv'
    output_file = './data/cleaned/earthquake-cleaned.csv'
    colonnes_a_retirer = ['Focal Depth', 'Mw Magnitude','Mb Magnitude', 'Mi Magnitude', 'MFA Magnitude','State', 'Unknown Magnitude', 'Region code', 'Intensity','EQ Primary'
                        ,'Earthquake : Missing','Earthquake : Missing Description','Earthquake : Injuries','Earthquake : Injuries Description','Earthquake : Damage Description',
                        'Earthquakes : Houses destroyed','Earthquakes : Houses destroyed Description','Earthquakes : Houses damaged','Earthquakes : Houses damaged Description',
                        'Total Effects : Deaths','Total Effects : Deaths Description','Total Effects : Missing','Total Effects : Missing Description','Total Effects : Injuries',
                        'Total Effects : Injuries Description','Total Effects : Damages in million Dollars','Total Effects : Damage Description','Total Effects : Houses Destroyed',
                        'Total Effects : Houses Destroyed Description','Total Effects : Houses Damaged','Total Effects : Houses Damaged Description']  # Colonnes à retirer

    data = pd.read_csv(input_file, delimiter=';')

    data = data.drop(columns=colonnes_a_retirer, errors='ignore')

    for column in data.columns:
        if data[column].dtype in ["float64", "int64"]:
            data[column] = data[column].fillna(0)

    if 'Flag Tsunami' in data.columns:
        data['Flag Tsunami'] = data['Flag Tsunami'].apply(
            lambda x: 'Yes' if x == 'Tsunami' else 'No'
        )

    if 'Earthquake : Deaths Description' in data.columns:
        data['Earthquake : Deaths Description'] = data['Earthquake : Deaths Description'].fillna("No deaths reported")
        
    if 'Ms Magnitude' in data.columns:
        data = data[data['Ms Magnitude'] > 0.0]

    data.to_csv(output_file, index=False, sep=';')

# Appel de la fonction


retirerColonnesEtNettoyer()

