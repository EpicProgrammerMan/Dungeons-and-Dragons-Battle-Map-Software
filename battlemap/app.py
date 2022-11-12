# tutorial: https://www.youtube.com/watch?v=GVs26OxzE3o
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Flask dockerized'

def main():
    """
    Start a web server to run the application.
    """
    # When debug = True, it tries to detect changes,
    # but since it's running with docker it can't really do that so it crashes
    app.run(debug = False, host = '0.0.0.0' )
    # print(__name__)