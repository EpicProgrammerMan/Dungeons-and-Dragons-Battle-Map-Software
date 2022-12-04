from battlemap.views.app import app
import json
# 3 ways to get data from request object.
# Anything after "?" is a query string.

@app.route('/players', methods=['GET'])
def get_players():
    """ Returns a list of players. """
    return 'Get players called'

@app.route('/players', methods=['PUT'])
def create_player():
    """ Creates a new player. """
    return 'Create player'
    