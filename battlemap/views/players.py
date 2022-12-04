from battlemap.views.app import app
from battlemap.models.database import db_session
from battlemap.models.players import PlayerModel
from flask import request, jsonify
# 3 ways to get data from request object.
# Anything after "?" is a query string.

@app.route('/players', methods=['GET'])
def get_players():
    """ Returns a list of players. """
    return 'Get players called'

@app.route('/players', methods=['PUT'])
def create_player():
    """ Creates a new player. """
    # Create the player object.
    name = request.json['name']
    player = PlayerModel(name=name)
    
    # Commit the player to the database.
    db_session.add(player)
    db_session.commit()

    # Return player data.
    response = {
        'player_id': player.id,
        'player_name': player.name,
        'player_created': player.created,
    }
    return jsonify(response)

    # HOMEWORK!!!!
    # FINISH THE REST OF THE APIs USING SQLALCHEMY!!!!!!!