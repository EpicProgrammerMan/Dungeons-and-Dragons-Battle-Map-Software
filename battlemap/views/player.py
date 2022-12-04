from battlemap.views.app import app
import json
# 3 ways to get data from request object.
# Anything after "?" is a query string.

@app.route('/player/<player_id>', methods=['GET'])
def get_player(player_id):
    """ Returns a list of players. """
    return f'Get player called with {player_id}'

@app.route('/player/<player_id>', methods=['POST'])
def update_player(player_id):
    """ Creates a new player. """
    return f'Update player called with {player_id}'