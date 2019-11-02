"""Create farm table

Revision ID: e25ffe4bcd28
Revises: 
Create Date: 2019-11-01 00:22:43.783442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e25ffe4bcd28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'farm',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('latitude', sa.Numeric),
        sa.Column('longitude', sa.Numeric),)


def downgrade():
    op.drop_table('farm')
