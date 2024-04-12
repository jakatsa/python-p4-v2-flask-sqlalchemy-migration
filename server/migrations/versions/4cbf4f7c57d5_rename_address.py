"""rename address

Revision ID: 4cbf4f7c57d5
Revises: deee63a51ca8
Create Date: 2024-04-12 09:42:16.668191

"""
from alembic import op   
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cbf4f7c57d5'
down_revision = 'deee63a51ca8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')


    # ### end Alembic commands ###
