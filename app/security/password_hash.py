from pwdlib import PasswordHash

HASH = PasswordHash.recommended()

def hashed_password(password: str) -> str:
    return HASH.hash(password)

