from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import games

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(games.router)