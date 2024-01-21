from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routes import iris


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(iris.router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[get_settings().cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = get_app()
