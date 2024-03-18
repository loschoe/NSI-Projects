#!/usr/bin/env python

import pygame
import sys

# Initialisation de pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

def meilleur_score():
    """
    Charge les meilleurs scores à partir du fichier 'best_score.tkt'.
    
    Returns:
        list: Une liste contenant les meilleurs scores pour chaque niveau.
    """
    records = []
    try:
        with open("best_score", 'r') as file:
            for line in file:
                try:
                    score = int(line.strip())
                    records.append(score)
                except ValueError:
                    pass  # Ignore les lignes qui ne peuvent pas être converties en entier
    except FileNotFoundError:
        # Si le fichier n'existe pas, initialise les scores à 0
        records = [0, 0, 0]
        with open("best_score", 'w+') as file:
            for score in records:
                file.write(str(score) + '\n')
    return records

def sauvegarde_scors(records):
    """
    Enregistre les meilleurs scores dans le fichier 'best_score'.

    Args:
        records (list): Liste des meilleurs scores.
    """
    with open("best_score", 'w') as file:
        for score in records:
            file.write(str(score) + '\n')

def draw_grid(screen, x, y, L, square_size, show_possible_moves):
    """
    Dessine le quadrillage de la fenêtre de jeu.

    Args:
        screen: Surface de la fenêtre de jeu.
        x (int): Position x du joueur.
        y (int): Position y du joueur.
        L (list): Labyrinthe.
        square_size (int): Taille d'une case du quadrillage.
        show_possible_moves (bool): Indique si les mouvements possibles doivent être affichés en bleu.
    """
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j * square_size, i * square_size, square_size, square_size))
            elif show_possible_moves and ((i == y and abs(j - x) == 3) or (j == x and abs(i - y) == 3) or \
                   (abs(i - y) == 2 and abs(j - x) == 2)):
                pygame.draw.rect(screen, BLUE, (j * square_size, i * square_size, square_size, square_size))
            else:
                color = SILVER
                pygame.draw.rect(screen, color, (j * square_size, i * square_size, square_size, square_size), 1)

def deplacement_possible(x, y, L, score, Record):
    """
    Vérifie si un mouvement est possible pour le joueur.

    Args:
        x (int): Position x du joueur.
        y (int): Position y du joueur.
        L (list): Labyrinthe.
        score (int): Score actuel.
        Record (int): Meilleur score.

    Returns:
        bool: True si un mouvement est possible, False sinon.
    """
    if y > 2 and L[y - 3][x] != 1:
        return True
    if y < len(L) - 3 and L[y + 3][x] != 1:
        return True
    if x > 2 and L[y][x - 3] != 1:
        return True
    if x < len(L[0]) - 3 and L[y][x + 3] != 1:
        return True
    if y < len(L) - 2 and x < len(L[0]) - 2 and L[y + 2][x + 2] != 1:
        return True
    if y < len(L) - 2 and x > 1 and L[y + 2][x - 2] != 1:
        return True
    if y > 1 and x > 1 and L[y - 2][x - 2] != 1:
        return True
    if y > 1 and x < len(L[0]) - 2 and L[y - 2][x + 2] != 1:
        return True
    print("Perdu ! Aucun mouvement possible", score, "cases fermées")
    print("Le record initial s'élève à : ", Record)
    if Record < score:
        Record = score
        print("Nouveau record !")

    return False


# Charge les meilleurs scores :
records = meilleur_score()

# Définit les niveaux :
tpr1 = 470
tpr23 = 800
ex1 = 10
ex2 = 20
ex3 = 100

niveau = input("Souhaitez-vous faire le niveau 1 (1), le niveau 2 (2), ou le niveau 3 (3) ?")
assert niveau in ['1', '2', '3'], "Niveau invalide !"

if niveau == "1":
    programme = ex1
    taille = tpr1
else:
    programme = ex2 if niveau == "2" else ex3
    taille = tpr23

# Définit la taille de la fenêtre de jeu :
width, height = taille, taille
square_size = width // programme
WINDOW_SIZE = (width, height)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Infernal")

# Initialise le labyrinthe et le joueur :
L = [[0 for _ in range(programme)] for _ in range(programme)]
x, y = 0, 0
score = 1

# Initialisation de la liste pour enregistrer la séquence des touches pressées
sequence_touches = []
historique_mouvements = []

# Variable pour indiquer si les mouvements possibles doivent être affichés en bleu
show_possible_moves = False

running = True
while running:
    if not deplacement_possible(x, y, L, score, records[int(niveau) - 1]):
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_z:
                if y > 2 and L[y - 3][x] != 1:
                    L[y][x] = 1
                    score += 1
                    historique_mouvements.append((x, y))
                    y -= 3

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if y < len(L) - 3 and L[y + 3][x] != 1:
                    L[y][x] = 1
                    score += 1
                    historique_mouvements.append((x, y))
                    y += 3

            elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                if x > 2 and L[y][x - 3] != 1:
                    L[y][x] = 1
                    score += 1
                    historique_mouvements.append((x, y))
                    x -= 3

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if x < len(L[0]) - 3 and L[y][x + 3] != 1:
                    L[y][x] = 1
                    score += 1
                    historique_mouvements.append((x, y))
                    x += 3

            elif event.key == pygame.K_x:
                if y < len(L) - 2 and x < len(L[0]) - 2 and L[y + 2][x + 2] != 1:
                    L[y][x] = 1
                    score += 1
                    historique_mouvements.append((x, y))
                    x += 2
                    y += 2

            elif event.key == pygame.K_w:
                if y < len(L) - 2 and x > 1 and L[y + 2][x - 2] != 1:
                    L[y][x] = 1
                    score += 1
                    historique_mouvements.append((x, y))
                    x -= 2
                    y += 2

            elif event.key == pygame.K_a:
                if y > 1 and x > 1 and L[y - 2][x - 2] != 1:
                    L[y][x] = 1
                    score += 1
                    historique_mouvements.append((x, y))
                    x -= 2
                    y -= 2

            elif event.key == pygame.K_e:
                if y > 1 and x < len(L[0]) - 2 and L[y - 2][x + 2] != 1:
                    L[y][x] = 1
                    score += 1
                    historique_mouvements.append((x, y))
                    x += 2
                    y -= 2

            # Option de revenir en arrière 
            if event.key == pygame.K_r:
                if historique_mouvements:
                    x, y = historique_mouvements.pop()
                    L[y][x] = 0  # Rétablir la case précédente
                    score -= 1  # Revenir au score d'avant
                    pygame.time.wait(200)

            # Option de quitter
            elif event.key == pygame.K_c:
                pygame.quit()
                sys.exit()

            # Activation de l'affichage des mouvements possibles en bleu
            elif event.key == pygame.K_i:
                show_possible_moves = True

        # Désactivation de l'affichage des mouvements possibles en bleu
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_i:
                show_possible_moves = False

    # Effacer l'écran
    screen.fill(WHITE)

    # Dessiner le quadrillage
    draw_grid(screen, x, y, L, square_size, show_possible_moves)

    # Afficher le joueur comme un carré bleu
    pygame.draw.rect(screen, BLUE, (x * square_size, y * square_size, square_size, square_size))

    # Rafraîchir l'écran
    pygame.display.flip()

# Met à jour les meilleurs scores si nécessaire
if score > records[int(niveau) - 1]:
    records[int(niveau) - 1] = score
    sauvegarde_scors(records)

pygame.quit()
sys.exit()
