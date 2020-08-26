#!/usr/bin/env python
# coding: utf-8

# # <font color="red"><center>OPENCLASSROOMS - PROJET 4</font>
# # <font color="red"><center>ANALYSEZ LES VENTES DE VOTRE ENTREPRISE</font>
# -----------------
# -----------------
# ## <center>Sommaire
# ###### <center>Un code de couleur à été attribué aux différentes missions à titre de repère
# -----------------
# ### <font color="darkblue">Mission 1: Base de données - Préparatifs
# #### <font color="mediumblue">I.Nettoyage des données
# - <font color="royalblue">I.1.Customers    
# - <font color="royalblue">I.2.Products    
# - <font color="royalblue">I.3.Transactions
# 
# #### <font color="mediumblue">II.Finalisation du support
# - <font color="royalblue">II.1.Jointure des trois tableaux de base
# - <font color="royalblue">II.2.Agrégations sur les mois
# - <font color="royalblue">II.3.Variables supplémentaires
# 
# -----------------
# ### <font color="darkorange">Mission 2: Analyses Graphiques
# #### <font color="goldenrod">I.Étude du chiffre d'affaires
# - <font color="peru">I.1.Évolution globale du chiffre d'affaires
# - <font color="peru">I.2.Évolution mensuelle du chiffre d'affaires
# - <font color="peru">I.3.Observation du mois d'Octobre
# - <font color="peru">I.4.Catégories de livres par nombre de ventes et par chiffre d'affaires
# - <font color="peru">I.5.Catégories de livres: Mesures de tendance centrale
#     
# #### <font color="goldenrod">II.Statistiques de la clientèle
# - <font color="peru">I.1.Étude des âges
# - <font color="peru">I.2.Étude des genres
# - <font color="peru">I.3.Répartition du chiffre d'affaires par client, courbe de Lorenz et indice de Gini
# - <font color="peru">I.4.Proportions de clients actifs/inactifs
#     
# #### <font color="goldenrod">III.Statistiques des sessions d'achats
# - <font color="peru">III.1.Montants des sessions
# - <font color="peru">III.2.Taille du panier moyen
# - <font color="peru">III.3.Répartition du panier moyen
#     
# #### <font color="goldenrod">IV.Analyses des ventes et des prix
# - <font color="peru">IV.1.Bilan des prix
# - <font color="peru">IV.2.Vendus et invendus
# - <font color="peru">IV.3.Prix des invendus
#     
#  
# -----------------
# ### <font color="firebrick">Mission 3: Étude des Corrélations
# #### <font color="crimson">I.Préparatifs et optimisations pour les analyses
# - <font color="brown">I.1.Fonctions utilitaires
# - <font color="brown">I.2.Tableaux de support et suppression des Outliers
#     
# #### <font color="crimson">II.Sexe des clients et catégories de produits achetés
# - <font color="brown">II.1.Tableau de contingence réel
# - <font color="brown">II.2.Tableau de contingence théorique
# - <font color="brown">II.3.Tableau de contingence coloré
# 
# 
# #### <font color="crimson">III.On verra
# - <font color="crimson">III.1.
# - <font color="crimson">III.2.
# -----------------
# -----------------
# ### Nous importons dans un premier temps l'ensembles de librairies nécessaires pour l'ensemble du projets.

# In[67]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pylab import arange, plot
from matplotlib.pyplot import figure

import datetime as dt

import scipy.stats as st
import statsmodels.api as sm
import statsmodels.formula.api as smf

import warnings
warnings.filterwarnings('ignore')


# -------------------------------
# -------------------------------
# -------------------------------
# -------------------------------
# -------------------------------

# # <font color="darkblue"><center>Mission 1: Base de données - Préparatifs</font>
# -----------------

# # <font color="mediumblue">I. Nettoyage des données

# ## <font color="royalblue">I.1. Customers

# <font color="midnightblue">Ce premier DataFrame nous renvoie la liste des clients qui ont effectué des achats dans l'année, caractérisés par leur identifiant client, leur sexe et leur année de naissance.

# In[17]:


customers = pd.read_csv("data/projet_4/base/customers.csv")
customers.head(5)


# <font color="midnightblue">Pour ce premier DataFrame, nous remplacerons l'année de naissance des clients par leur âge, puis nous retirerons de la clist les clients 'test'.

# In[18]:


customers["age"]=2022-customers.birth
customers=customers.drop(columns=["birth"])

customers=customers.loc[(customers["client_id"].isin(["ct_0", "ct_1"]))==False]

customers


# ## <font color="royalblue">I.2. Products

# <font color="midnightblue">Ce deuxième DataFrame nous renvoie la liste des produits (livres) achetés au cours de l'année, indexés par leur identifiant de produit, leur prix, et la catégorie (0, 1 ou 2) auxquelles ils appartiennent.

# In[19]:


products = pd.read_csv("data/projet_4/base/products.csv")
products.head(4)


# <font color="midnightblue">Repérons la petite valeur aberrante suivante: un des prix est négatif! Il s'agit d'un produit test. Nous allons donc l'enlever.

# In[20]:


products[products.price<0]


# In[21]:


products=products.loc[products["price"] > 0 ].reset_index(drop=True)
products


# ## <font color="royalblue">I.3. Transactions

# <font color="midnightblue">Enfin, il nous reste la liste des transactions effectuées au cours de l'année, où l'on peut notamment y repérer quel client a acheté tel ou tel livre.

# In[22]:


transactions = pd.read_csv("data/projet_4/base/transactions.csv")
transactions.head(2)


# <font color="midnightblue">Dans la cellule suivante, nous allons:
# - <font color="midnightblue"> Retirer les clients test.
# - <font color="midnightblue"> Nous débarasser des microsecondes (on y verra plus clair!)
# - <font color="midnightblue"> Faire un "split" de la date et de l'heure dans le cadre des analyses de la mission 2.

# In[201]:


#Retrait des clients test:
transactions=transactions.loc[(transactions.client_id!='ct_0')&(transactions.client_id!='ct_1')]

#Bon débarras des microsecondes:
D=[]
for date in transactions["date"]:
    date_claire=date.split(".")[0]
    D.append(date_claire)   
transactions["date"]=D

#On renomme la colonne "date" en "date_et_heure" et on la convertit en datetime:
transactions.rename(columns={"date": "date_et_heure"}, inplace=True)
transactions["date_et_heure"]=pd.to_datetime(transactions["date_et_heure"])


#La conversion de date_et_heure en datetime nous permet d'appliquer les fonctions date() et time() sur cette variable qui nous
#renvoient respectivement la date et l'heure:
DATES, HEURES = [], []
for dh in transactions["date_et_heure"]:
    DATES.append(dh.date())
    HEURES.append(dh.time())

#Séparation de "date_et_heure" et suppression de cette dernière:
transactions["date"]=DATES
transactions["heure"]=HEURES
transactions=transactions.drop(columns="date_et_heure")

transactions


# <font color="midnightblue">Enfin, vérifions s'il existe un produit présent dans "transactions" mais absent dans "products".

# In[202]:


is_absent=transactions[transactions.id_prod.isin(products.id_prod)==False]["id_prod"].unique()[0]
is_absent


# <font color="midnightblue">Ne vous en faites pas, nous allons régler ça dans la partie suivante.

# ------------------

# # <font color="mediumblue">II. Finalisation du support

# ## <font color="royalblue">II.1. Jointure des trois tableaux de base

# <font color="midnightblue">Nous créons maintenant le DataFrame "table", qui regroupera les trois DataFrames précédents traités et nettoyés. D'abord, on fait la jointure externe - afin de récupérer l'élément manquant dans products - de products et de transactions.

# In[203]:


table = pd.merge(products, transactions, on='id_prod', how='outer')
table


# <font color="midnightblue">Avant d'ajouter les clients, traîtons les valeurs manquantes, jusque là:
# - La colonne "categ", indique la catégorie de livres - 0, 1 ou 2 - qui se trouve être le premier chiffre de son identifiant produit "id_prod".
# - La colonne "price" présente une valeur nulle les livres 0_2245. Après analyse des mesures de tendance centrale, on fixera ce prix à 9,99 euros.

# In[204]:


#Fonction permettant de récupérer le premier chiffre d'un identifiant de produit dans nos données:
def get_categ(car):
    return  int(car.split("_")[0])

#Complétude de "categ":
table["categ"]=table.id_prod.apply(get_categ)

#Ajout du prix du livre 0_2245:
table["price"].fillna(9.99, inplace=True)

table.tail(3)


# <font color="midnightblue">On peut maintenant ajouter les données de "customers" à notre DataFrame par jointure interne et on le réindexe notre table selon les dates.

# In[205]:


table=pd.merge(table, customers)

table.sort_values(by="date", inplace=True)
table=table.reset_index(drop=True)

table


# <font color="midnightblue">Nous allons maintenant finaliser notre base de données, mais avant ça, quelques agrégations sur les mois de l'année s'imposent...

# ## <font color="royalblue">II.2. Agrégations sur les mois

# <font color="midnightblue">Dans le cadre des analyses graphiques à réaliser pour la mission 2, il sera intéressant d'étudier certaines variables selon les mois de l'année. Rappelons que notre étude futuriste s'étend de mars 2021 à février 2022. Le DataFrame suivant nous donne donc la liste des 12 mois de l'année, leur numéro de mois et leur "chronologie" dans notre étude (afin de pouvoir les classer en cas de besoin).

# In[9]:


calendar=pd.DataFrame({"nom_mois": ["janvier", "fevrier", "mars", "avril", "mai", "juin",
                                    "juillet", "août", "septembre", "octobre", "novembre", "decembre"],
                       "numero_mois": range(1, 13),
                       "chronologie": [22.01, 22.02, 21.03, 21.04, 21.05, 21.06, 
                                        21.07, 21.08, 21.09, 21.10, 21.11, 21.12]})
calendar


# <font color="midnightblue">Et ici, les fonctions qui nous permettront de passer facilement du nom du mois à son numéro, vice et versa, et éventuellement à leur chronologie.

# In[10]:


#Pour passer, par exemple, de "juillet" à 7:
def nom_mois(a):
    for i in calendar.index:
        if a==calendar.numero_mois[i]:
            return(str(calendar.nom_mois[i]))

#Pour passer, par exemple, de 4 à "avril":        
def nombre_mois(car):
    for i in calendar.index:
        if car==calendar.nom_mois[i]:
            return(float(calendar.numero_mois[i]))
        
def chronologie(car):
    for i in calendar.index:
        if car==calendar.nom_mois[i]:
            return(calendar.chronologie[i])


# ## <font color="royalblue">II.3. Variables supplémentaires

# <font color="midnightblue">Notons qu'une "session" est un groupe d'achats. Ce serait donc intéressant de savoir, combien de livres ont été achetés à chaque session. On crée donc la variable "basket_size" qui nous donnera cette indication.

# In[208]:


table["basket_size"]=table["session_id"].value_counts()[table["session_id"]].tolist()
table.head(3)


# <font color="midnightblue">Enfin, en vue des analyses graphiques que nous ferons, avoir le mois en vigueur rendra notre codage bien plus propre.

# In[209]:


#On reconverti la date en datetime:
table["date"]=pd.to_datetime(table["date"])

#On ajoute la colonne "mois" grâce à nos fonctions:
table["mois"]=table["date"].dt.month.apply(nom_mois)

#Et le jour du mois, ce sera utile:
table["jour"]=table["date"].dt.day

table


# <font color="midnightblue">On finit cette première mission en réorganisant notre DataFrame histoire d'y voir plus clair et on est parti pour la mission 2!

# In[210]:


#On réindexe notre support pour y voir plus clair:
table=table.reindex(columns=["id_prod", "categ", "price", 
                             "client_id", "sex", "age",
                             "session_id", "basket_size",
                             "date", "mois", "jour", "heure"])
table


# In[68]:


table=pd.read_csv("data/projet_4/reboot.csv")
table["date"]=pd.to_datetime(table["date"])
table


# ----------------------
# ----------------------
# ----------------------
# ----------------------

# # <font color="peru"><center>Mission 2: Analyses Graphiques
# -----------------

# # <font color="darkorange"> _Prémice - Agrégats & Fonctions Utilitaires_

# <font color="saddlebrown">Dans cette deuxième partie, nous allons effectuer diverses observations graphiques sur les ventes effectuées de mars 2021 à février 2022. Pour simplifier le codage, nous définissons ci-dessous quelques définitions et fonctions usuelles que nous utiliserons tout au long de la mission.

# In[69]:


def couleur(c):
    if c==0: return("steelblue") # Ce sera notre couleur de repère pour la catégorie 0.
    elif c==1: return("crimson") # Ce sera notre couleur de repère pour la catégorie 1.
    else: return("goldenrod") # Ce sera notre couleur de repère pour la catégorie 2.
    
palette=[couleur(c) for c in range(3)] # Notre palette de couleurs pour les 3 catégories.

categories_3=["Catégorie %d" %i for i in range(3)] # Nous servira à nommer les labels.

# On effectuera plusieurs études individuelles sur les ventes de chaque catégorie de livres:
categ_0=table.loc[table["categ"]==0]
categ_1=table.loc[table["categ"]==1]
categ_2=table.loc[table["categ"]==2]

# Une fonction pour effectuer facilement un groupby sur table:
def groupby_var(data, var):
    return(pd.DataFrame(data.groupby(var).sum()["price"]).reset_index())

# Une fonction qui réordonne chronologiquement (de mars à février) nos données:
def periode(data):
    data["chronologie"]=data["mois"].apply(chronologie)
    data=data.sort_values(by="chronologie")
    data.drop(columns="chronologie", inplace=True)
    return(data)

#On définit ici les paramètres des boxplots pour toute la suite de la mission:
medianprops = {'color':"black"}
meanprops = {'marker':'o', 'markeredgecolor':'black',
            'markerfacecolor':'firebrick'}


# <font color="saddlebrown">Nous nous baserons avant tout sur le DataFrame "table" établi lors de la  mission 1.

# In[70]:


table


# <font color="saddlebrown">Dans la partie II, nous réutiliserons le DataFrame "customers" introduit au début de la mission 1, où nous y ajoutons la colonne "is_active" qui renvoie "ACTIF" si le client en question a effectué au moins un achat au cours de la période étudiée (mars 2021 - février 2022), "INACTIF" sinon.

# In[71]:


def active(car):
    if car==True:
        return("ACTIF")
    else: return("INACTIF")
    
customers["is_active"]=customers["client_id"].isin(table.client_id).apply(active)
customers


# <font color="saddlebrown">Lors de la partie III, nous étudierons les sessions d'achats. On crée donc le DataFrame "sessions" qui regroupe les montants totaux de chaque session d'achat effectuée sur le site en cours d'année.

# In[72]:


sessions = pd.DataFrame(table.groupby(["session_id", "client_id", "age", "date", "mois", "jour"])
                        .sum()["price"]).reset_index()
sessions.rename(columns={"price": "montant_session"}, inplace=True)
effectifs = pd.DataFrame(table.session_id.value_counts().reset_index())
effectifs.columns=("session_id", "taille_panier")
sessions=pd.merge(sessions, effectifs)

sessions


# ----------------

# # <font color="darkorange">I. Étude du chiffre d'affaires

# ## <font color="goldenrod">I.1. Évolution globale du chiffre d'affaires

# <font color="saddlebrown">Observons dans un premier temps l'évolution du chiffre d'affaires de Mars 2021 à Février 2022.

# In[73]:


plt.figure(figsize=(12, 5))

table_gb_date = groupby_var(table, "date")

plt.plot(table_gb_date["date"], table_gb_date["price"], color="seagreen",
         label="Chiffre d'affaires", linewidth=1)

plt.title("Évolution du chiffre d'affaires au cours de l'année", fontsize=20)
plt.xlabel("")
plt.ylabel("Chiffre d'affaires en euros", fontsize=14)
plt.show()


# <font color="saddlebrown">On a une première approche de l'évolution du chiffre d'affaires global. On y observe une tendance à la hausse de cette évolution le long de l'année, progression interrompue entre les mois de septembre et novembre avec une forte chute du CA, avant une reprise normale de cette évolution dès novembre. Avant de continuer, distribuons cette courbe pour chaque catégorie de livres.

# In[74]:


figure(num=None, figsize=(12, 5), dpi=80)

for i in range(3):
    cat=groupby_var(table.loc[table["categ"]==i], "date")
    color=couleur(i)
    plt.plot(cat["date"], cat["price"], color=color, linewidth=1, label= "Catégorie %d" %i)

plt.title("Évolution du chiffre d'affaires au cours de l'année", fontsize=20)
plt.xlabel("")
plt.ylabel("Chiffre d'affaires", fontsize=14)

plt.legend()
plt.show()


# <font color="saddlebrown">On observe une rentabilité globale moins élevée pour la catégorie 2. Mais remarquons surtout la chute du chiffre d'affaires des trois catégories de livres vers novembre. Essayons de voir ça de plus près en regroupant ces analyses par mois.

# ## <font color="goldenrod">I.2. Évolution mensuelle du chiffre d'affaires

# <font color="saddlebrown">On voit une chute entre les mois d'août et novembre sur le graphique précédent. Regardons ça de plus près avec une analyse mensuelle.

# In[75]:


plt.figure(figsize=(7, 5))

emca = groupby_var(table, "mois")
emca["chronologie"]=emca["mois"].apply(chronologie)
emca=emca.sort_values(by="chronologie")

plt.bar(emca["mois"], emca["price"], color="seagreen")

plt.title("Évolution mensuelle du chiffre d'affaires", fontsize=15)
plt.xlabel("")
plt.ylabel("Chiffre d'affaires")
plt.xticks(rotation=45)
plt.show()


# <font color="saddlebrown">C'est ici qu'on repère la chute drastique du CA au mois d'octobre. Cela fera l'objet de notre prochaine partie. Tout d'abord, il serait intéressant d'analyser cet histogramme selon les 3 catégorie de livre.

# In[76]:


plt.figure(figsize=(7, 5))

eca=periode(table.pivot_table(index="mois",
                              columns="categ",
                              values="price",
                              aggfunc=sum).reset_index())
eca.columns=["mois", "categ_0", "categ_1", "categ_2"]

plt.bar(eca.mois, eca.categ_0+eca.categ_1+eca.categ_2, color=couleur(2), label="Catégorie 2")
plt.bar(eca.mois, eca.categ_0+eca.categ_1, color=couleur(1), label="Catégorie 1")
plt.bar(eca.mois, eca.categ_0, color=couleur(0), label="Catégorie 0")

plt.title("Chiffre d'affaires par catégorie de livres", fontsize=15)
plt.xlabel("")
plt.xticks(rotation = 'vertical')
plt.ylabel("Chiffre d'affaires")
plt.legend(loc="lower left")
plt.show()


# <font color="saddlebrown">On voit alors que c'est la catégorie 1 qui est la cause de la chute drastique du mois d'octobre.

# ## <font color="goldenrod">I.3. Observation du mois d'Octobre

# <font color="saddlebrown">Observons les ventes des livres au cours  du mois d'octobre.

# In[77]:


plt.figure(figsize=(12, 3))

octobre=table[table.mois=="octobre"].pivot_table(index=["date"],
                                                 columns=["categ"],
                                                 values=["price"],
                                                 aggfunc=sum).reset_index().fillna(0)
octobre.columns=["date", "categorie 0", "categorie 1", "categorie 2"]

for i in range(3):
    catego="categorie %d" %i
    plot(octobre["date"], octobre[catego], color=couleur(i), label=catego)
plt.title("Évolution du chiffre d'affaires au cours du mois d'Octobre", fontsize=10)
plt.xlabel("")
plt.ylabel("Chiffre d'affaires", fontsize=4)
plt.legend()
plt.show()


# <font color="saddlebrown">Effectivement, nous n'avons enregistré aucune vente entre le 2 et le 28 octobre inclus. Pourquoi? Faudra demander à la compta.

# ## <font color="goldenrod">I.4. Catégories de livres par nombre de ventes et par chiffre d'affaires

# <font color="saddlebrown">Nous allons tracer deux camemberts. Ils les parts des ventes selon les 3 catégories de livres, le premier selon le chiffre d'affaires, le deuxième selon les effectifs vendus.

# In[78]:


plt.figure(figsize=(10, 10))
plt.figure(1)

plt.subplot(2, 2, 1)
groupby_var(table, "categ")["price"].plot(kind="pie", colors=palette, labels=categories_3,
                                          autopct=lambda x: str(round(x, 2))+"%", shadow=True)
plt.title("Parts du chiffre d'affaires par catégorie de livre", fontsize=12)

plt.subplot(2, 2, 2)
table["categ"].value_counts(normalize=True).plot(kind="pie", colors=palette, labels=categories_3,
                                                 autopct=lambda x: str(round(x, 2))+"%")
plt.title("Parts des ventes par catégorie de livre", fontsize=12)

plt.show()


# <font color="saddlebrown">Comparaisons des deux diagrammes  circulaires:
# - Les livres de la catégorie 0 sont ceux qui se vendent en plus grandes quantités mais ne représentent pas la plus grande part du chiffre d'affaires.
# - Les livres de la catégorie 1 font la majeure partie du chiffre d'affaires, mais se vendent moins que la catégorie 0.
# - Les livres de la catégorie 2 sont ceux qui se vendent le moins et participent le moins au chiffre d'affaires. Néanmoins, la comparaison entre le taux de ventes et la participation au chiffre d'affaires laisse supposer que ce sont globalement les livres les plus chers dans notre inventaire.

# ## <font color="goldenrod">I.5. Catégories de livres: Mesures de tendance centrale

# <font color="saddlebrown">Analysons les mesures de tendance centrales des recettes des trois catégories de livres dans des boîtes à moustaches.

# In[79]:


categories = table["categ"].unique()
categ_ca = []

for i in categories:
    categ_ca.append(table[table["categ"]==i]["price"])
    
plt.boxplot(categ_ca, labels=categories, showfliers=False, medianprops=medianprops, 
            vert=False, patch_artist=True, showmeans=True, meanprops=meanprops)

plt.title("Chiffre d'affaires moyen par catégorie", fontsize=15)
plt.xlabel("Chiffre d'affaires moyen", fontsize=12)
plt.ylabel("", fontsize=15)
plt.yticks(fontsize=15)
plt.show()


# <font color="saddlebrown">On constate alors que les prix sont beaucoup plus élevés pour les livres de la catégorie 2. La catégorie 1 propose également des prix plus importants que ceux de la catégorie 0. Il semblerait qu'il y ait une corrélation entre les prix et les catégories de livres.

# ----------

# # <font color="darkorange">II. Statistiques de la clientèle

# ## <font color="goldenrod">II.2. Étude des âges

# <font color="saddlebrown">Tout d'abord, analysons les fréquences d'âge de nos clients.

# In[80]:


plt.figure(figsize=(14, 5))
plt.hist(customers["age"], density=True, width=0.5, bins=150, color="firebrick")
plt.title("Fréquences d'âge de nos clients")
plt.xlabel("âges")
plt.ylabel("fréquences")
plt.show()


# <font color="saddlebrown">La fréquence d'âge la plus forte chez nos clients est 18 ans. Les retraités se sentent de moins en moins concernés par nos produits. 50% de nos clients ont entre 30 et 55 ans. 25% ont moins de 30 ans et 25% ont plus de 55 ans.

# ## <font color="goldenrod">II.2. Étude des genres

# <font color="saddlebrown">Regardons maintenant les fréquences des genres de notre clientèle.

# In[81]:


customers["sex"].value_counts().plot(kind="pie", colors=["deeppink", "royalblue"], labels=["Femmes", "Hommes"],
                                     autopct=lambda x: str(round(x, 2))+"%", shadow=True)
plt.ylabel("")
plt.show()


# <font color="saddlebrown">Regardons ces fréquences de genre par catégorie de livres.

# In[82]:


plt.figure(figsize=(15, 15))
plt.figure(1)

for i in table.categ.unique():
    
    clients_i = pd.DataFrame(table.loc[table.categ==i].groupby(["client_id", "sex"]).sum()["price"]).reset_index()
    clients_i.rename(columns={"price": "depenses"}, inplace=True)
    nb_achats_i = pd.DataFrame(table.loc[table.categ==i].client_id.value_counts()).reset_index()
    nb_achats_i.columns=["client_id", "nombre_livres_achetes"]
    clients_i=pd.merge(clients_i, nb_achats_i)
    
    plt.subplot(1, 3, i+1)
    clients_i["sex"].value_counts(normalize=True).plot(kind='pie', colors=["deeppink", "royalblue"], 
                                                       labels=["Femmes", "Hommes"], autopct=lambda x: str(round(x, 2))+"%")
    plt.title("Catégorie %s" %i)
    plt.ylabel("")
    
plt.show()


# <font color="saddlebrown">On peut admettre a priori que le genre du client ne conditionne pas la catégorie de livres à laquelle il/elle va s'intéresser.

# ## <font color="goldenrod">II.3. Répartition du chiffre d'affaires par client, courbe de Lorenz et indice de Gini

# <font color="saddlebrown">Nous allons étudier la répartition des fréquences d'achats selon les âges de nos clients.

# In[83]:


plt.figure(figsize=(5, 5))

clients=pd.DataFrame(table.groupby("client_id").sum()["price"]).sort_values("price")

depenses = clients.price.values
n = len(depenses)

lorenz = np.append([0], np.cumsum(depenses)/sum(depenses))
gini=2*(0.5-lorenz.sum()/n)
plt.axes().axis("equal")

plt.plot(np.linspace(0-1/n, 1+1/n, n+1), lorenz)
plt.title("Courbe de Lorenz - Gini=%s" %(round(gini, 2)), fontsize=15)

X = arange(0,1,0.01)
Y=X
plot(X, Y)
plt.show()


# <font color="saddlebrown">On observe alors sur la courbe de  Lorenz, avec un indice de Gini proche de  0,5 que la répartition du CA par client n'est pas égalitaire. 

# ## <font color="goldenrod">II.4. Proportions de clients actifs/inactifs

# <font color="saddlebrown">Il existe des clients enregistrés sur le site qui n'ont effectué aucun achat. On appelle "client actif" un client qui a effectué au moins un achat sur la période étudiée, "inactif" sinon.

# In[84]:


customers["is_active"]=customers["client_id"].isin(table.client_id)
customers["is_active"].value_counts(normalize=True).plot(kind="pie", 
                                                         colors=["deepskyblue", "red"],
                                                         autopct=lambda x: str(round(x, 2))+"%")
plt.ylabel("")
plt.show()


# <font color="saddlebrown">Donc un peu moins d'un client sur 400 s'enregistre mais n'effectue aucun achat.

# -----------

# # <font color="darkorange">III. Statistiques des sessions d'achats

# ## <font color="goldenrod">III.1. Montants des sessions

# <font color="saddlebrown">Voyons comment a évolué la dépense moyenne des clients tout au long de l'année.

# In[85]:


plt.figure(figsize=(15, 5))
year =  pd.DataFrame(sessions.groupby(["date"]).mean()["montant_session"]).reset_index()

plot(year.date, year.montant_session, color="green")

plt.xlabel("dates")
plt.ylabel("moyenne des montants de session")
plt.show()


# <font color="saddlebrown">On retrouve bien la même évolution que celle du chiffre d'affaires étudié en première partie. Observons maintenant cette évolution sur un mois, en prenant la moyenne de ce montant pour chaque jour de chaque mois observé,
# en retirant le mois d'octobre en dépit de l'anomalie observé en première partie pour ne pas fausser les résultats.

# In[86]:


plt.figure(figsize=(15, 5))

mois =  pd.DataFrame(sessions.loc[sessions.mois!="octobre"].groupby(["jour"]).mean()["montant_session"]).reset_index()

plot(mois.jour, mois.montant_session, color="navy")
plt.xlabel("jours du mois")
plt.ylabel("moyenne des montants de session")
plt.show()


# <font color="saddlebrown">On observe en moyenne une tendance à la hausse au fil du mois. On peut  donc supposer que les clients effectuent généralement de plus gros  achats en  fin de mois. On repère ici les jours où les boosts de publicité à faire améliorerait nos ventes.

# ## <font color="goldenrod">III.2. Taille moyenne du panier

# <font color="saddlebrown">Une session d'achats regroupe parfois l'achat de plusieurs livres en même temps. On analyse ici la taille des paniers des transactions effectuées.

# In[87]:


plt.figure(figsize=(15, 5))

panier_moyen = pd.DataFrame(sessions.groupby("date").mean()["taille_panier"]).reset_index()

plot(panier_moyen.date, panier_moyen.taille_panier, color="darkorchid")
plt.xlabel("date")
plt.ylabel("taille moyenne du panier")
plt.show()


# <font color="saddlebrown">Il est intéressant de noter que tout au long de l'année, la taille moyenne du panier des clients atteint son maximum journalier fin septembre, juste avant  la chuste drastique du chiffre d'affaires au mois d'octobre. Analysons-le maintenant l'évolution de la taille moyenne du panier par mois.

# In[88]:


plt.figure(figsize=(7, 5))

panier_moyen_month = periode(pd.DataFrame(sessions.groupby("mois").mean()["taille_panier"]).reset_index())
panier_moyen_month = panier_moyen_month.set_index("mois")

panier_moyen_month["taille_panier"].plot.bar(color="plum")
plt.title("Chiffre d'affaires")
plt.xlabel("")
plt.ylabel("Euros")
plt.show()


# <font color="saddlebrown">Nous pouvons constater que le panier moyen est constant tous les mois, à peu de choses près. Le mois de septembre voit son panier moyen plus élevé que les autres, sans doute en vertue de la rentrée scolaire.

# ## <font color="goldenrod">III.3. Répartition du panier moyen

# <font color="saddlebrown">Regardons les fréquences de tailles des paniers.

# In[89]:


plt.figure(figsize=(7, 5))

sessions=sessions.sort_values("taille_panier")
sessions["taille_panier"].value_counts(normalize=True).plot(kind="bar", color="darkorange")
plt.xticks(rotation=0)
plt.show()


# <font color="saddlebrown">Une session cumule donc entre 1 et 14 articles vendus. On constate qu'environ la moitié des sessions n'enregistrent la vente que d'un seul livre. Bien entendu, plus la taille d'un panier est grande, plus se fréquence est faible dans le registre total des sessions d'achat. Il serait intéressant de voir la répartition des différentes tailles du panier lors des transactions.

# ------------

# # <font color="darkorange">IV. Analyses des ventes et des prix

# ## <font color="goldenrod">IV.1. Bilan des prix

# <font color="saddlebrown">Analysons maintenant les étendues des prix pour les 3 catégories avec des boîtes à moustaches.

# In[90]:


categories = products["categ"].unique()
categ_price = []

for i in categories:
    categ_price.append(products[products["categ"]==i]["price"])

plt.boxplot(categ_price, labels=categories, showfliers=False, medianprops=medianprops, 
            vert=False, patch_artist=True, showmeans=True, meanprops=meanprops)
plt.xlabel("Prix en euros")
plt.ylabel("Catégories")
plt.show()


# - <font color="saddlebrown">CATÉGORIE 0: Les prix varient entre 0,62 et 40,99 euros. En moyenne, ces livres coûtent environ 11,50 euros et la plupart d'entre eux se vendent à 4,99 euros. D'après le graphique ci-dessus, il s'agit de la catégorie "la moins chère".
# - <font color="saddlebrown">CATÉGORIE 1: Les prix varient entre 2 et 80,99 euros. En moyenne, ces livres coûtent environ 25,50 euros et la plupart d'entre eux se vendent à 22,99 euros. Cette catégorie semble s'adresser à tout poids de portefeuille.
# - <font color="saddlebrown">CATÉGORIE 2: Les prix varient entre 30,99 euros, et valent en moyenne environ 108,35 euros. La plupart d'entre eux coûtent 50,99 euros et d'après le graphique, il s'agit de la catégorie "la plus chère". Il s'agit également de la catégorie de livres proposant le choix le plus large au niveau des prix.

# ## <font color="goldenrod">IV.2. Vendus et invendus

# <font color="saddlebrown">Déterminons pour commencer la proportions de nos produits qui ne se sont pas vendus.

# In[91]:


products["is_sold"]=products.id_prod.isin(table.id_prod)

products.loc[products.is_sold==True, "is_sold"]="VENDUS"
products.loc[products.is_sold==False, "is_sold"]="INVENDUS"

products.is_sold.value_counts(normalize=True).plot(kind="pie", 
                                                   colors=["yellow", "red"], autopct=lambda x: str(round(x, 2))+"%")
plt.ylabel("")
plt.show()


# <font color="saddlebrown">Donc nous avons plus d'un livre sur 200 qui ne se vend pas, ça va pas. Voyons ça par catégorie.

# In[92]:


unsold = products[products.is_sold=="INVENDUS"]
unsold["categ"].value_counts(normalize=True).plot(kind="bar", color="crimson")
plt.xticks(rotation=0)
plt.show()


# <font color="saddlebrown">Va falloir revoir les commandes d'inventaire pour les livres de la catégorie 0.

# ## <font color="goldenrod">IV.3. Prix des invendus

# <font color="saddlebrown">Analysons maintenant les prix des invendus par rapport aux étendues de prix des livres qu'on vend.

# In[93]:


is_sold_or_not = products["is_sold"].unique()
price = []

for i in is_sold_or_not:
    price.append(products[products["is_sold"]==i]["price"])

plt.boxplot(price, labels=is_sold_or_not, showfliers=False, medianprops=medianprops, 
            vert=False, patch_artist=True, showmeans=True, meanprops=meanprops)
plt.xlabel("Prix en euros")
plt.ylabel("Catégories")
plt.show()


# <font color="saddlebrown">On peut voit clairement que les tendances centrales des vendus et des invendus ne sont pas les mêmes. Ce qui nous laisse supposer que certains livres sont trop chers pour susciter l'intérêt du client. Ainsi, la baisse immédiate des prix  des invendus de cette année serait susceptible faire vendre cette partie de nos produits pour l'année à venir.

# -------------
# -------------
# -------------
# -------------

# # <font color="darkred"><center>Mission 3: Étude des Corrélations
# -----------------

# # <font color="firebrick">I. Préparatifs et optimisations pour les analyses

# ### <font color="crimson">I.1. Fonctions utilitaires et identification des Outliers

# <font color="darkred">Nous nous baserons également dans ce sujet sur le DataFrame "table", regroupant les transactions, les clients et les produits, où comme précédemment, nous y avons appliqué la fonction "entier" définie ci-dessous pour une plus belle présentation.

# In[94]:


def entier(a):
    return int(a);

def round2(a):
    return round(a, 2);

#On donne, ici, la fonction eta_squared qui nous renvoie le rapport de corrélation entre une variable quantitative et une
#variable qualitative:
def eta_carre(x,y):
    moyenne_y = y.mean()
    classes = []
    for classe in x.unique():
        yi_classe = y[x==classe]
        classes.append({'ni': len(yi_classe),
                        'moyenne_classe': yi_classe.mean()})
    SCT = sum([(yj-moyenne_y)**2 for yj in y])
    SCE = sum([c['ni']*(c['moyenne_classe']-moyenne_y)**2 for c in classes])
    return SCE/SCT


# <font color="darkred">Nous allons également créer sur les tableaux de support la variable "tranche" pour "tranches d'âges", qui nous renverra trois catégories différentes selon l'âge  du  clients. Mon choix des intervalles de ces trois tranches d'âges résulte d'une première analyse des corrélations demandées, où je me suis aperçu que l'on pouvait reconsidérer certaines corrélations si l'on regroupait  les clients par ces trois tranches d'âges. La variable quantitative  "tranche" renverra:
# - "edtudiant" si le client est âgé de 30 ans ou moins.
# - "actif" si le client est âgé de 31 à 50 ans.
# - "senior" si le client est âgé de 51 ans ou plus.
# 
# Le choix des noms "etudiant", "actif" et "senior" est purement indicatif, ne considérons pas pour autant un individus de 51 ans comme un sénior dans la réalité!

# In[95]:


def get_tranche(a):
    if a<=30: return("etudiant")
    elif a<=50: return("actif")
    else: return("senior")


# <font color="darkred">Nous avons vu dans la partie II.2 de la mission 2 que les clients de 18 ans étaient en surplus par rapport aux autres. Nous les considérerons donc comme des Outliers pour une analyse plus objective sur les âges des clients. Nous les retirerons donc de nos données.

# In[96]:


def drop_18(data):
    return(data.loc[data.age!=18])


# <font color="darkred">Aussi, en constatant certaines dépenses exhorbitantes lors de cette même mission 2, nous pouvons fortement supposer que certains clients s'approvisionnent chez nous pour le compte d'une entreprise. Nous les identifierons à nouveau ci-dessous afin de les supprimer de nos tableaux pour des résultats plus objectifs sur nos clients et leurs tendances d'achats mêmes.

# In[97]:


def sup_depenses(data, p):
    return(data[data["depense_annuelle"]>p][["client_id", "depense_annuelle"]])


# ### <font color="crimson">I.2. Tableaux de support et suppression des Outliers

# <font color="darkred">On reprendra notre DataFrame "table" définit en fin de mission 1 pour diverses analyses des corrélations à venir. Nous retirons donc les clients de plus de 18 ans de nos données et nous ajoutons la colonne "tranche" au DataFrame définie précédemment.

# In[98]:


# Suppression des clients âgés de 18 ans:
table=drop_18(table)

# Ajout de la colonne "tranche":
table["tranche"]=table["age"].apply(get_tranche)

table=table.reset_index(drop=True)
table.head(3)


# <font color="darkred">Nous nous servirons également du DataFrame "clients" définie ci-dessous qui, basée sur "table", regroupe les données par clients, et renvoie le montant total de ce qu'ils ont dépensés en un an, ainsi que le nombre total de livres qu'ils ont achetés, toutes sessions confondues.

# In[99]:


# Création du DataFrame "clients":
clients = pd.DataFrame(table.groupby(["client_id", "sex", "age"]).sum()["price"]).reset_index()
clients.rename(columns={"price": "depense_annuelle"}, inplace=True)
nb_achats = pd.DataFrame(table["client_id"].value_counts()).reset_index()
nb_achats.columns=["client_id", "nombre_livres_achetes"]
clients=pd.merge(clients, nb_achats)

# Suppression des Outliers et ajout de la colonne "tranche":
clients=drop_18(clients)
clients["tranche"]=clients["age"].apply(get_tranche)

clients=clients.reset_index(drop=True)
clients.head(3)


# <font color="darkred">Observons les clients ayant dépensés plus de 1000 euros sur un an.

# In[100]:


sup_depenses(clients, 1000)


# <font color="darkred">Nous en observons un nombre trop important pour tous les considérer comme des Outliers. Fixons-nous un seuil de 3000 euros.

# In[101]:


sup_depenses(clients, 3000)


# <font color="darkred">On cible alors 4 clients qui ont dépensé plus de 50 mille euros en un an, et on peut admettre que les autres ont dépensé moins de 3000 euros. Ces 4 clients identifiés seront donc reconnus comme des Outliers et nous les retirons de nos données.

# In[102]:


clients=clients[clients.depense_annuelle<3000].reset_index(drop=True)
clients


# <font color="darkred">Nous retirons également ces clients du DataFrame "table" et nous allons enfin pouvoir entammer l'analyse des corrélations.

# In[103]:


table=table.loc[table["client_id"].isin(clients["client_id"])==True]
table


# ----------------

# # <font color="firebrick">II. Sexe des clients et catégories de produits achetés

# ### <font color="crimson">II.1. Tableau de contingence réel

# <font color="darkred">Nous cherchons, ici, à savoir si les hommes ou les femmes s'orientent plus vers telle ou telle catégorie  de livres. Créons dans un premier temps le tableau de contingence réel.

# In[104]:


c=table[["categ", "sex"]].pivot_table(index="categ",
                              columns="sex",
                              aggfunc=len)

cont =  c.copy()

tx = table["categ"].value_counts()
ty = table["sex"].value_counts()

cont.loc[:, "Total"] = tx
cont.loc["total", :] = ty
cont.loc["total", "Total"] = len(table)
cont


# <font color="darkred">Pour le moment, nous ne semblons pas distinguer de corrélations significatives. Mais la construction du tableau de contingence théorique en vue du tableau de contingence coloré peut contredire cette supposition.

# ### <font color="crimson">II.2. Tableau de contingence théorique

# <font color="darkred">Créons maintenant le tableau de contingence théorique en vue d'un test des éventuelles corrélations.

# In[105]:


tx = pd.DataFrame(tx)
ty = pd.DataFrame(ty)

tx.columns=["foo"]
ty.columns=["foo"]

n = len(table)
indep =  tx.dot(ty.T)/n

indep.sort_index(axis=1, inplace=True)
indep.sort_index(inplace=True)

indep


# <font color="darkred">Mesurons alors le Chi-2, le degré de liberté et la p_value.

# In[106]:


mesure = (c-indep)**2/indep

xi_n = mesure.sum().sum()
ddl = (len(c)-1)*(len(c.columns)-1)
pvalue = st.chi2_contingency(c)[1]

print("Degré de liberté:", ddl)
print("p_value:", round(pvalue, 20))
print("Chi-2:", xi_n)


# <font color="darkred">On s'aperçoit que la p_value est très proche de  0. Ce qui nous permet de rejeter l'hypothèse qu'il n'y a aucune indépendance entre le genre du client et les catégories de produits. On en déduit donc qu'il y a bien une corrélation entre le sexe des clients et les catégories de produits achetés.

# ### <font color="crimson">II.3. Tableau de contingence coloré

# <font color="darkred">Analysons maintenant cette corrélation pour chacune des 3 catégories de livre avec un tableau de contingence coloré.

# In[107]:


sns.heatmap(mesure/xi_n, annot=c-indep)
plt.title("Tableau de contingence coloré - Sexe des clients et catégories de livres")
plt.xlabel("sexe")
plt.ylabel("Catégories", fontsize=12)
plt.axis("equal")
plt.show()


# <font color="darkred">__Conclusion:__
# - Catégorie 0: Il y a une légère corrélation, en effet, les hommes semblent s'intéresser plus à cette catégorie de livres que les femmes.
# - Catégorie 1: Il y a corrélatation entre cette catégorie de livres et le genre du client. On voit ici que cette catégorie intéresse beaucoup plus les femmes que les hommes.
# - Catégorie 2: Le genre du client importe peu. Les femmes s'intéressent aussi fréquemment à cette catégorie de livres que les hommes.

# -------------

# # <font color="firebrick">III. Âge des clients et montant total des achats

# ### <font color="crimson">III.1.Diagramme de dispersion

# <font color="darkred">

# In[ ]:





# <font color="darkred">

# In[ ]:





# <font color="darkred">

# ### <font color="crimson">III.2.

# <font color="darkred">

# In[ ]:





# <font color="darkred">
