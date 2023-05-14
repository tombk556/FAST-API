"""add new columns to posts

Revision ID: 017c9fd0f24a
Revises: eed10f058da1
Create Date: 2023-05-14 20:04:10.512792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '017c9fd0f24a'
down_revision = 'eed10f058da1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
