"""Message

Revision ID: 59d489c87f64
Revises: 52df6843ddc5
Create Date: 2023-11-10 10:18:12.800608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '59d489c87f64'
down_revision: Union[str, None] = '52df6843ddc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employe', sa.Column('age', postgresql.ENUM('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', name='employe_age_between_enum'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employe', 'age')
    # ### end Alembic commands ###
