from battlemap.views.app import app
from battlemap.models.database import db_session
from battlemap.models.players import PlayerModel
from flask import request, jsonify, json
from battlemap.models.database import Base
from sqlalchemy import select

@app.route('/players', methods=['GET'])
def get_players():
    """ Returns a list of players. """
    
    # Gets a list of players from the database.
    stmt = select(PlayerModel)
    response = db_session.query(PlayerModel).all()
    db_session.commit()

    # return response
    mylist = []

    for i in response:
        mylist.append(i.__get__())

    return mylist

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