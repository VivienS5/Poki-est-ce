import random
import requests

class DataSeed:
    @staticmethod
    def demarrageSeed(numeroUser): #2 #récupère les idPokemon et les envoi à get_pokemon_data pour faire la request api
        global numero_partie
        images_pokemon = []
        if numeroUser:  # Vérifier si le texte d'entrée n'est pas vide
            numero_partie = int(numeroUser)
            resultats_seed_alea = chargementSeed(numero_partie)
            print("Résultats :", resultats_seed_alea)
            for idPokemon_gen in resultats_seed_alea:
                images_pokemon.extend(getPokemonData(idPokemon_gen))
            return images_pokemon
        else:
            print("Le champ du numéro de partie est vide.")

def chargementSeed(numero_partie): #2.1 #récupere le chiffre de la patie pour en faire une seed faussement aleatoire pour selectrionner les pokemons
    random.seed(numero_partie) 
    chiffres_aleatoires = [random.randint(0, 1010) for _ in range(25)]  
    return chiffres_aleatoires #r'envoi les id des pokemon à demarrage_seed

def getPokemonData(idPokemon_gen):
    url = "https://tyradex.vercel.app/api/v1/pokemon"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_data = []
        for pokemon in data:
            if pokemon['pokedexId'] == idPokemon_gen:  
                is_shiny = random.randint(0, 3) == 0
                if is_shiny and pokemon['sprites']['shiny']:
                    lien_image = pokemon['sprites']['shiny']
                else:
                    lien_image = pokemon['sprites']['regular']
                pokemon_data.append((lien_image, is_shiny))
        return pokemon_data
    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")