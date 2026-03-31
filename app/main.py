from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.routers.auth import router as auth_router
from app.core.database import engine, Base
from app import models

# Limiter usa o IP do cliente como identificador
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="API de Autenticação com JWT",
    description="API de autenticação com registro, login e rotas protegidas.",
    version="1.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)


@app.get("/")
def home():
    return {"mensagem": "API Auth JWT funcionando!"}