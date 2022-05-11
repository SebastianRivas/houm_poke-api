import pytest

import src.pokemon_procreate.procreate as poke_procreate


def test_function():
    raichu_procreate = poke_procreate.Procreate('https://pokeapi.co/api/v2/pokemon-species/', 'raichu')
    assert raichu_procreate.procreate() == 294
