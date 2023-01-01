# Simple example pytest script
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

from battlemap.views.app import app
from battlemap.views import init_api
init_api()

# https://circleci.com/blog/testing-flask-framework-with-pytest/
def test_flask():
    headers = { "Content-Type": "application/json" }
    response = app.test_client().get('/players', headers=headers)
    # curl --header "Content-Type: application/json" --request GET http://localhost:8002/player/2