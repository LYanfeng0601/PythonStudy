"""add address

Revision ID: 378afd441f72
Revises: fc7b86109eef
Create Date: 2020-05-04 11:40:02.881000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '378afd441f72'
down_revision = 'fc7b86109eef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_authors', sa.Column('address', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_authors', 'address')
    # ### end Alembic commands ###