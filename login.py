from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource 
import requests   
import json as JSON
import ast
from model_chess import check_password_hash
from model_chess import getUser
from model_chess import getName
# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
NameAPI = Blueprint('NameAPI', __name__,
                   url_prefix='/api/names')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(NameAPI)

data = []

class ChessAPI:
    class _check(Resource):
        def get(self):
            body = request.json()
            return check_password_hash




                


    # class _clear(Resource):


    api.add_resource(_check, '/')

if __name__ == "__main__": 
    print("LMAO LOOSER!")