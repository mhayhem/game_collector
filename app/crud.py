from app.database import get_connection

def get_all_games():
    connection = get_connection()
    games = connection.execute("SELECT * FROM games").fetchall()
    connection.close()
    return games



