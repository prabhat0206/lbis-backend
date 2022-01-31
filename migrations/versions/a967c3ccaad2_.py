"""empty message

Revision ID: a967c3ccaad2
Revises: 
Create Date: 2022-01-31 13:47:16.480442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a967c3ccaad2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('isVideo', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'isVideo')
    # ### end Alembic commands ###
