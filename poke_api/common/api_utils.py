import requests
from .helpers import *


def execute_service(service_url):
    response = requests.get(service_url)
    return response.json()


def get_data(url, *args):
    api_args = join_args(*args)
    service_url = url + api_args

    response_json = execute_service(service_url)
    return response_json
