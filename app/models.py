from enum import Enum
from pydantic import BaseModel


class Platform(Enum):
    ps = "Playstation"
    ps2 = "Playstation 2"
    ps3 = "Playstation 3"
    ps4 = "Playstation 4"
    ps5 = "Playstation 5"
    psp = "Playstation Portable"
    psv = "Playstation Vita"


class GameFormat(Enum):
    physical = "Fisico"
    digital = "Digital"


class GameStatus(Enum):
    purchased = "Comprado"
    unpurchased = "Sin comprar"
    

class Game(BaseModel):
    game_id = int
    user_id = int
    title = str
    genre = str
    platform = Enum
    game_format = Enum
    status = Enum
    img_url = str

class User(BaseModel):
    user_id = int
    username = str
    email = str


class UserDB(BaseModel):
    hashed_password = str
