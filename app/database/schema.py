from pydantic import BaseModel

class GameCreate(BaseModel):
    title: str
    genre: str
    platform: str
    game_format: str
    status: str
    img_url: str

class UserCreate(BaseModel):
    username: str
    password_hash: str
    email: str