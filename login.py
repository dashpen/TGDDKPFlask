from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from model_chess import getName, ChessUsers

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
NameAPI = Blueprint('NameAPI', __name__, url_prefix='/api/names')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(NameAPI)

# Add CORS support to the NameAPI blueprint
def after_request(response):
    # Add the 'Access-Control-Allow-Origin' and 'Access-Control-Allow-Headers' headers to the response
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

class Login(Resource):
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
        return response

api.add_resource(Login, '/')
