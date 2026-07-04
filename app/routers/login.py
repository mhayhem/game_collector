from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app import crud

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")
