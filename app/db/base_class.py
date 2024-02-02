import re
from typing import Any

import pendulum
from sqlalchemy import Column, DateTime, event
from sqlalchemy.ext.declarative import as_declarative, declared_attr


class TimeStampMixin:
    created_at = Column(DateTime(timezone=True), default=pendulum.now)
    created_at._creation_order = 9999
    updated_at = Column(DateTime(timezone=True), default=pendulum.now)
    updated_at._creation_order = 9999

    @staticmethod
    def _updated_at(mapper, connection, target):
        target.updated_at = pendulum.now()

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, "before_update", cls._updated_at)


@as_declarative()
class Base(TimeStampMixin):
    id: Any
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        class_name = cls.__name__.lower()
        snake_case = re.sub(r"(?<!^)(?=[A-Z])", "_", class_name).lower()
        return snake_case + "s"
