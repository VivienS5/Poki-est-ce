import pygame
import pygame_menu
import requests
from io import BytesIO
import random

# Ici je fais qu'un appel à l'api pour récupérer tout le putain de pokedex

# Initialisation de pygame
pygame.init()

# Définition de la taille de l'écran
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 840
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

def drawImage(image_url, index): #3.1 #dessine les images des pokemons
    # Define initial positions with additional spacing
    x_start = 15  # Début de la ligne
    y_start = 15  # Début en hauteur
    spacing = 15  # Espacement entre les carrés

    # Calculate x position based on index
    x_offset = index % 5
    x = x_start + (150 + spacing) * x_offset
    
    # Calculate y position based on index
    y_offset = index // 5
    y = y_start + (150 + spacing) * y_offset
    
    # Draw blue square
    pygame.draw.rect(screen, "lightblue", (x, y, 150, 150))
    
    # Fetch the image from the URL
    image_response = requests.get(image_url)
    img_poke = pygame.image.load(BytesIO(image_response.content))
    img_poke = pygame.transform.scale(img_poke, (150, 150))
    
    # Blit the image onto the screen
    screen.blit(img_poke, (x, y)) # Afficher l'image à la position actuelle

def selectPokemonAlea(): #3.2 #selectionne une case aléatoire et en fait le pokemon du joueur
    pokeJoueur = random.randrange(1, 25)
    print(pokeJoueur)

    # Déterminez les coordonnées de la case aléatoire sur la grille 5x5
    row = (pokeJoueur - 1) // 5
    col = (pokeJoueur - 1) % 5

    # Calcul des coordonnées du coin supérieur gauche du rectangle du joueur
    rect_x = 15 + (150 + 15) * col
    rect_y = 15 + (150 + 15) * row

    # Dessiner le rectangle du joueur à ces coordonnées
    pygame.draw.rect(screen, "blue", (rect_x, rect_y, 150, 150), 5)

def game(): #3 #Affichage de l'ecran de jeu
    running = True
    print("Lancement de la partie...")
    screen.fill("lightgray")
    nb_image = 0
    for url_image_poke in images_pokemon:
        drawImage(url_image_poke, nb_image)
        pygame.display.flip()
        nb_image += 1

    selectPokemonAlea()   

    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def start_menu(): #1 & 3 #Menu début de partie
    global numero_partie

    menu = pygame_menu.Menu("WHO'S THAT POKEMON", SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_ORANGE)

    text_input = menu.add.text_input('Numero de partie :', default='')
    
    def on_button_click():
        texte_entree = text_input.get_value()
        demarrage_seed(texte_entree)
        print("Done fetching api")
        game()

    menu.add.button('Play', on_button_click) 
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)

start_menu()
