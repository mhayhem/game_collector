from pydantic import BaseModel

class GameCreate(BaseModel):
    game_id: int
    user_id: int
    title: str
    genre: str
    platform: str
    game_format: str
    status: str
    img_url: str