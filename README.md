# 🔐 API de Autenticação com JWT (FastAPI)

API simples de autenticação desenvolvida com **FastAPI**, implementando registro de usuários, login e autenticação com **JWT (JSON Web Token)**.

---

## 🚀 Funcionalidades

- Registro de usuário
- Login com geração de token JWT
- Autenticação usando OAuth2
- Rota protegida (`/profile`)
- Documentação automática com Swagger

---

## 🛠 Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic
- Passlib
- Python-Jose (JWT)
- OAuth2PasswordBearer

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/isaporteela-dev/api-auth-jwt.git
cd api-auth-jwt
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Rodando o projeto

Inicie o servidor:

```bash
python -m uvicorn app:app --reload --port 8001
```

Acesse a documentação da API:

```
http://127.0.0.1:8001/docs
```

---

## 🔑 Fluxo de autenticação

### Registrar usuário

**POST /register**

```json
{
  "username": "isa",
  "password": "123"
}
```

### Login

**POST /login**

Retorna um token JWT.

### Autorizar

Clique em **Authorize 🔒** no Swagger e faça login.

### Acessar rota protegida

**GET /profile**

Retorna o usuário autenticado.

---

## 📁 Estrutura do projeto

```
api-auth-jwt
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 👩‍💻 Autora

**Isabella Portela**

Graduada em Medicina Veterinária  
Estudante de Análise e Desenvolvimento de Sistemas  
Backend Developer em formação (Python & Java)
