"""empty message

Revision ID: 6546b82d6e24
Revises: a66508788c53
Create Date: 2022-04-13 13:21:22.122442

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '6546b82d6e24'
down_revision = 'a66508788c53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('validation_record',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('frame_set', sa.String(length=1200), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('shot_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True),
    sa.ForeignKeyConstraint(['shot_id'], ['entity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_validation_record_shot_id'), 'validation_record', ['shot_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_validation_record_shot_id'), table_name='validation_record')
    op.drop_table('validation_record')
    # ### end Alembic commands ###
