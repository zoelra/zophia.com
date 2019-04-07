"""empty message

Revision ID: c6ea1f66e85c
Revises: 14d964b76b9d
Create Date: 2019-04-06 20:51:56.378947

"""

# revision identifiers, used by Alembic.
revision = 'c6ea1f66e85c'
down_revision = '14d964b76b9d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('link')
    ### end Alembic commands ###