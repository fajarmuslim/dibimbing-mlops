import uuid
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import (  # noqa
    Column,
    DateTime,
    Float,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.orm import sessionmaker

from app.dependencies.db import get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocalTest = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata_obj = MetaData()
predictions = Table(
    "predictions",
    metadata_obj,
    Column(
        "prediction_id",
        String(40),
        default=lambda: str(uuid.uuid4()),
        primary_key=True,
    ),
    Column("petal_length", Float),
    Column("petal_width", Float),
    Column("sepal_length", Float),
    Column("sepal_width", Float),
    Column("label", String(15)),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)

metadata_obj.create_all(engine)


@pytest.fixture(scope="module")
def override_db() -> Generator:
    def override_get_db():
        try:
            db = SessionLocalTest()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
