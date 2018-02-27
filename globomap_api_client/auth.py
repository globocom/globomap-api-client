import json

import requests

from globomap_api_client import GLOBOMAP_API_ADDRESS


class Auth(object):

    def __init__(self, api_url, username, password):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.generate_token()

    def generate_token(self):
        res = self._make_request()
        self.token = res['token']['id']

    def _make_request(self):
        url = '{}/v2/auth'.format(self.api_url)
        data = {
            'username': username,
            'password': password
        }
        res = request.post(url, data=json.dumps(data))
        if res.status_code == 200:
            return res.json()
