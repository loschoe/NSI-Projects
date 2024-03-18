# Les importations de modules : 
import turtle as stylo
import random

# Initialisation du stylo turtle qui sera appelé stylo et certaines variables : 
x = 0 
y = 0 
positionx_toit = 0

# Initialisation des couleurs en mode rgb : 
def couleur_aleatoire():
    """Cette fonction utilise le code RGB pour créer des variables couleurs"""
    r = random.randint(1, 250)  # Composant rouge
    g = random.randint(1, 250)  # Composant verte
    b = random.randint(1, 250)  # Composant bleue
    return (r, g, b)

# Tracé de la ligne d'horizon de la ville : 
def horizon():
    """Cette fonction trace la ligne d'horizon verte pour placer les maisons"""
    stylo.penup()
    stylo.goto(-1250, -350) # Les coordonnées du début de l'écran 
    stylo.pencolor((0, 80, 0))  # Couleur verte 
    stylo.pendown()
    stylo.pensize(100)
    stylo.forward(2500)
    stylo.penup()
          
# Définition de la fonction étage : 
def etage(x, y):
    """Cette fonction nous permet de créer un étage pour n'importe quel bâtiment"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    stylo.setheading(0)
    stylo.setheading(0)
    stylo.goto(x, y)
    stylo.pendown()
    stylo.pensize(2)
    stylo_color = couleur_aleatoire()
    stylo.color("black", stylo_color)
    stylo.begin_fill()
    for i in range(2):
        stylo.forward(200)
        stylo.left(90)
        stylo.forward(100)
        stylo.left(90)
    stylo.end_fill()
    stylo.penup()

# Définition de la fonction porte :             
def porte(x, y):
    """Cette fonction permet de poser une porte sur chaque bâtiment"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    stylo.setheading(0)
    stylo.goto(x, y)
    stylo.pendown()
    stylo.pensize(2)
    stylo_color = couleur_aleatoire()
    stylo.color('black', stylo_color)
    stylo.begin_fill()
    for i in range(2):
        stylo.forward(30)
        stylo.left(90)
        stylo.forward(60)
        stylo.left(90)
    stylo.end_fill()
    stylo.penup()

# Définition de la fonction fenêtre qui comporte une sortie aléatoire de création de balcon : 
def fenetre(x,y):
    """Cette fonction ajoute 3 fenêtres sur chaque étage et aléatoirement un balcon"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    stylo.color('light blue','white')
    stylo.goto(x,y)
    stylo.setheading(0)
    stylo.begin_fill() 
    stylo.pendown()
    stylo.pensize(1)
    for i in range(4):                  
        stylo.forward(40)
        stylo.left(90)
    stylo.end_fill()
    stylo.penup()
    # Balcon 
    balcon = random.randint(1,5)
    if balcon == 1 :
        stylo.pencolor((0, 0, 0))
        stylo.pendown()
        stylo.pensize(1)
        for i in range(2):
            stylo.forward(50)
            stylo.left(90)
            stylo.forward(25)
            stylo.left(90)
        stylo.pensize(2)
        for i in range(10):
            stylo.forward(5)
            stylo.left(90)
            stylo.forward(25)
            stylo.forward(-25)
            stylo.right(90)
        stylo.penup()

# Définition de la fonction toit qui comporte une sortie aléatoire de création de cheminée :                                
def toit(x,y):
    """Cette fonction pose un toit sur chaque bâtiment et ajoute une cheminée aléatoirement"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    choix_toit = random.randint(1,2)

    if choix_toit == 1 : 
        triangle(x,y)
        cheminee_trg(x,y)
    else :  
        plat(x,y)

# Les types de toits :         
def triangle(x,y):
    """Le toit sur la maison est triangulaire"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    toit_color = couleur_aleatoire()
    stylo.color('black', toit_color)
    stylo.goto(x,y)
    stylo.setheading(0)
    stylo.pendown()
    stylo.begin_fill()
    stylo.pensize(2)
    stylo.forward(200)
    stylo.left(140)
    stylo.forward(130)
    stylo.left(80)
    stylo.forward(130)
    stylo.end_fill()
    stylo.penup()

def cheminee_trg(x,y):
    """La cheminée du toit triangulaire"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    stylo.setheading(0)
    stylo.forward(200)
    stylo.left(140)
    stylo.forward(50)
    stylo.right(50)
    stylo.pendown()
    stylo.begin_fill()
    stylo.forward(80)
    stylo.left(90)
    stylo.forward(25)
    stylo.left(90)
    stylo.forward(60)
    stylo.end_fill()
    stylo.penup()   

def plat(x,y):
    """Le toit sur la maison est plat"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    toit_color = couleur_aleatoire()
    stylo.color('black', toit_color)
    stylo.goto(x,y)
    stylo.setheading(0)
    stylo.pendown()
    stylo.pensize(7)
    stylo.forward(200)
    stylo.penup()
   
# Le première étage de chaque bâtiment est le même seulement la couleur change : 
def premier_etage_par_default(x,y):
    """Créer l'emplacement du premier bâtiment"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    etage(x,y)
    x += 30 
    porte(x,-300) 
    x += 100
    y += 50               
    fenetre(x,y)

    x = positionx_toit

# Boucle de code : 
def ville(x, y):
    """Cette fonction crée la ville aléatoirement en appelant les diverses fonctions"""
    assert isinstance(x, int) and isinstance(y, int), "Erreur : Les coordonnées doivent être des entiers."
    etage_count = 0  
    premier_etage_par_default(x, y)
    y += 100
    nb_etages = random.randint(1, 6)
    etage_count += 1 
    
    for i in range(nb_etages):
        if etage_count == nb_etages:
            toit(x, y)
        else: 
            x_temp = x  
            etage(x_temp, y)  
            x += 20
            y += 50
            fenetre(x, y)
            x += 60
            fenetre(x, y)
            x += 60
            fenetre(x, y)
            y += 50
            etage_count += 1
            x = x_temp

# Easters eggs des avions : 
def easter_egg():
    """Dessine l'avion d'Alexandre"""
    # Dessiner le corps de l'avion
    stylo.setheading(0)
    stylo.penup()
    stylo.goto(-50, 0)
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("white")
    stylo.forward(200)
    stylo.right(90)
    stylo.forward(100)
    stylo.right(90)
    stylo.forward(200)
    stylo.right(90)
    stylo.forward(100)
    stylo.end_fill()
    
    #Dessiner le nez de l'avion 
    stylo.begin_fill()
    stylo.backward(100)
    stylo.left(90)
    stylo.forward(75)
    stylo.goto(-50,0)
    stylo.end_fill()
    
    #Dessiner l'aile de l'avion
    stylo.setheading(0)
    stylo.forward(50)
    stylo.begin_fill()
    stylo.color("blue")
    for i in range(2):
        stylo.forward(100)
        stylo.right(-120)
    stylo.forward(100)
    stylo.end_fill()
    stylo.penup()

    # Fin de l'avion 
    stylo.goto(0,-100)
    stylo.setheading(0)
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("blue")
    for i in range(2):
        stylo.forward(100)
        stylo.right(120)
    stylo.forward(100)
    stylo.end_fill()
    stylo.penup()

    # Dessiner la queue de l'avion
    stylo.setheading(0)
    stylo.goto(150, -50)
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("blue")
    stylo.left(-90)
    stylo.forward(50)
    stylo.setheading(10)
    stylo.forward(40)
    stylo.goto(150, 50)
    stylo.end_fill()
    stylo.penup()

    # Dessiner le corps de l'avion
    stylo.setheading(0)
    stylo.goto(-50, 0)
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("white")
    stylo.forward(200)
    stylo.right(90)
    stylo.forward(100)
    stylo.right(90)
    stylo.forward(200)
    stylo.right(90)
    stylo.forward(100)
    stylo.end_fill()
    stylo.penup()
    
    # Dessiner les fenêtres de l'avion
    stylo.goto(-15, -35)
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("black")
    stylo.circle(10)
    stylo.end_fill()

    stylo.penup()
    stylo.goto(35, -35)
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("black")
    stylo.circle(10)
    stylo.end_fill()

    stylo.penup()
    stylo.goto(85, -35)
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("black")
    stylo.circle(10)
    stylo.end_fill()

    stylo.penup()
    stylo.goto(135, -35)
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("black")
    stylo.circle(10)
    stylo.end_fill()

stylo_color = (0,0,0)

def planes2():
    """Pose l'avion de Louis à la place de celui d'Alexandre"""
    stylo.goto(0,200)
    stylo.setheading(0)
    stylo.pendown()
    stylo.pensize(2)
    stylo.color(stylo_color)
    stylo.begin_fill()
    stylo.forward(70)   # Première distance !
    stylo.left(50)      # Premier angle !
    stylo.forward(100)  # La distance de l'aile !
    stylo.setheading(0) 
    stylo.forward(10)   
    stylo.right(90) 
    stylo.forward(80)   # Flaps ! 
    stylo.left(90)      
    stylo.forward(60)   # Bout de l'avion !
    stylo.left(50)      # Angle de la queue !
    stylo.forward(60)   # Morceau de queue !
    stylo.right(160) 
    stylo.forward(70)
    stylo.left(40)
    stylo.forward(70)
    stylo.left(200)
    stylo.forward(60)
    stylo.left(50)
    stylo.forward(60)
    stylo.left(90)
    stylo.forward(80)
    stylo.right(90)
    stylo.forward(10)
    stylo.right(50)
    stylo.forward(100)
    stylo.left(50)
    stylo.forward(70)
    stylo.end_fill()
    stylo.penup()
    stylo.goto(0,200)
    stylo.begin_fill()
    stylo.pendown()
    stylo.circle(23, 180)
    stylo.end_fill()