from fastapi import FastAPI
from app.routers.auth import router as auth_router

app = FastAPI(
    title="API de Autenticação com JWT",
    description="API de autenticação com registro, login e rotas protegidas.",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {"mensagem": "API Auth JWT funcionando!"}