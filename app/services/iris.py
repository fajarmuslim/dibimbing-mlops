import logging
from typing import Any, List, Type

from joblib import load

from app.crud.iris import prediction
from app.models.iris import Prediction
from app.schemas.iris import IrisSingleRequest
from app.utils.constant import MODEL_PATH
from app.utils.response import create_standard_response

logging.config.fileConfig("app/logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class IrisPredictor:
    def __init__(self):
        self.model = load(MODEL_PATH)
        self.mapping_res = {0: "setosa", 1: "versicolor", 2: "virginica"}

    def post_process(self, pred: Any):
        return self.mapping_res[pred]

    def predict(self, db, features: List[IrisSingleRequest]) -> Type[Any]:
        formatted_features = [
            [
                item.sepal_length,
                item.sepal_width,
                item.petal_length,
                item.petal_width,
            ]
            for item in features
        ]
        logger.info(formatted_features)
        prediction_result = self.model.predict(formatted_features)

        res = []
        for feature, pred in zip(features, list(prediction_result)):
            post_process_pred = self.post_process(pred)
            res.append(post_process_pred)

            obj_in = Prediction(
                sepal_length=feature.sepal_length,
                sepal_width=feature.sepal_width,
                petal_length=feature.petal_length,
                petal_width=feature.petal_width,
                label=post_process_pred,
            )

            prediction.create(
                db=db,
                obj_in=obj_in,
            )

        logger.info(res)

        return create_standard_response(
            data=res,
        )
