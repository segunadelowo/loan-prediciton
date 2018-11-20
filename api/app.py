from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask import jsonify

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__': # only run on startup, if this file is called by another file dont run code below
    app.run(port=5001, debug=True)