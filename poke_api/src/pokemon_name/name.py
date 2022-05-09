from .helpers import *


class Name:

    api_service = ''
    limit = 0
    offset = 0

    def __init__(self, api_service, limit, offset):
        self.api_service = api_service
        self.limit = limit
        self.offset = offset

    def name(self):
        response_json = get_data(self.api_service, self.limit, self.offset)
        return filter_names(response_json)
