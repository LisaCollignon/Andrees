"""Added theme model

Revision ID: 2dfb8e56966f
Revises: 1f96b393c808
Create Date: 2020-12-15 20:20:54.709058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dfb8e56966f'
down_revision = '1f96b393c808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('theme', sa.String(), nullable=False),
    sa.Column('position', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename')
    )
    op.create_table('themes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('theme_name', sa.String(), nullable=False),
    sa.Column('permalink', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('permalink'),
    sa.UniqueConstraint('theme_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('themes')
    op.drop_table('images')
    # ### end Alembic commands ###
