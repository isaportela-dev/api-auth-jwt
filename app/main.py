from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.core.database import engine, Base
from app import models

app = FastAPI(
    title="API de Autenticação com JWT",
    description="API de autenticação com registro, login e rotas protegidas.",
    version="1.0.0",
)

# Cria as tabelas automaticamente ao iniciar
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)


@app.get("/")
def home():
    return {"mensagem": "API Auth JWT funcionando!"}