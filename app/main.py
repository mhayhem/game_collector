from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import games

app = FastAPI()

# routers
app.include_router(games.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

