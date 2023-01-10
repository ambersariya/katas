from fastapi import FastAPI

from src.ui.rest.routes import timeline


def create_app():
    app = FastAPI()
    app.include_router(timeline)
    return app
