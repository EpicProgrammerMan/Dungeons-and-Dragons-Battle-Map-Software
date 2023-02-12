from battlemap.views.app import app
from battlemap.models.database import db_session
from battlemap.models.players import PlayerModel
from flask import request, jsonify
from battlemap.models.database import Base
from sqlalchemy import select

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

# Updated to add "GET" before "POST"
@app.route('/player/<player_id>', methods=['GET', 'POST'])
def update_player(player_id):
    # I swear I updated this but it has changed back. Hmmm
    """ Creates a new player. """

    # The POST method is meant to change something about the player.
    # Lets change its name.
    newName = request.json['name']

    # Gets player from database whose id is the same as the id requested.
    stmt = select(PlayerModel).where(PlayerModel.id==player_id)

    player = db_session.execute(stmt).first()[0]
    
    player.name = newName

    # Now has to put the player back into the database apparently.
    # This doesn't work here, I want to replace one of the items
    # in the database. Not add a new one at the end.
    db_session.add(player)
    db_session.commit()

    return f'Update player called with {player_id}, set new name to be {newName}'