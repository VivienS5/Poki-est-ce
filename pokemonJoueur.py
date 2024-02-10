import pygame
import random

class PokemonJoueur:
    @staticmethod
    def selectPokemonAlea(screen): #3.2 #selectionne une case aléatoire et en fait le pokemon du joueur
        random.seed()
        pokeJoueur = random.randrange(1, 25)
        print(pokeJoueur)

        # Déterminez les coordonnées de la case aléatoire sur la grille 5x5
        row = (pokeJoueur - 1) // 5
        col = (pokeJoueur - 1) % 5

        # Calcul des coordonnées du coin supérieur gauche du rectangle du joueur
        rect_x = 10 + (150 + 15) * col
        rect_y = 10 + (150 + 15) * row

        # Dessiner le rectangle du joueur à ces coordonnées
        pygame.draw.rect(screen, "blue", (rect_x, rect_y, 160, 160), 5)