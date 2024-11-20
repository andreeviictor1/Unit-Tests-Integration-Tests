import math_func
import pytest
from pprint import pprint
from math_func import *



@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14


@pytest.mark.number
def test_divider():
    assert math_func.divider(10, 2) == 5
    assert math_func.divider(20) == 20
    assert math_func.divider(30, 2) == 15

def test_divide_zero():
    with pytest.raises(ValueError, match="Não pode ser divisivel por 0"):
        divider(1,0)


@pytest.mark.strings
def test_add_string():
    result = math_func.add('Hello ', 'World')
    assert result  == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result

@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello')
    assert result == 'HelloHello'
    assert type(result) is str
    assert 'Hello' in result


@pytest.mark.strings
def test_validator_email():
    assert math_func.validator_email('andre@teste.com')
    print("\nEmail Valido")
    assert math_func.validator_email('AndReT_es%te@teste.com')
    print("Email Valido")
    assert not math_func.validator_email('andre@test')
    print("Email Invalido")
    assert not math_func.validator_email('andre.test.com')
    print("Email Invalido")


@pytest.mark.fixture
def test_validator_api():
    resp = math_func.validator_api(1)
    pprint(resp)
    assert resp is not None


@pytest.fixture
def test_resposta_api():
    return validator_api(10)


@pytest.mark.fixture
def test_valida_resposta_api(test_resposta_api):
    variavel = test_resposta_api
    pprint(test_resposta_api)

    if variavel['name'] != 'Clementina DuBuque':
        print("\nUsuario nao Encontrado")
    else:
        assert test_resposta_api is not None
        print("\nUsuario Encontrado e Validado")

    # assert test_resposta_api['name'] != 'Clementina DuBuque'
    # print("\nUsuario nao Encontrado")
    # assert test_resposta_api['name'] == 'Clementina DuBuque'
    # print("\nUsuario Encontrado e Validado")


@pytest.mark.strings
def test_valida_pokemon_api():
    resultadoPoke = valida_pokemon_api("ditto")
    resultadoPoke2 = valida_pokemon_api("charmander")
    assert resultadoPoke is not None
    assert resultadoPoke["name"] == "ditto"
    assert resultadoPoke2 is not None
    assert resultadoPoke2["name"] == "charmander"


    print(f"\nNome do pokemon: " + resultadoPoke["name"])
    print(f"Nome do pokemon: " + resultadoPoke2["name"])






@pytest.mark.strings
def test_obter_todos_pokemons():
    resultadoPokemons = get_pokemons(limit=10)

    assert len(resultadoPokemons) > 0
    assert "bulbasaur" in resultadoPokemons
    print(f"\nTodos os nomes de Pokémons: ")
    for nome in resultadoPokemons:
        print(nome)