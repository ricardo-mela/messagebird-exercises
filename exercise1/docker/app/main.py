from flask import Flask
api = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"
