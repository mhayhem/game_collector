import jwt
from datetime import timezone, timedelta, datetime
from app.config import SECRET_KEY, ALGORITHM, TIME_EXPIRE_TOKEN


def create_token_acces(data: dict, expire_token: timedelta | None = None):
    to_encode = data.copy()
    
    if expire_token:
        expire = datetime.now(timezone.utc) + expire_token
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    
    to_encode.update({"exp": expire})
    if SECRET_KEY is None:
        return None
    
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return token