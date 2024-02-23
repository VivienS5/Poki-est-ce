import pygame
import requests
from io import BytesIO

from dessinEtoiles import dessinEtoile
from paint import Paint

pokemon_coordinates = []
class PokemonImage:
    @staticmethod
    def drawPokemon(screen, image_url, index, is_shiny=False, name_pokemon="", height="", weight="", img_type=[]):
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

            coo_pokemon = (x, y, 150, 150)
            pokemon_coordinates.append((name_pokemon, coo_pokemon))
            # print("pokemon_coordinates:", pokemon_coordinates)

            screen.blit(img_poke, (x, y))

            if is_shiny:
                star_size = 15
                star_color = (255, 255, 0)  # Jaune
                star_center = (x + 150 - star_size // 2, y + star_size // 2)
                etoile = dessinEtoile() #Utilise la classe Etoile pour dessiner l'étoile
                etoile.drawStar(screen, star_color, star_center, star_size)
        
         # Afficher le poids et la taille en bas
            font = pygame.font.Font(None, 20)
            text_height = font.render(f"{height}", True, (255, 255, 255))
            text_weight = font.render(f"{weight}", True, (255, 255, 255))
            screen.blit(text_height, (x + 110, y + 135))
            screen.blit(text_weight, (x + 0, y + 135))

            print("Type:", img_type)

        # afficher le type en haut a gauche
        for i, img_type_url in enumerate(img_type):
            image_type = requests.get(img_type_url)
            img_type_traite = pygame.image.load(BytesIO(image_type.content))
            img_type_traite = pygame.transform.scale(img_type_traite, (25, 25))

            screen.blit(img_type_traite, (x + 0 * (i + 1), y))
            x += 25
            
        Paint.paint(screen, ..., ..., ..., running=False)
        pygame.display.flip()
        
