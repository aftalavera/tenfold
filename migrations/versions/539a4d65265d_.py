"""empty message

Revision ID: 539a4d65265d
Revises: 1652406896c1
Create Date: 2015-10-04 07:51:37.769747

"""

# revision identifiers, used by Alembic.
revision = '539a4d65265d'
down_revision = '1652406896c1'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(length=20), nullable=True))
    ### end Alembic commands ###
