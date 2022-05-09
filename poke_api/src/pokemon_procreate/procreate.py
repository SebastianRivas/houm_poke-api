from .helpers import *


class Procreate:
    
    api_service = ''
    pokemon = ''

    def __init__(self, api_service, pokemon):
        self.api_service = api_service
        self.pokemon = pokemon

    def procreate(self):
        response_json = get_data(self.api_service, self.pokemon)
        return len(procreate_species(response_json))
