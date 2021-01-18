#!/usr/bin/env python
# coding: utf-8

# # <div style="border: 4px solid black; padding:4px"><font color="red"><center>OPENCLASSROOMS - PROJET 4</center></font> <font color="red"><center>ANALYSEZ LES VENTES DE VOTRE ENTREPRISE</center></font></div>

# ## <div style="border: 1px solid black; padding:2px"><center>Sommaire</center></div>

# ###### <center>Un code de couleur à été attribué aux différentes missions à titre de repère.</center>

# ## <center><a href="#m1"><font color="darkblue">Mission 1: Base de données</font></a></center>
# 
# <div style="display: flex; justify-content: space-around; flex-wrap:wrap"><div>
# 
# <a href="#m11"><font color="mediumblue" size="4px"><B>I.Nettoyage des données</B></font></a>
# <ul><li><a href="#m111"><font color="royalblue">I.1.Customers</font></a></li>
# <li><a href="#m112"><font color="royalblue">I.2.Products</font></a></li>
# <li><a href="#m113"><font color="royalblue">I.3.Transactions</font></a></li></ul>
# </div><div>
# 
# <a href="#m12"><font color="mediumblue" size="4px"><B>II.Finalisation du support</B></font></a>
# <ul><li><a href="#m121"><font color="royalblue">II.1.Jointure des trois tableaux de base</font></a></li>
# <li><a href="#m122"><font color="royalblue">II.2.Agrégations sur les mois</font></a></li>
# <li><a href="#m123"><font color="royalblue">II.3.Variables supplémentaires</font></a></li></ul>
# </div></div>

# ## <center><a href="#m2"><font color="darkorange">Mission 2: Analyses Graphiques</font></a></center>
# 
# <div style="display: flex; justify-content: space-around; flex-wrap:wrap">
# <div style="display: flex; flex-direction: column; justify-content: center"><div>
#     
# <a href="#m21"><font color="goldenrod" size="4px"><B>I.Étude du chiffre d'affaires</B></font></a>
# <ul><li><a href="#m211"><font color="peru">I.1.Évolution globale du chiffre d'affaires</font></a></li>
# <li><a href="#m212"><font color="peru">I.2.Évolution mensuelle du chiffre d'affaires</font></a></li>
# <li><a href="#m213"><font color="peru">I.3.Observation du mois d'Octobre</font></a></li>
# <li><a href="#m214"><font color="peru">I.4.Catégories de livres: ventes et chiffre d'affaires</font></a></li>
# <li><a href="#m215"><font color="peru">I.5.Catégories de livres: Mesures de tendance centrale</font></a></li></ul></div><div>
#     
# <a href="#m23"><font color="goldenrod" size="4px"><B>III.Statistiques des sessions d'achats</B></font></a>
# <ul><li><a href="#m231"><font color="peru">III.1.Montants des sessions</font></a></li>
# <li><a href="#m232"><font color="peru">III.2.Taille du panier moyen</font></a></li>
# <li><a href="#m233"><font color="peru">III.3.Répartition du panier moyen</font></a></li></ul></div></div>
# 
# <div style="display: flex; flex-direction: column; justify-content: center"><div>
# 
# <a href="#m22"><font color="goldenrod" size="4px"><B>II.Statistiques de la clientèle</B></font></a>
# <ul><li><a href="#m221"><font color="peru">I.1.Étude des âges</font></a></li>
# <li><a href="#m222"><font color="peru">I.2.Étude des genres</font></a></li>
# <li><a href="#m223"><font color="peru">I.3.Répartition du chiffre d'affaires par client</font></a></li>
# <li><a href="#m224"><font color="peru">I.4.Proportions de clients actifs/inactifs</font></a></ul></li>
# <font color="white">.</font></div><div>
#     
# <a href="#m24"><font color="goldenrod" size="4px"><B>IV.Analyses des ventes et des prix</B></font></a>
# <ul><li><a href="#m241"><font color="peru">IV.1.Bilan des prix</font></a></li>
# <li><a href="#m242"><font color="peru">IV.2.Vendus et invendus</font></a></li>
# <li><a href="#m243"><font color="peru">IV.3.Prix des invendus</font></a></li></ul></div></div></div>

# ## <center><a href="#m3"><font color="firebrick">Mission 3: Étude des Corrélations</font></a></center>
# 
# <div style="display: flex; justify-content: space-around; flex-wrap:wrap">
# <div style="display: flex; flex-direction: column; justify-content: center">
# <div>
# 
# <a href="#m31"><font color="crimson" size="4px"><B>I.Préparatifs et optimisations pour les analyses</B></font></a>
# <ul><li><a href="#m311"><font color="brown">I.1.Fonctions utilitaires</font></a></li>
# <li><a href="#m312"><font color="brown">I.2.Tableaux de support et suppression des Outliers</font></a></li>
# <li><a href="#m313"><font color="brown">I.3.Autres supports</font></a></li></ul></div><div>
#     
# <a href="#m33"><font color="crimson" size="4px"><B>III.Âge des clients et montant total des achats</B></font></a>
# <ul><li><a href="#m331"><font color="brown">III.1.Diagramme de dispersion</font></a></li>
# <li><a href="#m332"><font color="brown">III.2.Tranches d'âges et montant total des achats</font></a></li></ul></div><div>
#     
# <a href="#m35"><font color="crimson" size="4px"><B>V.Âge des clients et taille du panier moyen</B></font></a>
# <ul><li><a href="#m351"><font color="brown">V.1.Diagramme de dispersion</font></a></li>
# <li><a href="#m352"><font color="brown">V.2.Tranches d'âges et taille du panier moyen</font></a></li></ul></div></div>
#     
# <div style="display: flex; flex-direction: column; justify-content: center"><div>
#     
# <a href="#m32"><font color="crimson" size="4px"><B>II.Sexe des clients et catégories de produits achetés</B></font></a>
# <ul><li><a href="#m321"><font color="brown">II.1.Tableau de contingence réel</font></a></li>
# <li><a href="#m322"><font color="brown">II.2.Tableau de contingence théorique</font></a></li>
# <li><a href="#m323"><font color="brown">II.3.Tableau de contingence coloré</font></a></li></ul></div><div>
#     
# <a href="#m34"><font color="crimson" size="4px"><B>IV.Âge des clients et fréquences d'achats</B></font></a>
# <ul><li><a href="#m341"><font color="brown">IV.1.Diagramme de dispersion</font></a></li>
# <li><a href="#m342"><font color="brown">IV.2.Tranches d'âges et fréquences d'achats</font></a></li></ul></div><div>
#     
# <a href="#m36"><font color="crimson" size="4px"><B>VI.Âge des clients et catégories de produits achetés</B></font></a>
# <ul><li><a href="#m361"><font color="brown">VI.1.Rapport de corrélation</font></a></li>
# <li><a href="#m362"><font color="brown">VI.2.Tableau de contingence coloré</font></a></li></ul></div></div></div>

# ### <center>Nous importons dans un premier temps l'ensemble des librairies nécessaires pour l'ensemble du projet. </center>

# In[2]:


import pandas as pd ; import numpy as np ; import seaborn as sns ; import datetime as dt ; import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pylab import arange, plot ; from matplotlib.pyplot import figure
import scipy.stats as st ; import statsmodels.api as sm ; import statsmodels.formula.api as smf
from IPython.core.display import HTML ; import warnings ; warnings.filterwarnings('ignore')
HTML("""<style> .output_png {display: table-cell; text-align: center; vertical-align: middle} </style>""")


#   

#   

# # <div style="border: 2px solid darkblue; padding:5px; margin:5px"><a id="m1"><font color="darkblue"><center>Mission 1: Base de données</center></font></a></div>

# 
# # <a id="m11"><font color="mediumblue"><U>I. Nettoyage des données</U></font></a>

# ## <a id="m111"><font color="royalblue"><U><I>I.1. Customers</I></U></font></a>

# <font color="midnightblue">Ce premier DataFrame nous renvoie la liste des clients qui ont effectué des achats dans l'année, caractérisés par leur identifiant client, leur sexe et leur année de naissance.

# In[449]:


customers = pd.read_csv("data/projet_4/base/customers.csv")  ;  customers.head(5)


# <font color="midnightblue">Pour ce premier DataFrame, nous remplacerons l'année de naissance des clients par leur âge, puis nous retirerons de la clist les clients 'test'.

# In[450]:


customers["age"]=2022-customers.birth
customers=customers.drop(columns=["birth"]).loc[(customers["client_id"].isin(["ct_0", "ct_1"]))==False] ; customers


# ## <a id="m112"><font color="royalblue"><U><I>I.2. Products</I></U></font></a>

# <font color="midnightblue">Ce deuxième DataFrame nous renvoie la liste des produits (livres) achetés au cours de l'année, indexés par leur identifiant de produit, leur prix, et la catégorie (0, 1 ou 2) auxquelles ils appartiennent.

# In[451]:


products = pd.read_csv("data/projet_4/base/products.csv") ; products.head(4)


# <font color="midnightblue">Repérons la petite valeur aberrante suivante: un des prix est négatif! Il s'agit d'un produit test. Nous allons donc l'enlever.

# In[452]:


products[products.price<0]


# In[453]:


products=products.loc[products["price"] > 0 ].reset_index(drop=True) ; products


# ## <a id="m113"><font color="royalblue"><U><I>I.3. Transactions</I></U></font></a>

# <font color="midnightblue">Enfin, il nous reste la liste des transactions effectuées au cours de l'année, où l'on peut notamment y repérer quel client a acheté tel ou tel livre.

# In[454]:


transactions = pd.read_csv("data/projet_4/base/transactions.csv")  ;  transactions.head(2)


# <font color="midnightblue">Dans la cellule suivante, nous allons:
# - <font color="midnightblue"> Retirer les clients test.
# - <font color="midnightblue"> Nous débarasser des microsecondes (on y verra plus clair!)
# - <font color="midnightblue"> Faire un "split" de la date et de l'heure dans le cadre des analyses de la mission 2.

# In[455]:


# Retrait des clients "test":
transactions=transactions.loc[(transactions.client_id!='ct_0')&(transactions.client_id!='ct_1')]

# Bon débarras des microsecondes:
def date_claire(date):
    return(date.split(".")[0])
transactions["date"]=transactions["date"].apply(date_claire)

# On renomme la colonne "date" en "date_et_heure" et on la convertit en datetime:
transactions.rename(columns={"date": "date_et_heure"}, inplace=True)
transactions["date_et_heure"]=pd.to_datetime(transactions["date_et_heure"])


# La conversion de date_et_heure en datetime nous permet d'appliquer les fonctions get_date() et get_hour() sur cette
# variable nous renvoient respectivement la date et l'heure:

def get_date(dh):
    return(dh.date());
transactions["date"]=transactions["date_et_heure"].apply(get_date)

def get_hour(dh):
    return(dh.time());
transactions["heure"]=transactions["date_et_heure"].apply(get_hour)

# Nous n'aurons plus besoin de la colonne "date_et_heure":
transactions=transactions.drop(columns="date_et_heure")  ;  transactions


# <font color="midnightblue">Enfin, vérifions s'il existe un produit présent dans "transactions" mais absent dans "products".

# In[456]:


is_absent=transactions[transactions.id_prod.isin(products.id_prod)==False]["id_prod"].unique()[0]  ; is_absent


# <font color="midnightblue">Ne vous en faites pas, nous allons régler ça dans la partie suivante.

#    

# # <a id="m12"><font color="mediumblue"><U>II. Finalisation du support</U></font></a>

# ## <a id="m121"><font color="royalblue"><U><I>II.1. Jointure des trois tableaux de base</I></U></font></a>

# <font color="midnightblue">Nous créons maintenant le DataFrame "table", qui regroupera les trois DataFrames précédents traités et nettoyés. D'abord, on fait la jointure externe - afin de récupérer l'élément manquant dans products - de products et de transactions.

# In[457]:


table = pd.merge(products, transactions, on='id_prod', how='outer') ; table


# <font color="midnightblue">Avant d'ajouter les clients, traîtons les valeurs manquantes, jusque là:
# - La colonne "categ", indique la catégorie de livres - 0, 1 ou 2 - qui se trouve être le premier chiffre de son identifiant produit "id_prod".
# - La colonne "price" présente une valeur nulle les livres 0_2245. Après analyse des mesures de tendance centrale, on fixera ce prix à 9,99 euros.

# In[458]:


#Fonction permettant de récupérer le premier chiffre d'un identifiant de produit dans nos données:
def get_categ(car):
    return  int(car.split("_")[0])

#Complétude de "categ":
table["categ"]=table.id_prod.apply(get_categ)

#Ajout du prix du livre 0_2245:
table["price"].fillna(9.99, inplace=True)

table.tail(3)


# <font color="midnightblue">On peut maintenant ajouter les données de "customers" à notre DataFrame par jointure interne et on le réindexe notre table selon les dates.

# In[459]:


table = pd.merge(table, customers).sort_values(by="date").reset_index(drop=True) ; table


# <font color="midnightblue">Nous allons maintenant finaliser notre base de données, mais avant ça, quelques agrégations sur les mois de l'année s'imposent...

# ## <a id="m122"><font color="royalblue"><U><I>II.2. Agrégations sur les mois</I></U></font></a>

# <font color="midnightblue">Dans le cadre des analyses graphiques à réaliser pour la mission 2, il sera intéressant d'étudier certaines variables selon les mois de l'année. Rappelons que notre étude futuriste s'étend de mars 2021 à février 2022. Les listes suivantes nous donnent donc la liste des 12 mois de l'année et leur numéro de mois et leur "chronologie" dans notre étude (afin de pouvoir les classer en cas de besoin). Attention, notre étude s'étend de mars 2021 à 2022, d'où 21.nb_mois correspondra aux mois de mars à décembre inclus et 22.01 et 22.02 respectivement aux mois de janviers et février.

# In[460]:


# Listes pour nos aggrégations:
CALENDAR=["janvier", "fevrier", "mars", "avril", "mai", "juin", 
          "juillet", "août", "septembre", "octobre", "novembre", "decembre"]
CHRONOLOGIE=[22.01, 22.02, 21.03, 21.04, 21.05, 21.06, 21.07, 21.08, 21.09, 21.10, 21.11, 21.12]

# Pour passer, par exemple, de "juillet" à 7:
def nombre_mois(car):
    return(CALENDAR.index(car)+1)

# Pour passer, par exemple, de 4 à "avril":        
def nom_mois(n):
    return(CALENDAR[n-1])
    
# Pour passer, par exemple, de "avril" à "21.04" ou de "janvier" à "22.01":
def chronologie(car):
    return(CHRONOLOGIE[nombre_mois(car)-1])


# ## <a id="m123"><font color="royalblue"><U><I>II.3. Variables supplémentaires</I></U></font></a>

# <font color="midnightblue">Notons qu'une "session" est un groupe d'achats. Ce serait donc intéressant de savoir, combien de livres ont été achetés à chaque session. On crée donc la variable "basket_size" qui nous donnera cette indication.

# In[461]:


table["basket_size"]=table["session_id"].value_counts()[table["session_id"]].tolist()  ;  table.head(3)


# <font color="midnightblue">Enfin, en vue des analyses graphiques que nous ferons, avoir le mois en vigueur rendra notre codage bien plus propre.

# In[462]:


# On reconverti la date en datetime:
table["date"]=pd.to_datetime(table["date"])

# On ajoute la colonne "mois" grâce à nos fonctions:
table["mois"]=table["date"].dt.month.apply(nom_mois)

# Et le jour du mois, ce sera utile:
table["jour"]=table["date"].dt.day

# On réindexe notre support pour y voir plus clair:
table=table.reindex(columns=["id_prod", "categ", "price", 
                             "client_id", "sex", "age",
                             "session_id", "basket_size",
                             "date", "mois", "jour", "heure"]) ; table


#    

#    

#    

#       

# # <div style="border: 2px solid darkorange; padding:5px; margin:5px"><a id="m2"><font color="darkorange"><center>Mission 2: Analyses Graphiques</center></font></a></div>

#  

# # <font color="darkorange"> _Prémices - Agrégats & Fonctions Utilitaires_

# <font color="saddlebrown">Dans cette deuxième partie, nous allons effectuer diverses observations graphiques sur les ventes effectuées de mars 2021 à février 2022. Pour simplifier le codage, nous définissons ci-dessous quelques définitions et fonctions usuelles que nous utiliserons tout au long de la mission.

# In[463]:


def couleur(c):
    if c==0: return("steelblue") # Ce sera notre couleur de repère pour la catégorie 0.
    elif c==1: return("crimson") # Ce sera notre couleur de repère pour la catégorie 1.
    else: return("goldenrod") # Ce sera notre couleur de repère pour la catégorie 2.

palette=[couleur(c) for c in range(3)] # Notre palette de couleurs pour les 3 catégories.
categories_3 = ["Catégorie %d" %i for i in range(3)] # Nous servira à nommer les labels.

# On effectuera plusieurs études individuelles sur les ventes de chaque catégorie de livres:
[categ_0, categ_1, categ_2] = [table.loc[table["categ"]==i] for i in range(3)]

# Une fonction pour effectuer facilement un groupby sur table:
def groupby_var(data, var):
    return(pd.DataFrame(data.groupby(var).sum()["price"]).reset_index())

# Une fonction qui réordonne chronologiquement (de mars à février) nos données:
def periode(data):
    data["chronologie"]=data["mois"].apply(chronologie)
    data=data.sort_values(by="chronologie")
    data.drop(columns="chronologie", inplace=True)
    return(data)

# La fonction dim() nous permettra de définir à chaque fois les dimensions des figures que l'on affichera:
def dim(x, y): return(plt.figure(figsize=(x, y)))

# On définit ici les paramètres des boxplots et des camemberts pour toute la suite de la mission:
medianprops = {"color":"black"}
meanprops = {"marker":"o", "markeredgecolor":"black", "markerfacecolor":"firebrick"}
autopct=lambda x: str(round(x, 2))+"%"

# La fonction boxplot() qui nous renverra la boîte à moustaches d'une liste L selon les indices de "labels":
def boxplot(L, labels):
    return(dim(18, 3), plt.boxplot(L, labels=labels, showfliers=False, medianprops=medianprops, 
                                   vert=False, patch_artist=True, showmeans=True, meanprops=meanprops))


# <font color="saddlebrown">Nous nous baserons avant tout sur le DataFrame "table" établi lors de la  mission 1.

# In[464]:


table


# <font color="saddlebrown">Dans la partie II, nous réutiliserons le DataFrame "customers" introduit au début de la mission 1, où nous y ajoutons la colonne "is_active" qui renvoie "ACTIF" si le client en question a effectué au moins un achat au cours de la période étudiée (mars 2021 - février 2022), "INACTIF" sinon.

# In[465]:


def active(car):
    if car==True: return("ACTIF")
    else: return("INACTIF")
    
customers["is_active"]=customers["client_id"].isin(table.client_id).apply(active) ; customers


# <font color="saddlebrown">Lors de la partie III, nous étudierons les sessions d'achats. On crée donc le DataFrame "sessions" qui regroupe les montants totaux de chaque session d'achat effectuée sur le site en cours d'année.

# In[466]:


sessions = pd.DataFrame(table.groupby(["session_id", "client_id", "age", "date", "mois", "jour"])
                        .sum()["price"]).reset_index()

sessions.rename(columns={"price": "montant_session"}, inplace=True)
effectifs = pd.DataFrame(table.session_id.value_counts().reset_index())
effectifs.columns=("session_id", "taille_panier")
sessions=pd.merge(sessions, effectifs) ; sessions


#    

#    

# # <a id="m21"><font color="darkorange"><U>I. Étude du chiffre d'affaires</U></font></a>

# ## <a id="m211"><font color="goldenrod"><U><I>I.1. Évolution globale du chiffre d'affaires</I></U></font></a>

# <font color="saddlebrown">Observons dans un premier temps l'évolution du chiffre d'affaires de Mars 2021 à Février 2022.

# In[467]:


table_gb_date = groupby_var(table, "date")

dim(12, 5)
plt.plot(table_gb_date["date"], table_gb_date["price"], color="seagreen", label="Chiffre d'affaires", linewidth=1)

plt.title("Évolution du chiffre d'affaires au cours de l'année", fontsize=20)
plt.xlabel("") ; plt.ylabel("Chiffre d'affaires en euros", fontsize=14) ; plt.show()


# <font color="saddlebrown">On a une première approche de l'évolution du chiffre d'affaires global. On y observe une tendance à la hausse de cette évolution le long de l'année, progression interrompue entre les mois de septembre et novembre avec une forte chute du CA, avant une reprise normale de cette évolution dès novembre. Avant de continuer, distribuons cette courbe pour chaque catégorie de livres.

# In[468]:


figure(num=None, figsize=(12, 5), dpi=80)
for i in range(3):
    cat=groupby_var(table.loc[table["categ"]==i], "date")
    color=couleur(i)
    plt.plot(cat["date"], cat["price"], color=color, linewidth=1, label= "Catégorie %d" %i)

plt.title("Évolution du chiffre d'affaires au cours de l'année", fontsize=20)
plt.xlabel("") ; plt.ylabel("Chiffre d'affaires", fontsize=14) ; plt.legend() ; plt.show()


# <font color="saddlebrown">On observe une rentabilité globale moins élevée pour la catégorie 2. Mais remarquons surtout la chute du chiffre d'affaires des trois catégories de livres vers novembre. Essayons de voir ça de plus près en regroupant ces analyses par mois.

# ## <a id="m212"><font color="goldenrod"><U><I>I.2. Évolution mensuelle du chiffre d'affaires</I></U></font></a>

# <font color="saddlebrown">On voit une chute entre les mois d'août et novembre sur le graphique précédent. Regardons ça de plus près avec une analyse mensuelle.

# In[469]:


emca = groupby_var(table, "mois")
emca["chronologie"]=emca["mois"].apply(chronologie)
emca=emca.sort_values(by="chronologie")

dim(7, 5) ; plt.bar(emca["mois"], emca["price"], color="seagreen")
plt.title("Évolution mensuelle du chiffre d'affaires", fontsize=15)
plt.xlabel("") ; plt.ylabel("Chiffre d'affaires") ; plt.xticks(rotation=45) ; plt.show()


# <font color="saddlebrown">C'est ici qu'on repère la chute drastique du CA au mois d'octobre. Cela fera l'objet de notre prochaine partie. Tout d'abord, il serait intéressant d'analyser cet histogramme selon les 3 catégorie de livre.

# In[470]:


eca=periode(table.pivot_table(index="mois", columns="categ", values="price", aggfunc=sum).reset_index())
eca.columns=["mois", "categ_0", "categ_1", "categ_2"]

dim(7, 5)
plt.bar(eca.mois, eca.categ_0 + eca.categ_1 + eca.categ_2, color=couleur(2), label="Catégorie 2")
plt.bar(eca.mois, eca.categ_0 + eca.categ_1, color=couleur(1), label="Catégorie 1")
plt.bar(eca.mois, eca.categ_0, color=couleur(0), label="Catégorie 0")

plt.title("Chiffre d'affaires par catégorie de livres", fontsize=15)
plt.xlabel("") ; plt.xticks(rotation = 'vertical') ; plt.ylabel("Chiffre d'affaires") 
plt.legend(loc="lower left") ; plt.show()


# <font color="saddlebrown">On voit alors que c'est la catégorie 1 qui est la cause de la chute drastique du mois d'octobre.

# ## <a id="m213"><font color="goldenrod"><U><I>I.3. Observation du mois d'Octobre</I></U></font></a>

# <font color="saddlebrown">Observons les ventes des livres au cours  du mois d'octobre.

# In[471]:


octobre=table[table.mois=="octobre"].pivot_table(index=["date"], columns=["categ"],
                                                 values=["price"], aggfunc=sum).reset_index().fillna(0)
octobre.columns=["date", "categorie 0", "categorie 1", "categorie 2"]

dim(12, 3)
for i in range(3):
    catego="categorie %d" %i
    plot(octobre["date"], octobre[catego], color=couleur(i), label=catego)

plt.title("Évolution du chiffre d'affaires au cours du mois d'Octobre", fontsize=18)
plt.xlabel("") ; plt.ylabel("Chiffre d'affaires", fontsize=14) ; plt.legend() ; plt.show()


# <font color="saddlebrown">Effectivement, nous n'avons enregistré aucune vente entre le 2 et le 28 octobre inclus. Pourquoi? Faudra demander à la compta.

# ## <a id="m214"><font color="goldenrod"><U><I>I.4. Catégories de livres par nombre de ventes et par chiffre d'affaires</I></U></font></a>

# <font color="saddlebrown">Nous allons tracer deux camemberts. Ils les parts des ventes selon les 3 catégories de livres, le premier selon le chiffre d'affaires, le deuxième selon les effectifs vendus.

# In[472]:


dim(10, 10) ; plt.subplot(2, 2, 1)
groupby_var(table, "categ")["price"].plot(kind="pie", colors=palette, labels=["", "", ""], autopct=autopct)
plt.title("Parts du chiffre d'affaires par catégorie de livres", fontsize=12) ; plt.ylabel("")
plt.legend(categories_3, loc="lower right")

plt.subplot(2, 2, 2)
table["categ"].value_counts(normalize=True).plot(kind="pie", colors=palette, labels=["", "", ""], autopct=autopct)
plt.title("Parts des ventes par catégorie de livres", fontsize=12) ; plt.ylabel("")
plt.legend(categories_3, loc="lower right") ; plt.show()


# <font color="saddlebrown">Comparaisons des deux diagrammes  circulaires:
# - Les livres de la catégorie 0 sont ceux qui se vendent en plus grandes quantités mais ne représentent pas la plus grande part du chiffre d'affaires.
# - Les livres de la catégorie 1 font la majeure partie du chiffre d'affaires, mais se vendent moins que la catégorie 0.
# - Les livres de la catégorie 2 sont ceux qui se vendent le moins et participent le moins au chiffre d'affaires. Néanmoins, la comparaison entre le taux de ventes et la participation au chiffre d'affaires laisse supposer que ce sont globalement les livres les plus chers dans notre inventaire.

# ## <a id="m215"><font color="goldenrod"><U><I>I.5. Catégories de livres: Mesures de tendance centrale</I></U></font></a>

# <font color="saddlebrown">Analysons les mesures de tendance centrales des recettes des trois catégories de livres dans des boîtes à moustaches.

# In[473]:


categories = table["categ"].unique()
categ_ca = []

for i in categories:
    categ_ca.append(table[table["categ"]==i]["price"])
    
boxplot(categ_ca, categories)
plt.title("Chiffre d'affaires moyen par catégorie", fontsize=15)
plt.xlabel("Chiffre d'affaires moyen", fontsize=12) ; plt.ylabel("Catégories", fontsize=15)
plt.yticks(fontsize=15) ; plt.show()


# <font color="saddlebrown">On constate alors que les prix sont beaucoup plus élevés pour les livres de la catégorie 2. La catégorie 1 propose également des prix plus importants que ceux de la catégorie 0. Il semblerait qu'il y ait une corrélation entre les prix et les catégories de livres.

#    

#    

# # <a id="m22"><font color="darkorange"><U>II. Statistiques de la clientèle</U></font></a>

# ## <a id="m221"><font color="goldenrod"><U><I>II.1. Étude des âges</I></U></font></a>

# <font color="saddlebrown">Tout d'abord, analysons les fréquences d'âge de nos clients.

# In[474]:


dim(14, 5) ; plt.hist(customers["age"], density=True, width=0.5, bins=150, color="firebrick")
plt.title("Fréquences d'âge de nos clients", fontsize=18) ; plt.xlabel("Âges") ; plt.ylabel("Fréquences") ; plt.show()


# <font color="saddlebrown">La fréquence d'âge la plus forte chez nos clients est 18 ans. Les retraités se sentent de moins en moins concernés par nos produits. 50% de nos clients ont entre 30 et 55 ans. 25% ont moins de 30 ans et 25% ont plus de 55 ans.

# ## <a id="m222"><font color="goldenrod"><U><I>II.2. Étude des genres</I></U></font></a>

# <font color="saddlebrown">Regardons maintenant les fréquences des genres de notre clientèle.

# In[475]:


dim(5, 5) ;  customers["sex"].value_counts().plot(kind="pie", colors=["deeppink", "royalblue"], 
                                                  labels=["", ""], autopct=autopct)

plt.title("Fréquences d'achats selon le genre des clients", fontsize=14) ; plt.ylabel("")
plt.legend(["Femmes", "Hommes"], loc="lower right", fontsize=14) ; plt.show()


# <font color="saddlebrown">Regardons ces fréquences de genre par catégorie de livres.

# In[476]:


dim(15, 15)

for i in table.categ.unique():
    
    clients_i = pd.DataFrame(table.loc[table.categ==i].groupby(["client_id", "sex"]).sum()["price"]).reset_index()
    clients_i.rename(columns={"price": "depenses"}, inplace=True)
    nb_achats_i = pd.DataFrame(table.loc[table.categ==i].client_id.value_counts()).reset_index()
    nb_achats_i.columns=["client_id", "nombre_livres_achetes"]
    clients_i=pd.merge(clients_i, nb_achats_i)
    
    plt.subplot(1, 3, i+1)
    clients_i["sex"].value_counts(normalize=True).plot(kind='pie', colors=["deeppink", "royalblue"], 
                                                       labels=["", ""], autopct=autopct)
    plt.title("Catégorie %s" %i) ; plt.ylabel("")
    plt.legend(["Femmes", "Hommes"], loc="lower right")
    
plt.show()


# <font color="saddlebrown">On peut admettre a priori que le genre du client ne conditionne pas la catégorie de livres à laquelle il/elle va s'intéresser.

# ## <a id="m223"><font color="goldenrod"><U><I>II.3. Répartition du chiffre d'affaires par client, courbe de Lorenz et indice de Gini</I></U></font></a>

# <font color="saddlebrown">Nous allons étudier la répartition des fréquences d'achats selon les âges de nos clients.

# In[477]:


clients=pd.DataFrame(table.groupby("client_id").sum()["price"]).sort_values("price")
depenses = clients.price.values
n = len(depenses)

lorenz = np.append([0], np.cumsum(depenses)/sum(depenses))
gini=2*(0.5-lorenz.sum()/n)

dim(5, 5) ; plt.plot(np.linspace(0-1/n, 1+1/n, n+1), lorenz)
plt.axes().axis("equal") ; plt.title("Courbe de Lorenz - Gini=%s" %(round(gini, 2)), fontsize=15)

X = arange(0,1,0.01) ; Y=X
plot(X, Y) ; plt.show()


# <font color="saddlebrown">On observe alors sur la courbe de  Lorenz, avec un indice de Gini proche de  0,5 que la répartition du CA par client n'est pas égalitaire. 

# ## <a id="m224"><font color="goldenrod"><U><I>II.4. Proportions de clients actifs/inactifs</I></U></font></a>

# <font color="saddlebrown">Il existe des clients enregistrés sur le site qui n'ont effectué aucun achat. On appelle "client actif" un client qui a effectué au moins un achat sur la période étudiée, "inactif" sinon.

# In[478]:


customers["is_active"]=customers["client_id"].isin(table.client_id)

dim(5, 5) ; customers["is_active"].value_counts(normalize=True).plot(kind="pie", labels=["Actifs", "Inactifs"],
                                                                     colors=["chartreuse", "red"], autopct=autopct)
plt.ylabel("") ; plt.show()


# <font color="saddlebrown">Donc un peu moins d'un client sur 400 s'enregistre mais n'effectue aucun achat.

#     

#    

# # <a id="m23"><font color="darkorange"><U>III. Statistiques des sessions d'achats</U></font></a>

# ## <a id="m231"><font color="goldenrod"><U><I>III.1. Montants des sessions</I></U></font></a>

# <font color="saddlebrown">Voyons comment a évolué la dépense moyenne des clients tout au long de l'année.

# In[479]:


year =  pd.DataFrame(sessions.groupby(["date"]).mean()["montant_session"]).reset_index()

dim(15, 5) ; plot(year.date, year.montant_session, color="green")

plt.title("Montants des sessions d'achats au cours de l'année", fontsize=18)
plt.xlabel("") ; plt.ylabel("Moyennes des montants de session", fontsize=12) ; plt.show()


# <font color="saddlebrown">On retrouve bien la même évolution que celle du chiffre d'affaires étudié en première partie. Observons maintenant cette évolution sur un mois, en prenant la moyenne de ce montant pour chaque jour de chaque mois observé,
# en retirant le mois d'octobre en dépit de l'anomalie observé en première partie pour ne pas fausser les résultats.

# In[480]:


mois =  pd.DataFrame(sessions.loc[sessions.mois!="octobre"].groupby(["jour"]).mean()["montant_session"]).reset_index()

dim(15, 5) ; plot(mois.jour, mois.montant_session, color="navy")
plt.title("Montants moyens des sessions d'achats sur le mois", fontsize=18) ; plt.xticks(range(32))
plt.xlabel("Jours du mois", fontsize=12) ; plt.ylabel("Moyennes des montants de session", fontsize=12) ; plt.show()


# <font color="saddlebrown">On observe en moyenne une tendance à la hausse au fil du mois. On peut  donc supposer que les clients effectuent généralement de plus gros  achats en  fin de mois. On repère ici les jours où les boosts de publicité à faire améliorerait nos ventes.

# ## <a id="m232"><font color="goldenrod"><U><I>III.2. Taille moyenne du panier</I></U></font></a>

# <font color="saddlebrown">Une session d'achats regroupe parfois l'achat de plusieurs livres en même temps. On analyse ici la taille des paniers des transactions effectuées.

# In[481]:


panier_moyen = pd.DataFrame(sessions.groupby("date").mean()["taille_panier"]).reset_index()

dim(15, 5) ; plot(panier_moyen.date, panier_moyen.taille_panier, color="darkorchid")
plt.title("Tailles moyennes du panier de sessions au cours de l'année", fontsize=18)
plt.xlabel("") ; plt.ylabel("Taille moyenne du panier", fontsize=12) ; plt.show()


# <font color="saddlebrown">Il est intéressant de noter que tout au long de l'année, la taille moyenne du panier des clients atteint son maximum journalier fin septembre, juste avant  la chuste drastique du chiffre d'affaires au mois d'octobre. Analysons-le maintenant l'évolution de la taille moyenne du panier par mois.

# In[482]:


panier_moyen_month = periode(pd.DataFrame(sessions.groupby("mois").mean()["taille_panier"]).reset_index()).set_index("mois")

dim(7, 5) ; panier_moyen_month["taille_panier"].plot.bar(color="plum")
plt.title("Chiffre d'affaires") ; plt.xlabel("") ; plt.ylabel("Euros") ; plt.show()


# <font color="saddlebrown">Nous pouvons constater que le panier moyen est constant tous les mois, à peu de choses près. Le mois de septembre voit son panier moyen plus élevé que les autres, sans doute en vertue de la rentrée scolaire.

# ## <a id="m233"><font color="goldenrod"><U><I>III.3. Répartition du panier moyen</I></U></font></a>

# <font color="saddlebrown">Regardons les fréquences de tailles des paniers.

# In[483]:


sessions=sessions.sort_values("taille_panier")

dim(7, 5) ; sessions["taille_panier"].value_counts(normalize=True).plot(kind="bar", color="darkorange")
plt.title("Fréquences des tailles de panier d'achats", fontsize=18) ; plt.xticks(rotation=0, fontsize=15) ; plt.show()


# <font color="saddlebrown">Une session cumule donc entre 1 et 14 articles vendus. On constate qu'environ la moitié des sessions n'enregistrent la vente que d'un seul livre. Bien entendu, plus la taille d'un panier est grande, plus se fréquence est faible dans le registre total des sessions d'achat. Il serait intéressant de voir la répartition des différentes tailles du panier lors des transactions.

#      

#    

# # <a id="m24"><font color="darkorange"><U>IV. Analyses des ventes et des prix</U></font></a>

# ## <a id="m241"><font color="goldenrod"><U><I>IV.1. Bilan des prix</I></U></font></a>

# <font color="saddlebrown">Analysons maintenant les étendues des prix pour les 3 catégories avec des boîtes à moustaches.

# In[484]:


categories = products["categ"].unique()
categ_price = []

for i in categories:
    categ_price.append(products[products["categ"]==i]["price"])

boxplot(categ_price, categories)
plt.title("Bilan des prix de ventes selon les catégories de livres", fontsize=18)
plt.xlabel("Prix en euros", fontsize=15) ; plt.ylabel("Catégories", fontsize=15) ; plt.yticks(fontsize=14) ; plt.show()


# - <font color="saddlebrown">CATÉGORIE 0: Les prix varient entre 0,62 et 40,99 euros. En moyenne, ces livres coûtent environ 11,50 euros et la plupart d'entre eux se vendent à 4,99 euros. D'après le graphique ci-dessus, il s'agit de la catégorie "la moins chère".
# - <font color="saddlebrown">CATÉGORIE 1: Les prix varient entre 2 et 80,99 euros. En moyenne, ces livres coûtent environ 25,50 euros et la plupart d'entre eux se vendent à 22,99 euros. Cette catégorie semble s'adresser à tout poids de portefeuille.
# - <font color="saddlebrown">CATÉGORIE 2: Les prix varient entre 30,99 euros, et valent en moyenne environ 108,35 euros. La plupart d'entre eux coûtent 50,99 euros et d'après le graphique, il s'agit de la catégorie "la plus chère". Il s'agit également de la catégorie de livres proposant le choix le plus large au niveau des prix.

# ## <a id="m242"><font color="goldenrod"><U><I>IV.2. Vendus et invendus</I></U></font></a>

# <font color="saddlebrown">Déterminons pour commencer la proportions de nos produits qui ne se sont pas vendus.

# In[485]:


products["is_sold"]=products.id_prod.isin(table.id_prod)
products.loc[products.is_sold==True, "is_sold"]="VENDUS"
products.loc[products.is_sold==False, "is_sold"]="INVENDUS"

dim(5, 5) ; products.is_sold.value_counts(normalize=True).plot(kind="pie", colors=["yellow", "red"], autopct=autopct)
plt.title("Bilan des articles vendus et invendus", fontsize=15) ;  plt.ylabel("") ; plt.show()


# <font color="saddlebrown">Donc nous avons plus d'un livre sur 200 qui ne se vend pas, ça va pas. Voyons ça par catégorie.

# In[486]:


unsold = products[products.is_sold=="INVENDUS"].sort_values("categ")

dim(5, 5) ; unsold["categ"].value_counts(normalize=True).plot(kind="bar", colors=["steelblue", "goldenrod", "crimson"] )
plt.title("Invendus par catégories", fontsize=15) ; plt.xticks(rotation=0) ; plt.show()


# <font color="saddlebrown">Va falloir revoir les commandes d'inventaire pour les livres de la catégorie 0.

# ## <a id="m243"><font color="goldenrod"><U><I>IV.3. Prix des invendus</I></U></font></a>

# <font color="saddlebrown">Analysons maintenant les prix des invendus par rapport aux étendues de prix des livres qu'on vend.

# In[487]:


is_sold_or_not = products["is_sold"].unique()
price = []

for i in is_sold_or_not:
    price.append(products[products["is_sold"]==i]["price"])

dim(18, 2) ; plt.boxplot(price, labels=is_sold_or_not, showfliers=False, medianprops=medianprops, 
                         vert=False, patch_artist=True, showmeans=True, meanprops=meanprops)
plt.title("Bilan des prix de ventes des articles vendus et invendus", fontsize=15)
plt.xlabel("Prix en euros") ; plt.ylabel("Catégories") ; plt.show()


# <font color="saddlebrown">On peut voit clairement que les tendances centrales des vendus et des invendus ne sont pas les mêmes. Ce qui nous laisse supposer que certains livres sont trop chers pour susciter l'intérêt du client. Ainsi, la baisse immédiate des prix  des invendus de cette année serait susceptible faire vendre cette partie de nos produits pour l'année à venir.

#    

#    

# # <div style="border: 2px solid darkred; padding:5px; margin:5px"><a id="m3"><font color="darkred"><center>Mission 3: Étude des Corrélations</center></font></a></div>

# 
# # <a id="m31"><font color="firebrick"><U>I. Préparatifs et optimisations pour les analyses</U></font></a>

# ## <a id="m311"><font color="crimson"><U><I>I.1. Fonctions utilitaires et identification des Outliers</I></U></font></a>

# <font color="darkred">Nous nous baserons également dans ce sujet sur le DataFrame "table", regroupant les transactions, les clients et les produits, où comme précédemment, nous y avons appliqué la fonction "entier" définie ci-dessous pour une plus belle présentation.

# In[488]:


def entier(a): return int(a);
def round2(a): return round(a, 2);

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

# In[489]:


def get_tranche(a):
    if a<=30: return("etudiant")
    elif a<=50: return("actif")
    else: return("senior")


# <font color="darkred">Nous avons vu dans la partie II.2 de la mission 2 que les clients de 18 ans étaient en surplus par rapport aux autres. Nous les considérerons donc comme des Outliers pour une analyse plus objective sur les âges des clients. Nous les retirerons donc de nos données.

# In[490]:


def drop_18(data): return(data.loc[data.age!=18])


# <font color="darkred">Aussi, en constatant certaines dépenses exhorbitantes lors de cette même mission 2, nous pouvons fortement supposer que certains clients s'approvisionnent chez nous pour le compte d'une entreprise. Nous les identifierons à nouveau ci-dessous afin de les supprimer de nos tableaux pour des résultats plus objectifs sur nos clients et leurs tendances d'achats mêmes.

# In[491]:


def sup_depenses(data, p): return(data[data["depense_annuelle"]>p][["client_id", "depense_annuelle"]])


# <font color="darkred">La fonction nuage() prendra en paramètres un DataFrame data donné ainsi que deux de ses variables V1 et V2, afin d'en déterminer la droite de régression linéaire de V1 en fonction de V2, puis d'en tracer le diagramme de dispersion accompagné de cette droite.

# In[492]:


def nuage(data, V1, V2, couleur1, couleur2):
    dim(10, 5)
    
    # Calculs des paramètres a et b de la droite de régression linéaire (coefficient directeur et ordonnée à l'origine):
    X, Y = data[[V1]], data[V2] 
    X = X.assign(intercept = [1]*len(X))
    lr = sm.OLS(Y, X).fit()
    a, b = lr.params[V1], lr.params["intercept"]
    
    # Ici, on détermine l'intervalle d'affichage de cette droite:
    X = data[V1]
    fenetre = np.arange(min(X), max(X))
    
    # On affiche maintenant le diagramme de dispersion accompagné de cette fameuse droite:
    plt.plot(X, Y,  "o", color=couleur1)
    plt.plot(fenetre, [a*x+b for x in fenetre], color=couleur2, linewidth=3)


# <font color="darkred">Pour chaque diagramme de dispersion tracé, on affichera juste en-dessous le coefficient de corrélation de Pearson de ces deux variables et sa p_value avec la fonction pearson().

# In[513]:


def pears(data, V1, V2):
    X, Y = data[V1], data[V2]
    pearson = st.pearsonr(X, Y)[0]
    p_value = st.pearsonr(X, Y)[1]
    print("Coefficient de corrélation de Pearson:", pearson)
    print("Sa p_value est de:", p_value)


# ## <a id="m312"><font color="crimson"><U><I>I.2. Tableaux de support et suppression des Outliers</I></U></font></a>

# <font color="darkred">On reprendra notre DataFrame "table" définit en fin de mission 1 pour diverses analyses des corrélations à venir. Nous retirons donc les clients de plus de 18 ans de nos données et nous ajoutons la colonne "tranche" au DataFrame définie précédemment.

# In[494]:


# Suppression des clients âgés de 18 ans:
table=drop_18(table)

# Ajout de la colonne "tranche":
table["tranche"]=table["age"].apply(get_tranche)
table=table.reset_index(drop=True) ; table.head(3)


# <font color="darkred">Nous nous servirons également du DataFrame "clients" définie ci-dessous qui, basée sur "table", regroupe les données par clients, et renvoie le montant total de ce qu'ils ont dépensés en un an, ainsi que le nombre total de livres qu'ils ont achetés, toutes sessions confondues.

# In[495]:


# Création du DataFrame "clients":
clients = pd.DataFrame(table.groupby(["client_id", "sex", "age"]).sum()["price"]).reset_index()
clients.rename(columns={"price": "depense_annuelle"}, inplace=True)
nb_achats = pd.DataFrame(table["client_id"].value_counts()).reset_index()
nb_achats.columns=["client_id", "nombre_livres_achetes"]
clients=pd.merge(clients, nb_achats)

# Suppression des Outliers et ajout de la colonne "tranche":
clients=drop_18(clients)
clients["tranche"]=clients["age"].apply(get_tranche).reset_index(drop=True) ; clients.head(3)


# <font color="darkred">Observons les clients ayant dépensés plus de 1000 euros sur un an.

# In[496]:


sup_depenses(clients, 1000)


# <font color="darkred">Nous en observons un nombre trop important pour tous les considérer comme des Outliers. Fixons-nous un seuil de 3000 euros.

# In[497]:


sup_depenses(clients, 3000)


# <font color="darkred">On cible alors 4 clients qui ont dépensé plus de 50 mille euros en un an, et on peut admettre que les autres ont dépensé moins de 3000 euros. Ces 4 clients identifiés seront donc reconnus comme des Outliers et nous les retirons de nos données.

# In[498]:


clients=clients[clients.depense_annuelle<3000].reset_index(drop=True) ; clients


# <font color="darkred">Nous retirons également ces clients du DataFrame "table" et nous allons enfin pouvoir entammer l'analyse des corrélations.

# In[499]:


table=table.loc[table["client_id"].isin(clients["client_id"])==True] ; table


# ## <a id="m313"><font color="crimson"><U><I>I.3. Autres supports</I></U></font></a>

# <font color="darkred">Créons la table "mean_purchase_month" qui affiche la moyenne du nombre d'achats par mois pour chaque client avec leur âge.

# In[501]:


mean_purchase_month = table.pivot_table(index=["client_id", "age", "tranche"],
                          columns=["mois"],
                          values=["basket_size"],
                          aggfunc=sum)
mean_purchase_month=mean_purchase_month.fillna(0)
mean_purchase_month["mean_purchaseamonth"]=mean_purchase_month.mean(axis=1)
mean_purchase_month["mean_purchaseamonth"]=mean_purchase_month.mean_purchaseamonth.apply(round2)
mean_purchase_month=mean_purchase_month.reset_index()

mean_purchase_month.columns=["client_id", "age", "tranche",
                "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12",
               "mean_purchaseamonth"]

mean_purchase_month.drop(columns=["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12"], inplace=True)
mean_purchase_month.head(3)


# <font color="darkred">Remarquons la présence de quelques Outliers.

# In[502]:


len(mean_purchase_month[mean_purchase_month.mean_purchaseamonth>50])


# <font color="darkred">Sur 8600 clients, seuls 11 ont une moyenne d'achats par mois supérieure à 50. Pour donner un indice de corrélation plus fiable, on peut néglier ces 15 éléments en question.

# In[503]:


mean_purchase_month=mean_purchase_month[mean_purchase_month.mean_purchaseamonth<=50] ; mean_purchase_month


# <font color="darkred">Enfin, créons le DataFrame "panier", à partir de "table", afin d'avoir un tableau nous donnant chaque identifiant de client avec son âge et la taille moyenne de ses paniers pour l'ensemble de ses achats.

# In[504]:


panier = pd.DataFrame(table.groupby(["client_id", "age", "tranche"]).mean()["basket_size"]).reset_index()
panier.rename(columns={"basket_size": "panier_moyen"}, inplace=True)
panier["panier_moyen"]=panier["panier_moyen"].apply(round2) ; panier


#    

# # <a id="m32"><font color="firebrick"><U>II. Sexe des clients et catégories de produits achetés</U></font></a>

# ## <a id="m321"><font color="crimson"><U><I>II.1. Tableau de contingence réel</I></U></font></a>

# <font color="darkred">Nous cherchons, ici, à savoir si les hommes ou les femmes s'orientent plus vers telle ou telle catégorie  de livres. Créons dans un premier temps le tableau de contingence réel.

# In[522]:


c = table[["categ", "sex"]].pivot_table(index="categ", columns="sex", aggfunc=len)
cont =  c.copy()

tx = table["categ"].value_counts()
ty = table["sex"].value_counts()

cont.loc[:, "Total"], cont.loc["total", :] = tx, ty
cont.loc["total", "Total"] = len(table) ; cont


# <font color="darkred">Pour le moment, nous ne semblons pas distinguer de corrélations significatives. Mais la construction du tableau de contingence théorique en vue du tableau de contingence coloré peut contredire cette supposition.

# ## <a id="m322"><font color="crimson"><U><I>II.2. Tableau de contingence théorique</I></U></font></a>

# <font color="darkred">Créons maintenant le tableau de contingence théorique en vue d'un test des éventuelles corrélations.

# In[523]:


tx, ty = pd.DataFrame({"foo": tx}) , pd.DataFrame({"foo": ty})
indep=tx.dot(ty.T)/len(table) ; indep


# <font color="darkred">Mesurons alors le Chi-2, le degré de liberté et la p_value.

# In[507]:


mesure = (c-indep)**2/indep

xi_n = mesure.sum().sum()
ddl = (len(c)-1)*(len(c.columns)-1)
pvalue = st.chi2_contingency(c)[1]

pd.DataFrame({"": [str(ddl), round(pvalue, 20), xi_n]}, index=["Dégré de liberté", "pvalue", "Chi-2"])


# <font color="darkred">On s'aperçoit que la p_value est très proche de  0. Ce qui nous permet de rejeter l'hypothèse qu'il n'y a aucune indépendance entre le genre du client et les catégories de produits. On en déduit donc qu'il y a bien une corrélation entre le sexe des clients et les catégories de produits achetés.

# ## <a id="m323"><font color="crimson"><U><I>II.3. Tableau de contingence coloré</I></U></font></a>

# <font color="darkred">Analysons maintenant cette corrélation pour chacune des 3 catégories de livre avec un tableau de contingence coloré.

# In[508]:


dim(10, 5) ; sns.heatmap(mesure/xi_n, annot=c-indep)
plt.title("Tableau de contingence coloré - Sexe des clients et catégories de livres", fontsize=15)
plt.xlabel("Sexe", fontsize=12) ; plt.ylabel("Catégories", fontsize=15) ; plt.yticks(fontsize=15, rotation=0)
plt.axis("equal") ; plt.show()


# <font color="darkred">__Conclusion:__
# - Catégorie 0: Il y a une légère corrélation, en effet, les hommes semblent s'intéresser plus à cette catégorie de livres que les femmes.
# - Catégorie 1: Il y a corrélatation entre cette catégorie de livres et le genre du client. On voit ici que cette catégorie intéresse beaucoup plus les femmes que les hommes.
# - Catégorie 2: Le genre du client importe peu. Les femmes s'intéressent aussi fréquemment à cette catégorie de livres que les hommes.

#    

# # <a id="m33"><font color="firebrick"><U>III. Âge des clients et montant total des achats</U></font></a>

# ## <a id="m331"><font color="crimson"><U><I>III.1. Diagramme de dispersion</I></U></font></a>

# <font color="darkred">Nous nous baserons, cette fois-ci, sur les colonnes "age" et "depense_annuelle" du DataFrame "clients" définit en introduction de la mission 3.

# In[509]:


clients[["client_id", "age", "depense_annuelle"]]


# <font color="darkred">Déterminons maintenant le diagramme de dispersion entre l'âge des clients et le montant total des achats, la droite de régression linéaire de ce diagramme, ainsi que le coefficient de corrélation de Pearson afin d'avaluer s'il y a bien corrélation entre ces deux variables quantitatives.

# In[514]:


nuage(clients, "age", "depense_annuelle", "seagreen", "orange")
plt.title("Diagramme de dispersion âges, montant total", fontsize=20)
plt.xlabel("Âges") ; plt.ylabel("Montant total") ; plt.show()
pears(clients, "age", "depense_annuelle")


# <font color="darkred">Ce nuage de points nous laisse supposer, qu'il existe une corrélation négative entre l'âge des clients et le montant total des dépenses. À la vue de la "pente" de la droite de régression linéaire (coefficient directeur négatif) et par le calcul d'un coefficient de corrélation de Pearson proche de -0,2, on en conclue que l'on peut supposer une corrélation négative faible entre l'âge des clients et le montant total des achats: Plus un client est âgé, moins il dépense chez nous en un an. Cependant, aucune fonction affine à coefficient directeur négatif ne se dégage vraiment de ce nuage de  points si l'on analyse  le graphique sans le traçage  de la droite de régression linéaire. On observe d'ailleurs que les clients âgés d'entre 31 et 50 ans semblent dépenser plus que les moins de 30 ans, alors qu'on avait supposé une corrélation négative. Il serait donc plus judicieux d'étudier la corrélation entre les trois tranches d'âges des clients prédéfinies en introduction et le montant total des achats.

# ## <a id="m332"><font color="crimson"><U><I>III.2. Tranches d'âges et montant des achats</I></U></font></a>

# <font color="darkred">C'est par l'intermédiaire de boîtes à moustaches qu'on va vérifier s'il y a corrélation entre les trois tranches d'âges prédéfinies et la dépense annuelle.

# In[441]:


tranches = clients["tranche"].unique()
tranche_montant = []

for i in tranches:
    tranche_montant.append(clients[clients["tranche"]==i]["depense_annuelle"])

boxplot(tranche_montant, tranches)
plt.title("Montant total des dépenses selon les tranches d'âges", fontsize=18)
plt.xlabel("Somme des dépenses", fontsize=15) ; plt.ylabel("") ; plt.yticks(fontsize=15) ; plt.show()

print("Rapport de corrélation:", 100*round(eta_carre(clients["tranche"], clients["depense_annuelle"]), 3))


# <font color="darkred">Les moyennes de ces trois bloxplots semblent presque homogène. Avec un rapport de corrélation d'environ 8,9%, on peut en déduire une corrélation moyenne entre les tranches d'âges et le montant total des dépenses: Les "actifs" semblent  dépenser légèrement plus que les étudiants qui, eux, dépensent plus que les seniors.

# ---------

# # <a id="m34"><font color="firebrick"><U>IV. Âge des clients et fréquences d'achats</U></font></a>

# ## <a id="m341"><font color="crimson"><U><I>IV.1. Diagramme de dispersion</I></U></font></a>

# <font color="darkred">Ici, c'est la table "mean_purchase_month" qui nous sera utile. Elle renvoie la fréquence moyenne du nombre d'achats par mois de chaque client. Analysons le diagramme de dispersion en question.

# In[515]:


nuage(mean_purchase_month, "age", "mean_purchaseamonth", "turquoise", "darkgoldenrod")
plt.title("Diagramme de dispersion âges, fréquence d'achats par mois", fontsize=20)
plt.xlabel("Âges") ; plt.ylabel("Panier moyen par mois") ; plt.show()
pears(mean_purchase_month, "age", "mean_purchaseamonth")


# <font color="darkred">Malgré un coefficient de Pearson proche de  0, le nuage de points semble  indiquer une éventuelle corrélation entre  l'âge des clients et la fréquence d'achats: Les clients âgés de 31 à 50 effectuent plus d'achats chaque mois, que les tranches d'âges inférieure et supérieure. 

# ## <a id="m342"><font color="crimson"><U><I>IV.2. Tranches d'âges et fréquences d'achats</I></U></font></a>

# <font color="darkred">Il serait alors très intéressant de se demander s'il y a corrélation entre les tranches d'âges des  clients et cette  fréquence  d'achats.

# In[516]:


# On s'intéresse aux tranches d'âges présentes parmi les mean_purchase_month ayant effectué des achats dans chacune de 
# nos 3 catégories de produits:

tranches = mean_purchase_month["tranche"].unique()
frequence = []

for i in tranches:
    frequence.append(mean_purchase_month[mean_purchase_month["tranche"]==i]["mean_purchaseamonth"])

boxplot(frequence, tranches)
plt.title("Fréquence d'achats par mois par tranche d'âges", fontsize=18)
plt.xlabel("fréquence d'achats par mois") ; plt.ylabel("") ; plt.yticks(fontsize=15) ; plt.show()

print("Rapport de corrélation:", eta_carre(mean_purchase_month["tranche"], mean_purchase_month["mean_purchaseamonth"]))


# <font color="darkred">Notre supposition est vérifiée. Avec un rapport de corrélation très fort d'environ 35%, on peut fortement suggérer que les clients âgés d'entre 31 et 50 ans dépensent plus par mois que les deux autres tranches d'âges, à peu près équivalentes entre elles à ce niveau-là.

#    

# # <a id="m35"><font color="firebrick"><U>V. Âge des clients et taille du panier moyen</U></font></a>

# ## <a id="m351"><font color="crimson"><U><I>V.1. Diagramme de dispersion</I></U></font></a>

# <font color="darkred">Le DataFrame "panier" nous renvoie la taille moyenne des paniers des clients à l'issue des sessions d'achats. C'est sur celui-ci que nous traçons le diagramme de dispersion.

# In[517]:


nuage(panier, "age", "panier_moyen", "grey", "red")
plt.title("Diagramme de dispersion âges, panier moyen", fontsize=20)
plt.xlabel("Âges") ; plt.ylabel("Panier moyen") ; plt.show()
pears(panier, "age", "panier_moyen")


# <font color="darkred">Ce nuage de points nous laisse supposer, qu'il existe une corrélation négative entre l'âge des clients et le panier moyen. À la vue de la "pente" de la droite de régression linéaire (coefficient directeur négatif) et par le calcul d'un coefficient de corrélation de Pearson proche de -0,2, on en conclue qu'il existe une corrélation négative faible entre l'âge des clients et le panier moyen. L'absence  de points dans le rectangle [31; 50]x[0; 2] nous laisse penser que le panier moyen est globalement plus élevés chez  les  actifs. Comme pour la question 3, il ne se dégage aucune régression linéaire de ce nuage de points. C'est pourquoi nous allons encore une fois réétudier cette corrélation, cette fois-ci avec les tranches d'âges.

# ## <a id="m352"><font color="crimson"><U><I>V.2. Tranches d'âges et taille du panier moyen</I></U></font></a>

# <font color="darkred">Les boîtes à moustaches suivantes nous donneront un indice de cette éventuelle corrélation.

# In[134]:


tranches = panier["tranche"].unique()
size = []

for i in tranches:
    size.append(panier[panier["tranche"]==i]["panier_moyen"])

plt.boxplot(size, labels=tranches, showfliers=False, medianprops=medianprops, 
            vert=False, patch_artist=True, showmeans=True, meanprops=meanprops)
plt.title("Taille moyenne du panier par tranche d'âges", fontsize=14)
plt.xlabel("Taille moyenne du panier")
plt.ylabel("")
plt.show()

print("Rapport de corrélation:", 100*round(eta_carre(panier["tranche"], panier["panier_moyen"]), 3), "%")


# <font color="darkred">Le  rapport de  corrélation est supérieur  à 20%. On peut donc, à  la  vue  des boîtes, fortement  supposer une  corrélation simillaire à la celle de la question précédente: le panier moyen semble être plus élevés chez les personnes âgés d'entre 31 et 50  ans.

#     

#    

# # <a id="m36"><font color="firebrick"><U>VI. Âge des clients et catégories de produits achetés</U></font></a>

# ## <a id="m361"><font color="crimson"><U><I>VI.1. Rapport de corrélation</I></U></font></a>

# <font color="darkred">Cette fois-ci, on reprend notre DataFrame initial "table" sur lequel on analyse les éventuelles corrélations entre les âges des clients et les catégories de produits achetés.

# In[519]:


categories = table["categ"].unique()
categ_ages = []

for i in categories:
    categ_ages.append(table[table["categ"]==i]["age"])
    
boxplot(categ_ages, categories)
plt.title("Âge des clients et catégories de produits achetés", fontsize=18)
plt.xlabel("Âges", fontsize=15) ; plt.ylabel("Catégories", fontsize=15) ; plt.yticks(fontsize=15) ; plt.show()

print("Rapport de corrélation:", 100*round(eta_carre(table["categ"], table["age"]), 3), "%")


# <font color="darkred">Avec un rapport de corrélation d'environ 10%, on peut donc sereinement qu'il y a corrélation entre  l'âge des clients et les catégories de produits achetés: on remarque que la boîte à moustaches de la catégorie 2 diffère bien des deux autres, plus rapprochées. La catégorie 2 s'adresse globalement à une clientèle plus jeune, entre 18 et 25 ans, notamment, tandis que les moyennes d'âge des catégorie 0 et 1 semblent plus homogènes, et intéressent apparemment tout type de client, quelque soit l'âge.

# ## <a id="m362"><font color="crimson"><U><I>VI.2. Tranches d'âges et montant des achats</I></U></font></a>

# <font color="darkred">Afin d'appuyer nos suppositions, nous allons, une dernière fois, vérifier les potentielles corrélations entre les catégories de produits achetées et variable qualitative "tranche". Cette fois-ci, il s'agit donc de l'étude entre deux variables qualitatives, nous revenons donc au fameux tableau de contingence coloré.

# In[531]:


c = table[["categ", "tranche"]].pivot_table(index="categ", columns="tranche", aggfunc=len) ; cont =  c.copy()

tx, ty = table["categ"].value_counts(), table["tranche"].value_counts()
cont.loc[:, "Total"], cont.loc["total", :] = tx, ty
cont.loc["total", "Total"] = len(table) ; cont
tx, ty = pd.DataFrame({"foo": tx}) , pd.DataFrame({"foo": ty})
indep=tx.dot(ty.T)/len(table) ; indep

mesure = (c-indep)**2/indep
xi_n = mesure.sum().sum()
ddl = (len(c)-1)*(len(c.columns)-1)
pvalue = st.chi2_contingency(c)[1]

dim(12, 5) ; sns.heatmap(mesure/xi_n, annot=c-indep)
plt.title("Tranches d'âges des clients et catégories de livres", fontsize=18)
plt.xlabel("") ; plt.ylabel("Catégories", fontsize=15) ; plt.yticks(rotation=0, fontsize=15)
plt.axis("equal") ; plt.show()

print("pvalue:", pvalue) ; print("Chi-2:", xi_n)


# <font color="darkred">On observe finalement bien la corrélation supposée précédemment: Avec un pvalue nulle et un Chi-2 de 100 mille d'ordre de grandeur, on peut affirmer sans crainte que les étudiants s'intéressent beaucoup plus à la catégorie 2 que les actifs et les seniors. Pour les catégories 0 et 1, l'âge du client importe peu: tous semblent semblent porter à peu près le même degré d'intérêt pour chacune de ces deux catégories, qu'ils soient étudiants, actifs ou seniors.
