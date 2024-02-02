from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings

engine = create_engine(
    get_settings().sqlalchemy_database_uri,
    pool_pre_ping=True,
    connect_args={
        "options": f"-c timezone="
        f"{get_settings().sqlalchemy_database_connect_timezone} "
        f"-c search_path={get_settings().postgres_schema}"
    },
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
