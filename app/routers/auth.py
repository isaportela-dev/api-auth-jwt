from fastapi import HTTPException
from app.schemas.user import UserCreate
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from app.core.security import SECRET_KEY, ALGORITHM
from app.schemas.user import UserPublic, Token
from app.services.auth import register_user, login_user, users_db

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> UserPublic:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if not username or username not in users_db:
            raise HTTPException(status_code=401, detail="Token inválido")
        return UserPublic(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


@router.post("/register", response_model=UserPublic, status_code=201)
def register(user: UserCreate):
    return register_user(user)


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_user(form_data.username, form_data.password)


@router.get("/profile", response_model=UserPublic)
def profile(current_user: UserPublic = Depends(get_current_user)):
    return current_user