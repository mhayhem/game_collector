from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app import crud

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    games = crud.get_all_games()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"games": games})