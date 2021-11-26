"""Add reply_id to notifications.

Revision ID: 77d6820f494f
Revises: 87efceb6745b
Create Date: 2021-11-14 16:33:29.498193

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '77d6820f494f'
down_revision = '87efceb6745b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notification', sa.Column('reply_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True))
    op.create_index(op.f('ix_notification_reply_id'), 'notification', ['reply_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    op.drop_index(op.f('ix_notification_reply_id'), table_name='notification')
    op.drop_column('notification', 'reply_id')
    # ### end Alembic commands ###
