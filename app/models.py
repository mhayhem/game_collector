class Game:
    def __init__(self, title: str, genre: str, platform: str, game_format: str, status: str):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.game_format = game_format
        self.status = status
    
    def __str__(self):
        return f"{self.title} ({self.platform}) {self.status}"