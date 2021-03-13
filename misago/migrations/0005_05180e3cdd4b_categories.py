"""categories

Revision ID: 05180e3cdd4b
Revises: f99b40a61441
Create Date: 2019-12-15 21:48:55.261543

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "05180e3cdd4b"
down_revision = "f99b40a61441"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "misago_categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("type", sa.Integer(), nullable=False),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.Column("depth", sa.Integer(), nullable=False),
        sa.Column("left", sa.Integer(), nullable=False),
        sa.Column("right", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("color", sa.String(length=7), nullable=True),
        sa.Column("icon", sa.String(length=255), nullable=True),
        sa.Column("threads", sa.Integer(), server_default="0", nullable=False),
        sa.Column("posts", sa.Integer(), server_default="0", nullable=False),
        sa.Column("is_closed", sa.Boolean(), nullable=False),
        sa.Column("extra", sa.JSON(), nullable=False),
        sa.ForeignKeyConstraint(
            ["parent_id"], ["misago_categories.id"], ondelete="RESTRICT"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_misago_categories_left"), "misago_categories", ["left"], unique=False
    )
    op.create_index(
        op.f("ix_misago_categories_type"), "misago_categories", ["type"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_misago_categories_type"), table_name="misago_categories")
    op.drop_index(op.f("ix_misago_categories_left"), table_name="misago_categories")
    op.drop_table("misago_categories")
    # ### end Alembic commands ###
