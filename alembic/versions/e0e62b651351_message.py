"""message

Revision ID: e0e62b651351
Revises: e587a0256c77
Create Date: 2023-10-10 12:07:05.410079

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0e62b651351'
down_revision: Union[str, None] = 'e587a0256c77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogs_tags')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs_tags',
    sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], name='blogs_tags_blog_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name='blogs_tags_tag_id_fkey'),
    sa.PrimaryKeyConstraint('blog_id', 'tag_id', name='blogs_tags_pkey')
    )
    # ### end Alembic commands ###
