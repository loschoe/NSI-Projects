# Interface : 
titre = '''
  _____      _           ______             _            
 |  __ \    (_)         |  ____|           (_)           
 | |__) | __ _ _ __ ___ | |__   _ __   __ _ _ _ __   ___ 
 |  ___/ '__| | '_ ` _ \|  __| | '_ \ / _` | | '_ \ / _ \\
 | |   | |  | | | | | | | |____| | | | (_| | | | | |  __/
 |_|   |_|  |_|_| |_| |_|______|_| |_|\__, |_|_| |_|\___|
                                      __/ |             
                                     |___/               
'''
infos = '''
[Mode 1] : Recherche d'un nombre premier
[Mode 2] : Recherche de tous les nombres premiers d'un seuil 
[Mode 3] : Recherche d'un nombre premier + conversion en binaire 
[Mode 4] : Recherche d'un nombre premier + conversion en hexadécimal 
[Mode 5] : Recherche d'un nombre diadique
[Mode 6] : Décomposer un nombre en produits de nombres premiers
[Mode L] : Lire les données du fichier txt
[Mode S] : Sauvegarder le résultat dans un fichier txt
[Mode Q] : Quitter 
[Mode E] : Supprime les données du fichier txt

'''

resultats = []
nom_fichier = 'resultats.txt'

# Fonction est_nombre_premier() déjà connue 
# Fonction déjà connue 
def est_nombre_premier(nombre):
    diviseurs = 0
    for div in range(1, nombre + 1):
        if nombre % div == 0:
            diviseurs += 1
    if diviseurs == 2:
        return True
    else:
        return False
########################################################################################################
########## MODE 1 #############
# Le mode 1 permet à l'utilisateur de rechercher si un nombre est premier ou non :
# Fonction déjà connue 
    
def mode1():
    nombre = int(input("Quel nombre voulez-vous rechercher ?"))
    if est_nombre_premier(nombre):
        resultats.append((nombre, "est premier"))
        print(f"{nombre} est un nombre premier.")
    else:   
        resultats.append((nombre, "n'est pas premier"))
        print(f"{nombre} n'est pas un nombre premier.")

########################################################################################################
########## MODE 2 #############
# Le mode 2 permet à l'utilisateur de rechercher si plusieurs nombres sont premiers :
# Fonction déjà connue 
        
def seuil():
        seuil = int(input("Quel est le seuil ?"))
        while seuil <= 2:
            seuil = int(input("Erreur, veuillez réessayer ! Quel est le seuil ?"))
        return seuil

def mode2():
    def trouver_nombres_premiers_jusquau_seuil(seuil):
        produits = [k for k in range(seuil) if est_nombre_premier(k)]
        return produits
    def afficher_resultats(produits):
        print("Nombres premiers jusqu'au seuil : ", produits)
    # Demander le seuil à l'utilisateur
    seuil_utilisateur = seuil()
    # Trouver les nombres premiers jusqu'au seuil
    resultats_premiers = trouver_nombres_premiers_jusquau_seuil(seuil_utilisateur)
    # Afficher les résultats
    resultats.append((resultats_premiers, "Les nombres premiers du seuil"))
    afficher_resultats(resultats_premiers)

########################################################################################################
########## MODE 3 #############
# Le mode 3 permet à l'utilisateur de convertir un ou plusieurs nombres en binaire:
# Fonction déjà connue 

def convert_binaire(*decimal_numbers) -> list[str]:
    '''Convertit un (des) nombre(s) décimal (aux) en binaire'''
    return_list = []

    for decimal_number in decimal_numbers:
        return_string = ""
        quot = decimal_number // 2
        rest = decimal_number % 2
        return_string += str(rest)

        while quot != 0:
            rest = quot % 2
            quot = quot // 2
            return_string += str(rest)
        return_list.append(return_string[::-1])
    return return_list

def mode3():

    action = input("Convertir n1 ou n1+ ? (un ou plusieurs ?)")
    if action == 'n1':
        nombre = int(input("Quel est le nombre ?"))
        resultats_binaire = convert_binaire(nombre)
        resultats.append(("Conversion de", nombre, "en binaire :", resultats_binaire))
        print(f"Conversion de {nombre} en binaire : {resultats_binaire}")
        
    
    elif action == 'n1+':
        nombres = list(map(int, input("Entrez plusieurs nombres séparés par des espaces : ").split()))
        resultats_binaires = convert_binaire(*nombres)
        for nombre, resultat_binaire in zip(nombres, resultats_binaires):
            resultats.append(("Conversion de", nombre, "en binaire :", resultat_binaire))
        print(f"Conversion de {nombres} en binaire : {resultats_binaires}")
        
########################################################################################################
########## MODE 4 #############
# Le mode 4 permet à l'utilisateur de convertir un ou plusieurs nombres en hexadécimale :
# Fonction déjà connue 

def test(reste):
    if reste == 10:
        return 'a'
    elif reste == 11:
        return 'b'
    elif reste == 12:
        return 'c'
    elif reste == 13:
        return 'd'
    elif reste == 14:
        return 'e'
    elif reste == 15:
        return 'f'
    else:
        return str(reste)

def convert_hexa(*nombres):
    return_list = []

    for nombre in nombres:
        return_string = ""
        quotient, reste = nombre // 16, nombre % 16
        return_string += test(reste)
        while quotient != 0:
            reste = quotient % 16
            quotient = quotient // 16
            return_string += test(reste)
        return_list.append(return_string[::-1])
    return return_list

def mode4():
    action = input("Convertir n1 ou n1+ ? (un ou plusieurs ?)")
    if action == 'n1':
        nombre = int(input("Quel est le nombre ?"))
        resultats_hexa = convert_hexa(nombre)
        print(f"Conversion de {nombre} en hexadécimal : {resultats_hexa}")
        resultats.append(("Conversion de", nombre, "en hexadecimal :", resultats_hexa))
    elif action == 'n1+':
        nombres = list(map(int, input("Entrez plusieurs nombres séparés par des espaces : ").split()))
        resultats_hexa = convert_hexa(*nombres)
        print(f"Conversions en hexadécimal : {resultats_hexa}")
        for nombre, resultat_hexa in zip(nombres, resultats_hexa):
            resultats.append(("Conversion de", nombre, "en hexadecimal :", resultat_hexa))

########################################################################################################
########## MODE 5 #############
# Le mode 5 permet à l'utilisateur de savoir si un nombre est dyadique :
# Fonction déjà connue 

def est_dyadique(nombre : float):
    for i in range(35):
        nombre *= 2
        if nombre % 1 == 0:
            return True 
        return False  
        
def mode5():
    nombre = float(input("Entrez un nombre non entier à tester : "))
    if est_dyadique(nombre):
        resultats.append((nombre, "est dyadique"))
        print(f"{nombre} est un nombre dyadique.")
    else:
        resultats.append((nombre, "n'est pas dyadique"))
        print(f"{nombre} n'est pas un nombre dyadique.")

########################################################################################################
########## MODE 6 #############
# Le mode 6 permet à l'utilisateur de décomposer un nombre en facteur premiers :        
# Pour ce faire, la variable va être divisée par des diviseurs tant qu'on peut (2 ; 3 ; 5 ...) puis les divisieurs sont notés dans une liste et elle est affichée 
def decomposer_en_nombres_premiers(nombre):
    facteurs_premiers = []
    diviseur = 2

    while nombre > 1:
        while nombre % diviseur == 0:
            facteurs_premiers.append(diviseur)
            nombre //= diviseur
        diviseur += 1

    return facteurs_premiers

def mode6():
    nombre = int(input("Quel nombre veux-tu décomposer en facteurs premiers ? "))
    resultat = decomposer_en_nombres_premiers(nombre)
    resultats.append(("Décomposition en facteurs premiers de", nombre, ":", resultat))
    print(f"Les facteurs premiers de {nombre} sont : {resultat}")

########################################################################################################
########## MODE 7 #############
# Le mode 7 permet à l'utilisateur de sauvegarder ses données dans un fichier txt :
# Création du fichier 
def sauvegarde_donnees(nom_fichier, resultats):
    with open(nom_fichier, 'a') as fichier:
        for element in resultats:
            fichier.write(str(element) + '\n')

# Sauvegarde 
def mode7():
    sauvegarde_donnees(nom_fichier, resultats)

########################################################################################################
########## MODE 8 #############
# Le mode 8 permet à l'utilisateur de lire les données stockées dans le fichier txt :
    
def mode8():
    try:
        with open(nom_fichier, 'r') as fichier:
            liste_lue = [eval(line.strip()) for line in fichier]
        print("Lecture du fichier resultats :", liste_lue)
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas encore. Veuillez exécuter le mode 7 pour créer le fichier.")

########################################################################################################
########## MODE 9 #############
# Le mode 9 permet à l'utilisateur de supprimer les données dans le fichier txt :
        
def mode9(nom_fichier):
    try:
        with open(nom_fichier, 'w') as fichier:
            fichier.write("")  # Réécrire complètement le fichier pour effacer son contenu
        print(f"Le contenu du fichier {nom_fichier} a été effacé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

########################################################################################################
# Utilisation de l'interface

# Affichage du Titre et des informations concernant les modes d'utilisation 
def main():
    print(titre)
    print(infos)

    # Création d'une boucle d'execution 
    while True:
        mode = input("Quel mode voulez-vous utiliser ? mod1 / mod2 / mod3 / mod4 / mod5 / mod6 / l / s / q / e : ")
        try:
            if mode == 'mod1':
                mode1()
            elif mode == 'mod2':
                mode2()
            elif mode == 'mod3':
                mode3()
            elif mode == 'mod4':
                mode4()
            elif mode == 'mod5':
                mode5()
            elif mode == 'mod6':
                mode6()
            elif mode == 's':
                mode7()
            elif mode == 'l':
                mode8()
            elif mode == 'e':
                mode9(nom_fichier)
            elif mode == 'q':
                break
            else:
                print("Mode non reconnu. Veuillez choisir un mode valide.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()