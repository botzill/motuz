"""empty message

Revision ID: bb59b6777634
Revises: f8ecac0421e8
Create Date: 2020-03-16 00:44:44.801831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb59b6777634'
down_revision = 'f8ecac0421e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hashsum_job', sa.Column('option_download', sa.Boolean(), server_default='f', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hashsum_job', 'option_download')
    # ### end Alembic commands ###