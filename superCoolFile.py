from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from model_chess import getUser

from model_chess import ChessUsers

chess_user_api = Blueprint('chess_user_api', __name__,
                   url_prefix='/api/chess_users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(chess_user_api)
class UserAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            # uid = body.get('uid')
            # if uid is None or len(uid) < 2:
            #     return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            password = body.get('password')
            dob = body.get('dob')

            ''' #1: Key code block, setup USER OBJECT '''
            uo = ChessUsers(name=name)
            
            ''' Additional garbage error checking '''
            # set password if provided
            if password is not None:
                uo.set_password(password)
            # convert to date type
            if dob is not None:
                try:
                    uo.dob = datetime.strptime(dob, '%m-%d-%Y').date()
                except:
                    return {'message': f'Date of birth format error {dob}, must be mm-dd-yyyy'}, 210
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            uo.create()
            # success returns json of user
            if uo:
                return jsonify(uo.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {uo.uid} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = ChessUsers.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps


    class _UpdateChessGame(Resource):
        def post(self, uid):
            body = request.get_json()
            user = getUser(uid)
            user.update_games(body)

    class _DeleteGame(Resource):
        def delete(self, uid, gameID):
            user = getUser(uid)
    
    class _DeleteUser(Resource):
        def delete(self, uid):
            user = getUser(uid)
            user.delete()
            return 'deleted user with uid ' + str(uid)


    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_UpdateChessGame, "/update_game/<int:uid>")
    api.add_resource(_DeleteUser, "/delete_user/<int:uid>")