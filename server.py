from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource 
import requests   
import ast

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
server = Blueprint('server', __name__,
                   url_prefix='/api/server')  # endpoint prefix 

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(server)

data = []

class ChessAPI:

    class _get(Resource):
        def get(self):
            return data

    class _push(Resource):
        def post(self):
            global data
            body = request.get_data(..., True)
            print(body)
            data.append(body)
            return data 
    
    class _start(Resource):
        def post(self):
            # request body format: "{'data' : {'uid1' : 1234, 'uid2' : 1234, 'move1' : 'move1', 'move2' : 'move2'}}"
            global data
            body = ast.literal_eval(request.get_data(..., True).replace("[", "{").replace("]", "}"))
            data.append(body)
            return data

    class _clear(Resource):
        def clear(self):
            global data
            data = []
            return data


    api.add_resource(_get, '/')
    api.add_resource(_push, '/post')
    api.add_resource(_start, '/start')
    api.add_resource(_clear, '/clear')

if __name__ == "__main__": 
    print("LMAO LOOSER!")