from battlemap.views import init_api
from tests.utils.api import request
from json import dumps
# Imports all the api endpoints.
init_api()


def create():
    """ Make an api request to docker """
    return request('put', '/players', '{"name":"fish"}')

def rename(id, name):
    """ Renames a player. """
    return request('post', f'/player/{id}', dumps({"name":name}))
def get(id):
    """ Returns a player. """
    return request('get', f'/player/{id}', None)