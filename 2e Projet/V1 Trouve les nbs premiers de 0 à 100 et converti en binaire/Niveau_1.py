# La fonction est_premier(nombre:int) effectue les mêmes tâches que la fonction recherche_premier() mais en plus compacte
def est_premier(nombre: int):
    diviseurs = 0
    for div in range(1, nombre + 1):
        if nombre % div == 0:
            diviseurs += 1
    if diviseurs == 2:
        return True
    else:
        return False

# La fonction convert_binaire(nombre) convertit un nombre décimal en sa représentation binaire et renvoie la chaîne binaire du nombre.
# Elle utilise la méthode vu en cours mais peut être remplacée par la fonction .bin
def convert_binaire(nombre):
    return_string = ""
    quotient, reste = nombre // 2, nombre % 2
    return_string += str(reste)
    while quotient != 0:
        reste = quotient % 2
        quotient = quotient // 2
        return_string += str(reste)
    return return_string[::-1] # Permet de faire l'inversion pour avoir la représentation binaire dans le bon sens

# Faire un exemple avec les nombres premiers de 0 à 100 et appeler la fonction est_premier()
premiers = [k for k in range(1,101) if est_premier(k)]
print([[i, convert_binaire(i) ]for i in premiers])