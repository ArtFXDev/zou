from flask import Blueprint
from zou.app.utils.api import configure_api_from_blueprint

from .resources import GameResource, GameScoreResource


routes = [
    ("/data/gaming/<game_id>/scores", GameScoreResource),
    ("/data/gaming/games", GameResource),
]

blueprint = Blueprint("gaming", "gaming")
api = configure_api_from_blueprint(blueprint, routes)
