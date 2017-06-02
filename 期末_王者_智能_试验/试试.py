import requests
import json

class Daiwan(object):
    """docstring for Daiwan."""

    BASE_URL = 'http://lolapi.games-cube.com'
    USER_API_URL = '/UserArea'

    token = ''

    def __init__(self, token):
        self.token = token

    def get_user_info(self, username):
        headers = {'DAIWAN-API-TOKEN': self.token }
        return requests.get(self.BASE_URL + self.USER_API_URL + '?keyword=' + username, headers = headers).json()

demo = Daiwan('XXXX-XXXX-XXXX-XXXX')
print(demo.get_user_info('亚瑟'))
