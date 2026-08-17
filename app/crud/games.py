from models import Game, GameFormat, GameStatus, GameCreate
from database.db_script import get_connection 

CON = get_connection()

def _row_to_game(row) -> Game:
    return Game.model_validate(row)


def get_all_games() -> list[Game]:
    try:
        rows = CON.execute(
            """
            SELECT * 
            FROM games;
            """).fetchall()
        
        return [_row_to_game(row) for row in rows]
    
    finally:
        CON.close()

def get_game_by_id(id: int) -> Game| None:
    try:
        row = CON.execute(
            """
            SELECT title 
            FROM games 
            WHERE game_id = ?;
            """,
            (id,)
        ).fetchone()
        
        if row is None:
            return None
        
        return _row_to_game(row)
    
    finally:
        CON.close()


# create Game

def create_game_object(game: GameCreate, user_id: int) -> Game | None:
    try:
        cursor = CON.execute(
            """
            INSERT INTO games
            (title, genre, platform, game_format, status, img_url, user_id)
            VALUES
            (?, ?, ?, ?, ?, ?, ?);
            """,
            (game.title,
            game.genre,
            game.platform,
            game.game_format,
            game.status,
            game.img_url,
            user_id)
        )
        
        CON.commit()
        
        id = cursor.lastrowid
        
        if id is None:
            return None
        
        return get_game_by_id(id)
    
    finally:
        CON.close()


# modify data

def update_status(new_status: GameStatus, game_id: int):
    try:
        cursor = CON.execute(
            """
            UPDATE games
            SET status = ?
            WHERE game_id = ?;
            """,
            (new_status, game_id)
            )
        
        CON.commit()

        return cursor.rowcount > 0
    
    finally:
        CON.close()