import csv
import pandas as pd

"""
Code de replication de CSV 


def retirerColonnes(input_file, output_file, colonnes_a_retirer):
    
    Retire les colonnes indésirables pour continuer
    avec les colonnes souhaitees
    
    # Lire le fichier d'entrée
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile, delimiter=';')  # Préciser le délimiteur (;)
        
        # Créer une nouvelle liste d'en-têtes sans les colonnes à retirer
        nouvelles_colonnes = [col for col in reader.fieldnames if col not in colonnes_a_retirer]
        
        # Écrire dans un nouveau fichier CSV
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=nouvelles_colonnes, delimiter=';')
            writer.writeheader()  # Écrire les en-têtes
            
            
            # Écrire chaque ligne sans les colonnes à retirer
            for row in reader:
                if row['Month'] and row['Day']:
                    nouvelle_ligne = {col: row[col] for col in nouvelles_colonnes}
                    writer.writerow(nouvelle_ligne)
                

    print("Nettoyage terminé. \n")

# Appel de la fonction
input_file = '../../data/raw/earthquake.csv'
output_file = '../../data/raw/earthquake-data.csv'
colonnes_a_retirer = ['Focal Depth', 'Mw Magnitude','Mb Magnitude', 'Mi Magnitude', 'MFA Magnitude','State', 'Unknown Magnitude', 'Region code', 'Intensity','EQ Primary'
                      ,'Earthquake : Missing','Earthquake : Missing Description','Earthquake : Injuries','Earthquake : Injuries Description','Earthquake : Damage Description','Earthquakes : Houses destroyed','Earthquakes : Houses destroyed Description','Earthquakes : Houses damaged','Earthquakes : Houses damaged Description','Total Effects : Deaths','Total Effects : Deaths Description','Total Effects : Missing','Total Effects : Missing Description','Total Effects : Injuries','Total Effects : Injuries Description','Total Effects : Damages in million Dollars','Total Effects : Damage Description','Total Effects : Houses Destroyed','Total Effects : Houses Destroyed Description','Total Effects : Houses Damaged','Total Effects : Houses Damaged Description']  # Colonnes à retirer

retirerColonnes(input_file, output_file, colonnes_a_retirer)
"""

def cleanRows():
    """
    Args : aucun
    Remplacement des valeurs non numériques dans les différentes colonnes

    """
    monCsv = '../../data/raw/earthquake-data.csv'
    data = pd.read_csv(monCsv, delimiter=';')
    for column in data.columns:
        if data[column].dtype == "float64" or data[column].dtype == "int64":
            data[column].fillna(0, inplace=True)


    data['Flag Tsunami'] = data['Flag Tsunami'].apply(lambda x: 'Tsunami' if x == 'Tsunami' else 'No')    # Si la colonne est en NaN on remplace par "No" 

    data['Earthquake : Deaths Description'].fillna("No deaths reported", inplace=True)   # Remplace les NaN par une information

    for column in data.columns:
        print(data[column])


def initialiseData():
    monCsv = '../../data/raw/earthquake-data.csv'
    data = pd.read_csv(monCsv, delimiter=';')
    print(data.head())
    with open(monCsv, 'r') as eq:
        c = csv.DictReader(eq, delimiter=';')
        return c
initialiseData()
cleanRows()
