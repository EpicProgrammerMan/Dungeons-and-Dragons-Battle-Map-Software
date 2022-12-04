from battlemap.views.app import app

@app.route("/")
def hello_world():
    return 'Flask dockerized'