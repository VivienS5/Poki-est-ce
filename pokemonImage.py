import pygame
import requests
from io import BytesIO

from dessinEtoiles import dessinEtoile

class PokemonImage:
    @staticmethod
    def drawPokemon(screen, image_url, index, is_shiny=False):
        x_start = 15  # Début de la ligne
        y_start = 15  # Début en hauteur
        spacing = 15  # Espacement entre les carrés

        x_offset = index % 5
        x = x_start + (150 + spacing) * x_offset
        
        y_offset = index // 5
        y = y_start + (150 + spacing) * y_offset
        
        pygame.draw.rect(screen, "lightblue", (x, y, 150, 150))
        
        if image_url:
            image_response = requests.get(image_url)
            img_poke = pygame.image.load(BytesIO(image_response.content))
            img_poke = pygame.transform.scale(img_poke, (150, 150))
            screen.blit(img_poke, (x, y))

            if is_shiny:
                star_size = 15
                star_color = (255, 255, 0)  # Jaune
                star_center = (x + 150 - star_size // 2, y + star_size // 2)
                etoile = dessinEtoile() #Utilise la classe Etoile pour dessiner l'étoile
                etoile.drawStar(screen, star_color, star_center, star_size)
        pygame.display.flip()
