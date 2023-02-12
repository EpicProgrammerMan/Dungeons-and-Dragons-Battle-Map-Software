from battlemap.views.app import app
from battlemap.views import init_api
# Imports all the api endpoints.
init_api()


def request(requestType, endpoint, dataInput):
    """ Make an api request to docker """
    headers = { "Content-Type": "application/json" }
    method = getattr(app.test_client(), requestType)
    return method( endpoint, headers=headers, data=dataInput )