"""Added notes table

Revision ID: 0514e3418c6b
Revises: 
Create Date: 2020-08-20 10:17:31.453707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0514e3418c6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notes')
    # ### end Alembic commands ###
