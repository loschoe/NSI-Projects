# Les importations des modules : 
import random
from Pubbly_lib import *

nbr_aleat = int(input("Combien de bâtiments souhaitez-vous ? (entre 2 et 6) (entrez 0 pour avoir une ville aléatoire)"))

# Création de la fenêtre et ses paramètres : 
# Définition du mode de couleurs rgb :  
stylo.colormode(255)
window = stylo.Screen()  
window.title("Welcome to the Pubbly city !")
LONGUEUR = 2500
HAUTEUR = 1500
window.setup(width=HAUTEUR, height=HAUTEUR, startx=0, starty=0)  
window.bgcolor(150, 200, 200)

# Initialisation du stylo turtle qui sera appelé stylo : 
stylo.speed(0)
x = 0 
y = 0 

# Initialisation du décord : 
horizon()

# Appel de la fonction principale et création de variables d'aléatoire : 
x = -630

assert isinstance(nbr_aleat, int), "Erreur ! Le nombre de bâtiments doit être un entier."
match nbr_aleat : 
    case 0 :
        nb_batiments = random.randint(2,6)
    case _ : 
        assert 2 <= nbr_aleat <= 6, "Erreur ! Le nombre de bâtiments doit être compris entre 2 et 6."
        nb_batiments = nbr_aleat
assert isinstance(nb_batiments, int), "Erreur ! Le nombre de bâtiments doit être un entier."

for i in range(nb_batiments):
    ville(x,-300)
    depl_partl = random.randint(1,3)
    match depl_partl:
        case 1 : 
            x += 200
        case 2 : 
            x += 225
        case 3 : 
            x += 225
        case _:
            assert False, "Erreur ! Mouvement de bâtiment invalide."

if nb_batiments==2:
    avion = random.randint(1,2)
    match avion : 
        case 1 : 
            easter_egg()
        case 2 : 
            planes2()

# Définir une fonction pour quitter la fenêtre turtle avec la touche 'c': 
def quitter():
    window.bye()
window.onkey(quitter, "c")
window.listen()
window.mainloop()
