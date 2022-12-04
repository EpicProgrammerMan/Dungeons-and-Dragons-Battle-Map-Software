# tutorial: https://www.youtube.com/watch?v=GVs26OxzE3o
from flask import Flask
# All API routes use Flask object. API objects need access to this.
# Split into player API, app object, and main.py.
app = Flask(__name__)