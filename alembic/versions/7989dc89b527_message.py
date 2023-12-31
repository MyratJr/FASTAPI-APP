"""Message

Revision ID: 7989dc89b527
Revises: bd0556495f81
Create Date: 2023-11-10 10:36:33.327605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7989dc89b527'
down_revision: Union[str, None] = 'bd0556495f81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('employe_new_degree_fkey', 'employe', type_='foreignkey')
    op.drop_column('employe', 'new_degree')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employe', sa.Column('new_degree', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('employe_new_degree_fkey', 'employe', 'employe_new_degree', ['new_degree'], ['id'])
    # ### end Alembic commands ###
