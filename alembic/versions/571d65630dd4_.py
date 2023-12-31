"""empty message

Revision ID: 571d65630dd4
Revises: 7c3178200ff9
Create Date: 2023-10-25 13:08:31.148399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '571d65630dd4'
down_revision: Union[str, None] = '7c3178200ff9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employe_age_between', 'age_between')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employe_age_between', sa.Column('age_between', postgresql.ENUM('18 ýaşa çenli', '18-20 ýaş', '21-22 ýaş', "23-24 ýaş'25-29 ýaş", '30-34 ýaş', '35-39 ýaş', '40-49 ýaş', name='employe_age_between_enum'), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
