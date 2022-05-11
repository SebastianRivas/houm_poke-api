from common.api_utils import *


def procreate_species(response_json):
    arr_species = []

    for egg_group in response_json['egg_groups']:
        egg_group_json = get_data(egg_group['url'])

        for pokemon_specie in egg_group_json['pokemon_species']:
            if pokemon_specie not in arr_species:
                arr_species.append(pokemon_specie)

    return arr_species
