"""create user table

Revision ID: d8f1ac9818c5
Revises: b2bf6d9fbc95
Create Date: 2023-05-15 20:42:03.624489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8f1ac9818c5'
down_revision = 'b2bf6d9fbc95'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass

def downgrade() -> None:
    op.drop_table('users')
    pass
