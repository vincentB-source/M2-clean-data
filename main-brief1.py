import pandas as pd
import seaborn as sns

from os.path import join as join

import matplotlib.pyplot as plt

import numpy as npimport 
import missingno as msno


df_data = pd.read_csv(join('data','data-all-68482f115ac04033078508.csv'))

print ("Describe :")
print(df_data.describe())

print ("Info :")
print(df_data.info())


# heatmap pour les relaction entre les données manquantes
# voir png généré
#fig = msno.heatmap(df_data)
#fig_copy = fig.get_figure()
#fig_copy.savefig('plot.png', bbox_inches = 'tight')

# suppression doublons
df_filtered = df_data.drop_duplicates()

"""
#analyse des données avec sns
# histplot pour analyser les données
sns.histplot(df_filtered['loyer_mensuel'], kde=True)
plt.show()

# Boxplot pour détecter les outliers
sns.boxplot(x=df_filtered['age'])
plt.show()
sns.boxplot(x=df_filtered['taille'])
plt.show()
sns.boxplot(x=df_filtered['poids'])
plt.show()
sns.boxplot(x=df_filtered['historique_credits'])
plt.show()
sns.boxplot(x=df_filtered['risque_personnel'])
plt.show()
sns.boxplot(x=df_filtered['score_credit'])
plt.show()
sns.boxplot(x=df_filtered['loyer_mensuel'])
plt.show()
sns.boxplot(x=df_filtered['montant_pret'])
plt.show()

#on supprime les lignes avec 3 valeurs nulles ou plus.
df_filtered = df_filtered.dropna(thresh=17)

print(df_filtered['niveau_etude'].unique())
['master' 'bac' 'doctorat' 'aucun' 'bac+2']
print(df_filtered['situation_familiale'].unique())
['célibataire' 'divorcé' 'veuf' 'marié' nan]
print(df_filtered['sexe'].unique())
['H' 'F']
print(df_filtered['sport_licence'].unique())
['non' 'oui']
print(df_filtered['smoker'].unique())
['non' 'oui']
"""


# on séléctionne que les colonnes intéressantes
# on élimine nom prenom sexe nationalite_francaise score_credit (pas assez de données) historique_credit (pas assez de données)  date_creation_compte (possible de l'exploiter pour l'ancienneté ?)
df_filtered = df_filtered[['age', 'taille', 'poids', 'revenu_estime_mois', 'sport_licence', 'niveau_etude', 'region', 'smoker', 'revenu_estime_mois', 'situation_familiale', 'risque_personnel', 'loyer_mensuel', 'montant_pret']]

# Traitement des variables catégorielles 
df_filtered['niveau_etude'] = df_filtered['niveau_etude'].map({
    'aucun': 0,
    'bac': 1,
    'bac+2': 2,
    'master': 3,
    'doctorat': 4
})
df_filtered['smoker'] = df_filtered['smoker'].map({
    'non': 0,
    'oui': 1
})
df_filtered['sport_licence'] = df_filtered['sport_licence'].map({
    'non': 0,
    'oui': 1
})
df_filtered['situation_familiale'] = df_filtered['situation_familiale'].map({
    'divorcé': 0,
    'célibataire': 1,
    'veuf': 2,
    'marié': 3
})

# Filtrer les lignes où le poids est supérieur à 30
df_filtered = df_filtered[df_filtered['poids'] > 30]
# Filtrer les lignes où le loyer_mensuel est supérieur à 0
df_filtered = df_filtered[df_filtered['loyer_mensuel'] > 0]

# Remplacer les valeurs manquantes par 0
df_filtered['situation_familiale'] = df_filtered['situation_familiale'].fillna(0)

# Remplacer les valeurs manquantes par la moyenne de la colonne
df_filtered['revenu_estime_mois'] = df_filtered['revenu_estime_mois'].fillna(df_filtered['revenu_estime_mois'].mean())
# Remplacer les valeurs manquantes par la moyenne de la colonne
df_filtered['loyer_mensuel'] = df_filtered['loyer_mensuel'].fillna(df_filtered['loyer_mensuel'].mean())
# Remplacer les valeurs manquantes par la moyenne de la colonne
df_filtered['montant_pret'] = df_filtered['montant_pret'].fillna(df_filtered['montant_pret'].mean())


# Filtrer les outliers (par exemple, couper les loyer_mensuel à plus de 3 fois l'écart interquartile)
Q1 = df_filtered['loyer_mensuel'].quantile(0.25)
Q3 = df_filtered['loyer_mensuel'].quantile(0.75)
IQR = Q3 - Q1
df = df_filtered[(df_filtered['loyer_mensuel'] >= (Q1 - 1.5 * IQR)) & (df_filtered['loyer_mensuel'] <= (Q3 + 1.5 * IQR))]

print ("Describe :")
print(df_filtered.describe())

print ("Info :")
print(df_filtered.info())
