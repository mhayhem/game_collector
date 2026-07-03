from db_script import get_connection
from models import User, Game

# get information to db

def get_all_games() -> list[Game]:
    with get_connection() as connection: # refactorizar en una función externa
        rows = connection.execute("SELECT * FROM games").fetchall()
    
    # refactorizar en una función externa
    return [Game(
        game_id=row["game_id"],
        user_id=row["user_id"],
        title=row["title"],
        genre=row["genre"],
        platform=row["platform"],
        game_format=row["game_format"],
        status=row["status"],
        img_url=row["img_url"]) for row in rows
        ]

def get_game_by_name(title: str) -> Game| None:
    with get_connection() as connection: # refactorizar en una función externa
        cursor = connection.execute(
            "SELECT title FROM games WHERE title = ?;",
            (title,)
        )
    row = cursor.fetchone()
    if row is None:
        return None
    # refactorizar en una función externa
    return Game(
        game_id=row["game_id"],
        user_id=row["user_id"],
        title=row["title"],
        genre=row["genre"],
        platform=row["platform"],
        game_format=row["game_format"],
        status=row["status"],
        img_url=row["img_url"]
    )

# modify data

def update_status(new_status: str, game_id: int):
    with get_connection() as connection: # refactorizar en una función externa
        connection.execute("""
            UPDATE games
            SET status = ?
            WHERE game_id = ?;
            """,
            (new_status, game_id)
        )
    connection.commit()

# crud users

# get user


def get_all_user() -> list[User]:
    with get_connection() as connection: # refactorizar en una función externa
        rows = connection.execute("SELECT * FROM users;").fetchall()

    # refactorizar en una función externa
    return [User(
        user_id=row["user_id"],
        username=row["username"],
        password_hash=row["password_hash"],
        email=row["email"]
    ) for row in rows]
    
def get_user_by_name(name: str) -> User | None:
    with get_connection() as connection: # refactorizar en una función externa
        cursor = connection.execute(
            """
            SELECT username 
            FROM users
            WHERE username = ?;
            """,
            (name,))
    
    row = cursor.fetchone()
    
    if row is None:
        return None
    # refactorizar en una función externa
    return User(
        user_id=row["user_id"],
        username=row["username"],
        password_hash=row["password_hash"],
        email=row["email"]
    )

# modify data

def create_user(user: User):
    with get_connection() as connection: # refactorizar en una función externa
        connection.execute(
            """
            INSERT users (username,  email, password_hash)
            VALUES (? , ?, ?);x
            """,
            (user.username, user.email ,user.password_hash)
        )
    connection.close()
