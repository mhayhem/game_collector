from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="login")

templates = Jinja2Templates(directory="app/templates")


