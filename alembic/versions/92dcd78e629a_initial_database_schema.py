"""Initial database schema

Revision ID: 92dcd78e629a
Revises: d51975b81bec
Create Date: 2023-10-25 12:11:49.698556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92dcd78e629a'
down_revision: Union[str, None] = 'd51975b81bec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
