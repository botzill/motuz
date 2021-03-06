"""empty message

Revision ID: f8ecac0421e8
Revises: e9dc9c11604f
Create Date: 2020-03-11 19:54:37.078687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8ecac0421e8'
down_revision = 'e9dc9c11604f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('copy_job', sa.Column('notification_email', sa.String(), nullable=True))
    op.add_column('hashsum_job', sa.Column('notification_email', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hashsum_job', 'notification_email')
    op.drop_column('copy_job', 'notification_email')
    # ### end Alembic commands ###
