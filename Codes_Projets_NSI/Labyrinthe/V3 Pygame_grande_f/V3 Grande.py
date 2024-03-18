# les importations : 
import pygame 
import keyboard 
import time 
import tkinter as tk

##### Nous avons décidé de faire une interface tkinter et afficher le fonctionnement du jeu pour le joueur

# Fonction pour fermer la fenêtre
def fermer_window():
    window.destroy()
    
from tkinter import ttk
   
# Déclaration des variabless
ColorBG = '#ADD8E6'
ColorText = '#b1b5b5'
tab_font = ("Arial", 12)

# Créer une fenêtre principale + configs
window = tk.Tk()
window.title("The Labyrinthe")
window.geometry("1080x720")
window.minsize(480, 360)

# Bouton "Quitter" 
quit_bouton = tk.Button(window, text="Play !", font=("Arial", 15), bg="red", fg="white", command=window.quit)
quit_bouton.grid(row=3, column=0, padx=10, pady=10, sticky="n")  # Utilisation de padx et pady pour l'espacement

# Création du label "Bienvenue"
label_bienvenue = tk.Label(window, text="Bienvenue dans le Labyrinthe\nUtilisez zqsd ou les flèches directionnelles pour vous déplacer.\n Le joueur est le carré bleu\nLes clés à récupérer sont les carrés oranges\n Lorsque les portes sont ouvertes elles passent en jaune\n\nAmusez vous bien\n\nAppuyer sur le bouton en haut à gauche", font=("Calibri", 20))
label_bienvenue.grid(row=3, column=2, padx=10, pady=10, sticky="ns")
# Boucle principale
window.mainloop()



# Initialisation de pygame :
pygame.init()

# Définiton des couleurs : 
# Murs
# Personnage 
# Porte fermée
# clés 
# Porte ouverte  
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
ORANGE = (255,140,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Création de la fenetre 
WINDOW_SIZE = (799, 799)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Labyrinthe, utilise zqsd")

L = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,9,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1],
    [1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1],
    [1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1],
    [1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1],
    [1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
    [1,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
    [1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
    [1,1,0,1,0,0,1,0,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1],
    [1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1],
    [1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
    [1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
    [1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1],
    [1,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
    [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,6,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1],
    [1,0,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,7,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,1],
    [1,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
    [1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1],
    [1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,8,1,0,1,1,0,0,0,0,1,0,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1],
    [1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1],
    [1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1],
    [1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,1],
    [1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

T = [[""for _ in range(42)] for _ in range(42)]
SQUARE_SIZE = WINDOW_SIZE[0]/len(L)

# Variables 
# Joueur 
x = 1
y = 1
quit = False

# Boucle de jeu : 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if y > 0 and L[y - 1][x] != 1 and L[y - 1][x] != 2 and L[y - 1][x] != 3 and L[y - 1][x] != 4 and L[y - 1][x] != 5:
                    y -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if y < len(L) - 1 and L[y + 1][x] != 1 and L[y + 1][x] != 2 and L[y + 1][x] != 3 and L[y + 1][x] != 4 and L[y + 1][x] != 5:
                    y += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if x > 0 and L[y][x - 1] != 1 and L[y][x - 1] != 2 and L[y][x - 1] != 3 and L[y][x - 1] != 4 and L[y][x - 1] != 5:
                    x -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if x < len(L[0]) - 1 and L[y][x + 1] != 1 and L[y][x + 1] != 2 and L[y][x + 1] != 3 and L[y][x + 1] != 4 and L[y][x + 1] != 5:
                    x += 1
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y > 0 and L[y - 1][x] != 1 and L[y - 1][x] != 2 and L[y - 1][x] != 3 and L[y - 1][x] != 4 and L[y - 1][x] != 5:
                    y -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if y < len(L) - 1 and L[y + 1][x] != 1 and L[y + 1][x] != 2 and L[y + 1][x] != 3 and L[y + 1][x] != 4 and L[y + 1][x] != 5:
                    y += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x > 0 and L[y][x - 1] != 1 and L[y][x - 1] != 2 and L[y][x - 1] != 3 and L[y][x - 1] != 4 and L[y][x - 1] != 5:
                    x -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if x < len(L[0]) - 1 and L[y][x + 1] != 1 and L[y][x + 1] != 2 and L[y][x + 1] != 3 and L[y][x + 1] != 4 and L[y][x + 1] != 5:
                    x += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                pygame.quit()

#glitchs PASSPARTOUT et PORTUGUES
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                L[1][21] = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                L[21][10] = 10
                L[40][21] = 10
                L[21][41] = 10

    # Définition des clés :  
    if L[y][x] == 6:
        L[21][10] = 10
    # C2 
    if L[y][x] == 7:
        L[40][21] = 10
    # C3
    if L[y][x] == 8:
        L[21][41] = 10
    # C4 
    if L[y][x] == 9:
        L[0][20] = 10
    if (x, y) == (20, 0):
        running = False
        pygame.quit()

# Effacer l'écran
    screen.fill(WHITE)

    # Afficher le labyrinthe
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 2:
                pygame.draw.rect(screen, RED, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 3:
                pygame.draw.rect(screen, RED, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 4:
                pygame.draw.rect(screen, RED, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 5:
                pygame.draw.rect(screen, RED, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 6:
                pygame.draw.rect(screen, ORANGE, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 7:
                pygame.draw.rect(screen, ORANGE, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 8:
                pygame.draw.rect(screen, ORANGE, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 9:
                pygame.draw.rect(screen, ORANGE, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif L[i][j] == 10:
                pygame.draw.rect(screen, YELLOW, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    # Afficher le joueur (cheval) comme un carré bleu
    pygame.draw.rect(screen, BLUE, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Rafraîchir l'écran
    pygame.display.flip()