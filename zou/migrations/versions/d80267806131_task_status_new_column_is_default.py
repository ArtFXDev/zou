"""task_status new column is_default

Revision ID: d80267806131
Revises: b8c0a0f9d054
Create Date: 2022-05-03 14:43:47.946725

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
from zou.migrations.utils.base import BaseMixin

# revision identifiers, used by Alembic.
revision = "d80267806131"
down_revision = "b8c0a0f9d054"
branch_labels = None
depends_on = None


class TaskStatus(declarative_base(), BaseMixin):
    """
    Describe the state of a task. A status marked as reviewable expects a
    preview file linked to relate comment.
    """

    __tablename__ = "task_status"
    name = sa.Column(sa.String(40), nullable=False)
    short_name = sa.Column(
        sa.String(10), unique=True, nullable=False, index=True
    )
    color = sa.Column(sa.String(7), nullable=False)

    is_done = sa.Column(sa.Boolean(), default=False, index=True)
    is_artist_allowed = sa.Column(sa.Boolean(), default=True)
    is_client_allowed = sa.Column(sa.Boolean(), default=True)
    is_retake = sa.Column(sa.Boolean(), default=False)
    is_feedback_request = sa.Column(sa.Boolean(), default=False, index=True)
    is_default = sa.Column(sa.Boolean(), default=False, index=True)
    shotgun_id = sa.Column(sa.Integer)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "task_status", sa.Column("is_default", sa.Boolean(), nullable=True)
    )
    op.create_index(
        op.f("ix_task_status_is_default"),
        "task_status",
        ["is_default"],
        unique=True,
    )
    # ### end Alembic commands ###

    # Set the todo task status is_default to True
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    todo_task_status = (
        session.query(TaskStatus)
        .filter(TaskStatus.name == "Todo")
        .one_or_none()
    )
    if todo_task_status:
        todo_task_status.is_default = True
        session.commit()


def downgrade():
    # Set the todo task status to default short_name/name/color
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    todo_task_status = (
        session.query(TaskStatus).filter(TaskStatus.is_default == True).one()
    )
    todo_task_status.name = "Todo"
    todo_task_status.short_name = "todo"
    todo_task_status.color = "#FFFFFF"
    session.commit()

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_task_status_is_default"), table_name="task_status")
    op.drop_column("task_status", "is_default")
    # ### end Alembic commands ###
