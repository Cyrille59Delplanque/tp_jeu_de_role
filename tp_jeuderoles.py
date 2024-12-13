# # TP : Jeu de rôle

# ### Étape 1 : Créer un dictionnaire de personnage

# Créez un dictionnaire représentant un personnage avec les clés suivantes :

# - **nom**
# - **classe**
# - **niveau**
# - **points_de_vie**
# - **inventaire**
#   - L'inventaire sera une liste de dictionnaires avec pour clés :
#     - **nom**
#     - **quantité**

# **Remarque : notre personnage commencera avec 3 potions de soin dans l'inventaire.**

# ## Les fonctions :

# ### 1. Ajouter des objets à l'inventaire :

# - Créez une fonction qui permet d'ajouter un ou plusieurs objets dans l'inventaire.

# ### 2. Modifier les statistiques :

# - Le personnage gagne un niveau et 20 points de vie supplémentaires.

# ### 3. Utiliser une potion de soin :

# Le personnage utilise une "potion de soin".

# - Supprimez cet objet de l'inventaire.
# - Ajoutez des points de vie aléatoires entre **1** et **50**.

# ### 4. Créer une fonction pour afficher les détails du personnage :

# Définissez une fonction `afficher_personnage(personnage)` qui affiche toutes les informations du personnage.

# ## Bonus :

# Implémentez une fonction `attaquer` qui prend deux personnages et réduit les points de vie du second personnage. Les dégâts infligés sont calculés comme suit :

# - **dégâts = 10 × niveau** du personnage attaquant.
# - Si le personnage attaqué meurt, alors l'attaquant récupérera l'intégralité de l'inventaire de son adversaire.

from random import randint

def model_personnage()->dict:
    """_model of caracters for the role play_

    Returns:
        dict: _all element that represent the caracter_
    """
    
    return {
       "nom":None,
       "classe":None,
       "niveau":None,
       "points de vie":None,
       "inventaire":None        
    }
    
def model_objet()->dict:
    """_model of the object that will be use in inventory_

    Returns:
        dict: _all element that are the object_
    """
    return {
       "nom":None,
       "quantité":None,      
    }
    
def visualisation_inventaire(inventaire:list):
    pass

def ajout_objet_inventaire(inventaire:list):
    pass

def modif_experience_personnage(personnage:dict):
    pass

def utiliser_fonction_soin(personnage:dict):
    pass

def supprimer_objet_inventaire(inventaire:list,objet:dict):
    pass

def ajout_point_de_vie(personnage:dict):
    pass

def afficher_personnage(personnage:dict):
    pass

def attaquer(personnage_attaquant:dict,personnage_attaque:dict):
    pass

def application_degat(personnage:dict):
    pass

def personnage_est_mort(personnage:dict):
    pass

def recuperation_inventaire(personnage_origine:dict,personnage_destinataire:dict):
    pass

def menu_du_jeu():
    pass

def affichage_menu():
    pass

def creation_personnage(liste_personnage:list):
    pass

def visualisation_liste_personnage(liste_personnage:list):
    pass
