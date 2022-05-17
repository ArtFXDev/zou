"""add column chat_webhook_mattermost

Revision ID: 7b1f765677d8
Revises: 3e0538ddf80f
Create Date: 2021-11-12 15:45:40.750324

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "7b1f765677d8"
down_revision = "3e0538ddf80f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "organisation",
        sa.Column(
            "chat_webhook_mattermost", sa.String(length=80), nullable=True
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("organisation", "chat_webhook_mattermost")
    # ### end Alembic commands ###
