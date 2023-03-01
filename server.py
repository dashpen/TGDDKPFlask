from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource 
import requests   
import ast
import json as JSON

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
server = Blueprint('server', __name__,
                   url_prefix='/api/server')  # endpoint prefix 

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(server)

data = []

def changeToJSON(bad):
    good = ''
    for i in bad:
        if i != "'":
            good = good + i
        elif i == "'":
            good = good + '"'
    return JSON.loads(good)
class ChessAPI:

    class _get(Resource):
        def get(self):
            return data

    class _push(Resource):
        def post(self):
            global data
            body = request.get_data(..., True).replace("[", "{").replace("]", "}")
            data.append(body)
            return data 
    
    class _start(Resource):
        def post(self):
            # request body format: {'gid' : {'uid1' : 1234, 'uid2' : 1234, 'move1' : 'move1', 'move2' : 'move2'}}
            global data
            body = request.get_data(..., True).replace("[", "{").replace("]", "}")
            body = changeToJSON(body)
            data.append(body)
            return data
        
    class _secondPlayer(Resource):
        def post(self):
            # body format : "["uid", "gid"]"
            global data
            body = changeToJSON(request.get_data(..., True))
            i = -1
            for item in data:
                i += 1
                if body[1] in item:
                    data[i][body[1]]["uid2"] = body[0]
            return data

    class _clear(Resource):
        def post(self):
            global data
            data = []
            return data

    class _pushMove(Resource):
        def post(self):
            global data
            body = changeToJSON(request.get_data(..., True))
            i = -1
            for item in data:
                i += 1
                if body[0] in item:
                    data[i][body[0]]["move1"] = body[1]
                    data[i][body[0]]["move2"] = body[2]

    class _createNewGid(Resource):
        def get(self):
            global data
            i = 0
            gid = "game" + str(i)
            for item in data:
                if gid in item:
                    testingGid = list(item)[0]
                    gid = testingGid[:4] + str(int(testingGid[4:]) + 1)
                i += 1
            return gid

    class _removeGame(Resource):
        def post(self):
            global data
            body = (request.get_data(..., True))
            i = -1
            for item in data:
                i += 1
                if body in item:
                    del data[i]

    api.add_resource(_get, '/')
    api.add_resource(_push, '/post')
    api.add_resource(_start, '/start')
    api.add_resource(_clear, '/clear')
    api.add_resource(_secondPlayer, '/secondPlayer')
    api.add_resource(_pushMove, '/pushMove')
    api.add_resource(_createNewGid, '/createNewGid')
    api.add_resource(_removeGame, '/removeGame')



if __name__ == "__main__": 
    print("LMAO LOOSER!")