set -a
. .env
alembic revision --autogenerate -m "feat(iris): init prediction table"
alembic upgrade heads
set +a
