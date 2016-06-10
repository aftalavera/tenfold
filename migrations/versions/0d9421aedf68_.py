"""empty message

Revision ID: 0d9421aedf68
Revises: 2ab777c1d6b4
Create Date: 2016-01-29 16:01:09.011676

"""

# revision identifiers, used by Alembic.
revision = '0d9421aedf68'
down_revision = '2ab777c1d6b4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('voters', sa.Column('photo_path', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('voters', 'photo_path')
    ### end Alembic commands ###