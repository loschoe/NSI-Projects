# La fonction est_premier() est déjà connue pour reconnaître un nombre premier : 
# Cf niv 1
def est_premier(nombre: int):
    diviseurs = 0
    for div in range(1, nombre + 1):
        if nombre % div == 0:
            diviseurs += 1
    if diviseurs == 2:
        return True
    else:
        return False
    
# La fonction seuil() permet de rechercher les nombres premiers dans un seuil précis : 
def seuil():
    seuil = int(input("Quel est le seuil ?"))
    if seuil <= 2:
        seuil = int(input("Erreur, veuillez réessayer ! Quel est le seuil ?"))
    return seuil

# Le seuil récupéré par le input est utilisé dans la fonction range() ci-dessous : 
def results_pour_seuil():
    resultats = [k for k in range(seuil()) if est_premier(k)]
    return resultats

# Convertir un nombre en base hexadécimal : 
# Infication des lettres pour les nombres de 10 à 15 : 
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

# La fonction convert_hexa(nombre) convertit un nombre décimal en sa représentation hexadécimale et renvoie la chaîne hexadécimale du nombre : 
# Elle utilise la méthode vu en cours mais peut être remplacée par la fonction .hex
def convert_hexa(nombre):
    return_string = ""
    quotient, reste = nombre // 16, nombre % 16
    return_string += test(reste)
    while quotient != 0:
        reste = quotient % 16
        quotient = quotient // 16
        return_string += test(reste)
    return return_string[::-1] # Permet de faire l'inversion pour avoir la représentation hexadécimale dans le bon sens

# La fonction demande() permet à l'utilisateur de rechercher un nombre et lui donne sa représentation hexadécimale : 
def demande(): 
    nombre = int(input("Quel nombre voulez-vous rechercher ?"))
    if est_premier(nombre):
        print(f"{nombre} est un nombre premier.")
        print(f"Représentation hexadécimale de {nombre}: {convert_hexa(nombre)}")
    else:
        print(f"{nombre} n'est pas un nombre premier.")

# La fonction est_dyadique permet de rechercher si un nombre est diadique en prenant son carré et vérifiant si c'est un entier : 
def est_dyadique(nombre : float):
    for i in range(35): # Il faut utiliser un rang() assez bas sinon il y a un risque de bug 
        nombre *= 2
        if nombre % 1 == 0:
            return True 
        return False  

# La fonction est test_diadique() appelle la fonction est_dyadique pour l'utiliser : 
def test_dyadique():
    nombre = float(input("Entrez un nombre non entier à tester : "))
    if est_dyadique(nombre):
        print(f"{nombre} est un nombre diadique.")
    else:
        print(f"{nombre} n'est pas un nombre diadique.")

# Appel des fonctions : 
print(results_pour_seuil())
test_dyadique()