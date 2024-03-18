L = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1],
     [1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1],
     [1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,1],
     [1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1],
     [1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1],
     [1,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1],
     [1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1],
     [1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,2],
     [1,0,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1],
     [1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,3,1],
     [1,0,0,1,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0,1],
     [1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,1],
     [1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1],
     [1,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1],
     [1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1],
     [1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1],
     [1,0,1,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1],
     [0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

x = 18
y = 0
cle =0
quit = False
egg=0

while quit == False:
    egg+=1
    print("tour", egg)
    if egg == 200:
        print("\n\n\n\n\n\ntu es trop nul dégage !\n\n\n\n\n\n")   # easter egg
        break
    # Créez une liste vide de 5 lignes et 10 colonnes pour T
    T = [["" for _ in range(20)] for _ in range(20)]

    coordone_x = -1
    coordone_y = -1

    # Parcourez la liste L
    for ligne in L:
        coordone_x = -1  # Réinitialisez coordone_x au début de chaque ligne
        coordone_y += 1  # Passez à la ligne suivante

        for elt in ligne:
            n = "   "
            if elt == 1:
                n = "▮▮▮"
            if elt == 2 :
                n = " ] "
            if elt == 3 :
                n = " 𝄞 "
            coordone_x += 1  # Passez à la colonne suivante
            T[coordone_y][coordone_x] = n

    # position du joueur 
    T[x][y] = " ♞ "


    # Affichez la grille T
    for ligne in T:
        print("".join(ligne))


# déplacements 
    playerInput = input("Entre votre déplacement (z,q,s,d) ou c pour quitter : ")
    if playerInput.lower() == "c":
        quit = True
        break

    ciblex = x
    cibley = y
    match playerInput:
        case "a" :
            print("envole toi")
            ciblex = 18
            cibley = 0
        case "zebi" :
            print("leon le roi des zebi")
        case "z":
            ciblex -= 1
        case "s":
            ciblex += 1
        case "d":
            cibley += 1
        case "q":
            cibley -= 1
    if L[ciblex][cibley] == 0 or L[ciblex][cibley] == 3:
        print("ok")
        if L[ciblex][cibley] == 3:
            cle = 1
            L[ciblex][cibley] = 0
        y = cibley
        x = ciblex
    if L[ciblex][cibley] == 2 and cle == 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\nBravo tu a fini en",egg, "\n\n\n")
        break
    if L[ciblex][cibley] == 2 and cle == 0:
        print("\n\n\n\n\n\n\n\n\n\n\n\ntu n'as pas la clé\n\n\n")
    if L[ciblex][cibley] == 1 :
        print("not ok")
