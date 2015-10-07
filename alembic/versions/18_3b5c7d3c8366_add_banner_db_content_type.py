"""Add Banner db_content_type

Revision ID: 3b5c7d3c8366
Revises: 4ed1a2dd2573
Create Date: 2015-08-22 16:03:36.301294

"""

# revision identifiers, used by Alembic.
revision = '3b5c7d3c8366'
down_revision = '4ed1a2dd2573'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute("INSERT INTO db_content_type (name) VALUES ('Banner')")
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute("DELETE FROM db_content_type WHERE name='Banner'")
    ### end Alembic commands ###