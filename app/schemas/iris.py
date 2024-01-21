from typing import List, Optional

from pydantic import BaseModel


class BaseResponse(BaseModel):

    status: int
    message: str
    data: Optional[List[str]]
    errors: Optional[List[str]]
    timestamp: int


class IrisSingleRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class IrisBatchRequest(BaseModel):
    features: List[IrisSingleRequest]


class IrisSingleResponse(BaseResponse):
    pass


class IrisBatchResponse(BaseResponse):
    pass
