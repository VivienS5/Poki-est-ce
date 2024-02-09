import pygame
import pygame_menu

# Initialisation de Pygame
pygame.init()

# Définition de quelques couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Définition des dimensions de la fenêtre
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Barre de progression Pygame")

# Création de la barre de progression
progress = 0
progress_bar = pygame.Rect(50, 150, 300, 20)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulation du chargement des images
    if progress < 100:
        progress += 1

    # Effacement de l'écran
    screen.fill(WHITE)

    # Dessin de la barre de progression
    pygame.draw.rect(screen, GREEN, (progress_bar.x, progress_bar.y, progress * 3, progress_bar.height))

    # Rafraîchissement de l'écran
    pygame.display.flip()

pygame.quit()
