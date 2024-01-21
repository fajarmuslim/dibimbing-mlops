import json

from fastapi import status
from fastapi.testclient import TestClient


def test_iris(
    client: TestClient,
) -> None:
    data = {
        "features": [
            {
                "sepal_length": 0,
                "sepal_width": 0,
                "petal_length": 0,
                "petal_width": 0,
            },
            {
                "sepal_length": 3,
                "sepal_width": 2,
                "petal_length": 4,
                "petal_width": 0,
            },
        ]
    }
    r = client.post("/iris", data=json.dumps(data))

    response = r.json()

    assert r.status_code == status.HTTP_200_OK
    assert response["status"] == status.HTTP_200_OK
    assert response["message"] == "OK"
    assert response["data"] is not None
    assert response["errors"] is None
    assert response["timestamp"] is not None
