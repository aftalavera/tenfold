"""empty message

Revision ID: 2ab777c1d6b4
Revises: a9e97a5d7fc
Create Date: 2015-10-05 13:12:23.015174

"""

# revision identifiers, used by Alembic.
revision = '2ab777c1d6b4'
down_revision = 'a9e97a5d7fc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    ### end Alembic commands ###
