from typing import Any, List, Type

from joblib import load

from app.schemas.iris import IrisSingleRequest
from app.utils.constant import MODEL_PATH
from app.utils.response import create_standard_response


class IrisPredictor:
    def __init__(self):
        self.model = load(MODEL_PATH)
        self.mapping_res = {0: "setosa", 1: "versicolor", 2: "virginica"}

    def post_process(self, pred: Any):
        return self.mapping_res[pred]

    def predict(self, features: List[IrisSingleRequest]) -> Type[Any]:
        formatted_features = [
            [
                item.sepal_length,
                item.sepal_width,
                item.petal_length,
                item.petal_width,
            ]
            for item in features
        ]
        result = self.model.predict(formatted_features)

        res = []
        for item in list(result):
            res.append(self.post_process(item))

        return create_standard_response(
            data=res,
        )
