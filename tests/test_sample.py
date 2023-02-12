from battlemap.views.app import app
from battlemap.views import init_api
init_api()
import pytest

# https://circleci.com/blog/testing-flask-framework-with-pytest/

# Run with command: docker-compose exec battlemap poetry run pytest
# I can try using fixtures.
TEST = [
       ( 'put', '/players', '{"name":"king blake the very cool"}' ),
       ( 'get', '/players', None ),
       ( 'get', '/player/1', None ),
       ( 'post', '/player/1', '{"name":"king blake the very cool and epic"}' )
       ]
@pytest.mark.parametrize('requestType, endpoint, dataInput', TEST)
def test_flask(database, requestType, endpoint, dataInput):
    headers = { "Content-Type": "application/json" }
    method = getattr(app.test_client(), requestType)
    response = method( endpoint, headers=headers, data=dataInput )
    assert response.status_code == 200