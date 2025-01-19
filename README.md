# Mini-projet - Analyse des séismes

# Guide d'utilisation

Afin d'ouvrir la visualisation du projet, une fois celui-ci téléchargé, vous pouvez exécuter la commande suivante :

```bash
python main.py
```

Si vous avez python 3, vous devrez plutôt utiliser `python3 main.py`.

Une fois le programme exécuté, la visualisation sera disponible en local. Le message suivant devrait s'afficher.

```bash
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'main'
 * Debug mode: on
 ```

Afin d'accéder à la visualisation, il faut donc aller à l'adresse locale http://127.0.0.1:8050/, sans arrêter le programme. En cas d'erreur, actualisez la page.

Une fois la visualisation ouverte, vous pouvez accéder aux représentations des données exploitées. Une barre de navigation permet d'accéder aux différentes pages : 

- `Accueil` permet de retourner à la première page.
- `Histogrammes` et `Cartes` permettent d'accéder aux représentations correspondantes.

# Représentation des données

Les données exploitées représentent les séismes dans le monde, avec leur date, magnitude, pays, s'ils ont déclenché ou non un tsunami, leur impact et nombre de morts.

Ces données sont représentées sous forme d'histogrammes et de cartes :

- un diagramme circulaire représentant la répartition des décès par pays

- un nuage de points représentant les décès par pays en fonction des différentes magnitudes

- un diagramme représentant le nombre de séismes/tsunamis en fonction des magnitudes

- un histogramme représentant le nombre de séismes/tsunamis par pays

- un histogramme représentant le cumul des décès en fonction de la magnitude des séismes

- une heatmap représentant les différentes zones plus ou moins impactées par les séismes

- une carte chlorophète des différents séismes dans le monde

# Guide de développeur

Le code est structuré en 3 dossiers. La classe main permet de lancer la visualisation, récupérer les données et l'initialisation des différentes pages.

- Le dossier `utils` contient les classes permettant de récupérer les données sur les séismes, et de les nettoyer pour ne garder que celles que l'on souhaite exploiter, dans un format simple à utiliser pour ce projet.

- Le dossier `pages` permet la présentation des visualisations dans chaque page (accueil, histogrames, cartes et à propos). Ce code peut être facilement modifié afin de changer la mise en page des visualisations, d'en rajouter ou retirer, via les fonctions d'initilisation de chaque classe.

- Le dossier `components` contient les classes de chaque éléments des différentes pages, dont la barre de navigation, les hauts et bas de page, et les différents composants et représentations de données. Cette partie de code peut également facilement être modifiée afin de modifier, retirer ou rajouter des représentations de données en modifiant les paramètres de celles-ci.

# Rapport d'analyse



# Copyright

Nous déclarons sur l'honneur que code fourni a été intégralement produit par nos soins.

Projet développé par Issa MAHAMAT et Lucie SOUIOU.