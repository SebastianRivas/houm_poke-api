from .helpers import *


class Weight:

    api_service = ''
    pokemon_type = ''

    def __init__(self, api_service, pokemon_type):
        self.api_service = api_service
        self.pokemon_type = pokemon_type

    def weight(self):
        response_json = get_data(self.api_service, self.pokemon_type)
        return weight_range(response_json)





