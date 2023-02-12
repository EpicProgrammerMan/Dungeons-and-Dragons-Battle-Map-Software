from battlemap.views.app import app
from battlemap.models.database import db_session
from battlemap.models.players import PlayerModel
from flask import request, jsonify
from battlemap.models.database import Base
from sqlalchemy import select
from sqlalchemy import update

@app.route('/player/<player_id>', methods=['GET'])
def get_player(player_id):
    """ Returns the details of a specified player. """

    # Gets a single player from the database using its player id.
    stmt = select(PlayerModel).where(PlayerModel.id==player_id)
    player = db_session.execute(stmt).first()[0]

    # Must convert player object into string.
    response = {
        'player_id': player.id,
        'player_name': player.name,
        'player_created': player.created,
    }
    return jsonify(response)

@app.route('/player/<player_id>', methods=['GET', 'POST'])
def update_player(player_id):
    """ Creates a new player. """

    newName = request.json['name']

    stmt = (update(PlayerModel).where(PlayerModel.id == player_id).values(name=newName))
    db_session.execute(stmt)

    return f'Update player called with {player_id}, set new name to be {newName}'