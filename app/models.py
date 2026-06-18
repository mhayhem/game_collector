class Game:
    def __init__(self, title: str, genre: str, platform: str, game_format: str, status: str) -> None:
        self.title = title
        self.genre = genre
        self.platform = platform
        self.game_format = game_format
        self.status = status
    
    def __str__(self) -> str:
        return f"{self.title} ({self.platform}) {self.status}"


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

