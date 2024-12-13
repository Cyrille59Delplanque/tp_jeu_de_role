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

menu1 = "Creer Personnage"
menu2 = "Voir Inventaire"
menu3 = "Utliser objet dans Inventaire"
menu4 = "Voir tous les Personnages et le détail "
menu5 = "Attaquer Personnage "
menu6 = "Se deplacer "

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
       "inventaire":[]      
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
    """_inventory visualisation_

    Args:
        inventaire (list): _list of objet_
    """
    if len(inventaire) <0:
        print("L'Inventaire est vide")
    else:
        for objet in inventaire:
            print (f"{objet["quantité"]} {objet["nom"]}")

def ajout_objet_inventaire(inventaire:list):
    pass

def modif_experience_personnage(personnage:dict):
    personnage["niveau"] += 1
    personnage["point de vie"] += 20

def utiliser_fonction_soin(personnage:dict):
    pass

def supprimer_objet_inventaire(inventaire:list,objet:dict):
    pass

def afficher_personnage(personnage:dict):
    for denomination,valeur in personnage.items():
        if denomination != "inventaire":
            print(f"{denomination} : {valeur}")
        else:
            visualisation_inventaire(valeur)

def attaquer(personnage_attaquant:dict,personnage_attaque:dict):
    application_degat(personnage_attaque,10*int(personnage_attaquant["niveau"]))

def application_degat(personnage:dict,degat:int):
    personnage["point de vie"] -= degat

def personnage_est_mort(personnage:dict)->bool:
    return True if personnage["point de vie"] else False

def recuperation_inventaire(personnage_origine:dict,personnage_destinataire:dict):
    pass

def menu_du_jeu(choix:int):
    match choix:
        case 0:
            exit()
        case 1:
            print(f"---  {menu1} ---")
            creation_personnage(model_personnage())
        case 2:
            print(f"---  {menu2} ---")
            #voir inventaire
        case 3:
            print(f"---  {menu3} ---")
            #utiliser objet ds inventaire
        case 4:
            print(f"---  {menu4} ---")
            #voir tout les personnages et le detail
        case 5:
            print(f"---  {menu5} ---")
            #attaquer personnage
        case 6:
            print(f"---  {menu6} ---")
            #se deplacer
        case _:
            print("Selection Incorrecte")
    print() 

def affichage_menu()->int:
    print("=== MENU PRINCIPAL JEU DE ROLE SANA CYRILLE ===")
    print("1. "+menu1)
    print("2. "+menu2)
    print("3. "+menu3)
    print("4. "+menu4)
    print("5. "+menu5)
    print("6. "+menu6)
    print("0. Quitter le programme")
    while True:
        try:
            return int(input("Votre Choix: "))
        except ValueError as error:
            print("Entrée incorrecte: ",error)

def creation_personnage(personnage:dict)->dict: 
    """_create a caracter with 3 potion de soin_

    Args:
        personnage (dict): _a model of caracter_

    Returns:
        dict: _a caracter created with 3 item in inventory_
    """
    for cle in personnage.keys():
        if cle != "inventaire":
            personnage[cle]=controle_saisie(cle)
    ajout_objet_inventaire(personnage["inventaire"],creation_objet(model_objet(),"Potion de soin",3))
    return personnage

def creation_objet(objet:dict,nom_objet:str=None,quantite:int=0)->dict: 
    """_create an objet that can be taken in inventory_

    Args:
        objet (dict): _an object as model_
        nom_objet (str): _name of the object to create_ Defaults to None.
        quantite (int): _quantity of the object to create_ Defauts to 0

    Returns:
        dict: _the object created_
    """
    if nom_objet is None:
        for cle in objet.keys():
            objet[cle]=controle_saisie(cle)
    else:
        objet["nom"] = nom_objet
        objet["quantité"] = quantite
    return objet

def controle_champ_vide(entree:str) -> bool:
    """_Control fonction to avoid empty field_

    Args:
        entree (str): _input to control_

    Returns:
        bool: _True if input is empty, False if not empty_    
        
    """
    
    if len(entree) == 0 :
        print("Le champ ne peut être vide")
        return True
    else:
        return False

def controle_saisie(cle:str)->str:
    """_ask for input and control for an item  _

    Args:
        cle (str): _item of caracter or object_

    Returns:
        str: _a valid input for the item of the caracter_
    """
    liste_numerique = ["niveau","points de vie","quantité"]
    liste_majuscule = ["nom"]
    liste_title = ["classe"] 
    
    while True:
        entree = input(f"Veuilez entrer le {cle}: ")
        if cle in liste_numerique and not controle_champ_vide(entree) :
            try:
                entree = int(entree)
                if entree < 0:
                    print("La valeur entrée ne peut pas être négative:")
                else:
                    break        
            except ValueError as error:
                print("La valeur entrée n'est pas un chiffre valide: ",error)
        elif cle in liste_majuscule and not controle_champ_vide(entree) :
            entree = entree.upper()
            break
        elif cle in liste_title and not controle_champ_vide(entree) :
            entree = entree.title()  
            break 
    return entree  

def ajout_personnage_jeu(liste_personnage:list, personnage:dict):
    """_add a caracters into the list of caracters_

    Args:
        liste_personnage (list): _list àf caracters_
        personnage (dict): _caracter_
    """
    liste_personnage.append(personnage)

def visualisation_liste_personnage(liste_personnage:list):
    """_show the list of caracter in game_

    Args:
        liste_personnage (list): _list of caracter_
    """
    for personnage in liste_personnage:
        print (f"{personnage["nom"]} {personnage["classe"]}") 

def controle_objet_dans_la_liste(liste_objet:list,objet:dict)->tuple:
    """_control if the objet name is already in the list of object_

    Args:
        liste_objet (list): _list of object_
        objet (dict): _object_

    Returns:
        tuple: _bool,index bool True if in the list, False if not and index is the index in the list if is found_
    """
    if len(liste_objet) <0:
        return False,_
    index_liste_inventaire = 0
    for objet_de_la_liste in liste_objet:
        if objet["nom"] == objet_de_la_liste["nom"]:
            return True,index_liste_inventaire
        index_liste_inventaire += 1
    return False,_

def ajout_quantite_objet_dans_la_liste(liste_objet:list,index_list:int,quantite:int):
    """_add quanity of an objet alreay in the list_

    Args:
        liste_objet (list): _list of object_
        index_list (int): _position of the object in the list_
        quantite (int): _quantity to add_
    """
    liste_objet[index_list]["quantité"] += quantite

#définir max de point de vie, max de niveau (l'inclure dans le controle de la saisie), definir fonction deplacement pour trouver des objets
#définir qté max d'objet dans l'inventaire et controler en cas d'ajout
#creer un sous menu inventaire pour utiliser les objets

#test = creation_objet(model_objet())
test2= creation_objet(model_objet(),"Potion de soin",3)
print(test2)