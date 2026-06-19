class Game:
    def __init__(
            self, title: str, genre: str, platform: str, game_format: str, 
            status: str, img_url: str, game_id: int | None = None, user_id: int | None = None) -> None:
        
        self.game_id = game_id
        self.title = title
        self.genre = genre
        self.platform = platform
        self.game_format = game_format
        self.status = status
        self.img_url = img_url
    
    def __str__(self) -> str:
        return f"{self.title} ({self.platform}) {self.status}"


class User:
    def __init__(self, username: str, password_hash: str, user_id: int | None = None) -> None:
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash

