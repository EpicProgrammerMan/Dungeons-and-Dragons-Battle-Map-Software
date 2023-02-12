from battlemap.views.app import app
import pytest
from tests.utils.api import request
from tests.utils import player

# https://circleci.com/blog/testing-flask-framework-with-pytest/

# Run with command: docker-compose exec battlemap poetry run pytest
TEST = [
       ( 'put', '/players', '{"name":"king blake the very cool"}' ),
       ( 'get', '/players', None ),
       ]
@pytest.mark.parametrize('requestType, endpoint, dataInput', TEST)
def test_api(cleanup, requestType, endpoint, dataInput):
    assert request(requestType, endpoint, dataInput).status_code == 200
# Write a test that creates a player, THEN updates their name or gets their information

def test_player_update(cleanup):
    """ Is a test that creates a player first, then sends a request involving it. """

    # Create the player.
    response = player.create()

    # Gets the id of the player.
    id = response.json['player_id']

    # Updates the player's name.
    player.rename(id, 'numberwang')

    # Checks the player's name.
    assert player.get(id).json['player_name'] == 'numberwang'