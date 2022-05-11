import src.pokemon_name.name as poke_name
import src.pokemon_procreate.procreate as poke_procreate
import src.pokemon_weight.weight as poke_weight


def execute_pokemon_names_process():
    pokemon_names = poke_name.Name('https://pokeapi.co/api/v2/pokemon?', 'limit=100000', '&offset=0')
    print(pokemon_names.name())

def execute_pokemon_procreate_process():
    raichu_procreate = poke_procreate.Procreate('https://pokeapi.co/api/v2/pokemon-species/', 'raichu')
    print(raichu_procreate.procreate())

def execute_pokemon_weight_process():
    fighting_weigh = poke_weight.Weight('https://pokeapi.co/api/v2/type/', '2')
    print(fighting_weigh.weight())
