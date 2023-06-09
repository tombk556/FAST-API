"""add-phonenumber

Revision ID: 932d236c5eae
Revises: 7542129e960b
Create Date: 2023-05-21 10:51:05.813616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '932d236c5eae'
down_revision = '7542129e960b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
