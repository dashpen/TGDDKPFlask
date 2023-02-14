from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource 
from model_chess import ChessUsers

import traceback

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
server2 = Blueprint('server2', __name__,
                   url_prefix='/api/server2')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(server2)

data = ["ada"]

class ChessAPI:

    class _get(Resource):
        def get(self):
            try:
                user = ChessUsers(name="aname", password="apassword", uid="12312")
                user.create()
            except Exception as e:
                return str(e)
            return user.read()

    class _push(Resource):
        def post(self):
            global data
            body = request.get_data(..., True)
            print(body)
            data.append(body)
            return data


    api.add_resource(_get, '/')
    api.add_resource(_push, '/post')
        

if __name__ == "__main__": 
    print("LMAO LOOSER!")