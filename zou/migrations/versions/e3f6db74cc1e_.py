"""

Revision ID: e3f6db74cc1e
Revises: df9f8a147e80
Create Date: 2022-03-21 17:26:12.103387

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "e3f6db74cc1e"
down_revision = "df9f8a147e80"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "search_filter",
        "search_query",
        existing_type=sa.VARCHAR(length=200),
        type_=sa.String(length=500),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "search_filter",
        "search_query",
        existing_type=sa.String(length=500),
        type_=sa.VARCHAR(length=200),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
