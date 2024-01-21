from fastapi import APIRouter

from app.schemas.iris import IrisBatchRequest, IrisBatchResponse
from app.services.iris import IrisPredictor

router = APIRouter(prefix="/iris", tags=["Iris"])
iris_predictor = IrisPredictor()


@router.post(
    "",
    response_model=IrisBatchResponse,
    name="POST batch iris",
)
def iris_prediction(request: IrisBatchRequest):
    return iris_predictor.predict(features=request.features)
