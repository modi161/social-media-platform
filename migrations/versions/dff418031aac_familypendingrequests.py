"""FamilyPendingRequests

Revision ID: dff418031aac
Revises: 905c1fe380e5
Create Date: 2024-04-28 14:44:28.485056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dff418031aac'
down_revision = '905c1fe380e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FamilyPendingRequests',
    sa.Column('UserId', sa.Integer(), nullable=False),
    sa.Column('FamilyId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['UserId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('UserId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('FamilyPendingRequests')
    # ### end Alembic commands ###
