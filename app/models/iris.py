import uuid

from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Prediction(Base):
    prediction_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    sepal_length = Column(Float, nullable=False)
    sepal_width = Column(Float, nullable=False)
    petal_length = Column(Float, nullable=False)
    petal_width = Column(Float, nullable=False)
    label = Column(String(15), nullable=False)
