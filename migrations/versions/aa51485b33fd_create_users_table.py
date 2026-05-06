"""create users table
Revision ID: aa51485b33fd
Revises: 
Create Date: 2026-03-30 20:05:13.015391
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = 'aa51485b33fd'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'token_blacklist',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('token', sa.String(), unique=True, index=True, nullable=False),
        sa.Column('revoked_at', sa.DateTime(), nullable=True),
    )

def downgrade() -> None:
    op.drop_table('token_blacklist')