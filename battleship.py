from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from model_chess import getUser

from model_battleship import BattleshipUsers
from model_battleship import get_scores

battleship_user_api = Blueprint('battleship_user_api', __name__,
                   url_prefix='/api/battleship_users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(battleship_user_api)

class UserAPI:        
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('username')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            score = body.get('score')
            ''' #1: Key code block, setup USER OBJECT '''
            uo = BattleshipUsers(username=name, score=score)
            ''' #2: Key Code block to add user to database '''
            # create user in database
            uo.create()
            # success returns json of user
            if uo:
                return jsonify(uo.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {uo.username} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = BattleshipUsers.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    
    class _Scores(Resource):
        def get(self):
            return jsonify(get_scores())

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Scores, '/scores')
    api.add_resource(_Read, '/')