from app.crud.base import CRUDBase
from app.models.iris import Prediction


class CRUDIrisPrediction(CRUDBase[Prediction]):
    pass


prediction = CRUDIrisPrediction(Prediction)
