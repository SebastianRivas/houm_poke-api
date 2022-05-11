from common.api_utils import *


def weight_range(response_json):
    arr_weight = []

    for pokemon_info in response_json['pokemon']:
        weight_json = get_data(pokemon_info['pokemon']['url'])

        if int(weight_json['id']) <= 151:
            arr_weight.append(weight_json['weight'])

    weight = [max(arr_weight), min(arr_weight)]

    return weight
