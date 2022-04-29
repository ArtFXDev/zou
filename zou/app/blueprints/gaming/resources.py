from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from zou.app.mixin import ArgsMixin

from zou.app.services import gaming_service


class GameResource(Resource, ArgsMixin):
    def get(self):
        return gaming_service.get_games()

    @jwt_required
    def post(self):
        (name) = self.get_arguments()
        return gaming_service.create_game(name)

    def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        args = parser.parse_args()

        return (args["name"],)


class GameScoreResource(Resource, ArgsMixin):
    def get(self, game_id):
        return gaming_service.get_scores_by_game(game_id)

    @jwt_required
    def post(self, game_id):
        (points) = self.get_arguments()
        return gaming_service.create_score(game_id, points)

    def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("points", type=int)
        args = parser.parse_args()

        return (args["points"],)
