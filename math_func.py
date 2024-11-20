import re
from re import match

import requests
from urllib3 import request


def add(x, y=2):
    return x + y

def product(x, y=2):
    return x * y

def divider(x, y=1):
    if y == 0:
        raise ValueError("Não pode ser divisivel por 0")
    return x/y


def validator_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))


def validator_api(id):
    apiusuario = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    if apiusuario.status_code == 200:
        return apiusuario.json()
    return None


def resposta_api():
    return validator_api(10)



def valida_pokemon_api(pokemonName):
    respostaAPI = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
    if respostaAPI.status_code == 200:
        return respostaAPI.json()
    return None



def resposta_pokemon_api(pokemonName):
    return valida_pokemon_api(pokemonName)


def get_pokemons(limit=10):
    pokemons = []
    url = "https://pokeapi.co/api/v2/pokemon"

    while url:
        respostaAPI2 = requests.get(url)
        if respostaAPI2.status_code == 200:
            dados = respostaAPI2.json()
            pokemons.extend([pokemon["name"] for pokemon in dados["results"]])
            if len(pokemons) >= limit:
                break
            url = dados["next"]
        else:
            break

    return pokemons[:limit]