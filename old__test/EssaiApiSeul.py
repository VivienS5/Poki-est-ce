import requests

images_pokemon = []


def get_pokemon_data(idPokemon_gen): #2.2 #fais l'appel à l'API pour récupérer les images des pokemons
    global images_pokemon
    url = "https://pokebuildapi.fr/api/v1/pokemon/"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for pokemon in data:
            if pokemon['pokedexId'] in idPokemon_gen:  # recherche dans le pokedexId l'id qu'on génère
                lien_image = pokemon['image']
                images_pokemon.append(lien_image)   
        print(images_pokemon)
    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")

def envoi():
    
    idPokemon_gen = [1, 3, 5, 7, 9, 100]

    get_pokemon_data(idPokemon_gen)

envoi()