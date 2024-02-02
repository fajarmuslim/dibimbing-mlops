from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.schemas.iris import IrisBatchRequest, IrisBatchResponse
from app.services.iris import IrisPredictor

router = APIRouter(prefix="/iris", tags=["Iris"])
iris_predictor = IrisPredictor()


@router.post(
    "",
    response_model=IrisBatchResponse,
    name="POST batch iris",
)
def iris_prediction(request: IrisBatchRequest, db: Session = Depends(get_db)):
    return iris_predictor.predict(db=db, features=request.features)
