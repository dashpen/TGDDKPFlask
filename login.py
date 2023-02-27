from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource 
import requests   
import json as JSON
import ast
from model_chess import check_password_hash
from model_chess import getUser
from model_chess import ChessUsers
# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
NameAPI = Blueprint('NameAPI', __name__,
                   url_prefix='/api/names')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(NameAPI)
class _Read(Resource):
        def get(self):
            body = request.get_json()
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 400
            password = body.get('password')
            user = ChessUsers.query.filter_by(_name=name).first()
            if user is None or not user.is_password(password):
                return {'message': f"Invalid user id or password"}, 400
            return jsonify(user.read())
            
api.add_resource(_Read, '/')