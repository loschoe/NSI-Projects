#importation des modules keyboard et time permettant d'utiliser le clavier et d'attendre.

import keyboard
import time

#Définition de la liste L, le labyrinthe 
L = [
    ["■ ","■ ","■ ","■ ","■ ","■ ","■ ","■ ","■ ","■ ","■ "],
    ["■ ","  ","  ","  ","  ","  ","■ ","  ","  ","  ","■ "],
    ["■ ","  ","■ ","  ","■ ","  ","■ ","  ","■ ","  ","■ "],
    ["■ ","  ","■ ","  ","■ ","  ","⩎","  ","■ ","  ","■ "],
    ["■ ","  ","■ ","  ","■ ","  ","■ ","■ ","■ ","  ","■ "],
    ["■ ","§ ","■ ","  ","■ ","  ","■ ","  ","  ","  ","■ "],
    ["■ ","■ ","■ ","  ","■ ","  ","■ ","  ","■ ","■ ","■ "],
    ["■ ","  ","  ","  ","■ ","  ","■ ","  ","  ","  ","■ "],
    ["■ ","  ","■ ","■ ","■ ","  ","■ ","■ ","■ ","  ","■ "],
    ["■ ","  ","  ","☻ ","■ ","  ","  ","  ","■ ","⚑ ","■ "],
    ["■ ","■ ","■ ","■ ","■ ","■ ","■ ","■ ","■ ","■ ","■ "]
     ]

# La position d'arrivée x=9 y=9
# Départ en x=0 y=0

#Règles:
print("Vous pouvez utiliser les touches z,q,s et d pour vous mouvoir. Le joueur est matérialisé par un ☻, la sortie l'est par un ⚑, les murs sont des ■.")
print("Pour pouvoir passer la porte, il vous faudra obtenir la clé !")
print("Votre mission est d'atteindre la sortie. Bonne chance !")

#Fonction d'affichage

def affichage(L):
    for row in L :
        print("".join(row))
affichage(L)


#Départ en x=0 y=0
x,y=(9,3)
#compteur de mouvement
mouvement = 0

#Déplacements tant que le joueur n'est pas à la sortie
while True:
    if mouvement == 130 :
        print("Tu n'es pas le couteau le plus aiguisé du tirroir...")
        break   
    elif keyboard.is_pressed("z"):
        mouvement+=1
        time.sleep(0.1)
        if L[x-1][y] == "  ":
            L[x-1][y]="☻ "
            L[x][y]="  "
            x=x-1
            affichage(L)
        elif L[x-1][y] == "⚑ ":
            L[x-1][y]="☻ "
            L[x][y]="  "
            x=x-1
            affichage(L)
        elif L[x-1][y] == "§ ":
            L[x-1][y]="☻ "
            L[x][y]="  "
            x=x-1
            L[3][6]="  "
            affichage(L)
    elif keyboard.is_pressed("s"):
        mouvement+=1
        time.sleep(0.1)
        if L[x+1][y] == "  ":
            L[x+1][y]="☻ "
            L[x][y]="  "
            x=x+1
            affichage(L)
        elif L[x+1][y] == "⚑ ":
            L[x+1][y]="☻ "
            L[x][y]="  "
            x=x+1
            affichage(L)
        elif L[x+1][y] == "§ ":
            L[x+1][y]="☻ "
            L[x][y]="  "
            x=x+1
            L[3][6]="  "
            affichage(L)
    elif keyboard.is_pressed("d"):
        mouvement+=1
        time.sleep(0.1)
        if L[x][y+1] == "  ":
            L[x][y+1]="☻ "
            L[x][y]="  "
            y=y+1
            affichage(L)
        elif L[x][y+1] == "⚑ ":
            L[x][y+1]="☻ "
            L[x][y]="  "
            y=y+1
            affichage(L)
        elif L[x][y+1] == "§ ":
            L[x][y+1]="☻ "
            L[x][y]="  "
            y=y+1
            L[3][6]="  "
            affichage(L)
    elif keyboard.is_pressed("q"):
        mouvement+=1
        time.sleep(0.1)
        if L[x][y-1] == "  ":
            L[x][y-1]="☻ "
            L[x][y]="  "
            y=y-1
            affichage(L)
        elif L[x][y-1] == "⚑ ":
            L[x][y-1]="☻ "
            L[x][y]="  "
            y=y-1
            affichage(L)
        elif L[x][y-1] == "§ ":
            L[x][y-1]="☻ "
            L[x][y]="  "
            y=y-1
            L[3][6]="  "
            affichage(L)
    elif x==9 and y==9:
        print("Vous avez trouvé la sortie !")
        print("Vous avez réalisé",mouvement," mouvements avant de trouver la sortie.")
        break