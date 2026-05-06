from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token, verify_refresh_token
from app.schemas.user import UserCreate, UserPublic, Token, TokenFull, RefreshTokenRequest
from app.models.user import User, TokenBlacklist

def register_user(user: UserCreate, db: Session) -> UserPublic:
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    new_user = User(
        username=user.username,
        password_hash=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserPublic(username=new_user.username)

def login_user(username: str, password: str, db: Session) -> TokenFull:
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    access_token = create_access_token({"sub": username})
    refresh_token = create_refresh_token({"sub": username})
    return TokenFull(access_token=access_token, refresh_token=refresh_token)

def refresh_access_token(refresh_request: RefreshTokenRequest) -> Token:
    username = verify_refresh_token(refresh_request.refresh_token)
    if not username:
        raise HTTPException(status_code=401, detail="Refresh token inválido ou expirado")
    new_access_token = create_access_token({"sub": username})
    return Token(access_token=new_access_token)

def logout_user(token: str, db: Session) -> dict:
    existing = db.query(TokenBlacklist).filter(TokenBlacklist.token == token).first()
    if existing:
        raise HTTPException(status_code=400, detail="Token já revogado")
    blacklisted = TokenBlacklist(token=token)
    db.add(blacklisted)
    db.commit()
    return {"message": "Logout realizado com sucesso"}

def is_token_blacklisted(token: str, db: Session) -> bool:
    return db.query(TokenBlacklist).filter(TokenBlacklist.token == token).first() is not None