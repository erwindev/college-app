"""removed redundant column

Revision ID: 1c3484b1939f
Revises: 6dc19aade91d
Create Date: 2019-02-23 09:36:19.538099

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1c3484b1939f'
down_revision = '6dc19aade91d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('temp_table', 'create_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('temp_table', sa.Column('create_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
