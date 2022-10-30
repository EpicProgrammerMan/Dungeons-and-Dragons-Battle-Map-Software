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
    app.run(debug = True, host = '0.0.0.0' )