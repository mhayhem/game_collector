from dotenv import load_dotenv
import os

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"
TIME_EXPIRE_TOKEN = 30

if SECRET_KEY is None:
    raise RuntimeError("SECRET KEY is not configured")