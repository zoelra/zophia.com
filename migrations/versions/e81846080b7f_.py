"""empty message

Revision ID: e81846080b7f
Revises: c6ea1f66e85c
Create Date: 2019-04-06 21:33:24.054118

"""

# revision identifiers, used by Alembic.
revision = 'e81846080b7f'
down_revision = 'c6ea1f66e85c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('article', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    ### end Alembic commands ###
