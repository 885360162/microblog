"""Fix column issue

Revision ID: ceabd67713f1
Revises: df2d748947ab
Create Date: 2018-01-02 21:50:23.123285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceabd67713f1'
down_revision = 'df2d748947ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('disable', sa.Boolean(), nullable=True))
    with op.batch_alter_table('comments') as batch_op:
    	batch_op.drop_column('disbale')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('disbale', sa.BOOLEAN(), nullable=True))
    op.drop_column('comments', 'disable')
    # ### end Alembic commands ###
