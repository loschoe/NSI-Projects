# Les importations : 
from turtle import *
import random

# Définition du mode de couleurs 
colormode(255)

# Création de la fenêtre et ses paramètres : 
window = Screen()  
window.title("Welcome to the ALEXLOU city !")
longueur = 2500
hauteur = 1500
window.setup(width=hauteur, height=hauteur, startx=0, starty=0)  
window.bgcolor(150, 200, 200)

# Initialisation du crayon : 
stylo = Turtle()
stylo.speed(0)
x = 0 
y = 0 

# Initialisation des couleures : 
def couleur_aleatoire():
    r = random.randint(1, 250)  # Composante rouge
    g = random.randint(1, 250)  # Composante verte
    b = random.randint(1, 250)  # Composante bleue
    return (r, g, b)

# Tracé de la ligne d'horizon : 
stylo.penup()
stylo.goto(-1250, -350)
stylo.pencolor((0, 80, 0))  # Couleur fixe : verte 
stylo.pendown()
stylo.pensize(100)
stylo.forward(2500)
stylo.penup()

# Etage                hauteur 100, longueur 200
def etage(x, y):
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

# Porte                  hauteur 50, longueur 25
def porte(x, y):
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

# Toit                                 Longueur 200
def toit(x,y):  
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

# Fenêtre : 
def fenetre(x,y):
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

positionx_toit = 0
# Première étage 
def premier_etage_par_default(x,y):
    etage(x,y)        # Minimum pour l'étage -300, max 300
    x = x + 35 
    porte(x,-300) 
    x = x + 100
    y = y + 50               
    fenetre(x,y)

    x = positionx_toit



# Hauteur 100

premier_etage_par_default(-675,-300)
# Deuxième étage 
etage(-675, -200)
x = -675 
x = x + 20                     
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
# troisième étage  
etage(-675, -100)
x = -675                       
x = x + 20                     
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
# quatrième étage  
etage(-675, 0)
x = -675                        
x = x + 20                     
fenetre(x,50)
x = x + 60
fenetre(x,50)
x = x + 60
fenetre(x,50)
# cinquième étage  
etage(-675, 100)
x = -675                        
x = x + 20                     
fenetre(x,150)
x = x + 60
fenetre(x,150)
x = x + 60
fenetre(x,150)                       
# sixième étage  
etage(-675, 200)                       
x = -675                        
x = x + 20                     
fenetre(x,250)
x = x + 60
fenetre(x,250)
x = x + 60
fenetre(x,250)
# Toit :
positionx_toit = -675 
toit(positionx_toit, 300) 

premier_etage_par_default(-450,-300)
# Deuxième étage 
etage(-450, -200)
x = -450
x = x + 20                     
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
# troisième étage  
etage(-450, -100)
x = -450                       
x = x + 20                     
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
# quatrième étage  
etage(-450, 0)
x = -450                        
x = x + 20                     
fenetre(x,50)
x = x + 60
fenetre(x,50)
x = x + 60
fenetre(x,50)
# cinquième étage  
etage(-450, 100)
x = -450                        
x = x + 20                     
fenetre(x,150)
x = x + 60
fenetre(x,150)
x = x + 60
fenetre(x,150)                       
# sixième étage  
etage(-450, 200)                       
x = -450                        
x = x + 20                     
fenetre(x,250)
x = x + 60
fenetre(x,250)
x = x + 60
fenetre(x,250)
# Toit :
positionx_toit = -450
toit(positionx_toit, 300)

premier_etage_par_default(-225,-300)
# Deuxième étage 
etage(-225, -200)
x = -225
x = x + 20                     
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
# troisième étage  
etage(-225, -100)
x = -225                       
x = x + 20                     
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
# quatrième étage  
etage(-225, 0)
x = -225                      
x = x + 20                     
fenetre(x,50)
x = x + 60
fenetre(x,50)
x = x + 60
fenetre(x,50)
# cinquième étage  
etage(-225, 100)
x = -225                        
x = x + 20                     
fenetre(x,150)
x = x + 60
fenetre(x,150)
x = x + 60
fenetre(x,150)                       
# sixième étage  
etage(-225, 200)                       
x = -225                        
x = x + 20                     
fenetre(x,250)
x = x + 60
fenetre(x,250)
x = x + 60
fenetre(x,250)
# Toit :
positionx_toit = -225
toit(positionx_toit, 300) 

premier_etage_par_default(0,-300)
# Deuxième étage 
etage(0, -200)
x = 0 
x = x + 20                     
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
# troisième étage  
etage(0, -100)
x = 0                       
x = x + 20                     
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
# quatrième étage  
etage(0, 0)
x = 0                        
x = x + 20                     
fenetre(x,50)
x = x + 60
fenetre(x,50)
x = x + 60
fenetre(x,50)
# cinquième étage  
etage(0, 100)
x = 0                        
x = x + 20                     
fenetre(x,150)
x = x + 60
fenetre(x,150)
x = x + 60
fenetre(x,150)                       
# sixième étage  
etage(0, 200)                       
x = 0                        
x = x + 20                     
fenetre(x,250)
x = x + 60
fenetre(x,250)
x = x + 60
fenetre(x,250)
# Toit : 
positionx_toit = 0 
toit(positionx_toit, 300)

premier_etage_par_default(225,-300)
# Deuxième étage 
etage(225, -200)
x = 225 
x = x + 20                     
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
# troisième étage  
etage(225, -100)
x = 225                       
x = x + 20                     
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
# quatrième étage  
etage(225, 0)
x = 225                        
x = x + 20                     
fenetre(x,50)
x = x + 60
fenetre(x,50)
x = x + 60
fenetre(x,50)
# cinquième étage  
etage(225, 100)
x = 225                        
x = x + 20                     
fenetre(x,150)
x = x + 60
fenetre(x,150)
x = x + 60
fenetre(x,150)                       
# sixième étage  
etage(225, 200)                       
x = 225                       
x = x + 20                     
fenetre(x,250)
x = x + 60
fenetre(x,250)
x = x + 60
fenetre(x,250)
# Toit : 
positionx_toit = 225 
toit(positionx_toit, 300)

premier_etage_par_default(450,-300)
# Deuxième étage 
etage(450, -200)
x = 450 
x = x + 20                     
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
x = x + 60
fenetre(x,-150)
# troisième étage  
etage(450, -100)
x = 450                       
x = x + 20                     
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
x = x + 60
fenetre(x,-50)
# quatrième étage  
etage(450, 0)
x = 450                        
x = x + 20                     
fenetre(x,50)
x = x + 60
fenetre(x,50)
x = x + 60
fenetre(x,50)
# cinquième étage  
etage(450, 100)
x = 450                        
x = x + 20                     
fenetre(x,150)
x = x + 60
fenetre(x,150)
x = x + 60
fenetre(x,150)                       
# sixième étage  
etage(450, 200)                       
x = 450                      
x = x + 20                     
fenetre(x,250)
x = x + 60
fenetre(x,250)
x = x + 60
fenetre(x,250)
# Toit : 
positionx_toit = 450 
toit(positionx_toit, 300)

# Définir une fonction pour quitter quand la touche "c" est pressée
def quitter():
    window.bye()
window.onkey(quitter, "c")
window.listen()
window.mainloop()

# Lancement de la fenêtre : 
window.mainloop()




