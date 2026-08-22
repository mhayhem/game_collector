from enum import Enum
from pydantic import BaseModel
from datetime import datetime, timedelta

class GameFormat(Enum):
    physical = "Fisico"
    digital = "Digital"


class GameStatus(Enum):
    purchased = "Comprado"
    unpurchased = "Sin comprar"
    

class Game(BaseModel):
    game_id: int
    user_id: int
    title: str
    genre: str
    developer: str 
    year_release: datetime
    img_url: str

class PublicUser(BaseModel):
    user_id: int
    username: str
    email: str
    disabled: bool

class User(BaseModel):
    user_id: int
    username: str
    email: str
    disabled: bool
    is_admin: bool

class RegisterUser(BaseModel):
    username: str
    email: str
    password: str


class UserDB(User):
    hashed_password: str


class AccessToken(BaseModel):
    access_token: str
    type_token: str