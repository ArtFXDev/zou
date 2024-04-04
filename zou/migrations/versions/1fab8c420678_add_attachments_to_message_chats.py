"""add attachments to message chats


Revision ID: 1fab8c420678
Revises: 92b40d79ad3f
Create Date: 2024-03-28 13:22:39.592100

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '1fab8c420678'
down_revision = '92b40d79ad3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attachment_file', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chat_message_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True))
        batch_op.drop_constraint('attachment_uc', type_='unique')
        batch_op.create_index(batch_op.f('ix_attachment_file_chat_message_id'), ['chat_message_id'], unique=False)
        batch_op.create_foreign_key(None, 'chat_message', ['chat_message_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attachment_file', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_attachment_file_chat_message_id'))
        batch_op.create_unique_constraint('attachment_uc', ['name', 'comment_id'])
        batch_op.drop_column('chat_message_id')

    # ### end Alembic commands ###
