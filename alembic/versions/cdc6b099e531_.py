"""empty message

Revision ID: cdc6b099e531
Revises: 29b52d0e3559
Create Date: 2023-10-20 09:59:41.457705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdc6b099e531'
down_revision: Union[str, None] = '29b52d0e3559'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ManyToManyEmployeEnd_knowledge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employe_id', sa.Integer(), nullable=True),
    sa.Column('end_knowledge', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('employe_rer_fkey', 'employe', type_='foreignkey')
    op.drop_column('employe', 'rer')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employe', sa.Column('rer', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('employe_rer_fkey', 'employe', 'employe_end_knowledge', ['rer'], ['id'])
    op.drop_table('ManyToManyEmployeEnd_knowledge')
    # ### end Alembic commands ###
