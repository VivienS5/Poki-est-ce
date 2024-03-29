import pygame
import random

from config import NBR_POKEMON

class PokemonJoueur:
    @staticmethod
    def selectPokemonAlea(screen): #3.2 #selectionne une case aléatoire et en fait le pokemon du joueur
        random.seed()
        pokeJoueur = random.randrange(1, NBR_POKEMON)
        print(pokeJoueur)

        # Déterminez les coordonnées de la case aléatoire sur la grille 8x8
        row = (pokeJoueur - 1) // (NBR_POKEMON // 5)
        col = (pokeJoueur - 1) % (NBR_POKEMON // 5)

        # Calcul des coordonnées du coin supérieur gauche du rectangle du joueur
        rect_x = 10 + (150 + 15) * col
        rect_y = 10 + (150 + 15) * row

        # Dessiner le rectangle du joueur à ces coordonnées
        pygame.draw.rect(screen, "blue", (rect_x, rect_y, 160, 160), 5)