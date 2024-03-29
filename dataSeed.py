import random
import requests

class DataSeed:
    @staticmethod
    def demarrageSeed(numeroUser):
        global numero_partie
        images_pokemon = []  # Liste pour stocker les données des Pokémon
        
        if numeroUser:
            numero_partie = int(numeroUser)
            resultats_seed_alea = chargementSeed(numero_partie)
            
            # Récupérer les données de chaque Pokémon séquentiellement
            for idPokemon_gen in resultats_seed_alea:
                pokemon_data = DataSeed.getPokemonData(idPokemon_gen)
                images_pokemon.append(pokemon_data)
                
            return images_pokemon
        else:
            print("Le champ du numéro de partie est vide.")

    @staticmethod
    def getPokemonData(idPokemon_gen):
        url = f"https://tyradex.vercel.app/api/v1/pokemon/{idPokemon_gen}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon = response.json()
            is_shiny = random.randint(0, 3) == 0
            name_pokemon = pokemon['name']['fr']
            height = pokemon['height']
            weight = pokemon['weight']
            imgType = pokemon['types']
            
            type_images = []
            for type_info in imgType:
                if "image" in type_info:
                    type_images.append(type_info["image"])
            
            if is_shiny and pokemon['sprites']['shiny']:
                lien_image = pokemon['sprites']['shiny']
            else:
                lien_image = pokemon['sprites']['regular']
            pokemon_data = (lien_image, is_shiny, name_pokemon, height, weight, type_images)
            
            return pokemon_data
        else:
            print(f"Failed to retrieve data for Pokemon ID {idPokemon_gen}. Status code: {response.status_code}")

def chargementSeed(numero_partie):
    random.seed(numero_partie) 
    chiffres_aleatoires = [random.randint(0, 1010) for _ in range(25)]  
    return chiffres_aleatoires
