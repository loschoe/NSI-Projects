import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu de Parcours")

# Couleurs
blanc = (255, 255, 255)
rouge = (255, 0, 0)

# Position initiale du joueur
x_joueur = 50
y_joueur = hauteur_fenetre // 2

# Taille et vitesse du joueur
largeur_joueur = 50
hauteur_joueur = 50
vitesse_joueur = 5

# Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement du joueur
    touches = pygame.key.get_pressed()
    if touches[pygame.K_UP] and y_joueur > 0:
        y_joueur -= vitesse_joueur
    if touches[pygame.K_DOWN] and y_joueur < hauteur_fenetre - hauteur_joueur:
        y_joueur += vitesse_joueur
    if touches[pygame.K_LEFT] and x_joueur > 0:
        x_joueur -= vitesse_joueur
    if touches[pygame.K_RIGHT] and x_joueur < largeur_fenetre - largeur_joueur:
        x_joueur += vitesse_joueur

    # Dessiner la fenêtre
    fenetre.fill(blanc)
    pygame.draw.rect(fenetre, rouge, (x_joueur, y_joueur, largeur_joueur, hauteur_joueur))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.Clock().tick(30)
