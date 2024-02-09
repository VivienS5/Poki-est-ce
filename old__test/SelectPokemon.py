import pygame
import random
pygame.init()

# Définition de la taille de l'écran
SCREEN_WIDTH = 560
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Devipoke')
screen.fill("lightgray")

def selectPokemonAlea():
    pokeJoueur = random.randrange(1, 25)
    print(pokeJoueur)
    

def draw_blue_square(index):
    
    # Define initial positions with additional spacing
    x_start = 10  # Début de la ligne
    y_start = 10  # Début en hauteur
    spacing = 10  # Espacement entre les carrés

    # Calculate x position based on index
    x_offset = index % 5
    x = x_start + (100 + spacing) * x_offset
    
    # Calculate y position based on index
    y_offset = index // 5
    y = y_start + (100 + spacing) * y_offset
    
    # Draw blue square
    pygame.draw.rect(screen, "blue", (x, y, 100, 100))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Appel de la fonction pour dessiner les carrés bleus
    for i in range(25): 
        draw_blue_square(i)
    
    pygame.display.flip()

pygame.quit()
