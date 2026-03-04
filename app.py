from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()

# ===== Config =====
SECRET_KEY = "troque-essa-chave-por-uma-mais-grande-e-aleatoria"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# "Banco de dados" em memória
users_db: dict[str, dict] = {}

class UserCreate(BaseModel):
    username: str
    password: str

class UserPublic(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserPublic:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if not username or username not in users_db:
            raise HTTPException(status_code=401, detail="Token inválido")
        return UserPublic(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

@app.get("/")
def home():
    return {"mensagem": "API Auth JWT funcionando!"}

@app.post("/register", response_model=UserPublic, status_code=201)
def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    users_db[user.username] = {
        "username": user.username,
        "password_hash": hash_password(user.password),
    }
    return UserPublic(username=user.username)

from fastapi.security import OAuth2PasswordRequestForm

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    db_user = users_db.get(username)

    if not db_user or not verify_password(password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/profile", response_model=UserPublic)
def profile(current_user: UserPublic = Depends(get_current_user)):
    return current_user