import pygame
import pygame_menu

from pokemonImage import PokemonImage, pokemon_coordinates
from pokemonJoueur import PokemonJoueur
from dataSeed import DataSeed
from paint import Paint

# Initialisation de pygame
pygame.init()

# Définition de la taille de l'écran
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 840
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Devipoke')
screen.fill("lightgray")

def game(images_pokemon):
    running = True
    print("Lancement de la partie...")
    screen.fill("lightgray")
    
    PokemonJoueur.selectPokemonAlea(screen) #selectionne une case aléatoire et en fait le pokemon du joueur
    
    for index, (image_url, is_shiny, name_pokemon) in enumerate(images_pokemon):
        print("------------", image_url, name_pokemon, "------------")
        PokemonImage.drawPokemon(screen, image_url, index, is_shiny, name_pokemon) #Dessine les pokemons sur l'écran

    Paint.paint(screen, SCREEN_WIDTH, SCREEN_HEIGHT, pokemon_coordinates, running=True) #Appel de la fonction paint de la classe Paint pour pouvoir dessiner dans le jeu

    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

def start_menu(): #1 & 3 #Menu début de partie

    menu = pygame_menu.Menu("WHO'S THAT POKEMON", SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_ORANGE)

    text_input = menu.add.text_input('Numero de partie :', default='', valid_chars=[0,1,2,3,4,5,6,7,8,9])
    
    def on_button_click():
        texte_entree = text_input.get_value()
        images_pokemon = DataSeed.demarrageSeed(texte_entree)  # Appel de demarrage_seed avec texte_entree
        print("Done fetching api")
        game(images_pokemon)  # Passer les données récupérées à la fonction game

    menu.add.button('Play', on_button_click) 
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)

start_menu()
