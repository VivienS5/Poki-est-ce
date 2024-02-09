import pygame
import pygame_menu
import requests
from io import BytesIO
import random

# Ici je fais qu'un appel à l'api pour récupérer tout le putain de pokedex

# Initialisation de pygame
pygame.init()

# Définition de la taille de l'écran
SCREEN_WIDTH = 560
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Devipoke')
screen.fill("lightgray")

# Liste pour stocker les URLs des images des Pokémon
images_pokemon = []

def demarrage_seed(numeroUser): #2 #récupère les idPokemon et les envoi à get_pokemon_data pour faire la request api
    global numero_partie
    if numeroUser:  # Vérifier si le texte d'entrée n'est pas vide
        numero_partie = int(numeroUser)
        resultats_seed_alea = chargement_seed(numero_partie)
        print("Résultats :", resultats_seed_alea)
        for idPokemon_gen in resultats_seed_alea:
            get_pokemon_data(idPokemon_gen)
    else:
        print("Le champ du numéro de partie est vide.")

def chargement_seed(numero_partie): #2.1 #récupere le chiffre de la patie pour en faire une seed faussement aleatoire pour selectrionner les pokemons
    random.seed(numero_partie) 
    chiffres_aleatoires = [random.randint(0, 800) for _ in range(25)]  
    return chiffres_aleatoires #r'envoi les id des pokemon à demarrage_seed

def get_pokemon_data(idPokemon_gen): #2.2 #fais l'appel à l'API pour récupérer les images des pokemons
    global images_pokemon
    url = "https://pokebuildapi.fr/api/v1/pokemon/"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for pokemon in data:
            if pokemon['pokedexId'] == idPokemon_gen:  # recherche dans le pokedexId l'id qu'on génère
                lien_image = pokemon['image']
                images_pokemon.append(lien_image)   
                print(lien_image, pokemon['name'])
    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")

def drawImage(image_url, index): #3.1 #dessine les images des pokemons // j'ai demander à gpt de nettoyer ton code alors tu t'embrouilles avec lui :3
    # Define initial positions
    x = 10
    y = 10
    
    # Calculate x position based on index
    x_offset = index % 5
    if x_offset != 0:
        x = 110 * x_offset
    
    # Calculate y position based on index
    y_offset = index // 5
    if y_offset != 0:
        y = 110 * y_offset
    
    # Fetch the image from the URL
    image_response = requests.get(image_url)
    img_poke = pygame.image.load(BytesIO(image_response.content))
    img_poke = pygame.transform.scale(img_poke, (100, 100))
    
    # Blit the image onto the screen
    screen.blit(img_poke, (x, y)) # Afficher l'image à la position actuelle

def game(): #3 #Affichage de l'ecran de jeu
    running = True
    print("Lancement de la partie...")
    screen.fill("lightgray")
    nb_image = 0
    for url_image_poke in images_pokemon:
        drawImage(url_image_poke, nb_image)
        pygame.display.flip()
        nb_image += 1
        
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def start_menu(): #1 & 3 #Menu début de partie
    global numero_partie

    menu = pygame_menu.Menu('Welcome', 560, 560, theme=pygame_menu.themes.THEME_BLUE)

    text_input = menu.add.text_input('Numero de partie :', default='')
    
    def on_button_click():
        texte_entree = text_input.get_value()
        demarrage_seed(texte_entree)
        print("Done fetching api")

    menu.add.button('Validation', on_button_click) 
    menu.add.button('Play', game) 
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)

start_menu()
