"""Add new field to User model

Revision ID: 2112f293a4ff
Revises: 1df1d86a9834
Create Date: 2023-10-11 12:56:05.454985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2112f293a4ff'
down_revision: Union[str, None] = '1df1d86a9834'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_constraint('employe_professional_education_fkey', 'employe', type_='foreignkey')
    op.drop_constraint('employe_end_knowledge_fkey', 'employe', type_='foreignkey')
    op.drop_constraint('employe_vocational_training_fkey', 'employe', type_='foreignkey')
    op.drop_column('employe', 'vocational_training')
    op.drop_column('employe', 'professional_education')
    op.drop_column('employe', 'end_knowledge')
    op.add_column('employe_end_knowledge', sa.Column('emploes', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employe_end_knowledge', 'emploes')
    op.add_column('employe', sa.Column('end_knowledge', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('employe', sa.Column('professional_education', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('employe', sa.Column('vocational_training', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('employe_vocational_training_fkey', 'employe', 'employe_vocational_training', ['vocational_training'], ['id'])
    op.create_foreign_key('employe_end_knowledge_fkey', 'employe', 'employe_end_knowledge', ['end_knowledge'], ['id'])
    op.create_foreign_key('employe_professional_education_fkey', 'employe', 'employe_professional_education', ['professional_education'], ['id'])
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey'),
    sa.UniqueConstraint('name', name='roles_name_key')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key')
    )
    # ### end Alembic commands ###