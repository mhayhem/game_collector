import jwt
import os
from dotenv import load_dotenv
from datetime import timezone, timedelta, datetime

ALGORITHM = "HS256"
TIME_EXPIRE_TOKEN = 30

load_dotenv()

def create_token_acces(data: dict, expire_token: timedelta | None = None):
    to_encode = data.copy()
    
    secret_key = os.getenv("SECRET_KEY")
    
    if expire_token:
        expire = datetime.now(timezone.utc) + expire_token
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    
    to_encode.update({"exp": expire})
    if secret_key is None:
        return None
    
    token = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
    
    return token