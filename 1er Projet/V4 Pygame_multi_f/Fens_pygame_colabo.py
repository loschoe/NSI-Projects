import pygame
import keyboard
import time
import tkinter as tk
from PIL import Image, ImageTk

# Initialisation de pygame :
pygame.init()

# Définition des couleurs :
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLUEJ = (0, 208, 255)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
YELLOW = (255, 255, 0)

# Création de la fenêtre
WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Labyrinthe, utilise zqsd et passe par la clé pour trouver la sortie")

# Création de la liste représentant les murs et les zones de vide :
L = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1],
     [1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1],
     [1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,1],
     [1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1],
     [1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1],
     [1,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1],
     [1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1],
     [1,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,2],
     [1,0,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1],
     [1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,4,1],
     [1,0,0,1,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0,1],
     [1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,1],
     [1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1],
     [1,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1],
     [1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1],
     [1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1],
     [3,0,1,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1],
     [3,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

# Créez une liste vide de 5 lignes et 10 colonnes pour T
T = [["" for _ in range(20)] for _ in range(20)]

# Variables
# Joueur
x = 0
y = 18

a = 0
b = 17

cle = 0
quit = False

# Fonction pour centrer une image dans une fenêtre Tkinter
def center_image_label(window_width, window_height, image_width, image_height):
    x = (window_width - image_width) // 2
    y = (window_height - image_height) // 2
    return x, y

# Boucle de jeu :
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y > 0 and L[y - 1][x] != 1:
                    y -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if y < len(L) - 1 and L[y + 1][x] != 1:
                    y += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x > 0 and L[y][x - 1] != 1:
                    x -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if x < len(L[0]) - 1 and L[y][x + 1] != 1:
                    x += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if b > 0 and L[b - 1][a] != 1:
                    b -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if b < len(L) - 1 and L[b + 1][a] != 1:
                    b += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if a > 0 and L[b][a - 1] != 1:
                    a -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if a < len(L[0]) - 1 and L[b][a + 1] != 1:
                    a += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                pygame.quit()

    if L[y][x] == 4:
        L[8][19] = 5

    if L[b][a] == 4:
        L[8][19] = 5

    if L[y][x] == 5:
        print("T'as gagné sale fils de pute")
        root = tk.Tk()
        root.title("Bravo !!")

        # Chargement de l'image avec Pillow
        image_path = r"C:\Users\loschoe\OneDrive - College Episcopal Saint-Etienne de Strasbourg\NSI\petin.png"
        image_pil = Image.open(image_path)

        # Conversion de l'image pour l'utiliser avec Tkinter
        image_tk = ImageTk.PhotoImage(image_pil)

        # Création d'une étiquette pour afficher l'image
        label = tk.Label(root, image=image_tk)
        label.pack()

        # Récupération des dimensions de la fenêtre après affichage
        root.update_idletasks()

        # Calcul de la position pour centrer l'image
        x, y = center_image_label(root.winfo_reqwidth(), root.winfo_reqheight(), image_tk.width(), image_tk.height())

        # Positionnement de l'image au centre
        label.place(x=x, y=y)

        # Démarrage de la boucle principale Tkinter
        root.mainloop()

        pygame.quit()

    if L[b][a] == 5:
        print("T'as gagné sale fils de pute")
        root = tk.Tk()
        root.title("Bravo !!")

        # Chargement de l'image avec Pillow
        image_path = r"C:\Users\loschoe\OneDrive - College Episcopal Saint-Etienne de Strasbourg\NSI\petin.png"
        image_pil = Image.open(image_path)

        # Conversion de l'image pour l'utiliser avec Tkinter
        image_tk = ImageTk.PhotoImage(image_pil)

        # Création d'une étiquette pour afficher l'image
        label = tk.Label(root, image=image_tk)
        label.pack()

        # Récupération des dimensions de la fenêtre après affichage
        root.update_idletasks()

        # Calcul de la position pour centrer l'image
        x, y = center_image_label(root.winfo_reqwidth(), root.winfo_reqheight(), image_tk.width(), image_tk.height())

        # Positionnement de l'image au centre
        label.place(x=x, y=y)

        # Démarrage de la boucle principale Tkinter
        root.mainloop()

        pygame.quit()

    # Effacer l'écran
    screen.fill(WHITE)

    # Afficher le labyrinthe
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j * 40, i * 40, 40, 40))
            elif L[i][j] == 2:
                pygame.draw.rect(screen, RED, (j * 40, i * 40, 40, 40))
            elif L[i][j] == 3:
                pygame.draw.rect(screen, GREEN, (j * 40, i * 40, 40, 40))
            elif L[i][j] == 4:
                pygame.draw.rect(screen, SILVER, (j * 40, i * 40, 40, 40))
            elif L[i][j] == 5:
                pygame.draw.rect(screen, YELLOW, (j * 40, i * 40, 40, 40))

    # Afficher le joueur (cheval) comme un carré bleu
    pygame.draw.rect(screen, BLUE, (x * 40, y * 40, 40, 40))

    # Afficher le deuxième joueur
    pygame.draw.rect(screen, BLUEJ, (a * 40, b * 40, 40, 40))
    # Rafraîchir l'écran
    pygame.display.flip()

# Quitter pygame
pygame.quit()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    