import pygame
import pygame_menu

from pokemonImage import PokemonImage, pokemon_coordinates
from pokemonJoueur import PokemonJoueur
from dataSeed import DataSeed
from paint import Paint
import threading

from config import SCREEN_WIDTH, SCREEN_HEIGHT
# Initialisation de pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Devipoke')
screen.fill("lightgray")

def game(images_pokemon):
    running = True
    threads = []
    print("Lancement de la partie...")
    screen.fill("lightgray")
    
    PokemonJoueur.selectPokemonAlea(screen) #selectionne une case aléatoire et en fait le pokemon du joueur
    
    for index, (image_url, is_shiny, name_pokemon, height, weight, imgType) in enumerate(images_pokemon):
        # Créer un thread pour chaque Pokémon et lancer le dessin en parallèle
        threadDessinPoke = threading.Thread(target=dessinPoke, args=(image_url, index, is_shiny, name_pokemon, height, weight, imgType))
        threads.append(threadDessinPoke)
        threadDessinPoke.start()  # Démarrer le thread
    
    for threadDessinPoke in threads:
        threadDessinPoke.join()  # Attendre la fin de tous les threads
    
    Paint.paint(screen, SCREEN_WIDTH, SCREEN_HEIGHT, pokemon_coordinates, running=True) #Appel de la fonction paint de la classe Paint pour pouvoir dessiner dans le jeu

    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
def dessinPoke(image_url, index, is_shiny, name_pokemon, height, weight, imgType):
    PokemonImage.drawPokemon(screen, image_url, index, is_shiny, name_pokemon, height, weight, imgType)

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
