import pytest

import pokemon.poke_api.src.pokemon_weight.weight as poke_weight


def test_function():
    fighting_weigh = poke_weight.Weight('https://pokeapi.co/api/v2/type/', '2')
    assert fighting_weigh.weight() == [1300, 195]
