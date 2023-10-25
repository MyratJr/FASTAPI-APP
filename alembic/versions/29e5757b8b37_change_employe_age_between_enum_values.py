"""Change employe_age_between_enum values

Revision ID: 29e5757b8b37
Revises: e4726ea713a3
Create Date: 2023-10-25 12:56:21.426368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29e5757b8b37'
down_revision: Union[str, None] = 'e4726ea713a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
