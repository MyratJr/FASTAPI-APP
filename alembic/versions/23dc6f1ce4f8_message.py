"""message

Revision ID: 23dc6f1ce4f8
Revises: 48ba7e37d330
Create Date: 2023-10-10 13:21:52.269931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23dc6f1ce4f8'
down_revision: Union[str, None] = '48ba7e37d330'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
