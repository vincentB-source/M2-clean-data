# Config env 

## env virtuel
python -m venv .venv
source .venv/bin/activate

## install package
pip freeze > requirements.txt
pip install -r requirements.txt

# lancement Module
## clean des données
python main.py

Avant nettoyage 
Describe :
                age        taille         poids  revenu_estime_mois  historique_credits  risque_personnel  score_credit  loyer_mensuel  montant_pret
count  10000.000000  10000.000000  10000.000000        10000.000000         4707.000000      10000.000000   4694.000000     7094.00000  10000.000000
mean      46.516500    170.003760     70.064080         2520.996200            2.543446          0.499094    573.495952     5175.89104   9149.762575
std       16.832845     10.006542     15.014911         1157.532502            1.691198          0.290107    159.140639     3750.61004  10785.937404
min       18.000000    119.200000     10.500000          500.000000            0.000000          0.000000    300.000000     -395.25000    500.000000
25%       32.000000    163.200000     59.800000         1683.000000            1.000000          0.240000    437.000000      985.76750    500.000000
50%       46.000000    170.100000     70.200000         2480.000000            3.000000          0.500000    574.000000     5000.00000   3600.605667
75%       61.000000    176.800000     80.300000         3304.000000            4.000000          0.750000    712.000000    10000.00000  16245.534725
max       75.000000    209.800000    145.200000         6826.000000            5.000000          1.000000    849.000000    10000.00000  53192.053509
Info :
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 9 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   age                 10000 non-null  int64  
 1   taille              10000 non-null  float64
 2   poids               10000 non-null  float64
 3   revenu_estime_mois  10000 non-null  int64  
 4   historique_credits  4707 non-null   float64
 5   risque_personnel    10000 non-null  float64
 6   score_credit        4694 non-null   float64
 7   loyer_mensuel       7094 non-null   float64
 8   montant_pret        10000 non-null  float64