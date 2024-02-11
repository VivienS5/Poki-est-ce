import pygame
import pygame_menu
import requests
from io import BytesIO
import random

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
    chiffres_aleatoires = [random.randint(0, 1010) for _ in range(25)]  
    return chiffres_aleatoires #r'envoi les id des pokemon à demarrage_seed

def get_pokemon_data(idPokemon_gen): 
    global images_pokemon
    url = "https://tyradex.vercel.app/api/v1/pokemon"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        lien_image = ""
        for pokemon in data:
            if pokemon['pokedexId'] == idPokemon_gen:  
                is_shiny = random.randint(0, 3) == 0  # 1 chance sur 4 d'être shiny
                if is_shiny and pokemon['sprites']['shiny']:
                    lien_image = pokemon['sprites']['shiny']
                else:
                    lien_image = pokemon['sprites']['regular']
                images_pokemon.append((lien_image, is_shiny))  # Ajouter is_shiny à la liste des images
                print(lien_image, pokemon['name'], "Shiny:", is_shiny)  # Afficher si le Pokémon est shiny
    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")


def drawImage(image_url, index, is_shiny=False): #3.1 #dessine les images des pokemons
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
    if image_url:  # Vérifier si l'URL de l'image est valide
        image_response = requests.get(image_url)
        img_poke = pygame.image.load(BytesIO(image_response.content))
        img_poke = pygame.transform.scale(img_poke, (150, 150))

        # Blit the image onto the screen
        screen.blit(img_poke, (x, y))

        if is_shiny:  # Si le Pokémon est shiny
            # Dessiner une étoile jaune en haut à droite
            star_size = 15
            star_color = (255, 255, 0)  # Jaune
            star_center = (x + 150 - star_size // 2, y + star_size // 2)
            draw_star(screen, star_color, star_center, star_size)

def selectPokemonAlea(): #3.2 #selectionne une case aléatoire et en fait le pokemon du joueur
<<<<<<< HEAD
    random.seed() 
=======
    random.seed()
>>>>>>> ee2946bc3ee98ab97949dc7320ce2583496fbd1d
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
    for image_data in images_pokemon:
        image_url, is_shiny = image_data  # Extraire l'URL de l'image et l'indicateur shiny
        drawImage(image_url, nb_image, is_shiny)  # Passer l'URL de l'image et l'indicateur shiny à drawImage
        pygame.display.flip()
        nb_image += 1

    selectPokemonAlea()   
    dessin()
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def dessin(): #3.3 #permet de dessiner
    running = True
    drawing = False
    pixels_rouges = [] 
    fond_origine = screen.copy()  # Capture du fond d'écran d'origine

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.MOUSEMOTION and drawing:
                pos = pygame.mouse.get_pos()  
                if 0 <= pos[0] < SCREEN_WIDTH and 0 <= pos[1] < SCREEN_HEIGHT:  # Vérifier si la position est à l'intérieur des limites de la fenêtre
                    couleur_origine = screen.get_at(pos) 
                    pygame.draw.circle(screen, (255, 0, 0), pos, 3)  
                    pixels_rouges.append((pos, couleur_origine))  
                    pygame.display.flip() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: 
                    screen.blit(fond_origine, (0, 0)) 
                    pygame.display.flip()  
                    pixels_rouges = []  

        pygame.display.update()


def draw_star(surface, color, center, size):
    # Définir les points de l'étoile
    outer_points = [
        (center[0], center[1] - size),  # point supérieur
        (center[0] + size * 0.3, center[1] - size * 0.3),  # point supérieur droit
        (center[0] + size, center[1]),  # point droit
        (center[0] + size * 0.3, center[1] + size * 0.3),  # point inférieur droit
        (center[0], center[1] + size),  # point inférieur
        (center[0] - size * 0.3, center[1] + size * 0.3),  # point inférieur gauche
        (center[0] - size, center[1]),  # point gauche
        (center[0] - size * 0.3, center[1] - size * 0.3)  # point supérieur gauche
    ]

    # Dessiner l'étoile en reliant les points
    pygame.draw.polygon(surface, color, outer_points)

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
