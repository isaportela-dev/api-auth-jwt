from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserPublic(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"