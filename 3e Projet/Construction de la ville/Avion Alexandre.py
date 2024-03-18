# Les importations des modules : 
from turtle import *
import random

# Définition du mode de couleurs rgb :  
colormode(255)

# Création de la fenêtre et ses paramètres : 
window = Screen()  
window.title("Welcome to the Pubbly city !")
longueur = 2500
hauteur = 1500
window.setup(width=hauteur, height=hauteur, startx=0, starty=0)  
window.bgcolor(150, 200, 200)

# Initialisation du crayon turtle qui sera appelé stylo : 
stylo = Turtle()
stylo.speed(0)
x = 0 
y = 0 


def onze_septenbre():
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
    stylo.penup()
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("blue")
    stylo.forward(100)
    stylo.right(-120)
    stylo.forward(100)
    stylo.right(-120)
    stylo.forward(100)
    stylo.end_fill()
    stylo.penup()

    stylo.goto(0,-100)
    stylo.setheading(0)
    stylo.penup()
    stylo.pendown()
    stylo.begin_fill()
    stylo.color("blue")
    stylo.forward(100)
    stylo.right(120)
    stylo.forward(100)
    stylo.right(120)
    stylo.forward(100)
    stylo.end_fill()

    # Dessiner la queue de l'avion
    stylo.penup()
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

    # Dessiner les fenêtres de l'avion
    stylo.penup()
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

onze_septenbre()

window.mainloop()


