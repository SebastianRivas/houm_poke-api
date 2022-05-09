import pytest

import pokemon.poke_api.src.pokemon_name.name as poke_name


def test_function():
    pokemon_names = poke_name.Name('https://pokeapi.co/api/v2/pokemon?', 'limit=100000', '&offset=0')
    assert pokemon_names.name() == 8
