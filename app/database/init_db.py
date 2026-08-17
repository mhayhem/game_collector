from pathlib import Path
from app.database.db_script import get_connection

DATABASE_DIR = Path(__file__).resolve().parent

SCHEMA_DIR = DATABASE_DIR / "schema.sql"
SEEDS_DIR = DATABASE_DIR / "seeds.sql"

CON = get_connection()

def init_db() -> None:
    try:
        with open(SCHEMA_DIR, "r", encoding="utf-8") as file:
            CON.executescript(file.read())
        
        with open(SEEDS_DIR, "r", encoding= "utf-8") as file:
            CON.executescript(file.read())
        
        CON.commit()
    
    finally:
        CON.close()