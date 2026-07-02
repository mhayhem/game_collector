from database import get_connection
from models import User

def get_all_games():
    connection = get_connection()
    games = connection.execute("SELECT * FROM games").fetchall()
    connection.close()
    return games

def update_status(new_status: str, game_id: int):
    with get_connection() as connection:
        connection.execute("""
            UPDATE games
            SET status = ?
            WHERE game_id = ?;
            """,
            (new_status, game_id)
        )
    connection.commit()

# última función 
def create_user(user: User):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT users (username, password_hash, email)
            VALUES (? , ?, ?);
            """
        )
    connection.close()