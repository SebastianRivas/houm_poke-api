import re

from common.api_utils import *


def filter_names(response_json):
    matches = 0
    regex = r'^([b-zB-Z]*a[b-zB-Z]*at[b-zB-Z]*)*([b-zB-Z]*at[b-zB-Z]*a[b-zB-Z]*)*$'

    for pokemon in response_json['results']:
        match = re.search(regex, pokemon['name'])

        if match is not None:
            matches += 1

    return matches
