# Config env 

## env virtuel
python -m venv .venv
source .venv/bin/activate

## install package
pip freeze > requirements.txt
pip install -r requirements.txt

# lancement Module
## clean des données sur le module brief 0
python main.py

## clean des données + clean ethique sur le module brief 0
python main-brief2.py

# Traitement du datasheet pour le brief 2

## Suppression des lignes en doublons

Il n'y avait pas de ligne en doublon

## Suppression de certaines colonnes

On élimine les colonnes nom et prenom qui ne servent pas pour la prédiction
On élimine les colonnes score_credit et historique_credit car elles n'ont pas assez de données
On élimine pour l'instant date_creation_compte (mais en se demandant qi il est possible de le l'exploiter pour l'ancienneté ?)

On élimine la colonne sexe car ce n'est pas éthique de la conserver pour cette prédiction (peut être pour le calcul de l'assurance ?)
On élimine la colonne nationalité_française car il n'est pas utile de la conserver pour cette prédiction (les documents sont vérifiés en agence)

## Traitement des variables catégorielles 

On associe des valeurs numériques à des catégories de réponses : niveau_etude, smoker, sport_licence & situation_familiale

## Traitement des données Nan
situation_familiale : si pas de données alors on met 1
revenu_estime_mois : on complète avec la moyenne
loyer_mensuel : on complète avec la moyenne
montant_pret : on complète avec la moyenne

# Filtrer les outliers 
Pour les loyer_mensuel on élimine ceux qui sont à plus de 3 fois l'écart interquartile