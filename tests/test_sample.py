# Simple example pytest script
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

from battlemap.views.app import app

# https://circleci.com/blog/testing-flask-framework-with-pytest/
def test_flask():
    breakpoint()
    headers = { "Content-Type": "application/json" }
    response = app.test_client().get('/players/2', headers=headers)
    # curl --header "Content-Type: application/json" --request GET http://localhost:8002/player/2