from typing import Any, List, Optional, Type

import pendulum
from fastapi import status
from pydantic import BaseModel, create_model

STANDARD_RESPONSE_CLASS_NAME = "StandardResponseModel"


def create_standard_response(
    status: int = status.HTTP_200_OK,
    message: str = "OK",
    data: Optional[List[Any]] = None,
    errors: Optional[List[str]] = None,
) -> Type[BaseModel]:
    model = create_model(
        STANDARD_RESPONSE_CLASS_NAME,
        status=(int, status),
        message=(str, ""),
        data=(List[str], None),
        errors=(Optional[List[str]], None),
        timestamp=(int, 0),
    )

    return model(
        status=status,
        message=message,
        data=data,
        errors=errors,
        timestamp=pendulum.now().int_timestamp,
    )
