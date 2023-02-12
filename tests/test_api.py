from battlemap.views.app import app
import pytest
from tests.utils.api import request

# https://circleci.com/blog/testing-flask-framework-with-pytest/

# Run with command: docker-compose exec battlemap poetry run pytest
TEST = [
       ( 'put', '/players', '{"name":"king blake the very cool"}' ),
       ( 'get', '/players', None ),
       ( 'get', '/player/1', None ),
       ( 'post', '/player/1', '{"name":"king blake the very cool and epic"}' ),
       ]
@pytest.mark.parametrize('requestType, endpoint, dataInput', TEST)
def test_flask(cleanup, requestType, endpoint, dataInput):
    assert request(requestType, endpoint, dataInput).status_code == 200