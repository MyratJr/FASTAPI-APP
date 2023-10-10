"""message

Revision ID: cc2f033d0169
Revises: 8090ec67c634
Create Date: 2023-10-09 11:09:15.343857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc2f033d0169'
down_revision: Union[str, None] = '8090ec67c634'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employe_age_between',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('age_between', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employe_age_between')
    # ### end Alembic commands ###