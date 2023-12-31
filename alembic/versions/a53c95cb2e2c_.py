"""empty message

Revision ID: a53c95cb2e2c
Revises: 92dcd78e629a
Create Date: 2023-10-25 12:15:49.891881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a53c95cb2e2c'
down_revision: Union[str, None] = '92dcd78e629a'
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
    op.create_table('ManyToManyEmploye_professional_education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employe_id', sa.Integer(), nullable=True),
    sa.Column('professional_education', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ManyToManyEmploye_vocational_training',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employe_id', sa.Integer(), nullable=True),
    sa.Column('vocational_training', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe_age_between',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('age_between', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe_end_knowledge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('knowledge_part', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe_knowledge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('knowledge', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe_nation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nation', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe_new_degree',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('degree', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe_professional_education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('professional_education', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe_sex',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sex', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe_vocational_training',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vocational_training', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_surname', sa.String(), nullable=False),
    sa.Column('nation', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('sex', sa.Integer(), nullable=False),
    sa.Column('new_degree', sa.Integer(), nullable=False),
    sa.Column('knowledge', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['age'], ['employe_age_between.id'], ),
    sa.ForeignKeyConstraint(['knowledge'], ['employe_knowledge.id'], ),
    sa.ForeignKeyConstraint(['nation'], ['employe_nation.id'], ),
    sa.ForeignKeyConstraint(['new_degree'], ['employe_new_degree.id'], ),
    sa.ForeignKeyConstraint(['sex'], ['employe_sex.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employe')
    op.drop_table('user')
    op.drop_table('employe_vocational_training')
    op.drop_table('employe_sex')
    op.drop_table('employe_professional_education')
    op.drop_table('employe_new_degree')
    op.drop_table('employe_nation')
    op.drop_table('employe_knowledge')
    op.drop_table('employe_end_knowledge')
    op.drop_table('employe_age_between')
    op.drop_table('ManyToManyEmploye_vocational_training')
    op.drop_table('ManyToManyEmploye_professional_education')
    op.drop_table('ManyToManyEmployeEnd_knowledge')
    # ### end Alembic commands ###
