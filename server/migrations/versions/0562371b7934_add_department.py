"""add Department

Revision ID: 0562371b7934
Revises: d2ccbc2a9064
Create Date: 2024-04-12 09:14:12.824769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0562371b7934'
down_revision = 'd2ccbc2a9064'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
