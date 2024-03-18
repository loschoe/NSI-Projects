def intput(arg): return int(input(arg))   # Mon Invention !!!!

def recherche_premier():
    nombre = intput("Nombre ?")
    diviseurs = 0

    for div in range(1,nombre+1):
        if nombre % div == 0:
            diviseurs += 1
    if diviseurs == 2 : 
        print(nombre, "est premier !")
    else : 
        print(nombre, "n'est pas premier !")

def est_premier(nombre:int):
    diviseurs = 0

    for div in range(1,nombre+1):
        if nombre % div == 0:
            diviseurs += 1
    if diviseurs == 2 : 
        return True
    else : 
        return False


def convert_binaire(nombre):

    return_string = ""
    quotient, reste = nombre // 2, nombre % 2

    return_string += str(reste) # mettre le premier chiffre binaire

    while quotient != 0:
        quotient, reste = quotient // 2, quotient % 2
        return_string += str(reste)

    return return_string[::-1] # Pour mettre le code binaire dans le bon sens 

print([k for k in range(1,101) if est_premier(k)])
