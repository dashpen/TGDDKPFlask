from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model_roulette import Roulette

roulette_bp = Blueprint('roulette_bp', __name__,
                   url_prefix='/api/roulette')
roulette_api = Api(roulette_bp)


class RouletteAPI(Resource):
    class _Get(Resource):
        def get(self):
            user = request.args.get("user")
            try:
                roulette = db.session.query(Roulette).filter_by(_user=user).one()
                if roulette:
                    return roulette.to_dict()
            except:
                return {"message": "user not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user", required=True, type=str)
        parser.add_argument("score", required=True, type=int)
        args = parser.parse_args()

        roulette = Roulette(args["user"], args["score"])
        try:
            db.session.add(roulette)
            db.session.commit()
            return roulette.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user", required=True, type=str)
        parser.add_argument("score", required=True, type=int)
        args = parser.parse_args()

        try:
            roulette = db.session.query(Roulette).filter_by(_user=args["user"]).one()
            if roulette:
                roulette.score = args["score"]
                db.session.commit()
                return roulette.to_dict()
            else:
                return {"message": "roulette not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

            try:
                roulette = db.session.query(Roulette).get(args["id"])
                if roulette:
                    db.session.delete(roulette)
                    db.session.commit()
                    return roulette.to_dict()
                else:
                    return {"message": "roulette not found"}, 404
            except Exception as e:
                db.session.rollback()
                return {"message": f"server error: {e}"}, 500
    class _GetAll(Resource):
        def get(self):
            users = Roulette.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps


    roulette_api.add_resource(_Create, "/create") #
    roulette_api.add_resource(_Update, "/update")
    roulette_api.add_resource(_Remove, "/remove")
    roulette_api.add_resource(_GetAll, "/")
