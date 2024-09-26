from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.routes import routers as v1_routers


def create_app():
    app = FastAPI(
        title="Алгоритмы, построение и анализ",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(v1_routers, prefix="/v1")

    return app
