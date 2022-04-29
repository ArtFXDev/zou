from sqlalchemy_utils import UUIDType

from zou.app import db
from zou.app.models.serializer import SerializerMixin
from zou.app.models.base import BaseMixin


class Game(db.Model, BaseMixin, SerializerMixin):

    name = db.Column(db.String(80))
    scores = db.relationship("GameScore", back_populates="game")

    def __repr__(self):
        return "<Game %s>" % self.id


class GameScore(db.Model, BaseMixin, SerializerMixin):

    points = db.Column(db.Integer)
    player_id = db.Column(
        UUIDType(binary=False), db.ForeignKey("person.id"), index=True
    )
    player = db.relationship("Person", back_populates="scores")
    game_id = db.Column(
        UUIDType(binary=False), db.ForeignKey("game.id"), index=True
    )
    game = db.relationship("Game", back_populates="scores")

    def __repr__(self):
        return "<GameScore %s>" % self.id
