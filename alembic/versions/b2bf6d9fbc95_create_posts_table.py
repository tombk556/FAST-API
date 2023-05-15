"""create posts table

Revision ID: b2bf6d9fbc95
Revises: 
Create Date: 2023-05-15 20:34:06.342031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2bf6d9fbc95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String()))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
