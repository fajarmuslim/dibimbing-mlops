"""feat(iris): init prediction table

Revision ID: 4f03ca853832
Revises:
Create Date: 2024-02-02 14:46:15.315231

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4f03ca853832"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "predictions",
        sa.Column("prediction_id", sa.UUID(), nullable=False),
        sa.Column("sepal_length", sa.Float(), nullable=False),
        sa.Column("sepal_width", sa.Float(), nullable=False),
        sa.Column("petal_length", sa.Float(), nullable=False),
        sa.Column("petal_width", sa.Float(), nullable=False),
        sa.Column("label", sa.String(length=15), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("prediction_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("predictions")
    # ### end Alembic commands ###
