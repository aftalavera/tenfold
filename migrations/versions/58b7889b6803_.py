"""empty message

Revision ID: 58b7889b6803
Revises: None
Create Date: 2015-10-03 19:43:35.121982

"""

# revision identifiers, used by Alembic.
revision = '58b7889b6803'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_code', sa.Integer(), nullable=True),
    sa.Column('department_nam', sa.String(length=100), nullable=True),
    sa.Column('city_code', sa.Integer(), nullable=True),
    sa.Column('city_nam', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dpi', sa.String(length=15), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dpi')
    )
    op.create_table('voters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dpi', sa.String(length=15), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('department', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('referred', sa.Text(), nullable=True),
    sa.Column('voted', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dpi')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voters')
    op.drop_table('users')
    op.drop_table('cities')
    ### end Alembic commands ###
