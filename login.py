
from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource 
import requests   
import json as JSON
import ast
from model_chess import getName
from model_chess import ChessUsers


# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
NameAPI = Blueprint('NameAPI', __name__,
                   url_prefix='/api/names')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
app = Flask(__name__)
api = Api(NameAPI)

# Add CORS support to the NameAPI blueprint

class _Read(Resource):
    def post(self):
        body = request.get_json(force=True)
        name = body.get('name')
        if name is None or len(name) < 2:
            return {'message': f'Name is missing, or is less than 2 characters'}, 400
        password = body.get('password')
        user = getName(name)
        # user = ChessUsers.query.filter_by(_name=name).first()
             
        if user is None:
            return {'message': f"Invalid user id or password"}, 400
        
        if not user.is_password_match(password):
            return {'message': f"wrong password"}, 400
        response = jsonify(user.read())
        
        # Add the 'Access-Control-Allow-Origin' header to the response
        response.headers.add('Access-Control-Allow-Origin', 'https://genechang1.github.io')
        
        return response

api.add_resource(_Read, '/')
