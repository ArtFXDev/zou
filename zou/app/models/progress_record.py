from sqlalchemy_utils import UUIDType

from zou.app import db
from zou.app.models.serializer import SerializerMixin
from zou.app.models.base import BaseMixin


class ProgressRecord(db.Model, BaseMixin, SerializerMixin):
    """
    An asset instance is the representation of an asset in a given shot or
    layout scene. It is useful for complex scenes where an asset needs extra
    treatments only related to the given shot or layout scene.
    An asset can have multiple instances in a scene or in a shot (ex: a sword in
    a battle field).
    """

    value = db.Column(db.String(1200))
    shot_id = db.Column(
        UUIDType(binary=False), db.ForeignKey("entity.id"), index=True
    )
    shot = db.relationship("Entity", back_populates="progress")

    def __repr__(self):
        return "<ProgressRecord %s>" % self.id
