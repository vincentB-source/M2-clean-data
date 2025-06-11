import pandas as pd
import seaborn as sns

from os.path import join as join

import matplotlib.pyplot as plt

import numpy as npimport 
import missingno as msno


df_data = pd.read_csv(join('data','data_numeric_only.csv'))

print ("Describe :")
print(df_data.describe())

print ("Info :")
print(df_data.info())


# heatmap pour les relaction entre les données manquantes
# voir png généré
fig = msno.matrix(df_data)
fig_copy = fig.get_figure()
fig_copy.savefig('plot.png', bbox_inches = 'tight')

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
"""

#on supprime les lignes avec 3 valeurs nulles ou plus. On tombe a 9272 
# Pour info, si on met avec 2 ou plus on tombe à 5839
df_filtered = df_filtered.dropna(thresh=7)

# on séléctionne que les colonnes intéressantes
df_filtered = df_filtered[['age', 'taille', 'poids', 'revenu_estime_mois', 'risque_personnel', 'loyer_mensuel', 'montant_pret']]

# Filtrer les lignes où le poids est supérieur à 30
df_filtered = df_filtered[df_filtered['poids'] > 30]
# Filtrer les lignes où le loyer_mensuel est supérieur à 0
df_filtered = df_filtered[df_filtered['loyer_mensuel'] > 0]


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