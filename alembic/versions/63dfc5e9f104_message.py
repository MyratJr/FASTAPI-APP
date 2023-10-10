"""message

Revision ID: 63dfc5e9f104
Revises: 77f38f81809b
Create Date: 2023-10-10 09:50:58.542461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63dfc5e9f104'
down_revision: Union[str, None] = '77f38f81809b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_authors')
    op.drop_table('books')
    op.drop_table('authors')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('authors_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='authors_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('books',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('books_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='books_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('book_authors',
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('blurb', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], name='book_authors_author_id_fkey'),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name='book_authors_book_id_fkey'),
    sa.PrimaryKeyConstraint('book_id', 'author_id', name='book_authors_pkey')
    )
    # ### end Alembic commands ###
