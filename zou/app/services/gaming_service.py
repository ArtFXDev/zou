from zou.app.models.gaming import Game, GameScore
from zou.app.services import (
    persons_service,
)


def get_games():
    return list(map(lambda x: x.serialize(), Game.get_all()))


def get_game(criterions):
    if isinstance(criterions, dict):
        game = Game.get_by(**criterions)
    else:
        game = Game.get_by(id=criterions)

    return game.serialize() if game else None


def create_game(name):
    game = get_game({"name": name})
    if not game:
        game = Game.create(name=name).serialize()

    return game


def create_score(game, points):
    game = get_game(game)
    player = persons_service.get_current_user()

    if game is None or player is None:
        raise Exception("The given game or player does not exists")

    return GameScore.create(
        game_id=game["id"],
        player_id=player["id"],
        points=points,
    ).serialize()


def get_scores_by_game(game, player=None):
    criterions = {"game_id": get_game(game)["id"]}
    if player is not None:
        criterions["player_id"] = persons_service.get_person(player)["id"]

    if game is None:
        raise Exception("The given game does not exists")

    return list(
        map(
            lambda x: x.serialize(),
            GameScore.get_all_by(**criterions),
        )
    )


def get_scores_by_player(player=None, game=None):
    criterions = {"player_id": persons_service.get_current_user().id}
    if player is not None:
        criterions["player_id"] = persons_service.get_person(player)["id"]
    if game is not None:
        criterions["game_id"] = get_game(game)["id"]

    if player is None:
        raise Exception("The given player does not exists")

    return list(
        map(
            lambda x: x.serialize(),
            GameScore.get_all_by(**criterions),
        )
    )
