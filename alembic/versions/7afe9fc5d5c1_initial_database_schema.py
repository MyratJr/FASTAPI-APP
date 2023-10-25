"""Initial database schema

Revision ID: 7afe9fc5d5c1
Revises: e55bb61daf1e
Create Date: 2023-10-25 12:10:42.287841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7afe9fc5d5c1'
down_revision: Union[str, None] = 'e55bb61daf1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
