"""empty message

Revision ID: e9a6247d5d65
Revises: 
Create Date: 2020-12-02 22:01:48.989923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9a6247d5d65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rasp_sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sensor_name', sa.String(length=255), nullable=False),
    sa.Column('temperature_measure', sa.Float(), nullable=False),
    sa.Column('humidity_measure', sa.Float(), nullable=False),
    sa.Column('time_stamp', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sensor_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rasp_sensor')
    # ### end Alembic commands ###