from fastapi import HTTPException
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserCreate, UserPublic, Token

# "Banco de dados" em memória (por enquanto)
users_db: dict[str, dict] = {}


def register_user(user: UserCreate) -> UserPublic:
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    users_db[user.username] = {
        "username": user.username,
        "password_hash": hash_password(user.password),
    }
    return UserPublic(username=user.username)


def login_user(username: str, password: str) -> Token:
    db_user = users_db.get(username)
    if not db_user or not verify_password(password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": username})
    return Token(access_token=token)