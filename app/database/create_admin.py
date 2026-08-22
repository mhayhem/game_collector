import os
from dotenv import load_dotenv
import sqlite3
from app.database.db_script import get_connection
from app.security.password_hash import hashed_password



load_dotenv()

def create_admin() -> None:
    
    
    username = os.getenv("ADMIN_USERNAME")
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")
    
    if not username or not email or not password:
        raise RuntimeError("Admin bootstrap variables are missing")
    
    con = get_connection()
    
    hash_password = hashed_password(password)
    
    try:
        cursor = con.execute(
            """ 
            INSERT INTO users (username, email, is_admin, password_hash)
            VALUES (?, ?, ?, ?);
            """,
            (username, email, True, hash_password)
        )
        
        if cursor.lastrowid is None:
            raise RuntimeError(
                "Could not retrieve the newly created admin ID"
                )
        
        con.commit()
        
    except sqlite3.IntegrityError as error:
        raise RuntimeError(
            "Admin Username or email already exists"
            ) from error
        
    
    finally:
        con.close()