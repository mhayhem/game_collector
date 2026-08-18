from models import User, UserDB, RegisterUser
from database.db_script import get_connection
from security.password_hash import hashed_password

CON = get_connection()

def _row_to_user(row):
    return User.model_validate(row)


def get_all_user() -> list[User]:
    try:
        rows = CON.execute(
            """
            SELECT *
            FROM users;
            """
        ).fetchall()
        
        return [_row_to_user(row) for row in rows]
    
    finally:
        CON.close()



def get_user_by_username(username: str) -> User | None:
    try:
        row = CON.execute(
            """
            SELECT username 
            FROM users
            WHERE username = ?;
            """,
            (username,)
            ).fetchone()
        
        return _row_to_user(row)
    
    finally:
        CON.close()



def create_user(user: RegisterUser):
    try:
        CON.execute(
            """
            INSERT INTO users (username,  email, password_hash)
            VALUES (? , ?, ?);
            """,
            (user.username, user.email, hashed_password(user.password))
        )
    
    finally:
        CON.close()
