"""empty message

Revision ID: f3cdee093c3a
Revises: e3f791d50878
Create Date: 2022-05-14 05:24:57.498088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3cdee093c3a'
down_revision = 'e3f791d50878'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('analysis', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'analysis', 'user', ['user_id'], ['id'])
    op.alter_column('book', 'image_book',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('book', 'image_book',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.drop_constraint(None, 'analysis', type_='foreignkey')
    op.drop_column('analysis', 'user_id')
    # ### end Alembic commands ###
