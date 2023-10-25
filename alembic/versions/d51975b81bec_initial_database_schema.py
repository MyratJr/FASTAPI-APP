"""Initial database schema

Revision ID: d51975b81bec
Revises: 7afe9fc5d5c1
Create Date: 2023-10-25 12:10:53.830650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd51975b81bec'
down_revision: Union[str, None] = '7afe9fc5d5c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
