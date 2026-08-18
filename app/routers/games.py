from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.models import Game, GameFormat, GameStatus
from app.crud.games import get_all_games

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    games = get_all_games()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"games": games})