from pydantic import BaseModel, field_validator
import re


class UserCreate(BaseModel):
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("A senha deve ter no mínimo 8 caracteres")
        if not re.search(r"[A-Z]", v):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula")
        if not re.search(r"\d", v):
            raise ValueError("A senha deve conter pelo menos um número")
        return v


class UserPublic(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"