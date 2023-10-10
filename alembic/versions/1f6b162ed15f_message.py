"""message

Revision ID: 1f6b162ed15f
Revises: 48e6b1e0b96e
Create Date: 2023-10-09 11:22:50.310919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f6b162ed15f'
down_revision: Union[str, None] = '48e6b1e0b96e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employe_nation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nation', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employe_nation')
    # ### end Alembic commands ###