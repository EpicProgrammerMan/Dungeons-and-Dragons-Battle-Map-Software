from battlemap.views.app import app
from battlemap.models.database import db_session
from battlemap.models.players import PlayerModel
from flask import request, jsonify
from battlemap.models.database import Base
from sqlalchemy import select

@app.route('/players', methods=['GET'])
def get_players():
    """ Returns a list of players. """
    
    # Gets a list of players from the database.
    stmt = select(PlayerModel)
    response = db_session.execute(stmt).fetchall()

    def response_dict(r):
        return dict(zip(r.keys(), r))

    def response_dicts(rs): 
        return list(map(response_dict, rs))

    return response_dicts(response)

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